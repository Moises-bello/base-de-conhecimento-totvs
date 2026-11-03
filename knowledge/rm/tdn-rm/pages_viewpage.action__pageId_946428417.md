---
content_hash: e33f985510add429e74c0f926520e25afa33af0aa5af4eae12fa058ed316f01a
fetched_at: '2026-06-29T00:12:09.493886+00:00'
page_id: '946428417'
product: rm
source: tdn-rm
title: DT - Lançamento Financeiro - Tipo "24 - Total Guia FGTS Digital"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=946428417
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Lançamento Financeiro Tipo  "24 - Total Guia FGTS Digital" |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13957](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13957 "View this issue") |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2406.280
* 12.1.2410.236
* 12.1.2502.149 e Superiores

## **03.****SITUAÇÃO/REQUISITO**

Na geração do lançamento financeiro do tipo **"24 - Total Guia FGTS Digital"**, o sistema está aplicando o percentual do FGTS sobre o valor total da base (soma da base mensal com a base de diferença). No entanto, conforme o comportamento esperado no eSocial, o percentual deve ser aplicado **separadamente** sobre a base mensal e sobre a base de diferença.

Essa divergência no cálculo resulta em diferenças de centavos entre os valores gerados pelo sistema e os enviados ao eSocial.

**04. SOLUÇÃO**

Implementamos a tratativa no cálculo do lançamento financeiro do tipo **"24 - Total Guia FGTS Digital"**, para que o percentual do FGTS seja aplicadoseparadamente sobre a base mensal e a base de diferença, alinhando-se ao comportamento esperado pelo eSocial.

**Exemplo:**

O funcionário teve sua folha processada no **período 1**, totalizando uma **base de FGTS de R$ 5.776,48**. Com a nova lógica, caso haja uma base complementar (diferença), o percentual será aplicado individualmente sobre cada base, evitando diferenças de centavos e garantindo conformidade com o eSocial.

O funcionário teve o lançamento de uma diferença no período 2, totalizando uma base de FGTS no valor de R$1.354,54.

Retorno do XML "S-5003 - Informações do FGTS por Trabalhador".

Observe que o lançamento financeiro realizou o cálculo corretamente:  
R$5.776,48 × 8% = R$462,11  
R$13.54,54 × 8% = R$108,36  
R$462,11 + 108,36 = **R$570,47**

## **05. DOCUMENTAÇÃO**

[Cadastros Financeiros](https://tdn.totvs.com.br/display/public/LRM/Cadastros+Financeiros)
