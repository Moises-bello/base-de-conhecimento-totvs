---
content_hash: 77b268602270bc40115356080c15a23b331693a77a1ae64f9791643a0cef41cf
fetched_at: '2026-06-29T00:08:28.197562+00:00'
page_id: '271667053'
product: rm
source: tdn-rm
title: 493042 MEDU-2625 DT Bolsa 100% com valor líquido resultante do lançamento maior
  que zero
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271667053
version: 109
---

# BOLSA 100% COM VALOR LÍQUIDO RESULTANTE DO LANÇAMENTO MAIOR DO QUE ZERO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Geração de lançamentos / Simulação de valores* |
| **Situação/Requisito:** | *Sistema com bolsa 100% arredonda os valores de forma que o valor líquido fique com 0,01 (um centavo) de diferença* |
| **Solução/Implementação:** | *Comparação do valor total de descontos com o valor original do lançamento considerando uma margem para ajustes. Se o valor da diferença estiver dentro da margem de ajuste, a diferença será somada aos valores de descontos.*  *A margem será considerada a partir de 0,01 centavo para cada tipo de desconto que o aluno possuir.*  *Se o aluno possuir somente o desconto na parcela, a margem será igual a 0,01*  *Se o aluno possuir o desconto na parcela e uma bolsa,  a margem será igual a 0,02*  *Se o aluno possuir três bolsas a serem aplicadas na parcela, a margem será igual a 0,03*  *Essa margem será considerada para fins de comparação com a diferença entre os valores totais de descontos e o valor original do lançamento a fim de se evitar que os vários arredondamentos feitos para valores de bolsas e descontos façam com que tenhamos um resultado inesperado no valor líquido do lançamento.*  ***Exemplo**:*  *Parcela calculada por número de créditos totalizando 100,995 *Sistema parametrizado para se trabalhar com duas casas decimais Bolsa de 100% totalizando 100,99**  **Sistema verificará que a diferença entre os valores de bolsas (descontos) - valor original do lançamento = 0,005 (menor que a margem de 0,01) e somará o valor de 0,005 aos valores de bolsas fazendo com que o valor líquido do lançamento seja igual a zero.** |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | *N/A* |

divs
