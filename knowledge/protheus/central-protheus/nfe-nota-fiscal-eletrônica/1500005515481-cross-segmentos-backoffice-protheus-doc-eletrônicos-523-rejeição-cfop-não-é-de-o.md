---
article_id: 1500005515481
category: NFe - Nota Fiscal Eletrônica
content_hash: 4dbedfa38efc23be7613c06d6a02758aec55eeab1204315c49234c83233b74ea
fetched_at: '2026-06-28T22:40:03.233530+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  523 Rejeição :
  CFOP não é de Operação Estadual e UF emitente igual à UF destinatário'
type: support-article
updated_at: '2025-06-26T14:47:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005515481-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-523-Rejei%C3%A7%C3%A3o-CFOP-n%C3%A3o-%C3%A9-de-Opera%C3%A7%C3%A3o-Estadual-e-UF-emitente-igual-%C3%A0-UF-destinat%C3%A1rio
---

**Dúvida**Como corrigir a rejeição 523 : CFOP não é de Operação Estadual e UF emitente igual à UF destinatário ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1 - O CFOP é de operação interestadual **(inicia por 2 ou 6)** e UF emitente = UF destinatário e CNPJ/CPF emissor diferente do CNPJ/CPF destinatário (NT 2010/004) Se emitente e o destinatário tiver CNPJ/CPF diferentes e  forem da mesma UF, verificar se o **CFOP** da nota está correto sendo iniciado por **2 ou 6;**

2- Caso o **CFOP** esteja errado alterar o CFOP pelo TES da nota no campo **Cod. Fiscal "F4\_CF", para um CFOP de operação interna**iniciado por **1 ou 5;**

![CFOP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11547042788375)

3- Após isso, exclua a **nota e gere novamente.**

4- Caso o **CFOP de operação interestadual** esteja correto, o CNPJ/CPF do emitente e do destinatário devem ser iguais.

* **Saiba Mais:**

Exceção 1: Se a tag UFCons (id:LA06) foi informada com UF diversa do emitente: **CFOP iniciado com 2 ou 6** é válido. (NT 2010/010) Observação: Regra de validação opcional, a critério da UF

* Para gerar a TAG é conforme **a documentação abaixo:**

*[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029 : Falha de schema na Tag descanp](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005010471-MP-NFE-029-Falha-de-schema-na-Tag-descANP-?source=search)*

Exceção 2: Se [UF emitente = UF destinatário] e [a tag finNFe (id:B25) indicar que esta é uma nota de ajuste (=3)]: será aceito o CFOP 6206 Observação: Regra de validação opcional, a critério da UF

1. Para gerar nota de estorno é conforme **a documentação abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Inclusão de Nota de Estorno e Estorno de Devolução (NF de devolução emitida com erros)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020898192)

2. No TES da nota no campo **Cod. Fiscal "F4\_CF", para um CFOP altere para o CFOP 6206**

![CFOP.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/11547042788375)

* Regra de **validação opcional, a critério da UF**

Exceção 3: A regra de validação acima não se aplica se informada ***UF do local de entrega (tag: entrega/UF) diferente da UF do emitente (tag: emit/enderEmit/UF).***

1. Preencher no pedido de vendas o campo ***Cli. Entrega** **C5\_CLIENT***

![20220503_141126.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071691477143)

2. Preencher no cadastro do Documento de entrada o campo **Fornec. Entrega F1\_FORENT**

![20220503_154452.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071691482519)

3. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_NFEDEST = .T.**

![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071691483799)

4. Após isso, **exclua a nota e gere** novamente.

Exceção 4: A regra de validação não se aplica se informada UF do ***local de retirada*** (tag: retirada/UF) diferente da UF do destinatário (tag: enderDest/UF); ***Observação: Regra de validação opcional, a critério da UF***

1. Preencher o **cliente** ***de retirad*****a** no pedido de vendas no campo ***Cli. Retirada** **C5\_CLIRET***

![20220503_165500.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071691485335)

2. Preencher no documento de entrada o campo **Fornec. Retirada F1\_FORRET na aba Informações Danfe**

![20220503_154452.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071691482519)

3. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_NFEDEST = .T.**

![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33071691483799)

4. Após isso, **exclua a nota e gere** novamente.

* ***Saiba mais:***

***Para mais informações referente** ao parâmetro **MV\_NFEDEST,** verifique o link abaixo:*

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=271850728)

* **Validação da Sefaz:**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9150694243095)
