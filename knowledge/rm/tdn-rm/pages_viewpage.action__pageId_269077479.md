---
content_hash: 9981cd24d0b182dcafa89e8ab73a34bfd634e100181a9e89ebf8c53cb1d1370a
fetched_at: '2026-06-29T00:08:22.140407+00:00'
page_id: '269077479'
product: rm
source: tdn-rm
title: 98545_DT_Cálculo_Valor_Liquido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269077479
version: 114
---

# Cálculo Valor Líquido

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Cálculo Valor Líquido. |
| **Situação/Requisito:** | Após executar um vinculo, para lançamentos que possuem multa e/ou juros calculado ao dia, onde, o sistema está parametrizado para utilizar o valor líquido parcial como valor base para cálculo, o valor líquido calculado está ficando negativo. |
| **Solução/Implementação:** | - No momento do vínculo o sistema irá verificar se o lançamento comum possui juros ou multa calculado como taxa ao dia e utiliza   como base para cálculo o valor líquido parcial.  - Quando o vínculo apresentar as características anteriores, será verificado se o Crédito de Adiantamento foi gerado antes ou depois da geração da   lançamento comum.  - Se já existir o credito de adiantamento antes do lançamento comum, a data máxima que poderá ser utilizada para vínculo será a data de vencimento do  lançamento comum, mesmo o vínculo sendo feito após esta data. Dessa forma, não será cobrado juros ou multa por já existir um credito de adiantamento  anterior.  Obs: Este comportamento também será observado após o vínculo, desta forma o cálculo do valor líquido ou baixa após a data do vínculo não irá calcular   juros ou multa.  Obs: Se não existir o Crédito antes do lançamento comum, a data máxima que poderá ser utilizada para calcular o valor líquido para o vínculo   será a data de emissão do Crédito de adiantamento, desta forma, os juros ou multa serão calculados até a data onde o cliente/fornecedor   passa a ter crédito.  Obs: Neste cenário não será possível fazer vários vínculos simultâneos, ou seja, após vincular uma mensalidade a um credito, deverá ser salvo   este vínculo para poder executar o próximo vinculo. |
| **Conversores e Parâmetros:** | NA. |
| **Chamados relacionados:** | 98545 |
| **Requisito (ISSUE):** | FIN000254. |

divs
