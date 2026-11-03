---
content_hash: 7016a6c85918501664b6fa0df4e45d6938851627692bfdaf22c05111ca28936a
fetched_at: '2026-06-29T00:10:51.289296+00:00'
page_id: '566461289'
product: rm
source: tdn-rm
title: Melhorias no funcionamento do Job
type: documentation
url: https://tdn.totvs.com/display/LRM/Melhorias+no+funcionamento+do+Job
version: 20
---

**CONTEÚDO**

## **01. VISÃO GERAL**

Neste documento serão citadas as melhorias que estão sendo feitas no funcionamento do Job, com o intuito de melhorar a sua performance.

Veja mais sobre a , .

## **02. ATUALIZAÇÃO DA GJOBSERVER**

Na verão 12.1.31, foi feito um ajuste no tempo de escrita nessa tabela.

Essa tabela possui informações dos servidores de job em atividade. Alguns de seus dados são obtidos pelo arquivo de alias.dat e outros o sistema atualiza de forma dinâmica, de acordo com o ambiente.

Pode-se consultar:

* Qual é o servidor controlador, que distribui os processos da fila (gjobserver.controlador)
* Quantos Jobs são executados simultaneamente pelo Host (gjobserver.maxjobs ou alias.dat:<JobServerMaxThreads>)
* Qual o intervalo de leitura da fila de processos (gjobserver.tempopool ou alias.dat: <JobServerPollingInterval>)
* Quantos Jobs estão sendo executados (gjobserver.numjobs)  (**Em Tempo de execução**)

Buscando melhorar a performance, o campo **gjobserver.numjobs** não mostrará mais quantos jobs estão sendo executados. E o campo **gjobserver.fulljobs**será preenchido com a regra:

ATENÇÃO

**Para saber o numJobs em tempo de execução é necessário executar a seguinte consulta SQL:**

sqlSQLtrue 1
GROUP BY GJOBXEXECUCAO.SERVIDOR
)
SELECT GJOBSERVER.NOMESERVIDOR,
GJOBSERVER.DATAULTATIV,
GJOBSERVER.MAXJOBS,
GJOBSERVER.TEMPOPOOL,
GJOBSERVER.CONTROLADOR,
GJOBSERVER.FULLJOBS,
CTE\_GJOBXEXECUCAO.NUMJOBS
FROM GJOBSERVER
LEFT JOIN CTE\_GJOBXEXECUCAO
ON (GJOBSERVER.NOMESERVIDOR = CTE\_GJOBXEXECUCAO.SERVIDOR)]]>

```

```

**0** - quando a quantidade de jobs em execução por aquele servidor forem igual a zero ou menor que a quantidade máxima que aquele server puder executar (maxjobs).

**1** - quando o servidor estiver executando a quantidade máxima de jobs configurada para ele (maxjobs).

A escrita no campo **gjobserver.dataultativ**também foi alterada.

Antes este campo era atualizado sempre que era feita uma verificação da fila de jobs pelo sistema. Essa verificação é feita de acordo com o valor configurado em gjobserver.tempopool.

Após a implementação da melhoria, o campo gjobserver.dataultativ será atualizado após 5 vezes o tempo configurado em gjobserver.tempopool.

## **03. TRATAMENTO PARA FINALIZAÇÃO DO JOB QUANDO O HOST QUE ESTÁ EXECUTANDO-O NÃO RESPONDE MAIS**

Na verão 12.1.31, foi feita uma melhoria de recovery do job.

Hoje um job em execução têm afinidade com o servidor que ele está em execução. A melhoria implementada afeta um cenário onde garantimos que se esse servidor cair durante a execução de um job e não retornar mais, outro servidor finalizará o processo com status de falha.

Caso o job não tenha recorrência, o controlador irá atualizar o processo que estava em execução com status de falha.

Se o job for recorrente, o controlador além de finalizar o processo com status de falha, irá criar o agendamento da próxima execução, considerando as mesmas regras da recorrência programada no job.

O processo acima ocorrerá quando o próprio host da execução inicial do job não conseguir finalizá-lo antes de cair e após o controlador remover esse host da GJOBSERVER.

