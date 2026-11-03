---
content_hash: 3ef42f5ad1d000ed2aecc458f094f0085da1a4bb7ecdb1405fdd32f5d00ec3dc
fetched_at: '2026-06-29T00:09:26.690165+00:00'
page_id: '423938371'
product: rm
source: tdn-rm
title: Exclusão de Cálculos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938371
version: 3
---

Este módulo é responsável por tratar o processo de exclusão de cálculos, que consiste em remover os registros dos cálculos do sistema.

**Regras para exclusão de Cálculo**

- Não é possível remover cálculos fora do mês de cálculo.

- Não será possível excluir cálculos (dentro do mês) de patrimônios com ocorrência no mês (será necessário excluir a ocorrência).

- A exclusão de um cálculo acarretará na exclusão de todos os cálculos posteriores a ele.

**Realizando a exclusão de Cálculo**

Para realizar a exclusão de cálculo deve ser acessado o menu Utilitários\Exclusão de Cálculos,  inicialmente deverão ser selecionados um ou mais patrimônios. Em uma segunda aba será possível optar por apagar as ocorrências do patrimônio, lembrando que esta funcionalidade é possível apenas para baixas e acréscimos. A exclusão de cálculos que possuem transferência monetária não ocorre pelo fato de que este tipo de ocorrência envolve mais de um patrimônio, o que geraria uma exclusão em cadeia.

Após realizar os procedimentos acima o processo poderá ser executado.

Será emitida uma mensagem de confirmação da exclusão.

O processo começará removendo as baixas e acréscimos associados ao(s) patrimônio(s) (caso seja parametrizado), para depois remover os cálculos do(s) patrimônio(s).

As ocorrências também devem ser apagadas levando em conta as várias moedas associadas a ela. Essa etapa é interna e nenhuma mensagem será apresentada. Caso o usuário não parametrize a exclusão de ocorrências, a exclusão poderá não acontecer caso exista uma ocorrência para aquele patrimônio (mesma data ou posterior). Após o processo encerrado, será apresentada uma mensagem, informando que o patrimônio em questão está sem cálculo, e que seria interessante a execução dos recálculos do mesmo, visto que esses cálculos são necessários para a liberação de Competência e para o Fechamento de Período.
