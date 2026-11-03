---
article_id: 1500004653542
category: NFe - Nota Fiscal Eletrônica
content_hash: 4a9cd26d561c254a57c6fbab8a18482f9a84d1069075cdcbb521ea4e1010368d
fetched_at: '2026-06-28T22:40:01.421136+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 443 Rejeição:
  Código da bandeira de cartão de crédito e/ou débito inexistente.  '
type: support-article
updated_at: '2021-09-01T11:01:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004653542--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-443-Rejei%C3%A7%C3%A3o-C%C3%B3digo-da-bandeira-de-cart%C3%A3o-de-cr%C3%A9dito-e-ou-d%C3%A9bito-inexistente
---

**Dúvida**Como solucionar a rejeição abaixo:

443 Rejeição: Código da bandeira de cartão de crédito e/ou débito inexistente ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Verificar se o Código da bandeira de **cartão de crédito e/ou débito (campo: tBand)** existe na tabela de códigos das operadoras de **cartão de crédito e/ou débito** publicada no Portal Nacional da Nota Fiscal Eletrônica Observação 1: Regra válida a partir de **03/05/2021** para **homologação** e **01/09/2021** para **produção.**

1- Verificar a lista de **Códigos das operadoras de Cartão de crédito e/ ou débito** aceitas pela Sefaz no link abaixo:

[Tabela de bandeiras de Cartões de Crédito/Débito - Publicada em 16/03/2021](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=txtcX/WzVFY=)

2- Se a nota foi realizada pelo **módulo do loja há o boletim do link abaixo:**

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=626650334>

**Na aba:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403752731031/mceclip0.png)

* **Importante:**

Se gerada pelo faturamento como não há tratamento padrão será necessário revisar a customização da empresa.

A utilização do ponto de entrada **PE01NFESEFAZ.**

Segue link com exemplo:

[PE01NFESEFAZ - Manipulação em dados do Grupo Detalhamento da Forma de Pagamento](http://tdn.totvs.com/pages/viewpage.action?pageId=348298539)

* **Validação da Sefaz:**

![rejeicao_443.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006135521/rejeicao_443.JPG)
