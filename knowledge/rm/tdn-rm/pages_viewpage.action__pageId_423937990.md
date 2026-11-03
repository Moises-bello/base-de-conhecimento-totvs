---
content_hash: e74d5483648f161301a4d05f7ae6332faef9af5a32c0518bc158df224ebc6160
fetched_at: '2026-06-29T00:09:24.673083+00:00'
page_id: '423937990'
product: rm
source: tdn-rm
title: Liberação de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937990
version: 5
---

A rotina de liberação de movimentos consiste em excluir permanentemente da base de dados as movimentações até uma determinada  data (definida pelo usuário), visando principalmente a liberação de espaço na base de dados.

Importante

Como os movimentos são **ELIMINADOS** da base, é de **INTEIRA RESPONSABILIDADE DO USUÁRIO** manter **BACKUP ATUALIZADO DA SUA BASE DE DADOS** antes de fazer a liberação para garantia de consultas futuras caso sejam necessárias.

Condições para execução da rotina de liberação de movimentos da base de dados:

1. Apenas usuários que tenham permissão de **supervisor** podem executar a rotina de liberação;
2. A liberação só poderá ser executada quando não houver nenhum outro usuário utilizando a base de dados, e durante a execução nenhum outro acesso será permitido em qualquer módulo;

   Atenção

   Para impedir o acesso de qualquer usuário ao sistema durante o processo de liberação de movimento, alteramos temporariamente os valores de controle de tabelas de uso interna. Desta forma, quando algum usuário tentar logar será apresentada a seguinte mensagem:  **GPARAMS com CRC inválido**. Depois de concluído o processo de liberação, os controles são recalculados e a base fica disponível para acesso.

   Considerando a necessidade de impedir novos acessos ao sistema durante o processo de liberação, não é aconselhável o uso dos parâmetros [Bloqueio de tela ou Desconexão Automática](https://tdn.totvs.com/pages/releaseview.action?pageId=181144884). O uso de qualquer um destes parâmetro bloqueia a tela exigindo um no login que será impedido.
3. Para bancos de dados SQL Server, deve ser adicionado ao Host.exe.config, a chave <add key="DBSCOMMANDTIMEOUT" value="3600"/> com um valor de no mínimo 3600s ou mais dependendo do caso. Isto visa evitar que ocorra o erro de "SQL Server Connection Time Out", já que comandos que afetam um grande volume de dados estarão sendo executados.

**Descrição do Processo**

Ao acessar o menu Liberação de Movimentos, o sistema abrirá uma janela para que o usuário informe a data limite para a liberação dos movimentos, e as opções de liberação disponíveis são:

**APENAS CONSISTIR se a base de dados pode ser liberada até esta data:**

Utilizada quando o usuário quiser apenas consistir se os movimentos podem ser liberados até a data informada. Esta etapa é executada também quando se seleciona as outras opções, pois é necessária para a geração do arquivo de log.

**Liberar APENAS se os movimentos até a data de liberação não tiverem NENHUMA PENDÊNCIA**:

A liberação poderá ser executada apenas para movimentos já consolidados e sem pendências.  
As situações que caracterizarão o movimento como **pendente** no processo de liberação seja iniciado são descritas a seguir:

* + Data de fechamento do estoque maior ou igual à data da liberação;
  + É movimento do tipo pedido e não esta baixado (que não tenham sido faturados ou recebidos);
  + Movimentos que aumentam o saldo de conta trabalho e que não tenham sido totalmente devolvidos;
  + Movimentos que diminuem o saldo de conta trabalho e que não tenham sido processadas;
  + Movimentos que diminuem o saldo de conta trabalho ou que tenham sido geradas pelo processo de conta trabalho, cujo movimento de entrada não tenha sido totalmente devolvido;
  + Não gerou lançamentos a Pagar/Receber;
  + Não quitou Lançamentos a Pagar/Receber;
  + Não escriturou o movimento ou o processo de escrituração não foi finalizado pelo Gestão Fiscal;
  + Não contabilizou o movimento ou o processo de Contabilização ainda não foi finalizado pelo Gestão Contábil;
  + Utilizado pelo TOTVS Manutenção.

Durante a execução do processo, o sistema verifica se os movimentos a serem liberados possuem algum tipo de pendência e, caso exista, o sistema grava a informação no arquivo de log do processo e interrompe a liberação.

**Liberar TODOS os movimentos até a data de liberação, INCLUSIVE AQUELES COM PENDÊNCIAS:**

A liberação será executada excluindo todas as movimentações, inclusive aquelas com pendências.

**Restrições**

* **Liberação de Movimentos de estoque de Terceiros:** O processo de liberação de movimentos, não permite liberar movimentos que utilizem ESTOQUE DE/COM TERCEIROS, pois a rotina de liberação de movimentos não gera saldo anterior para estoque de terceiros como acontece com a geração do saldo anterior dos produtos (TPRDLOCANT).
* **Liberação de Lançamentos Financeiros:** O processo de liberação de movimentos, não permite liberar movimentos que geraramlançamentos Financeiros.
* **Liberação de movimentos vinculados a ordem de serviço do TOTVS Manutenção:** O processo de liberação de movimento, não permite liberar movimentos gerados pelo TOTVS Manutenção.