Em ambiente 3 camadas, em cenários onde o host cair, se algum jobRunner estiver executando um job, esse jobRunner vai tentar finalizar a sua execução antes de se matar. Para evitar que a melhoria citada acima finalize esse job que está em execução e que continua comunicando com o banco, foi feito com que o jobrunner assuma o papel de atualizar a GJOBSERVER.DATAULTATIV e GJOBSERVER.FULLJOBS = 1, até finalizar o seu job. Assim, será adiado que o controlador remova esse host da GJOBSERVER e finalize seus jobs em execução, e com o campo fulljobs = 1 esse host não receberá mais jobs para serem executados.

## **04. ARMAZENAMENTO DO HISTÓRICO DE EXECUÇÃO DE JOBS NA TABELA GJOBXEXECUCAOHST**

A partir da versão 12.1.31, o histórico de execução de jobs ficará armazenado na tabela GJOBXEXECUCAOHST.

Com o intuito de melhorar a performance do sistema, ao que se refere a jobs, foi criada a tabela GJOBXEXECUCAOHST. Em versões anteriores, quaisquer jobs finalizados, agendados ou em execução eram armazenados na tabela GJOBXEXECUCAO.

O que mudou:

* No atualizador da versão 12.1.31 será criada a tabela GJOBXEXECUCAOHST e ao executá-lo grande parte dos jobs finalizados serão migrados da tabela GJOBXEXECUCAO e deletados da mesma. Por esse motivo, o atualizador pode demorar um tempo maior para ser executado, dependendo da quantidade de registros a serem migrados.
* **[****LEGADO → Ver tópico 06]** Após a atualização da base e migração dos registros, os próximos jobs finalizados serão migrados para a tabela de histórico em até 1 dia após sua execução. Foi criada uma rotina no sistema onde são escolhidos 3 horários do dia que normalmente existe o menor número de execução de jobs. E durante essas 3 horas os jobs finalizados podem ser migrados da tabela GJOBXEXECUCAO para a tabela GJOBXEXECUCAOHST.

A migração dos dados é feita via banco de dados e não é gerado um job para isso.  
Além disso, foi criada a view GJOBXEXECUCAOVIEW para listar todos os jobs, da tabela GJOBXEXECUCAO e GJOBXEXECUCAOHST.

Em ambiente 3 camadas = false, os registros serão migrados para a GJOBXEXECUCAOHST pelo atualizador.

Novidades do atualizador da 12.1.31:

* Ao atualizar a base, os jobs que estiverem sendo executados no momento da atualização serão encerrados da seguinte forma:
  + Quando a data de início de execução do job for mais antiga que 1 dia à execução do atualizador, o job será cancelado. Nesse cenário se o job for recorrente ele não será reagendado.
  + Quando a data de início de execução do job for de até 1 dia à execução do atualizador, o status do job será falha. Nesse cenário se o job for recorrente ele será reagendado.
* Em bases inconsistentes, jobs que apresentarem registro apenas na tabela GJOBXEXECUCAO e não tiver registro na tabela GJOBX serão excluídos.

## **05. LIMPEZA DE JOB SERVERS DA TABELA GKNOWNJOBSERVER**

A partir da versão 12.1.2306, foi adicionado um mecanismo para realizar a limpeza de JobServers da tabela GKNOWNJOBSERVER, mantendo a saúde e sanitização.

Para que um JobServer seja removido, será seguida a seguinte regra:

* + Não deve estar presente a tabela GJOBSERVER.
  + Não deve estar em GKNOWNJOBSERVERAPPSERVERRULES, ser definido como um Servidor de Aplicação.
  + Não deve estar em GKNOWNJOBSERVERRULE, ter afinidade com um processo.

## **06. MIGRAR JOBS FINALIZADOS PARA A TABELA DE HISTÓRICO**

A partir das versões 12.1.2406.232, 12.1.2410.165 e 12.1.2502.100, foi adicionada uma forma manual de se migrar jobs finalizados para a tabela de histórico.

Este processo é de extrema importância para o ambiente pois um acumulo de registros na tabela *GJOBXEXECUCAO* pode deixar a execução de processos cada vez mais lenta.

É recomendado o agendamento deste processo para uma execução regular, com o intuito de manter a saúde do ambiente.

Segue a documentação: [Migrar jobs finalizados para tabela de histórico](https://tdn.totvs.com/pages/viewpage.action?pageId=911867118)
