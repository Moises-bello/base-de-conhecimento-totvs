---
content_hash: 76d17ce20567eef25fe5701a65423dc3a9b7f83eb6be98e999456fc6c8b1d8da
fetched_at: '2026-06-29T00:09:01.048989+00:00'
page_id: '371625817'
product: rm
source: tdn-rm
title: DT Logs Complementares
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Logs+Complementares
version: 4
---

# Logs Complementares

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Logs Complementares |
| **Situação/Requisito:** | Alternativa para evitar acúmulo de dados (logs) na tabela PLOGCALCULO e suas dependentes. |
| **Solução/Implementação:** | Foi criado um processo na tela de Log de Cálculo que permite transferir logs para as tabelas complementares. Além disso, foi criado também uma tela para gerenciamento dos logs movidos para as tabelas complementares. |
| **Documento de Referência:** |  |

**Logs Complementares**

O módulo de Logs Complementares é uma solução que visa evitar problemas relacionados a desempenho por causa do armazenamento de uma grande quantidade de logs dos funcionários. Esses problemas podem surgir devido ao acumulo de uma grande quantidade de logs no sistema. Para atingir o objetivo proposto, o módulo **Logs Complementares** permite que os usuários do RM sejam capazes de mover logs gerados pela execução de cálculos da Folha de Pagamento para as tabelas de logs complementares. A ideia é a seguinte: para evitar que uma grande quantidade de logs de cálculo se acumulem nas tabelas tradicionais, é possível transferir parte dos logs para as tabelas complementares. A visualização dos logs complementares (logs que foram movidos para as tabelas complementares) vai acontecer de maneira parecida com o que feito na consulta de logs de cálculo tradicional. A única mudança é que, diferente de como os logs de cálculo são apresentados atualmente, os logs complementares são mostrados seguindo uma estratégia de mestre-detalhe. Na prática, isso significa que inicialmente são mostrados apenas os logs dos cálculos realizados. A visualização de logs dos funcionários é feita através de um anexo. Por fim, o módulo de Logs Complementares pode ser acessado através do menu:

**Folha de Pagamento > Folha Mensal > Consulta > Logs Complementares**

**A Tela de Logs Complementares:**

Ao entrar no módulo **Logs Complementares** o usuário se depara com uma visão exibindo informações sobre os logs de cálculo que foram movidos para as tabelas complementares. É possível visualizar detalhes sobre cada um dos processos clicando duas vezes na linha correspondente. Além disso, também é possível abrir um anexo que mostra detalhes dos logs gerados para cada funcionário afetado pelo cálculo executado.

**Mover Logs de Cálculo para Logs Complementares**

Na tela de gerenciamento dos logs de cálculo foi adicionado um processo para movimentar de logs. Essa funcionalidade permite que o usuário possa mover os logs relacionados a cálculos para as tabelas complementares.

Durante a realização do processo o usuário deve selecionar uma **data base**, para a movimentação, e clicar no botão de execução. Todos os logs, da coligada corrente, gerados até a data escolhida serão movidos para as tabelas complementares, ao fim do processo. Os logs movidos ainda poderão ser acessados através do módulo **Logs complementares** (**Folha de Pagamento > Folha Mensal > Consulta > Logs Complementares**).

**Importante**:

  1) Não é possível mover logs recentes para as tabelas complementares. Somente logs gerados até o dia primeiro dia de duas competências anteriores (considerando a competência atual) podem ser movidos para as tabelas complementares;

  2) Os logs de funcionários com o status ‘D’ não são movidos para as tabelas complementares;

**Exclusão de Logs Complementares**

Na tela de **Logs Complementares** foi adicionado um processo para realizar a exclusão desses logs no sistema. Diferente do processo de movimentação, que transfere logs de cálculo para as tabelas complementares, esse processo elimina, permanentemente, logs existentes nas tabelas complementares.

Para realizar esse processo é necessário fornecer uma data base e clicar no botão de execução. Ao executar o processo, todos os logs complementares da coligada corrente, e que foram gerados até a data escolhida, serão removidos, permanentemente, do sistema.

**Importante**:

  1) Logs complementares excluídos não podem ser recuperados. Antes de realizar essa ação é importante que o usuário se certifique que as informações não são mais necessárias;

  2) Não é possível excluir logs associados a funcionários que estiverem com a situação igual a **‘D’**;
