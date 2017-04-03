import os
from datetime import datetime
from django.utils import formats
from django.conf import settings
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Image,
                                Table, TableStyle)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import letter, A4
from xyberville.apps.users.models import User
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, inch, cm


class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        canvas.Canvas.__init__(self, *args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        """add page info to each page (page x of y)"""
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_number(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_number(self, page_count):
        # Change the position of this to wherever you want the page number to be
        self.drawRightString(211 * mm, 15 * mm + (0.2 * inch),
                             "Page %d of %d" % (self._pageNumber, page_count))


class MyPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    @staticmethod
    def _header_footer(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # # Header
        # header = []
        #
        # logo = os.path.join(settings.STATIC_ROOT, 'img/kop_surat.png')
        # im = Image(logo, 20 * inch, 2 * inch)
        # header.append(im)
        #
        # w, h = header.wrap(doc.width, doc.topMargin)
        # header.drawOn(canvas, doc.leftMargin, doc.height + doc.topMargin - h)

        # Footer
        # footer = Paragraph(
        #     'This is a multi-line footer.  It goes on every page.   ' * 5,
        #     styles['Normal'])
        # w, h = footer.wrap(doc.width, doc.bottomMargin)
        # footer.drawOn(canvas, doc.leftMargin, h)

        # Release the canvas
        canvas.restoreState()

    def print_user(self, user):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)

        style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'LEFT'),
                            ('TEXTCOLOR', (1, 1), (-2, -2), colors.black),
                            ('INNERGRID', (0, 0), (-1, -1), 0.25,
                             colors.transparent),
                            ('BOX', (0, 0), (-1, -1), 0.25, colors.transparent),
                            ])

        # Configure style and word wrap
        s = getSampleStyleSheet()
        s = s["BodyText"]
        s.wordWrap = 'CJK'

        # Our container for 'Flowable' objects
        elements = []
        logo = os.path.join(settings.STATIC_ROOT, 'img/kop_surat.png')
        im = Image(logo, 6.5 * inch, 1.5 * inch)
        elements.append(im)

        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='RightAlign', alignment=TA_RIGHT))

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        judul = '<font size=14><u><strong>SURAT PENGANTAR</strong></u></font>'
        nomor_surat = '001/M1/MNA/III/17'
        nomor = '<font size=10>NOMOR : %s</font>' % nomor_surat

        elements.append(Spacer(1, 12))
        elements.append(Paragraph(judul, styles['Title']))
        elements.append(Paragraph(nomor, styles['Title']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(
            '&nbsp;&nbsp;Yang bertanda tangan dibawah ini, menerangkan bahwa :',
            styles['Normal']
        ))
        elements.append(Spacer(1, 12))
        tanggal_lahir = user.profile.tanggal_lahir
        formatted_tanggal_lahir = formats.date_format(tanggal_lahir, "DATE_FORMAT")

        data = [
            ["Nama", ":", user.name],
            ["Tempat / Tgl. Lahir ", ":", "%s / %s" % (
                user.profile.tempat_lahir, formatted_tanggal_lahir)],
            ["Jenis Kelamin", ":", user.profile.get_kelamin_display()],
            ["Agama", ":", user.profile.get_agama_display()],
            ["Pekerjaan", ":", user.profile.pekerjaan],
            ["Nomor KTP", ":", user.profile.nik],
            ["Alamat", ":", "%s, RT. %s / RW. %s" % (user.profile.alamat,
                                                     user.profile.rt,
                                                     user.profile.rw)],
            ["", "", "KEL. %s, KEC. %s" % (user.profile.village,
                                           user.profile.district)],
            ["", "", "%s %s" % (user.profile.regency, user.profile.kode_pos)],
            ["Keperluan", ":", "MEMBUAT SKCK"]
        ]

        # TODO: Get this line right instead of just copying it from the docs
        t = Table(data, (6 * cm, 0.5 * cm, 9 * cm), None, style=style, hAlign='LEFT')

        # Send the data and build the file
        elements.append(t)
        elements.append(Spacer(1, 14))
        elements.append(Paragraph('&nbsp;&nbsp;Demikian surat pengantar ini '
                                  'dibuat untuk dapat dipergunakan '
                                  'sebagaimana mestinya dan yang', styles['Normal']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph('&nbsp;&nbsp;berkepentingan untuk menjadi maklum.', styles['Normal']))
        elements.append(Spacer(1, 20))
        date_joined = datetime.now()
        formatted_datetime = formats.date_format(date_joined,
                                                 "DATE_FORMAT")
        elements.append(Paragraph('Jakarta, %s' % formatted_datetime, styles[
            'RightAlign']))
        # doc.build(elements, onFirstPage=self._header_footer,
        #           onLaterPages=self._header_footer,
        #           canvasmaker=NumberedCanvas)
        doc.build(elements)

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf

    def print_pengantar(self, pengantar):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)

        style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'LEFT'),
                            ('TEXTCOLOR', (1, 1), (-2, -2), colors.black),
                            ('INNERGRID', (0, 0), (-1, -1), 0.25,
                             colors.transparent),
                            ('BOX', (0, 0), (-1, -1), 0.25, colors.transparent),
                            ])

        # Configure style and word wrap
        s = getSampleStyleSheet()
        s = s["BodyText"]
        s.wordWrap = 'CJK'

        # Our container for 'Flowable' objects
        elements = []
        logo = os.path.join(settings.STATIC_ROOT, 'img/kop_surat.png')
        im = Image(logo, 6.5 * inch, 1.5 * inch)
        elements.append(im)

        # A large collection of style sheets pre-made for us
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Justify', alignment=TA_CENTER))
        styles.add(ParagraphStyle(name='RightAlign', alignment=TA_RIGHT))

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        judul = '<font size=14><u><strong>SURAT PENGANTAR</strong></u></font>'
        nomor_surat = '001/M1/MNA/III/17'
        nomor = '<font size=10>NOMOR : %s</font>' % nomor_surat

        elements.append(Spacer(1, 12))
        elements.append(Paragraph(judul, styles['Title']))
        elements.append(Paragraph(nomor, styles['Title']))
        elements.append(Spacer(1, 12))
        elements.append(Paragraph(
            '&nbsp;&nbsp;Yang bertanda tangan dibawah ini, menerangkan bahwa :',
            styles['Normal']
        ))
        elements.append(Spacer(1, 12))
        tanggal_lahir = pengantar.user.profile.tanggal_lahir
        formatted_tanggal_lahir = formats.date_format(tanggal_lahir, "DATE_FORMAT")

        data = [
            ["Nama", ":", pengantar.user.name],
            ["Tempat / Tgl. Lahir ", ":", "%s / %s" % (
                pengantar.user.profile.tempat_lahir, formatted_tanggal_lahir)],
            ["Jenis Kelamin", ":", pengantar.user.profile.get_kelamin_display()],
            ["Agama", ":", pengantar.user.profile.get_agama_display()],
            ["Pekerjaan", ":", pengantar.user.profile.pekerjaan],
            ["Nomor KTP", ":", pengantar.user.profile.nik],
            ["Alamat", ":", "%s, RT. %s / RW. %s" % (pengantar.user.profile.alamat,
                                                     pengantar.user.profile.rt,
                                                     pengantar.user.profile.rw)],
            ["", "", "KEL. %s, KEC. %s" % (pengantar.user.profile.village,
                                           pengantar.user.profile.district)],
            ["", "", "%s %s" % (pengantar.user.profile.regency, pengantar.user.profile.kode_pos)],
            ["Keperluan", ":", "MEMBUAT SKCK"]
        ]

        # TODO: Get this line right instead of just copying it from the docs
        t = Table(data, (6 * cm, 0.5 * cm, 9 * cm), None, style=style, hAlign='LEFT')

        # Send the data and build the file
        elements.append(t)
        elements.append(Spacer(1, 14))
        elements.append(Paragraph('&nbsp;&nbsp;Demikian surat pengantar ini '
                                  'dibuat untuk dapat dipergunakan '
                                  'sebagaimana mestinya dan yang', styles['Normal']))
        elements.append(Spacer(1, 10))
        elements.append(Paragraph('&nbsp;&nbsp;berkepentingan untuk menjadi maklum.', styles['Normal']))
        elements.append(Spacer(1, 20))
        date_joined = datetime.now()
        formatted_datetime = formats.date_format(date_joined,
                                                 "DATE_FORMAT")
        elements.append(Paragraph('Jakarta, %s' % formatted_datetime, styles[
            'RightAlign']))
        # doc.build(elements, onFirstPage=self._header_footer,
        #           onLaterPages=self._header_footer,
        #           canvasmaker=NumberedCanvas)
        doc.build(elements)

        # Get the value of the BytesIO buffer and write it to the response.
        pdf = buffer.getvalue()
        buffer.close()
        return pdf

