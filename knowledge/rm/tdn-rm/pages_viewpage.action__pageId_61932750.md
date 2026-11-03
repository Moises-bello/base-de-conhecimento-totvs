---
content_hash: e87c201d2efd73cb3cd0e09a2bccfa3962a0bfb37189cb965933e6d88c2933bf
fetched_at: '2026-06-29T00:11:02.574567+00:00'
page_id: '61932750'
product: rm
source: tdn-rm
title: Distribuição de Processos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61932750
version: 1
---

1- Realizar a configuração no Alias manager habilitando o Processamento em Job.

**IMPORTANTE: Esta parametrização do Alias deverá ser realizada nos servidores que realizaram a distribuição dos processos, ou seja, em nosso exemplo utilizamos dois servidores apontando para uma mesma base de dados, esta conexão foi realizara através do Alias Manager e parametrizada conforme a figura abaixo.**

Após a parametrização do Alias deverá parar o serviço e inicia – lo novamente

2- Ao realizar a consulta no banco de dados observe que os servidores de Jobs serão apresentados. (conforme exemplo).

3- Acesse o RM.exe na guia (1) AMBIENTE selecionando o ícone: (2) Distribuição de Processos.

Observe que serão apresentados os servidores de Jobs que foram parametrizados (3).

4- Selecione o servidor que necessita parametrizar o processo e clique em adicionar

5- Selecione o Processo RptProcGenerateReport. Ao selecionar este processo, todos os relatórios executados em Jobs serão executados neste servidor parametrizado.

6- Importante: Clicar em Salvar para confirmar o processo selecionado.

A partir deste momento, todo relatório executado por Processo será gerado utilizando este

servidor parametrizado.

7- Ao acessar o menu AMBIENTE: Gerenciamento de Jobs, será possível visualizar o servidor que executou o Job do relatório em questão.

**Informações complementares:**

- Este exemplo utilizado foi baseado no processo: **RptProcGenerateReport** que refere-se a geração de relatórios em JOB.
