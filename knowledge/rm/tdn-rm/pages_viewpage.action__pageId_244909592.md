---
content_hash: a940dd3bee850c656fc83ca3f783d286021791fb22ef894e48342bfaf29633dc
fetched_at: '2026-06-29T00:08:15.541077+00:00'
page_id: '244909592'
product: rm
source: tdn-rm
title: BD0012_Limpeza_Tabelas_Log_Execução_Processos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244909592
version: 2
---

# Boletim Técnico - Sentinela

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | 12.1.8 ou superior |
| **Ocorrência:** | Limpeza Das Tabelas De Log De Execução De Processos |
| **Ambiente:** | Performance de Ambiente |
| **Passo a passo:** | A Totvs recomenda que não seja feita nenhuma intervenção direta no banco de dados, por isso temos mecanismos afim de facilitar os processos de limpeza das tabelas de log de execução de processos.    Tabelas envolvidas no processo de histórico de execução de processos:     * GJOBLOG - Processos executados * GJOBX - Tabela de Jobs * GJSJOBS - Jobs * GJOBQUEUE - Processos na fila para serem executados * GJOBXEXECUCAO - Execução de Jobs * GJOBXLOG - Log de Execução de Processos * GRELBATCH - Relatórios IN BATCH     **Limpeza pelo Sentinela (processo novo)**   1. Menu Executar, digitar Sentinela 2. Tarefas de execução agendada 3. Limpeza das Tabelas de Job 4. Atenção para a mensagem abaixo: 5. Processo realizado, o tempo para execução irá depender da quantidade de registros.  **Limpeza pelo processo antigo.**    1. Serviços Globais 2. Ambiente, Gerenciamento de Jobs 3. Todos 4. Processos, Limpar Log de Execução de Processos 5. Para a quantidade de dias, não existe um número definido. Os dias podem variar de acordo com a necessidade de cada cliente. O ideal é que seja feito uma análise a partir de uma quantidade de dias, por exemplo 15 dias e acompanhar o crescimento das tabelas e também dos arquivos de dados físicos. Ir ajustando conforme a necessidade. 6. Em execução 7. Processo finalizado, o tempo para execução irá depender da quantidade de registros. |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
