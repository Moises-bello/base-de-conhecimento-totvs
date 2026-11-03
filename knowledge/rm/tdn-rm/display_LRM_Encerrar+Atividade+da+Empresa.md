---
content_hash: 937f7294c77144d1392452f2c65da9e807c1e5dc353077ff41cb4eec04e854e8
fetched_at: '2026-06-29T00:10:07.848714+00:00'
page_id: '452719452'
product: rm
source: tdn-rm
title: Encerrar Atividade da Empresa
type: documentation
url: https://tdn.totvs.com/display/LRM/Encerrar+Atividade+da+Empresa
version: 9
---

O processo em questão tem o objetivo de encerrar a atividade da empresa junto ao eSocial, sendo necessário enviar o encerramento de todas as tabelas (S- 1005 a S-1080) além do evento "S-1000 - Informações do empregador/contribuinte/órgão público".

**Atenção**

1. Apesar de ser obrigatório o envio de encerramento para todos os eventos de tabela, o processo disponibilizará a sua execução por evento bastando selecionar o parâmetro "Selecionar eventos para encerramento". O usuário poderá definir a forma de geração conforme abaixo:  
Parâmetro Marcado: o usuário poderá definir os eventos a serem considerados na geração.  
Parâmetro Desmarcado: O usuário não poderá definir os eventos a serem considerados na geração , será gerado para todos os eventos.Por Default as informações serão visualizadas desabilitadas.  
    
2. Será disparado um gatilho de encerramento para todos os eventos selecionados.  
   
3. É possível utilizar uma data de encerramento específico para a execução do processo de encerramento para cada coligada. Quando essa data não é informada, é utilizada a data de encerramento geral para todas as coligadas.

**OBSERVAÇÃO**:

* Para cadastros que estão inativos (seção, eventos, etc), caso o parâmetro para desconsiderar eventos inativos esteja marcado, somente será gerado gatilho de encerramento se possuir gatilho de inclusão com status '10-Aceito Ret' na fila de eventos ou fila de eventos complementar.
* Eventos que estejam listados nas etapas **Funções a Desconsiderar, Eventos a Desconsiderar, Horários a Desconsiderar, Seções a Desconsiderar e Tomadores a Desconsiderar,** os gatilhos não serão gerados.
