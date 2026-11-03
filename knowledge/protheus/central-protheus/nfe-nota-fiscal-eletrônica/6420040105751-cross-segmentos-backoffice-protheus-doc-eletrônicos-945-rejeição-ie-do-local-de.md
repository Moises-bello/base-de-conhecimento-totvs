---
article_id: 6420040105751
category: NFe - Nota Fiscal Eletrônica
content_hash: 77e2fa01547e77c9e7e0236dfb42c3a628867457d473938c561810a0ce534add
fetched_at: '2026-06-28T22:40:03.384473+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  945 Rejeição:
  IE do local de entrega não cadastrada'
type: support-article
updated_at: '2025-07-14T14:17:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6420040105751-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-945-Rejei%C3%A7%C3%A3o-IE-do-local-de-entrega-n%C3%A3o-cadastrada
---

**Dúvida**Como solucionar a rejeição 945 Rejeição: IE do local de entrega não cadastrada ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**

1. Acessar o Cadastro de Contribuinte. Verifique se o ***IE do local de entrega está vinculada ao CNPJ*** no **Cadastro Centralizado de Contribuinte (CCC)** [*Clique Aqui*](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)

2. Após, verificar o **IE correto do cliente** ***de retirad*****a** altere no cadastro de cliente vinculado no campo ***Cli. Entrega** **C5\_CLIENT o campo Ins. Estad. A1\_INCRI***

![20220503_141126.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33453085998615)

3. Caso seja cadastro de fornecedor,  altere no cadastro de fornecedor vinculado no campo **Fornec. Entrega F1\_FORENT na aba Informações Danfe *o campo Ins. Estad. A2\_INCRI***

![20220503_154452.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33453086002071)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_NFEDEST = .T.**

![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33453086011287)

5. Após isso, **exclua a nota e gere** novamente.

* **Saiba mais:**

Caso o ***IE esteja correto ou não haja informação do IE no CCC,*** será necessário entrar em contato com o Sefaz.

Caso seja operação de venda triangular ajustar os campos **C5\_CLIREM, C5\_LOJAREM e C5\_LOJAREM**, conforme o link abaixo:

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=519719230)*

* ***Validação da Sefaz:***

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6420031820055)**
