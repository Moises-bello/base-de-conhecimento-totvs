---
article_id: 23444574168215
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 4af865308ac5f2d43ed3e27e699a173c00c1888639ed4d2a77381d2fc6221791
fetched_at: '2026-06-28T22:37:56.399980+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - JOB FINPIXMAIL - Envio
  do QRCODE PIX por E-mail
type: support-article
updated_at: '2024-06-17T21:45:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23444574168215-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-JOB-FINPIXMAIL-Envio-do-QRCODE-PIX-por-E-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23444545975575) Tempo aproximado para leitura: **00:10:00 min** **Dúvida**Como configurar o JOB de e-mail do envio do QRCODE do PIX para o cliente?

**Ambiente**Cross Segmento-TOTVS Backoffice (Linha Protheus)- Financeiro - A partir da release 12.1.2210

**Solução** **1 -** Inicialmente o cadastro do cliente deve possui em **Complemento do Cliente** a opção **Gera PIX = Igual a 2 = Sim, com envio de e-mail  
  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23444574126999)**

**2 -** Deve acessar a rotina **FINA890 - Monitor PIX** e clicar em **Outras Ações >> Configurar** 

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23444574129303)**

**3 -** Cadastrar os layouts de **Carta de Cobrança** e tipo de envio, **CNAB** ou **API**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23444574130711)**

**4 -** Acessar o Modulo **Configurador >> Schedule >> Agendamento** e cadastrar o JOB **FINPIXMAIL**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23444545989783)

**5 -** Realizar a transmissão de um título via **PIX** seja por **CNAB** ou **API,** será alterado o status para **QR Code Gerado**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23444574137879)**

**6 -** Ao rodar o JOB, será enviado o e-mail com as informações cadastradas do layout da carta de cobrança com o **QRCODE** em anexo  **![](https://centraldeatendimento.totvs.com/hc/article_attachments/23444574143511)**

**Saiba mais:**  
[Job para envio de e-mail dos títulos em situação de cobrança PIX.](https://tdn.totvs.com/pages/viewpage.action?pageId=736174501)  
[Pagamentos instantâneos - PIX](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
