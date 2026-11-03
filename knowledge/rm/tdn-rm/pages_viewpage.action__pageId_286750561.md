---
content_hash: 9561d9621823488459d09dfe4440235ab5340f0931a5d78f31e12331abf3ce3e
fetched_at: '2026-06-29T00:08:41.803893+00:00'
page_id: '286750561'
product: rm
source: tdn-rm
title: RMPAT00009_Exclusão de Ocorrências e Contabilização via Tarefa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286750561
version: 7
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.14. ou superior |
| **Ocorrência:** | Exclusão de Ocorrências e Contabilização via Tarefa |
| **Ambiente:** |  |
| **Passo a passo:** | Processo responsável pela Exclusão de Ocorrências ([Baixa – Total e Parcial](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.OcorrenciaBaixa.aspx) ).  A Exclusão de Ocorrências não será realizada nas seguintes situações: - Período de Cálculo diferente da ocorrência: a ocorrência só poderá ser excluída caso sua data esteja dentro do período de cálculo, ou seja, uma baixa (por exemplo) realizada no mês de janeiro de 2016 só poderá ser excluída caso o período de cálculo seja janeiro/2016. - Ocorrências com data anterior a última realizada: ao excluir uma ocorrência deve-se verificar a existência de ocorrências realizadas posteriormente a mesma. A exclusão deverá ser realizada respeitando a data considerando sempre a última ocorrência.  **Exemplo:** O patrimônio 01.01.001 possui 2 ocorrências, um acréscimo no dia 01/02/2016 e uma baixa parcial no dia 03/04/2016. Nesta situação a ocorrência a ser excluída é a baixa parcial, visto que foi a última realizada no patrimônio. Lembrando que o período de cálculo deverá estar em Abril/2016.    **Procedimento (Exclusão da Contabilização de Ocorrências):** Acesse Menu Operações patrimoniais | Consulta/Cancela | Selecione a baixa realizada (Baixa Total e/ou Parcial) | Selecione a Ocorrência | Aba Processos:  **Observação 1:** Caso a ocorrência esteja contabilizada e não esteja integrada para o módulo Contábil (Gestão Contábil / Rm Saldus), utilize a opção de 'Desfazer Contabilização'.  **Observação 2:** Caso a ocorrência esteja contabilizada e esteja integrada para o módulo Contábil (Gestão Contábil / Rm Saldus), será necessário realizar o processo selecionando a opção 'Solicitar a Exclusão de Contabilização (Via Tarefa)'. E prosseguir conforme segue abaixo:        Acesse Menu Operações patrimoniais | Consulta/Cancela | Seleciona a baixa realizada (Baixa Total e/ou Parcial) | Selecione a ocorrência | Aba Processos | Solicitar a Exclusão da Contabilização (Via Tarefa).        Realize o processo informando os parâmetros solicitados e execute. Gentileza verificar o log, mesmo que o processo seja concluído com sucesso essa análise é sempre importante em qualquer rotina.        Após solicitar a exclusão via Tarefa acesse o módulo Contábil (Gestão Contábil/Rm Saldus).        Aba Utilitários | Gerenciador | Tarefa | Selecione a Tarefa ao qual solicitou no RM Bonum | Processos | Executar Tarefa.            Informações e detalhes sobre as Tarefas e Permissões clique [aqui](http://tdn.totvs.com/pages/releaseview.action?pageId=77300698).  Após realizar o processo de exclusão da contabilização, selecione a ocorrência | Processos | Exclusão de ocorrências. |
| **Observações:** | Caso a ocorrência possua mais de um cenário, todos deverão ser selecionados no processo de Exclusão de ocorrências. |
