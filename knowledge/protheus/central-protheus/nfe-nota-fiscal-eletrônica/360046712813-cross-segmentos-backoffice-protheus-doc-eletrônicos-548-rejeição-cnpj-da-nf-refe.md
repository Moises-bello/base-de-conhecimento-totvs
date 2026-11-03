---
article_id: 360046712813
category: NFe - Nota Fiscal Eletrônica
content_hash: c1dcac0b9a5404090e0be4ecc56ae61e53e5defbb0485307af7d29124469b058
fetched_at: '2026-06-28T22:40:05.120708+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 548  Rejeição :
  CNPJ da NF referenciada invalido'
type: support-article
updated_at: '2025-08-12T00:37:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046712813-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-548-Rejei%C3%A7%C3%A3o-CNPJ-da-NF-referenciada-invalido
---

**Dúvida**Como solucionar a rejeição abaixo:

548 Rejeição: CNPJ da NF referenciada invalido?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Verifique se o seu XML gerou ***conforme exemplo abaixo:***

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360065500574)

2- Conforme o ***Manual de Orientação do Contribuinte página 178:***

![](https://totvssuporte.zendesk.com/attachments/token/6T2O8ssLuiPhaL8U9jbddCrRz/?name=inline1833503093.png)​  
  
A Sefaz Só é aceita a referencia de **modelo 1/ 1A com CNPJ.**  
  
O único tipo de nota aceito com CPF para a Sefaz é a de **Produtor Rural**, sendo assim é necessário que esteja como NFP que é o tipo próprio de nota para a Sefaz validar a Nota de Produtor Rural.

3- Se nota de Produtor Rural:  
  
4- Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = NFP **(Esta não é transmitida).**  
  
5- Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED **(Esta é transmitida).** Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:  
  
**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI** (nota de entrada).  
  
6 - Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.  
  
E, para referenciar a de origem, os três campos precisam estar preenchidos:  
  
**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI**(nota de entrada)  
  
7 - **Caso seja NFPe (Nota fiscal de produtor rural eletrônica)** será gerada a TAG refNFe:  
  
8- Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = SPED é preenchido o campo F1\_CHVNFE = com a chave da nota **(Esta não é transmitida).**  
  
9- Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED **(Esta é transmitida).** Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:  
  
**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI** (nota de entrada).  
  
10 - Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.  
  
E, para referenciar a de origem, os três campos precisam estar preenchidos:  
**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI (nota de entrada)**  
  
  
11 - Caso a nota seja de origem seja uma  **refNFe =** Modelo 55 Espécie = SPED, os campos devem estar preenchidos F1 ou F2\_ESPECIE = SPED,  FT\_ESPECIE e F3\_ESPECIE = SPED,  F1 ou F2\_CHVNFE = com a chave da nota, F3\_CHVNFE e FT\_CHVNFE = com a chave da nota;

12 - Se houver CNPJ preencher no cadastro de fornecedor ou cliente.

13- Se realmente a nota for uma **refNF=** Modelo 01, 01A, 02 Espécie = NF, NFe, NFA ou NFCF**sem CNPJ**a Sefaz não aceitará essa operação. 

* **Validação da Sefaz:**

![](https://totvssuporte.zendesk.com/attachments/token/xpfHu37nwve3CZecTvOqi5kA4/?name=inline1289926743.png)
