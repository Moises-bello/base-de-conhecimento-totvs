---
content_hash: 02449cf1b4d826a7eee8ca83ad5eb7624240482fcdfec5a7e56f3abea227876c
fetched_at: '2026-06-29T00:09:14.080813+00:00'
page_id: '421385115'
product: rm
source: tdn-rm
title: Impacto e Probabilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/Impacto+e+Probabilidade
version: 5
---

Permitir definir valores para probabilidade e o impacto de cada objetivo de um risco a cada reunião de acompanhamento.

A definição de impacto e probabilidade por reunião irá permitir um melhor acompanhamento do risco.

Para incluir e definir os impactos e probabilidades informe os campos abaixo:

**Objetivo do Projeto:**Esse campo lista todo os objetivos do projeto que estão vinculados a um grupo de objetivos (e esse grupo de objetivos deve estar informado nos parâmetros de projeto) veja mais detalhes em:

É importante verificar se o que objetivo desejado esteja dentro do grupo de objetivos do projeto e também informado o grupo de objetivos nos parâmetros de projeto pois faltando alguma dessas condições não será possível visualiza-lo na criação dos impactos e probabilidade.

**Reunião:** Informe a reunião que deseja vincular

Em seguida siga informando:

**objetivo quantitativo:**

**Valores principais:**

* Probabilidade - deverá ser informado o percentual de 0 a 100.
* Valor Máximo de Exposição (VME) = Impacto (principal) x Probabilidade (principal)

**Valores com incidências de medidas planejadas:**

* Impacto e probabilidade - Serão obtidos através do Cálculo dos valores incidentes no impacto e probabilidade presente no  .
* Valor Máximo de Exposição (VME) = Impacto (com incidências de medidas planejadas) x Probabilidade (com incidências de medidas planejadas)

**Valores com incidências de medidas realizadas:**

* Impacto e probabilidade - Serão obtidos através do Cálculo dos valores incidentes no impacto e probabilidade presente no  .
* Valor Máximo de Exposição (VME) = Impacto (com incidências de medidas realizadas) x Probabilidade (com incidências de medidas realizadas)

**Observação:**

* Os campos valores com incidência de medidas planejadas, incidência de medidas realizadas e VME ficarão desabilitados para inclusão.  O Preenchimento destes campos será através do processo de  ;
* Somente as reuniões associadas ao risco, que estiverem em andamento, ficarão visíveis para associar a um impacto e probabilidade;
* A probabilidade com incidência de medida planejada e com incidência de medida realizada terá seu valor definido no intervalo de 0 a 100%.

**Objetivo Qualitativo:**

* Impacto - deverá ser informado o atributo qualitativo previamente cadastrado no objetivo do projeto.
* Probabilidade - deverá ser informado o percentual de 0 a 100.

**Observações:**

* A definição do impacto e da probabilidade deve ser realizada quando um risco estiver com status em aberto ou após o seu planejamento se o mesmo estiver com status de mitigar, transferir/mitigar ou aceitar ativamente no caso de ameaças, ou estiver com status melhorar ou melhorar/compartilhar no caso de oportunidades.  Portanto não deve ser permitida alteração de impacto e probabilidade quando o risco estiver com status eliminar (ameaças), explorar (oportunidade) ou aceitar;
* O impacto e probabilidade associado a uma reunião encerrada não poderá ser editado ou excluído.

Os Objetivos do Projeto disponíveis para seleção serão os que pertenceram ao grupo definido no parâmetro do projeto.   
Se definido um Objetivo do Projeto qualitativo, ficarão habilitados os campos Impacto e Probabilidade (%) do grupo qualitativo. Se definido um objetivo do projeto quantitativo, ficarão habilitados os campos Impacto e Probabilidade (%) do grupo quantitativo.  
  
Os campos referente ao impacto e VME tem suas casas decimais definidas em: Parâmetros do projetos - Exibição - Geral - Casas decimais - Coeficientes.  
  
Os campos referente a probabilidade tem suas casas decimais definidas em: Parâmetros do projetos - Exibição - Geral - Casas decimais - Percentuais.
