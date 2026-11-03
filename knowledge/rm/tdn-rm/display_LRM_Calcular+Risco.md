---
content_hash: b7a3d474ff0b92edbb0426be729177ca885642167c45c2f9d6b85ad03d65bd24
fetched_at: '2026-06-29T00:09:15.505530+00:00'
page_id: '421385396'
product: rm
source: tdn-rm
title: Calcular Risco
type: documentation
url: https://tdn.totvs.com/display/LRM/Calcular+Risco
version: 3
---

O processo de calcular risco é constitui as seguintes etapas:

* **Cálculo do índice de importância** -  Calcula o valor atual do índice de importância do risco e o valor do índice de importância em cada reunião em aberto na qual o risco esteja associada.

O cálculo do índice de importância é dado pelos seguintes passos:

1. Obtém-se os valores de impacto e probabilidade, sobre os objetivos do projeto, associados ao risco.
2. Para cada objetivo em que o risco tenha valores de impacto e probabilidade definidos, multiplica-se o impacto pela probabilidade.
3. Soma o resultado da multiplicação obtida em cada objetivo para obtenção do índice de importância do risco.

∑ {Para todo objetivo do projeto} Peso Impacto x Probabilidade  
 **Exemplo:**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Objetivo do Projeto | Pesos |  |  | Total |
|  | Impacto | Probabilidade |  |
| Custo | 0,7 | 0,8 | 0,56 |
| Tempo | 0,3 | 0,9 | 0,27 |
| Qualidade | 0,2 | 0,4 | 0,08 |
|  |  |  | **0,91** |

**Índice de Importância do Risco =  0,91**  
**Observação:**

* O impacto e probabilidade considerados no cálculo para o campo "índice de importância atual" (visão do risco) são os valores associados a reunião mais recente;
* O impacto e probabilidade considerados no cálculo para o campo "índice de importância" (Anexos - Reuniões) são os valores mais recentes definidos até a data de abertura da reunião.

**Atenção:**

* Não serão calculados índices de importância vinculados a reuniões com status encerrada;
* O valor zero será atribuído ao peso caso não exista intervalo definido na escala.

* **Cálculo da matriz de impacto e probabilidade de objetivos**

O cálculo é constituído pelos seguintes passos:

1. 1. Obtenção de todos os objetivos do projeto em que o risco tenha valores de impacto e probabilidade definidos. Sendo considerados os valores mais atuais de impacto e probabilidade para cada objetivo.
   2. Para cada valor de impacto e probabilidade é verificado na escala parametrizada no projeto sobre qual quadrante da matriz o objetivo será posicionado.
   3. Os valores dos quadrantes são salvos e serão posteriormente utilizados para gerar a matriz através do anexo do risco  .

* **Cálculo dos valores incidentes no impacto e probabilidade**

1. Obtenção dos valores de incidência planejada e realizada referente a todas as medidas de contenção/impulsão.
2. Obtenção dos valores mais atuais de impacto e probabilidade associados a cada objetivo do projeto sobre um risco
3. Para cada valor de impacto e probabilidade são calculados os valores referentes aos seguintes campos da tela de impacto e probabilidade:

Valores com incidências de medidas planejadas:

* Impacto: (Impacto principal) + (Soma dos valores de impacto planejado, definido no anexo de incidência de impacto e probabilidade, de todas as medidas de contenção/impulsão referente ao mesmo objetivo do projeto do registro de impacto e probabilidade).
* Probabilidade: (Probabilidade principal) + (Soma dos valores de probabilidade planejada, definida no anexo de incidência de impacto e probabilidade, de todas as medidas de contenção/impulsão referente ao mesmo objetivo do projeto do registro de impacto e probabilidade)

Valores com incidências de medidas realizadas:

* Impacto: (Impacto principal) + (Soma dos valores de impacto realizado, definido no anexo de incidência de impacto e probabilidade, de todas as medidas de contenção/impulsão referente ao mesmo objetivo do projeto do registro de impacto e probabilidade).
* Probabilidade: (Probabilidade principal) + (Soma dos valores de probabilidade realiza, definida no anexo de incidência de impacto e probabilidade, de todas as medidas de contenção/impulsão referente ao mesmo objetivo do projeto do registro de impacto e probabilidade).

**Observações:**

* O processo calcular risco poderá ser executado para mais de um risco;
* Para execução do processo é necessário que os parâmetros "Escala", "Grupo de objetivos" e "Grupo de áreas de prioridade" esteja definidos.
