---
article_id: 360019492591
category: Financeiro - Contas a Pagar
content_hash: 9e98428943a0c6e363eefa92aee06a1cc61ee8e214c5e73262be28603d7493fc
fetched_at: '2026-06-28T22:38:08.311225+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA340 - Configuração
  dos parâmetros utilizados na Compensação '
type: support-article
updated_at: '2021-09-20T17:57:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019492591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Configura%C3%A7%C3%A3o-dos-par%C3%A2metros-utilizados-na-Compensa%C3%A7%C3%A3o
---

**Dúvida**  
Como configurar os parâmetros utilizados na rotina de Compensação a Pagar (FINA340):  
  
**Ambiente**  
Cross Segmento - BackOffice Linha Protheus – Financeiro  - A partir da versão 11.80  
  
  
**Solução**O parâmetro **MV\_PABRUTO** caso esteja com o valor 2 (Líquido), ao gerar títulos do tipo PA é mantida a geração com o valor líquido, em que são descontados os valores de impostos que podem ser retidos na inclusão.

Ao realizar a compensação de um título, por exemplo, do tipo NF com uma PA, sendo que ambas retêm impostos na baixa, é aconselhável os parâmetros abaixo sejam configurados da seguinte maneira, para que haja coerência de valores:

**MV\_COMPCP = .T.** - Indica se na compensação de uma NF com um PA os impostos serão proporcionalizados.  
**MV\_BP10925 = 2** - Considera valor Líquido na baixa Parcial descontados os impostos.  
**MV\_PAPRIME = 1** - Considera provisionamento de impostos para PA Líquido.

Quando o parâmetro **MV\_PABRUTO** estiver igual a 1 (Bruto) ao gerar títulos do tipo PA (Pagamentos Antecipados), é gerado com o valor bruto, não descontando os valores de impostos que podem ser retidos na inclusão. Então a compensação de uma NF com uma PA, deveria ser pelo valor bruto configurando os parâmetros conforme abaixo:

**MV\_PABRUTO = 1** - Bruto e **MV\_BX10925 = 1** Imposto na baixa ou **MV\_BX10925=2** Imposto na emissão  
**MV\_BP10925 = 1** - Considera valor Bruto na baixa Parcial sem descontar os impostos.  
**MV\_PAPRIME = 2** - Não considera provisionamento de impostos para PA Líquido.  
Observação.:

O parâmetro **MV\_COMPCP** não influencia caso o parâmetro **MV\_PABRUTO** esteja com o valor em 1. Independente dos títulos terem impostos, ou não, é necessário a parametrização.

A compensação entre NF x PA, partindo tanto da NF como do PA, não é permitida caso o parâmetro **MV\_PABRUTO** esteja com o valor 2 (Líquido) e as naturezas estiverem diferentes.

**Saiba Mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=354465728>
