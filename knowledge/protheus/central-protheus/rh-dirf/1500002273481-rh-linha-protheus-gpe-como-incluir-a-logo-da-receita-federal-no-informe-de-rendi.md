---
article_id: 1500002273481
category: RH – DIRF
content_hash: 16364dbe7b017d649ef446c8e1c5b459a248f56a5b25c6b878840e70b1f22e29
fetched_at: '2026-06-28T22:44:06.899646+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir a logo da Receita Federal no Informe
  de Rendimentos
type: support-article
updated_at: '2025-06-16T20:20:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002273481-RH-Linha-Protheus-GPE-Como-incluir-a-logo-da-Receita-Federal-no-Informe-de-Rendimentos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32854373256983)**Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como incluir o logo da Receita Federal no Informe de Rendimentos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.  
  
**Solução**1) Para incluir a logo da receita no informe de rendimentos deve ser efetuado o seguinte procedimento:

**Obs.:** O logo para ser considerado na impressão do informe de rendimentos, além de possuir extensão **.bmp** deve possuir **dimensão 119x94, largura: 119, altura: 94.**

![receita.bmp](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002259121)  
  
2) Baixe a imagem da internet conforme acima e abra o **MSPAINT**através do menu iniciar e efetue a seguinte configuração:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002197422)

3) Salve o arquivo com extensão **.bmp** na pasta system do Protheus:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002199402)

4) Gere o informe de rendimentos conforme abaixo.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103256393)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002261121)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101091634)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002261341)

**Observações:**Para ambiente Linux, deve ser configurado da maneira abaixo:

-System deve conter a imagem da receita com a seguinte nomenclatura para ambiente Linux:**RECEITA.BMP (Maiúsculo).**  
-Abra o**appserver.ini** e informe no caminho do **StartPath=/system****\** **(com barra invertida após a palavra System)**.

**Observação²:**

No envio do Informe de Rendimentos por e-mail, para que o logo seja impresso, é necessário gravar na mesma pasta que o informe de rendimentos, para que seja exibido corretamente.

<https://tdn.totvs.com/display/public/PROT/16389506+DRHCALCPRT-7805+DT+Informe+de+Rendimentos+por+e-mail+sem+o+logo+da+Receita+Federal>  
  
**Saiba Mais**  
[RH - Linha Protheus - GPE - Configuração de envio de informações por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwj1aAPVUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBn2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA1NjA1NjA1My1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29uZmlndXJhJUMzJUE3JUMzJUEzby1kZS1lbnZpby1kZS1pbmZvcm1hJUMzJUE3JUMzJUI1ZXMtcG9yLWUtbWFpbAY7CFQ6DnNlYXJjaF9pZEkiKWQ4Mjg5NjMxLTUyYWMtNDcxOS1hZDRhLTZiMmM0NTc0ZDI4MQY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiKlJIIC0gTGluaGEgUHJvdGhldXMgLSBlbnZpbyBwb3IgZW1haWwGOwhUOhJyZXN1bHRzX2NvdW50aQLQBw%3D%3D--043fe9530b6000539a0e65553766193fa6162521)  
[RH - Linha Protheus - GPE - Parametrização para envio do recibo e relatórios por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwjniSLHGgA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzExNTAxMDA3OTIwNy1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtUGFyYW1ldHJpemElQzMlQTclQzMlQTNvLXBhcmEtZW52aW8tZG8tcmVjaWJvLWUtcmVsYXQlQzMlQjNyaW9zLXBvci1lLW1haWwGOwhUOg5zZWFyY2hfaWRJIilkODI4OTYzMS01MmFjLTQ3MTktYWQ0YS02YjJjNDU3NGQyODEGOwhGOglyYW5raQc6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIipSSCAtIExpbmhhIFByb3RoZXVzIC0gZW52aW8gcG9yIGVtYWlsBjsIVDoScmVzdWx0c19jb3VudGkC0Ac%3D--2ad37b41f2fc8ea073030b832c988559e0615da9)  
[RH - Linha Protheus - GPE - Como incluir a logo da Receita Federal no Informe de Rendimentos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002273481-RH-Linha-Protheus-GPE-Como-incluir-a-logo-da-Receita-Federal-no-Informe-de-Rendimentos?source=search)
