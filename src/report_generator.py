from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(
        filename,
        title,
        summary_text
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(title, styles["Title"])
    )

    content.append(
        Spacer(1,12)
    )

    content.append(
        Paragraph(summary_text,
                  styles["BodyText"])
    )

    doc.build(content)
