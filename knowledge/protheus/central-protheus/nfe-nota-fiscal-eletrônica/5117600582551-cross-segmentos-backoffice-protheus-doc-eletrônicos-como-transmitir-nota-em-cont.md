---
article_id: 5117600582551
category: NFe - Nota Fiscal Eletrônica
content_hash: d1b064dbe68fc439bf83a28fd4d60ef11100646aaef778f571f399c0e87388f7
fetched_at: '2026-06-28T22:40:06.800622+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como transmitir
  nota em contingencia SVC-AN para SEFAZ MG
type: support-article
updated_at: '2025-07-25T18:43:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5117600582551-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-transmitir-nota-em-contingencia-SVC-AN-para-SEFAZ-MG
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33721657899031) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como transmitir nota em contingencia SVC-AN para SEFAZ MG ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.27

Cross Segmentos - TSS - Todas as versões.

**Solução:**

**1 - Verificar no site da Sefaz a disponibilidades de serviços.**

**<http://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx?versao=0.00&tipoConteudo=P2c98tUpxrI=>**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5117503261207)**

**2 - Para a SEFAZ de MG deve transmitir as notas em modalidade SVC-AN**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5117524516887)**

**3 - Para que não tenham problemas com as notas em contingência, indicamos que confirmem com a Sefaz qual a contingência indicada. Após confirmarem, a contingência deve ser configurada na rotina NFe Sefaz > Outras Ações > Parâmetros > NFe > Selecione a modalidade indicada pela Sefaz > Salve > OK:**

**![](https://totvssuporte.zendesk.com/attachments/token/UIJFNOWIaiEwimVvNdJlcya1Y/?name=inline-848738425.png)​  
  
4 - Em seguida é só seguir com as transmissões.**

Ao entrar em modo contingencia é necessário gerar a nota do zero para que a mesma tenho o seu xml montado com a modalidade referente a modalidade configurada em Outras Ações - Parâmetros - NFe.

**5- Após a Sefaz voltar a normalidade é necessário retransmitir as notas que estava em contingencia na mesma modalidade que foram transmitidas.**

***OBS: Orientamos a entrar em contato com a SEFAZ caso tenha duvidas ou necessite de alguma informação pontual sobre os serviços.***
