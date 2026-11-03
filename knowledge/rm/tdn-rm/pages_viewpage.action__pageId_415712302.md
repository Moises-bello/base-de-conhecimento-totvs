---
content_hash: 770391ec2bbf82be1bdb03008ea592262c42f0926cb1e0603f051280bdcf0049
fetched_at: '2026-06-29T00:09:12.115878+00:00'
page_id: '415712302'
product: rm
source: tdn-rm
title: DT Gerar Relatório Contábil Balancete Consolidado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415712302
version: 28
---

# Gerar Relatório Contábil Balancete Consolidado

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Contábil |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Processo | Gerar relatório contábil Balancete Consolidado |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Cálculo Saldo Consolidado | Saldo das contas contábeis consolidadas através de um plano paralelo do tipo consolidado. | | Contas Paralelas | Contas Paralelas. | | Contas Contábeis | Contas Contábeis. | | Lançamentos Contábeis | Partidas a débito e crédito que compõem o lançamento contábil. | | Período Fechado/Liberado | Saldo das contas contábeis de períodos fechados e/ou liberados que são utilizado para compor total. | |
| **Cadastros Iniciais:** | Plano de contas Paralelo  Lançamentos contábeis |
| **Parâmetro(s):** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1953> - (Rotina que retorna o saldo consolidado para o relatório consolidado processar)  <http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1878>  <http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1986>  <http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-1877> - (Implementação da estrutura server necessária para executar o relatório balancete consolidado)  <http://jiraproducao.totvs.com.br/browse/CONTROLADORIA01-2094> -(Apresentar coluna de eliminações no balancete consolidado.) |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL, Oracle |
| **Tabelas Utilizadas:** | CCONTA2, CCTACTA2, CCONTA, CPARTIDA, CSALDOEXERCICIO, CEXERCICIO |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.22 |

#

## Descrição

O balancete consolidado reflete a contabilidade de uma empresa ou organização num determinado período e tem como objetivo consolidar os saldos das contas contábeis que foram associadas a um plano de contas paralelo do tipo "Consolidação de Saldos". A tela de parâmetros possui 3 abas que serão detalhadas a seguir.

**1 - Dados**

**Período inicial e final:**Intervalo de datas para impressão do relatório.

**Plano de contas consolidado da coligada corrente:** Plano de contas, com finalidade Consolidação de Saldos, que será utilizado na geração do relatório. Vale ressaltar que serão exibidos apenas os planos de conta da coligada corrente. Caso ele seja alterado ou apagado o filtro de contas paralelas será limpo.

**Selecionar Coligada/Filial:**Permite selecionar Coligadas/Filiais cujos dados serão processados e consolidados no relatório. É importante frisar que serão exibidas apenas a coligada corrente e as coligadas controladas por ela.

**Desconsiderar eliminação de valores:** Marcando esta opção as eliminações cadastradas irão deixar de compor o saldo atual.

**Totais das contas sintéticas embaixo:**Com esta opção marcada as totalizações das contas sintéticas serão apresentados ao final de suas contas analíticas, caso contrário os totais serão apresentados à frente das respectivas contas.

**Totalizar ao final débitos/créditos:**Marcando esta opção os toais a débito e a créditos serão impressas no final do relatório.

**Filtro de contas paralelas:**Permite filtrar o relatório por uma ou mais contas paralelas e por faixas de contas (Ex: da conta 1.1.1.1.001 até a conta 1.1.1.1.008). Também é possível excluir uma conta ou um intervalo individualmente ou limpar todos os filtros criados através do botão "Limpar todos".

**2 - Layout**

**Imprimir níveis superiores em negrito:** Imprime os níveis sintéticos em negrito.

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

**N.º página inicial:** Permite informaro número da página inicial para impressão. Com a opção utilizar Numeração Sequencial de páginas marcada, este campo assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado.

**Utilizar Numeração Sequencial:** Esta opção só ficará habilitada com o Parâmetro "Utilizar Numeração Sequencial de Páginas" marcado. Marque esta opção para que seu relatório obedeça à numeração sequencial informada nos parâmetros do TOTVS Gestão Contábil.

