---
article_id: 4407610573975
category: NFe - Nota Fiscal Eletrônica
content_hash: 1136be5a139d6e18ca6a9717e56d55555905530c4101b83da5f78186bb3260f7
fetched_at: '2026-06-28T22:40:07.196589+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - type mismatch on
  +  on NFEPAG(NFESEFAZ.PRW) '
type: support-article
updated_at: '2021-09-01T19:33:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407610573975-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-type-mismatch-on-on-NFEPAG-NFESEFAZ-PRW
---

**Dúvida**Como solucionar a mensagem type mismatch on + on NFEPAG(NFESEFAZ.PRW)   
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**1 -** Crie os parâmetros abaixo, **verifique se os parâmetros estão como Caractere  e se está preenchido o conteúdo.**

Para inclusão/alteração dos parâmetros, acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir** e informar:

**Parâmetro****utilizado em operações de saída (Faturamento):**

Nome de Var.: **MV\_MFATIPR**

Tipo: **1 - Caractere**

Cont. Por: **"Negociação Futura"**

![](https://tdn.totvs.com.br/download/attachments/626650334/image2021-6-29_20-3-17.png?version=1&modificationDate=1625007797530&api=v2)

**Parâmetro****utilizado em operações de entrada (Compras):**

Nome de Var.: **MV\_TPAGCOM**

Tipo: **1 - Caractere**

Cont. Por: **"Negociação Futura"**

![](https://tdn.totvs.com.br/download/attachments/626650334/image2021-6-29_20-3-47.png?version=1&modificationDate=1625007828070&api=v2)
