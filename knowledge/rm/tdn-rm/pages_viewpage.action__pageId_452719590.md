---
content_hash: e8ab41d9ba728645385a5cc5eda2beadb4d80f881f808975c8c1372584a9fcb4
fetched_at: '2026-06-29T00:10:08.832088+00:00'
page_id: '452719590'
product: rm
source: tdn-rm
title: Gráfico - Avaliação de desempenho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719590
version: 2
---

**Gráfico - Avaliação de desempenho**

Serão disponibilizados três modelos de gráficos:

* Comparativo do percentual de aproveitamento,
* Comparativo de notas
* Quadrante: Potencial x Desempenho.

Os valores exibidos nos gráficos poderão ser visualizados também na pasta "Resultados". Para cada modelo de gráfico é executada uma rotina de cálculo, veja abaixo as rotinas executadas:

**1) Comparativo do percentual de aproveitamento** - Neste gráfico, o aproveitamento é calculado da seguinte forma:

% Aproveitamento = (Nota / Nota máxima)x100,

sendo que:

Nota = Nota obtida x Peso do item x Peso do avaliador x Peso na função

Nota máxima = Nota máxima obtida x Peso do item x Peso do avaliador x Peso na função, onde:

**Nota obtida** = Nota do avaliador, ou seja, refere-se à nota que o avaliador informou para cada item avaliado. O valor considerado é aquele definido no campo "valor" da escala gráfica utilizada na avaliação. Para verificar estes valores utilize a opção "Alterar escalas(notas)" existente na pasta "Configurações".

**Nota máxima obtida**: Refere-se à maior nota que o avaliador poderia informar para cada item avaliado. O valor considerado é aquele definido no campo "valor" da escala gráfica utilizada na avaliação. Para verificar qual seria este valor máximo utilize a opção "Alterar escalas(notas)" existente na pasta "Configurações" e identifique qual a maior escala da avaliação.

**Peso do item**: Peso do item na avaliação. Se o escala gráfica escolhida nas opções de "Configurações" da avaliação for simples, este peso será igual a 1(um); se for mista, o peso do item será aquele informado pelo usuário durante a montagem.

**Peso do avaliador**: Peso do avaliador na avaliação. Se o modelo de avaliação escolhido nas opções de "Configurações" da avaliação for 90 graus ou 180 graus, o peso será igual a 1(um); se for 360 graus, o peso do avaliador será aquele informado pelo usuário na pasta "Avaliadores/avaliados".

**Peso na função**: Refere-se à ordem de graduação do item na função. Este peso é importante quando o item avaliado é uma competência. Para verificar este peso, consulte na função a competência que esta sendo avaliada. Em seguida verifique a graduação desta competência; já no cadastro da graduação em questão verifique o valor do campo "Graduação da competência". Este será o valor considerado para o peso na função.

**Observação**

No caso de ações e fatores organizacionais o peso na função será sempre igual a 1(um).

**A****tenção**

Quando a avaliação estiver agrupada por cargo e a competência avaliada não estiver vinculada à função do avaliado, o valor considerado para o peso das competências que aparecem em mais de uma função será o maior valor; já as competências que estão vinculadas na função do avaliado e que também aparecem em outras funções do mesmo cargo, será considerando o peso da competência associada na função do avaliado.

**2) Comparativo de notas**

Este gráfico tem o objetivo de correlacionar as notas das pessoas avaliadas com a nota máxima que cada uma poderia obter. Os valores utilizados neste gráfico são:

a soma das notas (A) de cada item avaliado e a nota máxima(B) que poderia ser obtida na avaliação, sendo que:

Nota = Nota obtida x Peso do item x Peso do avaliador

Nota máxima = Nota máxima obtida x Peso do item x Peso do avaliador,onde:

**Nota do obtida**: Refere-se à nota que o avaliador informou para cada item avaliado. O valor considerado é aquele definido no campo "valor" da escala gráfica utilizada na avaliação. Para verificar estes valores utilize a opção "Alterar escalas(notas)" existente na pasta "Configurações".

**Nota máxima obtida**: Refere-se à maior nota que o avaliador poderia informar para cada item avaliado. O valor considerado é aquele definido no campo "valor" da escala gráfica utilizada na avaliação. Para verificar qual seria este valor máximo utilize a opção "Alterar escalas(notas)" existente na pasta "Configurações" e identifique qual a maior escala da avaliação.

**Peso do item:** Peso do item na avaliação. Se o escala gráfica escolhida nas opções de "Configurações" da avaliação for simples, este peso será igual a 1. Se for mista, o peso do item será aquele informado pelo usuário durante a montagem.

**Peso do avaliador:** Peso do avaliador na avaliação. Se o modelo de avaliação escolhido nas opções de "Configurações" da avaliação for 90 graus ou 180 graus, o peso será igual a 1 (um); se for 360 graus, o peso do avaliador será aquele informado pelo usuário na pasta "Avaliadores/avaliados".

**3) Quadrante: Potencial x Desempenho** Cada item selecionado para comparação na tela de montagem do gráfico representa um ponto no quadrante. Diferentemente dos demais gráficos, o quadrante sempre precisa de dois valores para cada ponto plotado. O primeiro valor, eixo x, refere-se ao percentual de aproveitamento obtido pela avaliação das ações prescritas para cada avaliado. O segundo valor, eixo y, corresponde ao percentual de aproveitamento obtido pela avaliação das competências de cada avaliado. Desta forma, cada ponto no gráfico representa uma relação entre um conjunto de competências (potencial) e um conjunto de ações (resultado).

Para o cálculo do percentual de aproveitamento a fórmula utilizada é: % Aproveitamento = (Nota / Nota máxima)x100.

**Atenção**

A fórmula é a mesma considerada para o gráfico comparativo de notas, porém são consideradas, no cálculo, apenas as competências (eixo y) e ações (eixo x).

**Observação**

- Para qualquer um dos gráficos, caso seja utilizado o filtro por seção, função ou cargo, serão verificadas todas as pessoas avaliadas e o agrupamento para o cálculo da nota será feito conforme filtro selecionado.

Por exemplo, quando o usuário selecionar uma função, estará selecionando para o sistema um conjunto de todos os avaliados que estão efetivamente cadastrados nestas funções. O sistema calculará uma nota geral a partir da média aritmética das notas de todos os avaliados pertencentes á função. A nota final será então a proporção entre esta média e a média das notas máximas destes mesmos avaliados.

- Para o modelo de avaliação 180 graus serão considerados para o cálculo os valores da avaliação consensual.

- Para o modelo de avaliação 360 graus será considerado para o cálculo a média aritmética das notas obtidas e notas máximas das avaliações realizadas, pois neste modelo vários avaliadores podem avaliar um mesmo avaliado.