Este recurso auxiliará na emissão de relatórios legais com formatos diferentes em uma única sequência com finalidade de encadernação. Por exemplo, emite-se o Razão da 1ª a 20ª página, logo em seguida emite-se um balancete da página 21ª a 40ª e assim sucessivamente. Desta forma a sequência de página será continua feita automaticamente. Com esta opção marcada, o campo de **N.º página inicial**assumirá o valor da sequência automática gerada pelo sistema, não podendo ser alterado. Automaticamente será carregado a última página impressa para dentro do campo Nº página Inicial. Ao finalizar o relatório o parâmetro é atualizado de acordo com o número da última página gerada.

**Data de Emissão:** Data que será impressa no cabeçalho do relatório. O usuário poderá digitar a data desejada ou, se preferir, poderá selecioná-la através do ícone que se encontra à frente deste campo. A data default deste campo será sempre a atual, dessa forma a funcionalidade de salvar parâmetro por usuário não deve ser considerada. Se esse campo ficar em branco a data de emissão não será impressa.

**Descrição da Contagem de Página:**Determina a descrição que será impressão na emissão do relatório para o número de página. Exemplo: Folha 01 ou Pág. 01

**Quantidade de páginas por arquivo:** Opção criada para bases com grande volume de dados, pois existe uma limitação da quantidade de página que cada máquina consegue processar e exibir. Após informar a quantidade de páginas por arquivo o relatório será quebrado quando a quantidade informada for atingida, tornando possível o processamento e a exibição do relatório.

**3 - Campos**

Nesta aba estão todos os campos existentes e que poderão ser ou não considerados no relatório, basta selecioná-lo com a opção “Imprimir” marcada, pois caso contrário o mesmo não será impresso. Nesta aba é possível também alterar o tamanho dos campos desde que o total de caracteres não seja ultrapassado. A variação de tamanho de impressão dos campos será alterada conforme o tamanho de fonte e a orientação do relatório (Paisagem ou Retrato). Estão disponíveis, para impressão, os seguintes campos:

* **Código:** Código da conta
* **Descrição:** Descrição da conta
* **Anterior:** Saldo anterior
* **Débitos:** Saldo a débito
* **Créditos:** Saldo a crédito
* **Movimento:** Movimentação da conta
* **Eliminação**: Saldo das Eliminações da conta
* **Saldo atual:** Saldo da conta

A opção autocompletar irá ajustar o campo Descrição com a diferença entre o limite e o total de caracteres: Ex: Digamos que o Limite seja de 124 caracteres, o Total 110 e o campo Descrição 30. Após marcar a opção ""Autocompletar" o campo Descrição irá receber 30 + 124 - 110, ou seja, 44 caracteres.

**Cálculo dos saldos exibidos pelo relatório**

**Anterior:** Composto pelo saldo do último exercício liberado mais a movimentação, da conta consolidada (paralela), anterior a data de início do relatório. 

**Débito:** Composto pelo somatório de todas as partidas a débito, da conta consolidada (paralela), que foram realizadas no período de datas informado pelo usuário.

**Crédito:** Composto pelo somatório de todas as partidas a crédito, da conta consolidada (paralela), que foram realizadas no período de datas informado pelo usuário.

**Movimento (Débitos - Créditos):** Composto por toda movimentação do período de datas informado no relatório. Como são consolidados os saldos das contas contábeis de várias coligadas, podem haver divergências entre os períodos em que elas realizaram fechamento.

Ex: Digamos que a coligada 1 tenha fechado período em 2017 e a coligada 2 não tenha realizado o fechamento em 2017. Se o período informado no relatório for de 01/01/2017 a 31/12/2017 o saldo anterior e o saldo atual ficarão corretos, porém a coluna movimento não irá refletir corretamente as movimentações realizadas nesse período para a coligada 1, pois os lançamento a débito e a crédito já se encontram na tabela de exercício fechado.

O ideal é que a coligada controladora e suas controladas realizem fechamentos no mesmo período, evitando que as informações contábeis reflitam incorretamente as movimentações realizadas dentro do período desejado.

**Eliminação**: Composto por todas as movimentações eliminadas cadastradas para conta no período em que o relatório será gerado.

**Saldo Atual:** Composto pelo saldo anterior mais a movimentação da conta consolidada (paralela).

## Procedimento para Utilização

1 - Acesse o menu Balancete Consolidado, existente na aba relatórios.

2 - Entre com as informações necessárias na aba Dados.

3 - Entre com as informações necessárias na aba Layout.

4 - Entre com as informações necessárias na aba Campos.

5 - Execute o relatório.
