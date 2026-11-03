---
article_id: 4433554205335
category: NFe - Nota Fiscal Eletrônica
content_hash: a08eeb5787612b814a9f4cdf439c9518b16fde0e5dcbf34a085b6a71481a2812
fetched_at: '2026-06-28T22:40:05.554177+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 944 Rejeição: IE
  do local de retirada não vinculada ao CPF'
type: support-article
updated_at: '2022-05-03T19:58:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4433554205335-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-944-Rejei%C3%A7%C3%A3o-IE-do-local-de-retirada-n%C3%A3o-vinculada-ao-CPF
---

**Dúvida**Como corrigir a 944 Rejeição: IE do local de retirada não vinculada ao CPF ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informado ***CPF do local de retirada e IE do local de retirada não vinculada***  
***ao CPF***

1. Acessar Cadastro de Contribuinte verifique se o ***CPF do local de retirada e IE do local de retirada** estão vinculados.*[Clique Aqui](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)

2. Após, verificar o **IE correto do cliente** ***de retirad*****a** altere no cadastro de cliente vinculado no campo ***Cli. Retirada** **C5\_CLIRET o campo Ins. Estad. A1\_INCRI***

![20220503_165500.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5850776327191/20220503_165500.gif)

3. Caso seja cadastro de fornecedor,  altere no cadastro de fornecedor vinculado no campo **Fornec. Retirada F1\_FORRET na aba Informações Danfe *o campo Ins. Estad. A2\_INCRI***

![20220503_154452.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5849075991319/20220503_154452.gif)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_NFEDEST = .T.**

![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5846418753687/20220503_140213.gif)

5. Após isso, **exclua a nota e gere** novamente.

* **Saiba mais:**

Caso o ***IE esteja correto ou não haja informação do IE no CCC,*** será necessário entrar em contato com o Sefaz.

* ***Validação da Sefaz:***

***![944_rejeicao.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4433550427927/944_rejeicao.PNG)***
