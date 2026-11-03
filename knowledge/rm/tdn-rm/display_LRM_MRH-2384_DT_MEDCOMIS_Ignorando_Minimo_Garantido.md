---
content_hash: b78b7f33ba8e31020e4cd1b21815d5a66ad4e66ca224112f0c9d1aaf8906e44e
fetched_at: '2026-06-29T00:08:22.136827+00:00'
page_id: '269077311'
product: rm
source: tdn-rm
title: MRH-2384_DT_MEDCOMIS_Ignorando_Minimo_Garantido
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-2384_DT_MEDCOMIS_Ignorando_Minimo_Garantido
version: 111
---

# FUNÇÃO MEDCOMIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função de Formula* |
| **Situação/Requisito:** | *A função MEDCOMIS, possui o comportamento de quando a média do funcionário for menor que o mínimo garantido pelo sindicato, o retorno da formula será sempre o mínimo garantido, porém de acordo com as necessidades do cliente foi preciso criar uma opção para que a formula pudesse retornar o valor original da média de comissão independente de ser menor do que o mínimo.* |
| **Solução/Implementação:** | *Foi ajustada a função para que exista uma possibilidade do cliente poder ignorar o mínimo garantido no retorno da formula.*  *Desta forma anteriormente a função era utilizada da seguinte forma:*    *MEDCOMIS('1') , desta forma o sistema retornava o valor das médias de comissão, porém quando o valor da média era menor que o mínimo, a função retornava o mínimo e não o valor original.*  Foi adicionada a função uma possibilidade de passar um parâmetro após o tipo de média para informar que o mínimo será ignorado.  Desta forma caso queira que o mínimo será ignorado, o parâmetro agora deve ser utilizado da seguinte forma : MEDCOMIS(1PARAMS:S).  Onde a informação PARAMS: informa que será passado um novo parâmetro além do primeiro que indicava qual era o tipo de média , e o S informa o valor do parâmetro, que neste caso seria que o valor do mínimo seria ignorado. |
| **Chamados relacionados:** | MRH-2384 |

divs
