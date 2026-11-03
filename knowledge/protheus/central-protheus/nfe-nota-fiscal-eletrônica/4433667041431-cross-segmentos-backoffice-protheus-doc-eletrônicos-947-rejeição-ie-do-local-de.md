---
article_id: 4433667041431
category: NFe - Nota Fiscal Eletrônica
content_hash: 73b2760f192676c534365d57cad6b604ff4830cfbf0ff6206c251eb70a727215
fetched_at: '2026-06-28T22:40:05.559623+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 947 Rejeição: IE
  do local de entrega não vinculada ao CNPJ'
type: support-article
updated_at: '2025-07-15T12:13:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4433667041431-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-947-Rejei%C3%A7%C3%A3o-IE-do-local-de-entrega-n%C3%A3o-vinculada-ao-CNPJ
---

**Dúvida**Como solucionar a rejeição 947 Rejeição: IE do local de entrega não vinculada ao CNPJ ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informado CNPJ do local de entrega e IE do local de entrega não vinculada  
ao ***CNPJ (tratar Regime Especial de IE Única)***

1. Acessar o Cadastro de Contribuinte. Verifique se o ***CNPJ do local de entrega e IE do local de entrega não vinculada ao CNPJ*** (tratar Regime Especial de IE Única) **Cadastro Centralizado de Contribuinte (CCC)** [*Clique Aqui*](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)

2. Após, verificar o **IE correto do cliente** ***de retirad*****a** altere no cadastro de cliente vinculado no campo ***Cli. Entrega** **C5\_CLIENT o campo Ins. Estad. A1\_INCRI***

![20220503_141126.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5851081620759)

3. Caso seja cadastro de fornecedor,  altere no cadastro de fornecedor vinculado no campo **Fornec. Entrega F1\_FORENT na aba Informações Danfe *o campo Ins. Estad. A2\_INCRI***

![20220503_154452.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476795585175)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_NFEDEST = .T.**

![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476735187863)

5. Após isso, **exclua a nota e gere** novamente.

* **Saiba mais:**

Caso o ***IE esteja correto ou não haja informação do IE no CCC,*** será necessário entrar em contato com o Sefaz.

Caso seja operação de venda triangular ajustar os campos **C5\_CLIREM, C5\_LOJAREM e C5\_LOJAREM**, conforme o link abaixo:

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=519719230)*

* ***Validação da Sefaz:***

*![947.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4433682760983)*
