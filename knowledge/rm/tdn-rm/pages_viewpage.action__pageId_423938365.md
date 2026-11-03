---
content_hash: d981eae91fdeb90c3c40e1bb2a1010e07df67f1edb9fd2da6a9408a7a60504ad
fetched_at: '2026-06-29T00:09:26.681062+00:00'
page_id: '423938365'
product: rm
source: tdn-rm
title: Distribuição de Valores por Filial 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938365
version: 2
---

A distribuição de valores por filial tem como objetivo ratear, para cada filial, todos os valores previamente calculados para os patrimônios de acordo com o período em que eles permaneceram nas filiais através das Transferências de Controle existentes. Esse processo deve ser executado para geração do relatório de "Agrupamento por tempo filial" e para a realização da contabilização rateada por tempo de permanência dos patrimônios em cada filial.

Para a utilização do processo deve-se primeiramente habilitar em Opções | Parâmetros | RM Bonum | Integração, o parâmetro "Contabilizar por tempo em cada filial".  
A seguir serão descritas as validações e a regra de negócio aplicada na distribuição de valores por filial.  
   
**Seleção do tipo de distribuição**

A distribuição de valores por filial poderá ser realizada para "Todos os patrimônios", para "Os patrimônios determinados automaticamente pelo sistema" ou para "Os patrimônios selecionados" pelo usuário. Caso o usuário opte por selecionar as opções "Todos os patrimônios" ou "Os patrimônios determinados automaticamente pelo sistema", o sistema irá solicitar apenas a execução do processo, pois, os patrimônios serão automaticamente selecionados pelo sistema. Caso o usuário opte por utilizar "Os patrimônios selecionados" será necessário passar por uma nova etapa do processo, onde haverá um lookup que exibirá apenas patrimônios que não foram baixados em período anterior. Ao final da execução será gerado um log informando o status da execução.

**Regras sobre o processo:**

* Relatório Agrupamento por Tempo Filial: Através deste relatório será possível visualizar a depreciação dos patrimônios de forma rateada, baseando-se no tempo que ele permaneceu em cada filial. Ele só poderá ser acessado se parâmetro de sistema "Contabilizar por tempo em cada filial" estiver marcado. Vale ressaltar que o processo de distribuição de valores deverá ser executado antes da emissão do relatório. Somente assim será possível gerar as informações necessárias para exibição do relatório "Agrupamento por tempo filial".
* Contabilização da Depreciação/Correção Monetária: Na tela de parâmetros desse processo haverá a opção "Contabilizar por tempo em cada filial". Se o parâmetro de sistema "Contabilizar por tempo em cada filial" estiver marcado esta opção sempre virá marcada. Estando marcada, a contabilização deverá contemplar a distribuição de valores por filial, respeitando o período de permanência do patrimônio em cada filial. Vale ressaltar que o processo de distribuição de valores deverá ser executado, para todos os patrimônios, antes da contabilização. Somente assim será possível gerar as informações necessárias para realização da contabilização por filial. Atenção: Caso existam patrimônios que estejam sofrendo depreciação, mas que não passaram pelo processo de distribuição de valores será enviada uma mensagem de erro solicitando a realização do rateio por filial.
* Baixa, acréscimo, transferência monetária, impairment e recuperação de impairment: Não permitirá a realização de uma baixa total se existirem transferências de controle e/ou alocação do patrimônio com datas superiores a da baixa. Não permitirá a realização de ocorrências com datas anteriores as das transferências de controle contabilizas ou com contabilização pendente. Após a contabilização do cálculo de depreciação não é possível gerar ocorrências.
* Transferência de controle: Não permitirá a realização de transferências de controle quando houver uma ou mais ocorrências, contabilizadas ou com contabilização pendente, cujas datas sejam posteriores a data da transferência. Após a contabilização do cálculo de depreciação não é possível gerar transferência de controle.
* Liberação de competência: Irá verificar se utiliza rateio por tempo em filial e avisará caso existam patrimônios sem rateio.
