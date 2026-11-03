---
article_id: 8504462981911
category: NFe - Nota Fiscal Eletrônica
content_hash: 53250c7c62b82cae856779f41582138f108d0b151ce9be513c98f781194a4683
fetched_at: '2026-06-28T22:40:05.127591+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 551 Rejeição: IE
  da NF referenciada de produtor inválido'
type: support-article
updated_at: '2025-07-09T12:19:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8504462981911-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-551-Rejei%C3%A7%C3%A3o-IE-da-NF-referenciada-de-produtor-inv%C3%A1lido
---

**Dúvida**Como solucionar a 551 Rejeição: IE da NF referenciada de produtor inválido ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as verões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se informada NF de Produtor referenciada (tag:refNFP): – IE com zeros, nulo ou DV inválido para a UF

A SEFAZ está validando se o IE é de produtor rural e, caso seja, é necessário gerar a TAG referenciando a nota.

Para isso, quando é feita a nota de entrada, se o IE do destinatário for de produtor rural, tem que haver a tag referenciando a contranota.

* **Caso seja NFP (Nota fiscal de produtor rural) será gerada a TAG refNFP:**

1. Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = NFP ***(Esta não é transmitida).***

![20220401_141509.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347648079255)

2. Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED ***(Esta é transmitida).***Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:

***D1\_ITEMORI, D1\_SERIORI, D1\_NFORI*** (nota de entrada).

![20220401_142404.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347616131991)

3. Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota **deve ser referenciada à que foi transmitida** e não à primeira, com formulário próprio = Não.

E, para referenciar a de origem, os três campos precisam estar preenchidos:

***D1\_ITEMORI, D1\_SERIORI, D1\_NFORI***(nota de entrada)

4. Acessar o Cadastro de Contribuinte. Verifique se o ***IE do local de entrega está vinculada ao CNPJ*** no **Cadastro Centralizado de Contribuinte (CCC)**[*Clique Aqui*](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)

5. Preencher no cadastro de fornecedor,  altere o IE correto no campo***Ins. Estad. A2\_INCRI***

* **Caso seja NFPe (Nota fiscal de produtor rural eletrônica) será gerada a TAG refNFe:**

1- Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = SPED é preenchido o campo F1\_CHVNFE = com a chave da nota ***(Esta não é transmitida).***

![20220401_142758.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347616132631)

2. Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED ***(Esta é transmitida).*** Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:

***D1\_ITEMORI, D1\_SERIORI, D1\_NFORI*** (nota de entrada).

![20220401_142404.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347616131991)

3. Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.

E, para referenciar a de origem, os três campos precisam estar preenchidos:

***D1\_ITEMORI, D1\_SERIORI, D1\_NFORI (nota de entrada)***

4. Acessar o Cadastro de Contribuinte. Verifique se o ***IE do local de entrega está vinculada ao CNPJ*** no **Cadastro Centralizado de Contribuinte (CCC)**[*Clique Aqui*](https://dfe-portal.svrs.rs.gov.br/Nfe/Ccc)

5. Preencher no cadastro de fornecedor,  altere o IE correto no campo***Ins. Estad. A2\_INCRI***

* ***Validação da Sefaz:***

![551.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/8504034013335)
