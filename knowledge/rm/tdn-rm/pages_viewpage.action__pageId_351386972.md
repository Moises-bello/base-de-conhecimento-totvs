---
content_hash: 74034ffc1b6c4deb2e5b644fed45876eca7e8870603c4ca181671343f971c30f
fetched_at: '2026-06-29T00:08:56.934929+00:00'
page_id: '351386972'
product: rm
source: tdn-rm
title: RMPAT00007_Exclusão de Cálculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351386972
version: 2
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Patrimonial |
| **Versões:** | 12.1.18 |
| **Ocorrência:** | Exclusão de Cálculos |
| **Ambiente:** |  |
| **Passo a passo:** | Este módulo é responsável por tratar o processo de exclusão de cálculos, que consiste em remover os registros dos cálculos do sistema.    **Regras para Exclusão de Cálculo** - Não é possível remover cálculos fora do mês de cálculo. - Não será possível excluir cálculos (dentro do mês) de patrimônios com ocorrência no mês (será necessário excluir a ocorrência).  - A exclusão de um cálculo acarretará na exclusão de todos os cálculos posteriores a ele.    **Realizando a exclusão de Cálculo** Acessar: Utilitários | Exclusão de Cálculos.        Para realizar a exclusão de cálculo deve ser acessado o menu Utilitários\Exclusão de Cálculos,  inicialmente deverão ser selecionados um ou mais [patrimônios](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.Patrimonio.aspx). Em uma segunda aba será possível optar por apagar as ocorrências do patrimônio, lembrando que esta funcionalidade é possível apenas para baixas e acréscimos. A exclusão de cálculos que possuem transferência monetária não ocorre pelo fato de que este tipo de ocorrência envolve mais de um patrimônio, o que geraria uma exclusão em cadeia.  Na tela do processo selecione a opção ‘Incluir’ para selecionar os patrimônios que deseja:        No filtro digite os valores necessários para que o sistema apresente os patrimônios, ou digite o sinal de percentual e selecione a opção de filtrar, desta forma todos os cadastros de patrimônio serão apresentados.        Selecione os patrimônios necessários ou todos da visão.        Verifique todos os patrimônios selecionados para o processo.        Selecione a opção para apagar as ocorrências dos patrimônios selecionados.        Após realizar os procedimentos acima o processo poderá ser executado.            Esta é a tela da aba Cálculo Razão do patrimônio antes da execução do processo:        Esta é a visão da aba Cálculo Razão após a execução do processo, lembrando que a rotina exclui somente os cálculo do período de cálculo em aberto:        Será emitida uma mensagem de confirmação da exclusão. O processo começará removendo as baixas e acréscimos associados ao(s) patrimônio(s) (caso seja parametrizado), para depois remover os cálculos do(s) patrimônio(s).  As ocorrências também devem ser apagadas levando em conta as várias moedas associadas a ela. Essa etapa é interna e nenhuma mensagem será apresentada. Caso o usuário não parametrize a exclusão de ocorrências, a exclusão poderá não acontecer caso exista uma ocorrência para aquele patrimônio (mesma data ou posterior).  Após o processo encerrado, será apresentada uma mensagem, informando que o patrimônio em questão está sem cálculo, e que seria interessante a execução dos recálculos do mesmo, visto que esses cálculos são necessários para a liberação de Competência e para o Fechamento de Período. |
| **Observações:** |  |
