---
content_hash: 6b8727144dc86d0b2e44fe789a61fe836a909fd50a736bae05613c78b5ea92dc
fetched_at: '2026-06-29T00:10:08.725511+00:00'
page_id: '452719567'
product: rm
source: tdn-rm
title: Gerenciador de Logs Complementares
type: documentation
url: https://tdn.totvs.com/display/LRM/Gerenciador+de+Logs+Complementares
version: 2
---

O módulo de Logs Complementares é uma solução que visa evitar problemas relacionados a desempenho por causa do armazenamento de uma grande quantidade de logs gerados por cálculos da Folha de Pagamento. Esses problemas podem surgir, principalmente, devido ao acumulo de uma grande quantidade de logs de funcionários no sistema. Para atingir o objetivo proposto, o módulo Logs Complementares permite que os usuários do RM sejam capazes de mover logs gerados pela execução de cálculos da Folha de Pagamento para as tabelas de logs complementares. A ideia é a seguinte: para evitar que uma grande quantidade de logs de cálculo se acumulem nas tabelas tradicionais, é possível transferir parte dos logs para as tabelas complementares. A visualização dos logs complementares (logs que foram movidos para as tabelas complementares) vai acontecer de maneira parecida com o que feito na consulta de logs de cálculo tradicional. A única mudança é que, diferente de como os logs de cálculo são apresentados Gerenciador de Log de Cálculo, os logs complementares são mostrados seguindo uma estratégia de mestre-detalhe. Na prática, isso significa que inicialmente são mostrados apenas os logs dos cálculos realizados. A visualização de logs dos funcionários é feita através de um anexo. Por fim, o módulo de Logs Complementares pode ser acessado através do menu: **Folha de Pagamento > Folha Mensal > Consulta > Logs Complementares**

**Mover Logs de Cálculo para Logs Complementares** Na tela de **Gerenciador de Logs de Cálculo** foi adicionado um processo para movimentar os logs de cálculos existentes no sistema. Essa funcionalidade permite que o usuário possa mover os logs relacionados a cálculos das tabelas de logs tradicionais para as tabelas complementares. Durante a realização desse processo o usuário deve selecionar uma data base, para a movimentação, e clicar no botão de execução. A data fornecida como parâmetro servirá como um limite de até quais logs devem ser movidos. Dessa forma, todos os logs, da coligada corrente, gerados até a data escolhida serão movidos para as tabelas complementares, ao fim do processo. Os logs movidos ainda poderão ser acessados através do módulo **Gerenciador de Logs Complementares** (Folha de Pagamento > Folha Mensal > Consulta > Logs Complementares). Importante:

1. Não é possível mover logs recentes para as tabelas complementares. A regra utilizada para permitir a transferência é: somente logs gerados até o dia primeiro dia de duas competências anteriores (considerando a competência atual) podem ser movidos para as tabelas complementares;
2. Os logs de funcionários com o status "D" não são movidos para as tabelas complementares;
3. Logs de funcionários que possuem a coligada 0 são sempre transferidos estando sujeitos apenas a data da transferência e a restrição de funcionários com situação "D";

**A Tela de Logs Complementares**

Ao entrar no módulo **Logs Complementares** o usuário se depara com uma visão que exibe informações sobre os logs de cálculo que foram movidos para as tabelas complementares. É possível visualizar detalhes sobre cada um dos processos clicando duas vezes na linha correspondente. Na janela aberta, é possível verificar detalhes sobre a execução do cálculo e, se o usuário quiser, visualizar essas informações no Bloco de Notas (através de um botão próprio). Além disso, também é possível abrir um anexo que mostra os logs gerados para cada funcionário afetado pelo cálculo executado. Da mesma forma que acontece no caso dos logs de cálculo, com um clique duplo é possível verificar as informações contidas no log.  
    
 **Exclusão de Logs Complementares**

Na tela de Logs Complementares foi adicionado um processo para realizar a exclusão desses logs no sistema. Diferente do processo de movimentação, que transfere logs de cálculo para as tabelas complementares, esse processo elimina, permanentemente, logs existentes nas tabelas complementares. Por esse motivo, é importante que, ao usar essa funcionalidade, o usuário esteja seguro do que está fazendo, já que é um processo irreversível. Para realizar esse procedimento é necessário fornecer uma data base e clicar no botão de execução. Ao executar o processo, todos os logs complementares da coligada corrente e que foram gerados até a data escolhida serão removidos, permanentemente, do sistema. Importante:

1. Logs complementares excluídos não podem ser recuperados. Antes de realizar essa ação é importante que o usuário se certifique que as informações não são mais necessárias;
2. Não é possível excluir logs associados a funcionários que estiverem com a situação igual a "D";

Importante:  
 No processo de liberação de competência, os logs continuam sendo excluídos, quando o parâmetro referente a essa ação for marcado. A mesma regra que é aplicada para os logs de cálculo tradicionais também vale para os logs movidos para as tabelas complementares. Dessa forma, quando o usuário opta por remover os logs dos funcionários, em uma liberação de competência, tanto os logs tradicionais quanto os que foram movidos para as tabelas complementares serão removidos, permanentemente, do sistema. O parâmetro, que define os logs que serão mantidos/apagados, pode ser alterado no parametrizador (Folha Mensal > Log's).

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Gerenciador de Log de Cálculo
