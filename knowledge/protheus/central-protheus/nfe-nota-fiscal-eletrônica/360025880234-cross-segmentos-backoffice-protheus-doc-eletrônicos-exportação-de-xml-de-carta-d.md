---
article_id: 360025880234
category: NFe - Nota Fiscal Eletrônica
content_hash: 06f08dc7a37ba61fda8232ed2668ce8f6cf358779ad48695b0502a8260fb8c53
fetched_at: '2026-06-28T22:40:06.860561+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Exportação de XML
  de Carta de Correção Eletrônica ( CCe / CC-e) no Protheus
type: support-article
updated_at: '2025-06-25T12:05:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025880234-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Exporta%C3%A7%C3%A3o-de-XML-de-Carta-de-Corre%C3%A7%C3%A3o-Eletr%C3%B4nica-CCe-CC-e-no-Protheus
---

**Dúvida**

Como exportar XML de  Carta de Correção Eletrônica ( CCe / CC-e) no Protheus ? 

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1-Entre No módulo do **Faturamento** Selecionar **Atualizações ->** **NF-e NFs-e ->** **NF-e Sefaz**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33040748602007)

 2- Ao entrar será apresentada a tela **Transmissão ?**

* Selecionar opção**3-CCe**e clicar em **OK**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33040743851159)

 3- Ao entrar será apresentada a tela **Tipo de NFe ?**

* Selecionar se a nota é de **Entrada** ou de **Saída,** informar a **Série** da nota, após isso clicar em **OK**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33040748604951)

  4- Ao entrar na Rotina **Monitoramento da CC-e**

* Selecionar a nota clicar em **Outras ações** -> **Transmissão**:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33040748605719)

 5- Será apresentada uma tela para digitar o **texto**

* Digitar o **Texto**  (**não pode ser copiado e colado**),  não deve ter acento, caracteres especiais, no mínimo **15** caracteres e no máximo **1000,** após digitar clicar em **Avançar**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33040743854999)

6- Para confirmar a transmissão do **evento**

* Selecionar **Outras ações** -> **Monitor**o evento deve estar como **Registrado e Vinculado.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33040748606743)

 7- Para **exportar** o XML da CCe

* **Clicar em Exportar:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041140093)

 8- Será apresentada uma tela com **Serie da nota fiscal ?, Nota Fiscal inicial ?, Nota fiscal final ?, Diretório de destino?, Data inicial ? e Data final ?**

* Informar os dados nos parâmetros e clicar em **OK**:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040305674)

* **Importante:**

Se ao exportar apresentar a mensagem ***NFESBRA : NFEEXPEVENTO: Método não disponível***

*Se ao transmitir a CC-e apresentar a mensagem**invalid property CCCEPDF on GETCFGCCE(TSSCONFIG.PRW)***

**1. Atualização do ambiente TSS (repositório)**

1. Atualizar o **repositório** com o último pacote de **expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)
