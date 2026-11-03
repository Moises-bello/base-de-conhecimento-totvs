---
content_hash: fd9576b2db52303d06f596f32f4bf3222254926d0e6990acb1d0c6ade2f1e6b7
fetched_at: '2026-06-29T00:08:27.216547+00:00'
page_id: '271400191'
product: rm
source: tdn-rm
title: Limpar Log de Execução de Processos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271400191
version: 19
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

**Acesse:** Ambiente | Gerenciamento de Jobs:

 Selecione os registros e clique em**Processos > Limpar Log de Execução de Processos**:

        

Nesta Tela é possível selecionar as opções desejadas para a realização da exclusão dos processos:

        

No Campo (Número de dias antes de excluir o processo) é possível parametrizar quantos dias serão mantidos os logs dos processos na base, sem excluir os processos listados.

**Exemplo**: Ao configurar o campo com valor 5, serão excluídos os logs, exceto dos últimos 5 dias (serão mantidos os últimos 5 dias).

A partir das versões 12.1.23.255, 12.1.24.203, 12.125.133, 12.1.26, no Campo 'Número de dias para excluir servidores parados' é possível parametrizar a quantidade de dias para excluir o servidor da GKNOWNJOBSERVER, em ambiente 3 camadas.

* Serão excluídos os servidores que a data de atualização do servidor (GKNOWNJOBSERVER.RECMODIFIEDON) for inferior ao dia atual menos o número de dias configurados.
* Também serão excluídos os itens da tabela GKNOWNJOBSERVERDIAGNOSTIC.
* Caso existam cadastros de afinidade de jobs para este servidor (<https://tdn.totvs.com/x/OKT6E>) ou servidor exclusivo (<https://tdn.totvs.com/x/i6f6E>), ele não será excluído, mesmo que a data da última execução de job esteja inferior a data configurada. (Tabelas para consulta: GKNOWNJOBSERVERRULE e GKNOWNJOBSERVERAPPSERVERRULES)

        Clicar em **Executar:**

**Detalhamento do comportamento de cada *flag*e a validação que é feita pelo sistema:**  
 

| Flag | Comportamento | Validação Realizada |
| --- | --- | --- |
| Excluir Processos Finalizados | Exclui *jobs* que terminaram normalmente a sua execução | Jobs com status= 2 |
| Excluir Processos Cancelados | Exclui *jobs* que foram cancelados | Jobs com status= 3 |
| Excluir Processos interrompidos pelo usuário | Exclui *jobs* em que a execução começou e foi interrompida | Jobs com status= 4 |
| Excluir Processos com erros | Exclui *jobs* que apresentaram erros | Jobs com status= 5 |
| Excluir Processos com avisos | Exclui *jobs*executados com avisos | Jobs com status= 6 |
| Excluir Processos com falha do servidor | Exclui*jobs*que apresentaram falha na comunicação com o servidor | Jobs com status= 7 |
| Excluir Processos desabilitados | Exclui *jobs* que foram desabilitados | Jobs com status = 8 |
| Excluir Processos não executados | Exclui *job* que ainda não foram executados | Valida se os campos **Servidor**, **Iniciado**, **Finalizado** e **Status**estãoem branco (vazio). |
| Excluir Processos recorrentes | Exclui *jobs* que tinham recorrência (não exclui os *jobs* que ainda serão executados e estão agendados, exclui apenas os que já foram executados) | Valida se o campo GJOBX.TIPORECORRENCIA não é nulo |
| \*Excluir Processos sob demanda | Exclui *jobs* que estão marcados para serem executados sob demanda | Valida se o campo  GJOBX.TIPOJOB é igual a 1 |
| Excluir relatórios gerados por processos | Exclui os dados da tabela de relatórios GRELBATCH |  |

   
\*Excluir Processos sob demanda : Esses jobs são os que tem o TIPOJOB igual a 1 e são marcados para serem executados sob demanda:

Importante

Esse processo é passível de agendamento. desde que o ambiente esteja configurado para trabalhar em 3 camadas.

        As  tabelas responsáveis pelo armazenamento das informações relacionadas aos jobs guardam grande número de registros e por isso devemos executar o processo de manutenção periodicamente.

        A manutenção das tabelas não possui impactos.

        O processo de limpeza de execução de processos foi implementado “furando a fila“, ou seja, é executado pelo APP para ser efetivo. Tendo como premissa o conceito de furar fila, não se leva em consideração as demais configurações, como por exemplo, afinidade. Esse processo deve funcionar dessa forma, pois, imaginando que pode haver alguma inconsistência (travamento) no Job Server, o processo não pode depender deste Servidor para ser executado.

A partir da versão **12.1.2502** estará disponível a flag **Excluir relatórios gerados por processos** (Tabela GRELBATCH).

O usuário logado no sistema visualizará Jobs da Coligada Global (0) se ele for supervisor do módulo do contexto ou se possuir algum perfil associado que contenha permissão no item "Gerenciamento de Jobs > Consultar Jobs emitidos de todos os Usuários".

A partir da versão **12.1.2506** esta rotina também poderá ser executada através da **Tarefa Agendada do Sentinela - Limpeza das Tabelas de Job**.false

**Versão:** 11.XX e 12.01.XX
