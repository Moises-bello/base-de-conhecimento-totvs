---
article_id: 360048287154
category: NFe - Nota Fiscal Eletrônica
content_hash: ccecce18445b40b5a7fc663fcd20c6943de703e091b3ea4c500dbd1e094aec83
fetched_at: '2026-06-28T22:40:00.453382+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 029: Falha de
  schema na Tag <mod>'
type: support-article
updated_at: '2021-10-11T15:08:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048287154--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-029-Falha-de-schema-na-Tag-mod
---

**Dúvida**Como solucionar a falha de Schema referente a TAG mod ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1 - Ao gerar falha de Schema referente ao **mod** verifique se o seu XML gerou conforme o exemplo abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072446033/mceclip1.png)

2 -A Sefaz só permite as Especie de notas abaixo:​

* **refCTe =**Modelo 57 Espécie = CTE

Caso a nota seja de origem seja uma  refNFe = Modelo 57 Espécie = CTE, os campos devem estar preenchidos F1 ou F2\_ESPECIE = CTE,  FT\_ESPECIE e F3\_ESPECIE = CTE,  F1 ou F2\_CHVNFE = com a chave da nota, F3\_CHVNFE e FT\_CHVNFE = com a chave da nota;

* **refNFe =** Modelo 55 Espécie = SPED

Caso a nota seja de origem seja uma  refNFe = Modelo 55 Espécie = SPED, os campos devem estar preenchidos F1 ou F2\_ESPECIE = SPED,  FT\_ESPECIE e F3\_ESPECIE = SPED,  F1 ou F2\_CHVNFE = com a chave da nota, F3\_CHVNFE e FT\_CHVNFE = com a chave da nota;

* **Caso seja NFPe (Nota fiscal de produtor rural eletrônica) será gerada a TAG refNFe:**

1- Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = SPED é preenchido o campo F1\_CHVNFE = com a chave da nota **(Esta não é transmitida).**  
  
  
2- Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED **(Esta é transmitida).** Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:  
**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI** (nota de entrada).  
  
  
3- Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.  
  
  
E, para referenciar a de origem, os três campos precisam estar preenchidos:  
  
**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI (nota de entrada)**

* **refNF=** Modelo 01, 01A, 02

Caso seja  os campos devem estar preenchidos F1 ou F2\_ESPECIE NF, NFe, NFA ou NFCF, FT\_ESPECIE e F3\_ESPECIE = NF, NFe, NFA ou NFCF  (modelo novo incluído na 4.00)

* **refNFP =** Modelo 04 ( Nota de produtor rural)

* **Caso seja NFP (Nota fiscal de produtor rural) será gerada a TAG refNFP:**

1- Primeiro, é feita uma nota de Entrada com formulário próprio = Não Espécie = NFP **(Esta não é transmitida).**  
  
  
2- Depois, é feita uma nota de Entrada com formulário próprio = Sim Espécie = SPED **(Esta é transmitida).**  
  
 Esta nota deve ser referenciada à anterior que não foi transmitida. E, para referenciar a de origem, os três campos a seguir precisam estar preenchidos:  
**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI** (nota de entrada).  
  
  
3- Quando é feita uma nota complementar ou de devolução, elas devem ter formulário próprio = Sim Espécie = SPED e essa nota deve ser referenciada à que foi transmitida e não à primeira, com formulário próprio = Não.  
  
  
E, para referenciar a de origem, os três campos precisam estar preenchidos:  
  
  
**D1\_ITEMORI, D1\_SERIORI, D1\_NFORI**(nota de entrada)
