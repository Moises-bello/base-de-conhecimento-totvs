---
content_hash: 737f1685bb4ee39209ebf528629e980063ba3e0425ce912bb3ae6daf53cc8e98
fetched_at: '2026-06-29T00:09:26.129948+00:00'
page_id: '423938271'
product: rm
source: tdn-rm
title: Relatório Ficha de Imobilizado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938271
version: 2
---

O Ficha de Imobilizado se trata do relatório de maior utilização dentro do Totvs Gestão Patrimonial. Substituindo o Razão Auxiliar, este relatório reúne informações referentes às movimentações tendo como finalidade o gerenciamento do patrimônio e/ou a prestação de contas à legislação em vigor.  
O Ficha de imobilizado permite que as informações sejam filtradas pelo intervalo de contas contábeis ou por grupo de patrimônio, possibilitando maior flexibilidade durante a parametrização.  
   
 **Regras para Emissão do Relatório**  
Como pré-requisito para composição deste relatório deverão ser importados, no gerador de relatórios, o Ficha de Imobilizado e Ficha de Imobilizado por Filial.

Sendo que o layout do relatório Ficha de Imobilizado apresenta os dados agrupados, ou seja, cada linha exibirá o somatória dos conjuntos de informações (como por exemplo o total de aquisições) sem distinguir a filial, diferentemente do relatório ficha de imobilizado por filial que realiza a quebra das informações. Neste último caso as informações de cada grupo de patrimônio ou contas contábeis  serão exibidas respeitando sua filial. Por exemplo, as aquisições do grupo de patrimônio 01 terá uma linha para a filial 01, depois para a filial 02 e assim sucessivamente. Os relatórios exibirão apenas as informações contidas dentro do período de cálculo em aberto (definido no fechamento de período), ou seja, não será possível visualizar movimentações anteriores e posteriores ao período em aberto.  
   
 **Emissão do Relatório Ficha de Imobilizado**  
Inicialmente devem ser informados os meses e anos, respectivamente, iniciais e finais desejados para apuração (seleção do período), quais patrimônios serão envolvidos (os ativos e/ou inativos) e o cenário de cálculo correspondente a estes patrimônios.

Lembrando que o cenário de cálculo é definido no grupo de patrimônio que está associado ao patrimônio. Caso seja necessário pode-se selecionar uma ou mais filiais. Desta forma somente as informações dos patrimônios existentes nas filiais selecionadas serão exibidas.

A maneira como as informações serão pesquisadas é extremamente importante para que os dados mantenham sua integridade. Sendo assim, é necessário selecionar uma opção entre o filtro por grupo de patrimônio (selecionado um ou mais grupos) ou pelas contas contábeis (definindo o intervalo de contas).

O Ficha de Imobilizado permite totalizar cada conjunto de informações definidas, neste caso, como de aquisições ou ocorrências (baixas, acréscimos e transferências monetárias). A totalização pode ser realizada para cada um dos conjuntos acima ou para todos.

Podem existir na base de dados patrimônios que possuem saldo, porém não tiveram movimentação no período a ser gerado o relatório. Desta forma, caso seja necessário exibir este tipo de informação é fundamental marcar a opção que permite imprimir dados dos grupo de patrimônio sem movimentação.

Também podem existir situações como a movimentação com valores zerados que está exemplificada abaixo: O patrimônio foi inserido no sistema, consequentemente no relatório será apresentada uma aquisição. Porém por algum motivo o cálculo de depreciação não foi executado. Desta forma, ao marcar opção "Imprime movimentações com valores zerados" o sistema apresentará a aquisição do patrimônio e depreciação igual a 0,00.

Ao solicitar a impressão de reavaliações serão apresentadas no relatório ficha de Imobilizado as reavaliações realizadas de acordo com a parametrização pré-definida. Como obrigatoriedade, para composição do layout das informações, deve ser informado o relatório (ficha de imobilizado ou ficha de imobilizado por filial).

Depois de realizada a correta parametrização, o relatório poderá ser executado, sendo que ao final serão apresentados o próprio relatório e o log contendo todas as informações referentes à execução do processo.

Veja Também

* Relatório de Contabilização
