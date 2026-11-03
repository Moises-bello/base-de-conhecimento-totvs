---
article_id: 360028872711
category: NFe - Nota Fiscal Eletrônica
content_hash: b32f8e44d1a15ff9f7e058fc24dc2d61e906c6e4c1aa2b813c3c7a3b05d4d9f8
fetched_at: '2026-06-28T22:40:06.711280+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar as TAGS
  entrega e retirada no XML
type: support-article
updated_at: '2025-06-17T11:54:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028872711-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-as-TAGS-entrega-e-retirada-no-XML
---

**Dúvida**Como gerar as TAGS  entrega e retirada no XML ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

## 

***O código de cliente de entrega e retirada precisa se diferente do código do cliente.***

1. Preencher os campos ***Cliente de retirada*** **C5\_CLIRET e  *Loja de retirada* C5\_LOJARET** no Pedido de Venda.

2. Preencher os campos ***Fornecedor de retirada*** **F1\_FORRET e *Loja de retirada* F1\_LOJARET** no Documento de entrada.

3. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em editar e informar ***MV\_NFEDEST = .T.***

***![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15752781498263)***

4. Preencher o campo de Cliente de entrega no pedido de vendas  **C5\_CLIENT**

**![20220503_141126.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15752808738967)**

5. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em editar e informar **MV\_NFEDEST = .T.**

![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/15752781498263)

**Já ao habilitar o parâmetro (.T.), a rotina passa a se comportar da seguinte forma:  
  
  
A tag de Destinatário - "<dest>"' será gerada com os dados do CLIENTE.  
  
Caso possua Cliente de Entrega, a tag de Entrega - "<entrega>" será gerada exatamente com os dados do Cliente de Entrega.  
  
Caso possua Cliente de Retirada, a tag de Retirada - "<retirada>" será gerada exatamente com os dados do Cliente de Retirada.**

Ou

**As regras do parâmetro MV\_NFEDEST são as seguintes:  
  
Por padrão o parâmetro está desabilitado (.F.), o que indica que o legado da rotina será mantido, comportando-se da seguinte forma:  
  
  
Para operações interestaduais (UF do emitente diferente da UF do Cliente de Entrega) e o CNPJ do Destinatário (Cliente) for DIFERENTE do emitente, serão considerados os dados do CLIENTE DE ENTREGA. Ou seja os dados do Cliente de Entrega serão gerados na tag de Destinatário - "<dest>".  
  
Para operações internas (UF do emitente igual a UF do Cliente de Entrega) e se o CNPJ do Destinatário (Cliente) for IGUAL ao do emitente, serão considerados os dados do CLIENTE, mesmo que as UF's sejam diferentes.- Ou seja os dados do Cliente serão gerados na tag de Destinatário - "<dest>".**

6. Preencher para ***operação de venda*** triangular os campos **C5\_CLIREM, C5\_LOJAREM e C5\_LOJAREM**, conforme o link abaixo:

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=519719230)*

* ***Saiba mais:***

Se preenchido os campos de ***Cliente ou Fornecedor e Loja de Retirada***, no XML da nota será gerado com a TAG referente a Retirada.

* **Importante:**

No **Danfe será impresso** conforme o link abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=485426275>

5.2 Informações do local de retirada:

***Caso haja preenchimento do grupo F - Local de retirada, fica possibilitada a exibição de informações no DANFE***em área especifica, conforme sugestão de modelo abaixo:

![](https://tdn.totvs.com/download/attachments/485426275/image2019-4-17_17-39-29.png?version=1&modificationDate=1555533570047&api=v2)

5.3 Informações do local de entrega:  
***Caso haja preenchimento do grupo G - Local de entrega, fica possibilitada a exibição de informações no DANFE*** em área especifica, conforme sugestão de modelo abaixo:

![](https://tdn.totvs.com/download/attachments/485426275/image2019-4-17_17-43-32.png?version=1&modificationDate=1555533812360&api=v2)

*[Clique Aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=271850728)*

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=519719230)*
