---
content_hash: d6d3f5dc0f26107af05caea9514abca264132a920772f0745a567a18f55d3cb2
fetched_at: '2026-06-29T00:08:03.938418+00:00'
page_id: '235330312'
product: rm
source: tdn-rm
title: TUMVYZ_DT_DIRF_Multiplos_Vinculos_Dados_Operadora_Saude
type: documentation
url: https://tdn.totvs.com/display/LRM/TUMVYZ_DT_DIRF_Multiplos_Vinculos_Dados_Operadora_Saude
version: 117
---

# DIRF/INFORME DE RENDIMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Quando existe um funcionário que possui duas chapas na mesma coligada, e ao gerar a DIRF marcando o parâmetro Com IRRF ou Rendimentos acima de R$ 6000 ou assalariado com rendimentos acima de 28123,91 ao gerar o Informe de rendimentos o sistema busca os valores de assistência à saúde porém ao realizar a geração da DIRF o valor de assistência à saúde não é levado.   Se o processo for realizado com o filtro todos estas informações são levadas. |
| **Solução/Implementação:** | *Ajustado para agrupar as informações com o mesmo CPF quando tem informação de assistência à saúde.* |
| **Chamados relacionados:** | *TUMVYZ,TUPRQV* |

divs
