---
article_id: 360026459834
category: Escrita Fiscal - Impostos - ISS
content_hash: 996f8d4b56bdb723553fe7b899581fdb87c2d5deb172dc9f74b37be980be9236
fetched_at: '2026-06-28T22:39:35.128071+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Nota conjugada (mercadoria
  e serviço) deduzindo o Item de serviço do total da nota mas destacando o valor do
  serviço em duplicatas
type: support-article
updated_at: '2021-06-17T12:34:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026459834-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-conjugada-mercadoria-e-servi%C3%A7o-deduzindo-o-Item-de-servi%C3%A7o-do-total-da-nota-mas-destacando-o-valor-do-servi%C3%A7o-em-duplicatas
---

**Dúvida**  
Como gerar uma nota conjugada descontando o item de serviço no total mas considerando em duplicatas?

**Ambiente**Protheus – Compras – A partir da versão 11.80.  
  
**Solução**Para realizarmos essa tratativa é importante que o cliente tenha acesso a configuração principal de nota fiscal conjugada:

Para emissão de nota fiscal em que contenha venda de mercadoria e serviço, realize as seguintes configurações:

**Mercadoria:**

* **TES:**
* CALCULA ICMS = SIM
* LIVRO FISCAL DE ICMS = TRIBUTADO
* CFOP: 5101
* AGREGA VALOR = SIM

**Serviços:**

* **TES:**
* CALCULA ICMS = NÃO
* LIVRO FISCAL DE ICMS = NÃO
* CALCULA ISS = SIM
* LIVRO FISCAL DE ISS = TRIBUTADO.
* AGREGA VALOR = SIM
* MV\_R51CFOP = 1933/2933/5933/6933

Abaixo link contendo tratamento somente para Notas Conjugadas no Protheus:

<http://tdn.totvs.com/pages/releaseview.action?pageId=54428499>

Todo caso, para realizar a tratativa destacada no título deste artigo, será necessário configurar os seguintes campos:

No TES da nota de serviço:

Agrega Valor = NÃO

Gera Duplicata = SIM

Parâmetro = MV\_DPAGREG = .T.
