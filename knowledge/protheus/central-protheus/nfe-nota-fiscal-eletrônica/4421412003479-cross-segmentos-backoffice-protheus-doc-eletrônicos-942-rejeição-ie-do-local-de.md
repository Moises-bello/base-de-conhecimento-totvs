---
article_id: 4421412003479
category: NFe - Nota Fiscal Eletrônica
content_hash: 07797bc2d585f00615fcffae9fe8b281ecc68b8a6528d25bcceeaae9197b0f93
fetched_at: '2026-06-28T22:40:05.543892+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 942 Rejeição: IE
  do local de retirada não cadastrada'
type: support-article
updated_at: '2025-07-15T12:20:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421412003479-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-942-Rejei%C3%A7%C3%A3o-IE-do-local-de-retirada-n%C3%A3o-cadastrada
---

**Dúvida**Como solucionar 942 Rejeição: IE do local de retirada não cadastrada   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1. Acessar Cadastro de Contribuinte da UF ***(Chave: UF Retirada , IE Retirada)*** **Cadastro Centralizado de Contribuinte (CCC)** [Clique Aqui](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)

Verifique se o IE do local de retirada existe na UF de destino (operação interestadual), se o contribuinte está habilitado e se o CNPJ informado está vinculado com a IE informada, para qualquer um dos ambientes de autorização ***(SEFAZ Autorizadora ou SEFAZ Virtual);***

2. Após, verificar o **IE correto do cliente** ***de retirad*****a** altere no cadastro de cliente vinculado no campo ***Cli. Retirada** **C5\_CLIRET o campo Ins. Estad. A1\_INCRI***

![20220503_165500.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5850776327191)

3. Caso seja cadastro de fornecedor,  altere no cadastro de fornecedor vinculado no campo **Fornec. Retirada F1\_FORRET na aba Informações Danfe *o campo Ins. Estad. A2\_INCRI***

![20220503_154452.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5849075991319)

4. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **alterar** **MV\_NFEDEST = .T.**

![20220503_140213.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5846418753687)

5. Após isso, **exclua a nota e gere** novamente.

* **Saiba mais:**

Caso o ***IE esteja correto ou não haja informação do IE no CCC,*** será necessário entrar em contato com o Sefaz.

* ***Validação da Sefaz:***

![942.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4421390342679)
