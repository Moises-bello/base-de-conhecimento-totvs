---
content_hash: 56803eb038f68377bdfb76d08490dfdfaf7171fd6d7058583b7f2352574e8a3e
fetched_at: '2026-06-29T00:09:10.459562+00:00'
page_id: '397385949'
product: rm
source: tdn-rm
title: RMPAT00002_Acréscimo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=397385949
version: 3
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | Totvs Gestão Patrimonial |
| **Versões:** | 12.1 |
| **Ocorrência:** | Acréscimo |
| **Ambiente:** |  |
| **Passo a passo:** | Este processo permite realizar acréscimo nos valores dos patrimônios de forma individual (somente um patrimônio selecionado) ou simultaneamente (definindo uma faixa de patrimônios).  **Parametrização** Para que a contabilização da ocorrência de acréscimo seja realizada deve-se marcar o parâmetro "Contabilizar Ocorrências" e definir o código do Lote (do sistema contábil) que receberá os lançamentos correspondentes.  Disponível em: Menu Ambiente > Parâmetros > Totvs Gestão de Patrimônio > Integração > Integração Contábil.      **O acréscimo não será realizado nas situações abaixo:** - Em patrimônios considerados Títulos; - Em patrimônios totalmente depreciados; - Em patrimônios totalmente baixados em período anterior; - Data do processo fora do período de cálculo.  **Exemplo:** Data do acréscimo 01/01/2010, período de cálculo do sistema patrimonial 01/2011.    **Procedimentos para realização do Acréscimo:**  O acréscimo pode ser executado a partir do menu Operações Patrimoniais | Acréscimo ou pela visão de patrimônios. Neste caso deve-se selecionar o(s) patrimônio(s) desejado(s) e escolher a opção Acréscimos em Processos (na barra de ferramentas).  Menu Operações Patrimoniais | Acréscimo:      Menu Cadastros | Patrimônio | Selecione o patrimônio | Processos | Acréscimo:      **Seleção de Patrimônios** Nesta etapa devem ser selecionados todos os patrimônios a serem utilizados no acréscimo. Esta opção será exibida caso o processo seja executado a partir do menu Operações Patrimoniais.          **Seleção dos dados complementares:  Tipo de acréscimo**   * Ratear Valor Nesta opção o valor da ocorrência será dividido pelo número de patrimônios envolvidos e posteriormente acrescentado a cada patrimônio. Ao escolher este tipo será habilitado o campo Valor da ocorrência onde o valor do acréscimo deverá ser informado.   **Exemplo:** Valor do acréscimo: R$ 1.000,00 Total de patrimônios selecionados: 5 Valor do acréscimo para cada patrimônio: R$ 200,00     * Por percentual Esta opção considerará o valor base corrigido do patrimônio como base para realização do cálculo do percentual. Ao escolher este tipo será habilitado o campo Percentual onde o percentual, menor ou igual a 100, deverá ser informado.   **Exemplo:** Percentual: 10 % Valor corrigido do patrimônio: R$ 10.000,00. Valor do acréscimo a ser gerado para cada patrimônio: R$ 1.000,00  **Data** A data a ser utilizada no processo deverá considerar a data base do patrimônio, a última ocorrência para este patrimônio e a data de aquisição do mesmo, ou seja, a data precisa estar dentro do período de calculo, deverá ser maior que a última ocorrência cadastrada e maior que a data de aquisição.  **Quantidade** Quantidade de itens que serão acrescentados para os patrimônios.  **Contabilização** A contabilização do acréscimo respeitará as informações definidas no Evento Contábil para criação dos lançamentos.  Ao marcar esta opção a [contabilização do acréscimo](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.ContabilizaAcrescimo.aspx) ficará como pendente, podendo ser realizada posteriormente após a execução com sucesso do acréscimo.    **Observações:** Para a contabilização o sistema considera a data do lote e a data da ocorrência, ou seja, o sistema não contabilizará ocorrência com data fora do período do lote contábil.  A contabilização só será realizada caso seja marcada a opção Contabilizar Ocorrência.    **Campo Observações** Campo livre que permite que sejam descritas informações que, posteriormente, podem ser visualizadas no histórico da ocorrência.      **Log** Após cada execução do acréscimo será exibido um log contendo informações referentes ao processo.  O resultado do acréscimo pode ser conferido a partir da aba Cálculo Razão no tela de edição do patrimônio.          **Observação:** A depreciação sobre o valor acrescido será calculada somente a partir da data do Acréscimo. |
| **Observações:** |  |
