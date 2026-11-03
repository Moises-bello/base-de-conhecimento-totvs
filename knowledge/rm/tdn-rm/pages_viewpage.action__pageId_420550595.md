---
content_hash: 8b80de6ec6e9973bb013d3c47f838d21945ee8f85eec47890cf6eb5295a21398
fetched_at: '2026-06-29T00:09:13.473365+00:00'
page_id: '420550595'
product: rm
source: tdn-rm
title: Relatório Balancete Consolidado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=420550595
version: 15
---

O balancete consolidado reflete a contabilidade de uma empresa ou organização num determinado período e tem como objetivo consolidar os saldos das contas contábeis que foram associadas a um plano de contas paralelo do tipo "Consolidação de Saldos".

O relatório gera os valores consolidados de acordo com as coligadas do [Grupo Empresarial](https://tdn.totvs.com/display/LRM/Grupo+Empresarial) informado no plano de contas paralelo e também pelo percentual de consolidação informado no cadastro de .

Acesse o menu "Relatórios" e em seguida a sub opção Balancete Consolidado. Será aberta uma janela de processo para configuração do Relatório. As informações escolhidas ao emitir este relatório serão gravadas pelo sistema nas preferencias do mesmo. Assim ao entrar novamente no relatório você visualizará as últimas opções escolhidas.

A tela de parâmetros possui 4 abas que serão detalhadas a seguir.

Aba Dados

**Período inicial e final:**Intervalo de datas para impressão do relatório.

**Plano de contas consolidado da coligada corrente:** Plano de contas, com finalidade Consolidação de Saldos, que será utilizado na geração do relatório. Vale ressaltar que serão exibidos apenas os planos de conta da coligada corrente. Caso ele seja alterado ou apagado o filtro de contas paralelas será limpo.

**Selecionar Coligada/Filial:**Permite selecionar Coligadas/Filiais cujos dados serão processados e consolidados no relatório. É importante frisar que serão exibidas apenas a coligada controladora e as coligadas controladas por ela.

**Desconsiderar eliminação de valores:**Marcando esta opção as eliminações cadastradas irão deixar de compor o saldo atual.

**Separador ponto e vírgula (; ) entre os dados:**Caso essa opção seja marcada, será inserido um ponto e vírgula (;) entre as informações do relatório, separando assim, as colunas.

**Totais das contas sintéticas embaixo:**Com esta opção marcada as totalizações das contas sintéticas serão apresentados ao final de suas contas analíticas, caso contrário os totais serão apresentados à frente das respectivas contas.

**Totalizar ao final débitos/créditos:**Marcando esta opção os toais a débito e a créditos serão impressas no final do relatório.

Aba Filtros

**Conta Paralela:** Permite emitir o relatório filtrando por uma ou mais contas PARALELAS especificas e por faixas de contas (Ex: Da conta paralela 1.1.1.1.001 até a conta paralela 1.1.1.1.008). Também é possível excluir uma conta, um intervalo individualmente e limpar todos os filtros criados através do botão "Limpar todos".

**Histórico:** Permite emitir o relatório filtrando por um ou mais Históricos Padrões. Serão disponibilizados para seleção os Históricos do tipo "*Fechamento*" das Coligadas que compõe o Grupo Empresarial do plano consolidado. Os históricos selecionados podem ser considerados ou desconsiderados para a emissão do relatório. Os filtros serão aplicados individualmente para cada Coligada. Por exemplo: se foi selecionado para considerar o histórico "XYZ" da Coligada 1, somente os lançamentos **desta Coligada** que tem o histórico em questão serão considerados. Não afetará a seleção dos lançamentos das demais Coligadas.

**Tipo de Valor / Moeda:** Permite escolher o valor e/ou moeda que será utilizado para a impressão de seu relatório.

* **Primeiro Valor:** Imprime o relatório utilizando o valor da moeda corrente.
* **Cotação de Outra Moeda:** Marcando esta opção você poderá imprimir os relatórios utilizando outra moeda.   
  Observação: Será possível selecionar apenas uma das moedas utilizadas no processos contábeis multimoeda. Elas estão disponíveis na etapa Moedas dos parâmetros de sistema.

**Formatação:** Permite definir qual será o formato Data e Separador de milhar impresso no relatório. Padrão de data Americano ou Brasileiro e separador de milhar com vírgula ou ponto.

Aba Layout

**Imprimir níveis superiores em negrito:** Imprime os níveis sintéticos em negrito.

**Usar o parâmetro de formato de impressão de saldos para Débito/Crédito:**Imprime os valores a débito, crédito e movimento respeitando o parâmetro de formato de impressão de saldos das contas. Observação: Ao marcá-la a opção "Não exibir sinais nos valores de débito/crédito" fica desabilitada.

**Não exibir sinais nos valores de débito/crédito:**Imprime os valores das colunas de débito e crédito sem sinal. Observação:Ao marcá-la a opção "Impressão de débitos e créditos respeita o parâmetro de formato de impressão de Saldos" ficará desabilitada.

**Alterar título do balancete:**Caso esta opção seja marcada poderá ser definido um novo título para o relatório, conforme desejado, com quantidade máxima de 28 caracteres.

**Inserir texto adicional no final:**Permite a digitação de um texto adicional ao final do relatório.

**Inserir observação abaixo do título**: Possibilita inserir um texto adicional que será impresso no cabeçalho do relatório, logo abaixo do título, e que poderá ter o tamanho de no Máximo 10 linhas. Caso o texto seja muito extenso o mesmo será truncado.

**Ordem alfabética nas contas analíticas:** Marcando esta opção as contas analíticas serão impressas ordenando alfabeticamente o campo Descrição.

**Orientação:**O relatório passa a possuir a orientação Retrato e Paisagem para a impressão e geração de arquivos. Com a orientação Paisagem selecionada, a aba Campos terá sua capacidade de impressão estendida.

**Tipo de arquivo:** Nesta opção estarão disponíveis vários formatos como Word (RTF), PDF, Arquivo texto (TXT), Excel, dentre outros, do qual o usuário poderá utilizar para a exportação do resultado do relatório para seu armazenamento.

**Margem Esquerda, Direita, Superior e Inferior:**Permite configurar as Margens Direita, Esquerda e Superior do relatório. Você poderá aumentar ou reduzir as margens utilizando espaçamentos entre 0 e 10 para a margem Direita, entre 0 e 25 para margem Esquerda e entre 0 e 10 para margem Superior e inferior.

**Cabeçalho apenas na primeira página:** Imprime o cabeçalho do relatório apenas na primeira página.

**N.º página inicial:**Permite informaro número da página inicial para impressão. Com a opção utilizar Numeração Sequencial de páginas marcada, este campo assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

**Utilizar Numeração Sequencial:** Esta opção só ficará habilitada com o Parâmetro "Utilizar Numeração Sequencial de Páginas" marcado. Marque esta opção para que seu relatório obedeça à numeração sequencial informada nos parâmetros do TOTVS Gestão Contábil.

Este recurso auxiliará na emissão de relatórios legais com formatos diferentes em uma única sequência com finalidade de encadernação. Por exemplo, emite-se o Razão da 1ª a 20ª página, logo em seguida emite-se um balancete da página 21ª a 40ª e assim sucessivamente. Desta forma a sequência de página será continua feita automaticamente. Com esta opção marcada, o campo de **N.º página inicial**assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

**Data de Emissão:** Data que será impressa no cabeçalho do relatório. O usuário poderá digitar a data desejada ou, se preferir, poderá selecioná-la através do ícone que se encontra à frente deste campo. A data default deste campo será sempre a atual, dessa forma a funcionalidade de salvar parâmetro por usuário não deve ser considerada. Se esse campo ficar em branco a data de emissão não será impressa.

**Descrição da Contagem de Página:**Determina a descrição que será impressão na emissão do relatório para o número de página. Exemplo: Folha 01 ou Pág. 01

**Quantidade de páginas por arquivo:** Opção criada para bases com grande volume de dados, pois existe uma limitação da quantidade de página que cada máquina consegue processar e exibir. Após informar a quantidade de páginas por arquivo o relatório será quebrado quando a quantidade informada for atingida, tornando possível o processamento e a exibição do relatório.

Aba Campos

Nesta aba estão todos os campos existentes e que poderão ser ou não considerados no relatório, basta selecioná-lo com a opção “Imprimir” marcada, pois caso contrário o mesmo não será impresso. Nesta aba é possível também alterar o tamanho dos campos desde que o total de caracteres não seja ultrapassado. A variação de tamanho de impressão dos campos será alterada conforme o tamanho de fonte e a orientação do relatório (Paisagem ou Retrato). Estão disponíveis, para impressão, os seguintes campos:

* **Código:** Código da conta
* **Descrição:** Descrição da conta
* **Anterior:** Saldo anterior
* **Débitos:** Saldo a débito
* **Créditos:** Saldo a crédito
* **Movimento:** Movimentação da conta
* **Eliminação:** Eliminações da conta
* **Saldo atual:** Saldo da conta

A opção autocompletar irá ajustar o campo Descrição com a diferença entre o limite e o total de caracteres.

Exemplo: Digamos que o Limite seja de 124 caracteres, o Total 110 e o campo Descrição 30. Após marcar a opção "Autocompletar" o campo Descrição irá receber 30 + 124 - 110, ou seja, 44 caracteres.

**Cálculo dos saldos exibidos pelo relatório**

**Anterior:** Composto pelo saldo do último exercício liberado mais a movimentação, da conta consolidada (paralela), anterior a data de início do relatório. 

**Débito:** Composto pelo somatório de todas as partidas a débito, da conta consolidada (paralela), que foram realizadas no período de datas informado pelo usuário.

**Crédito:** Composto pelo somatório de todas as partidas a crédito, da conta consolidada (paralela), que foram realizadas no período de datas informado pelo usuário.

**Movimento (Débitos - Créditos):** Composto por toda movimentação existente no período de datas informado no relatório. Como são consolidados os saldos das contas contábeis de várias coligadas, podem haver divergências entre os períodos em que elas realizaram fechamento.

Exemplo: Digamos que a coligada 1 tenha fechado período em 2017 e a coligada 2 não tenha realizado o fechamento em 2017. Se o período informado no relatório for de 01/01/2017 a 31/12/2017 o saldo anterior e o saldo atual ficarão corretos, porém a coluna movimento não irá refletir corretamente as movimentações realizadas nesse período para a coligada 1, pois os lançamento a débito e a crédito já se encontram na tabela de exercício fechado.

O ideal é que a coligada controladora e suas controladas realizem fechamentos no mesmo período, evitando que as informações contábeis reflitam incorretamente as movimentações realizadas dentro do período desejado.

**Atual:**Composto pelo saldo anterior mais a movimentação da conta consolidada (paralela) e considerando ou não as Eliminações conforme parametrização.
