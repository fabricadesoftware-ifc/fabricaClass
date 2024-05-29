import os
import matplotlib.pyplot as plt
import tempfile
import smtplib
from dotenv import load_dotenv 

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

load_dotenv()
def generate_pie_graph(df):
    try:
        fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

        counts = df['tipo_usuario'].value_counts(normalize=True) * 100

        wedges, texts, autotexts = ax.pie(counts, autopct='%1.1f%%', textprops=dict(color="w"))

        ax.legend(wedges, counts.index, title="Tipo de Usuário", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
        plt.setp(autotexts, size=8, weight="bold")
        ax.set_title("Distribuição de Tipo de Usuário")

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            imagem_temporaria = temp_file.name
            plt.savefig(imagem_temporaria)
            print(imagem_temporaria)
        return imagem_temporaria
    except Exception as e:
        print(f"Erro ao gerar imagem: {e}")
        raise e

async def send_graph_by_email(subject, message, recipient_list, image):
    try:

        remetente = os.getenv("EMAIL_HOST_USER")
        senha = os.getenv("EMAIL_HOST_PASSWORD")
        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = ", ".join(recipient_list)
        msg['Subject'] = subject

        with open(image, 'rb') as fp:
            img = MIMEImage(fp.read())
        img.add_header('Content-Disposition', 'attachment', filename=image)
        msg.attach(img)
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)

        server.sendmail(remetente, recipient_list, msg.as_string())
        server.quit()

        return "Email enviado com sucesso"
    except Exception as e:
        
        print(f"Erro ao gerar imagem ou enviar e-mail: {e}")
        return None
