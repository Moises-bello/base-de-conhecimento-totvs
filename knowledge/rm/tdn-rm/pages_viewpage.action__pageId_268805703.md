---
content_hash: f3afc8fcaace476bbd0a1a611ec6398fc0efb713725ddb3da3fb92998da85c4c
fetched_at: '2026-06-29T00:08:20.996818+00:00'
page_id: '268805703'
product: rm
source: tdn-rm
title: TW3987_DT_Geração_Lançamento_Com_Valor_Liquido_Negativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268805703
version: 109
---

# Geração de Lançamento

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | Geração de Lançamento |
| **Situação/Requisito:** | Temos situações em que o total de desconto concedido irá ultrapassar o valor original do lançamento em função dos arredondamentos e neste caso o valor líquido do lançamento financeiro ficará negativo (esta situação foi simulada parametrizando uma bolsa com a opção "Aplicar maior bolsa").  Com isso quando o sistema está parametrizado para baixar automaticamente lançamentos com valores liquido zerado estes lançamentos não são baixados.    Desta forma o cliente era obrigado a ajustar manualmente o lançamento.  Exemplo:  ------------------------------------------------------------  Desconto da Parcela 5 %   = 40,70 (valor calculado 40,695)  Bolsa de 95 %             = 773,21(valor calculado 773,205)  ------------------------------------------------------------  Valor total dos descontos = 813,91  ------------------------------------------------------------  Valor da Parcela          = 813,90  ------------------------------------------------------------ |
| **Solução/Implementação:** | Quando o cenário acima ocorrer, iremos estabelecer uma margem de ajuste de 0,01 centavos para o desconto e para cada bolsa (tipo=percentual), ou seja, se a diferença do valor total do desconto em relação ao valor original do lançamento estiver dentro desta margem, iremos ajusta o desconto para que o valor feche com o valor original.  Como no exemplo acima temos desconto na parcela e apenas uma bolsa, então a margem de ajuste será de 0.02 centavos, com isso a diferença é de 0,01 centavo e neste caso o sistema ajustara o desconto da bolsa para que o valor liquido do lançamento feche com o valor original do lançamento. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TW3987 |
| **Requisito (ISSUE):** | *N/A* |

divs
