---
article_id: 4441711528343
category: NFe - Nota Fiscal Eletrônica
content_hash: e9e25308cada8d86014723f89749f54e41c08900c9b5b9fcfea2a16e5022150f
fetched_at: '2026-06-28T22:40:05.564578+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 948 Rejeição: IE
  do local de entrega não vinculada ao CPF'
type: support-article
updated_at: '2025-07-15T12:11:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441711528343-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-948-Rejei%C3%A7%C3%A3o-IE-do-local-de-entrega-n%C3%A3o-vinculada-ao-CPF
---

**Dúvida**Como solucionar a 948 Rejeição: IE do local de entrega não vinculada ao CPF  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informado ***CPF do local de entrega e IE*** do local de entrega ***não vinculada ao CPF.***

1. Acessar Cadastro de Contribuinte Verifique se ***CPF do local de entrega e IE do local de entrega não vinculada ao CPF*** (tratar Regime Especial de IE Única) **Cadastro Centralizado de Contribuinte (CCC)** [*Clique Aqui*](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)

2. Após, verificar o **IE correto do cliente** ***de retirad*****a** altere no cadastro de cliente vinculado no campo ***Cli. Entrega** **C5\_CLIENT o campo Ins. Estad. A1\_INCRI***

![20220503_141126.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476730733463)

3. Caso seja cadastro de fornecedor,  altere no cadastro de fornecedor vinculado no campo **Fornec. Entrega F1\_FORENT na aba Informações Danfe *o campo Ins. Estad. A2\_INCRI***

![20220503_154452.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476730735127)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_NFEDEST = .T.**

![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33476740909847)

5. Após isso, **exclua a nota e gere** novamente.

* **Saiba mais:**

Caso o ***IE esteja correto ou não haja informação do IE no CCC,*** será necessário entrar em contato com o Sefaz.

Caso seja operação de venda triangular ajustar os campos **C5\_CLIREM, C5\_LOJAREM e C5\_LOJAREM**, conforme o link abaixo:

*[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=519719230)*
