---
article_id: 360043007793
category: NFe - Nota Fiscal Eletrônica
content_hash: 0883aac2922a903eef3b1d923a60c729c13252f2a3505240d6f1123a3d4590b7
fetched_at: '2026-06-28T22:40:00.073980+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como enviar DANFE
  e XML por e-mail via TSS
type: support-article
updated_at: '2026-05-22T20:08:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043007793-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-enviar-DANFE-e-XML-por-e-mail-via-TSS
---

**Dúvida**Como enviar DANFE e XML por e-mail via TSS?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**O Envio do XML é automático, para o envio do Danfe realizar o procedimento abaixo:**

1. Primeiramente é necessário acessar a rotina **Nfesefaz** e clicar no botão **Wiz config,** preencher os dados até a tela do **SMTP.**

Nesta tela localizar o botão **"Enviar DANFE por e-mail"**

* Há 3 opções:

**0-**Desabilitado (**não envia** o DANFE por e-mail)  
**1-** Enviar DANFE do TSS (neste caso é enviado DANFE com layout **padrão do TSS**)  
**2-** Enviar DANFE do ERP (neste caso é enviado DANFE com layout **do ERP que pode conter customização**)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360056842154)

2. Para a opção **2- Enviar DANFE do ERP** deverá seguir os procedimentos descritos no link abaixo:

[MP-TSS- ENVIO DE E-MAIL DO DANFE GERADO NO ERP (CUSTOMIZAÇÃO DISPONÍVEL VIA RDMake).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041452974)

3. É necessário que possua o arquivo **printer nas pastas Smartclient e Appserver do TSS:**

Link de download do artefato do Windows:

[Printer Windows X64](https://suporte.totvs.com/portal/p/10098/download#detail/693168)

[Printer Windows X32](https://suporte.totvs.com/portal/p/10098/download#detail/693163)

Link de download do artefato do MAC:

[Printer MAC](https://suporte.totvs.com/portal/p/10098/download#detail/693162)

Link de download do artefato do Linux:

[Printer Linux X64](https://suporte.totvs.com/portal/p/10098/download#detail/711950)

[PDF Printer X64](https://suporte.totvs.com/portal/p/10098/download#detail/693160)

[Printer Linux X32](https://suporte.totvs.com/portal/p/10098/download#detail/711949)

[PDF Printer X32](https://suporte.totvs.com/portal/p/10098/download#detail/693159)

4.  Caso utilize o sistema operacional Linux, recomendamos que todas as pastas estejam com permissão total (CHMOD 777). A configuração de e-mail necessita de autenticação ***(inserir senha do e-mail no wizard).*** Sem essa informação o TSS não consegue se comunicar com o servidor de SMTP.

* **Importante:**

Em **homologação,** será enviado **automaticamente o e-mail para a empresa o emitente e não para o destinatário.**
