---
content_hash: 306de5f522bca030e00b28eee698ca9598aa2c58a543bc04e99cc6f43eb4ce8a
fetched_at: '2026-06-29T00:10:20.039484+00:00'
page_id: '485434646'
product: rm
source: tdn-rm
title: DT Novo Fluxo de Caixa - 12.1.29
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Novo+Fluxo+de+Caixa+-+12.1.29
version: 98
---

# Novo Fluxo de Caixa

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Backoffice |
| **Módulo:** | TOTVS Gestão Financeira |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Fluxo de Caixa | Novo de fluxo de caixa |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Informe a(s) rotina(s) envolvidas. | Informe o nome técnico da(s) rotina(s) envolvidas. | |  |  | |
| **Cadastros Iniciais:** | Fluxo de Caixa. |
| **Parâmetro(s):** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | <http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-11562> |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQLServer e Oracle |
| **Tabelas Utilizadas:** | N/A |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.29 |

Novo Fluxo de CaixaVisão do Fluxo de CaixaVisão Fluxo de Caixa

A visão do Fluxo de Caixa é baseada no modelo clássico de Fluxos de Caixa utilizando planilhas eletrônicas. O Gestão Financeira, integrado ao Microsoft Excel, exibe uma planilha diretamente relacionada aos Lançamentos Financeiros e Extratos de Caixa.

Nesta visão também é possível visualizar gráficos de Entradas, Saídas e Saldo Final referente às informações geradas do Fluxo de Caixa.

Para visualizar o Fluxo de Caixa, basta acessar o menu Gestão Financeira | Fluxo de Caixa e preencher os dados para sua geração.

Neste modelo, é possível salvar o Fluxo de caixa gerado em dois modelos:

* Cenário: veja mais na aba Cenários;
* Arquivo  Excel: permite que o Fluxo de caixa gerado seja salvo em arquivo Excel, como demonstrado abaixo:

* Gráficos:

* Composição dos Saldos Iniciais: Apresenta a rastreabilidade da origem do saldo inicial por conta caixa, para valores Previsto e Realizado.

                                                    

Previsto

**Previsto:**É a soma do valor do rateio de Centro de Custo dos lançamentos em aberto mais a soma do valor em aberto para os lançamentos Baixado Parcialmente:

* Aplicando os filtros de conta caixa, centro de custo e período;
* Lançamento com status “Em aberto” ou “Baixado parcialmente”;
* Lançamentos diferentes de faturado;
* Lançamentos com o tipo baixa pendente diferente de 'Bloqueado pela confissão de dívida';
* Lançamentos que possuem Natureza Financeira;
* Lançamentos com classificação diferente de “Parcialmente Adiantado”;

Saldo disponível das Aplicações financeiras com vencimento entre o período informado e saldo diferente de zero;

Extrato de caixa manuais:

* Aplicando os filtros de conta caixa, centro de custo;
* Não compensado;
* Tipo Saque manual, Deposito manual, Saque transferência, Deposito transferência, Saque CPMF e Dep. Canc. CPMF.

**Saldo Inicial Previsto:** Soma do valor original (Receber – Pagar) dos lançamentos com data de vencimento menor que a data inicial do período;

* Lançamentos com status “Em aberto” ou “Baixado parcialmente”;
* Lançamentos diferentes de faturado;
* Lançamentos que possuem natureza financeira;
* Lançamentos com classificação diferente de “Parcialmente Adiantado”.

Realizado

**Realizados:**É a soma do valor do rateio de centro de custo baixado:

* Aplicando os filtros de conta caixa, centro de custo e período;
* Lançamento Baixados;
* Lançamentos que possuem natureza financeira;
* Lançamentos com classificação diferente de “Parcialmente Adiantado”;
* Lançamentos baixados por Acordo não são considerados;

Extratos de caixa manuais:

* Aplicando os filtros de conta caixa e centro de custo;
* Extrato compensado;
* Extrato do tipo saque manual, depósito manual, saque transferência, depósito transferência, saque CPMF e Dep. Canc. CPMF;
* Extrato que não possui lançamento vinculado;
* Extratos que possuem Natureza Financeira;

**Saldo Inicial Realizado:**É a soma do valor do rateio de centro de custo baixado (Receber – Pagar) dos lançamentos baixados com data de baixa menor que a data inicial do período:

* Lançamentos baixados e parcialmente baixados;
* Lançamentos que possuem natureza financeira;
* Lançamentos com classificação diferente de “Parcialmente Adiantado”;
* Lançamentos baixados por acordo não são considerados;

Saldo data base da conta caixa;

* Data base conta caixa menor que a data do término do período informado.

Soma dos Extratos de caixa manuais;

* Aplicando os filtros de conta caixa e centro de custo;
* Extrato compensado;
* Extrato do tipo saque manual, depósito manual, saque transferência, depósito transferência, saque CPMF e Dep. Canc. CPMF;
* Data de compensação menor que a data inicial do período;
* Extrato que não possui lançamento vinculado;
* Extrato que possui natureza financeira;

O Saldo Inicial Realizado é composto pelo Saldo Final Realizado do período anterior. Caso o parâmetro "Considerar período anterior" estiver selecionado, os valores do Saldo Inicial Realizado poderão sofrer alterações por filtrarem valores fora do período informado no processo.

Configurações

Periodicidade: Define o modo de exibição do Fluxo de Caixa dentro do período estabelecido, podendo ser:

* Diário: exibe no Fluxo de Caixa os valores totais diariamente;
* Semanal: exibe no Fluxo de Caixa os valores totais semanalmente;
* Mensal: exibe no Fluxo de Caixa os valores totais mensalmente;
* Trimestral: exibe no Fluxo de Caixa os valores totais a trimestralmente;
* Anual: exibe no Fluxo de Caixa os valores totais anualmente;
* Semestral: exibe no Fluxo de Caixa os valores totais semestralmente;
* Quinzenal: exibe no Fluxo de Caixa os valores totais quinzenalmente;

Observação: 

* Todas as opções disponíveis de periodicidade exibem valores referentes às movimentações realizadas que estiverem classificadas com o Centro de Custo e/ou Natureza Financeira.

Saldo inicial previsto por naturezas e/ou centros de custo: Ao selecionar esta opção, será considerado o saldo anterior previsto ao valor do período definido do fluxo de caixa. O Saldo Inicial Previsto terá seus valores zerados pois serão rateados para as naturezas na coluna Previsto do Fluxo de caixa.

Não considerar natureza com valor zerado: Define que quando marcado, o fluxo de caixa apresentará somente natureza que tenha valor e irá desconsiderar as naturezas cadastradas no sistema que não tenham valor. Quando desmarcado, o fluxo de caixa gerado apresentará todas as naturezas cadastradas no sistema, com e sem valor atribuído.

Considerar lançamento com conta/caixa vazia: Quando marcado, no fluxo de caixa gerado serão considerados os lançamentos que não tenham conta/caixa informada.

Considerar centro de custo por natureza: Ao selecionar esta opção, são exibidos no fluxo de caixa os valores por centro de custo de acordo com a natureza. O centro de custo será exibido com as informações: Coligada + Cód. Centro de Custo + Descrição.

Considerar baixa não compensada como previsão: Ao selecionar esta opção, o valor previsto será calculado considerando os lançamentos baixados com extratos ainda não compensados. Por exemplo, ao baixar um lançamento financeiro sem marcar a opção de "Compensar Extrato", a baixa será realizada e o extrato ficará com o status "Não compensado". Desta forma, se a baixa deste lançamento estiver no período selecionado e o parâmetro marcado, o valor será considerando no campo "Previsto". Se o lançamento estiver baixado com extrato compensado, o valor será exibido no campo "Realizado", utilizando a data de compensação como referência. 

Considerar apenas código sintético para natureza: Ao selecionar esta opção, serão apresentadas somente os códigos sintéticos do Centro de Custo e/ou Natureza Orçamentária Financeira no fluxo de caixa gerado.

Considerar somente os valores previstos na data prevista: Ao selecionar esta opção, o valor previsto será calculado considerando os valores dos lançamentos e extratos na data prevista. Exemplo: um lançamento no valor de R$100,00 com data de vencimento 01/07/2019, ao emitir o fluxo de caixa com periodicidade diária, o valor desse lançamento somente será considerado para o dia 01/07/2019, não sendo considerado para os dias posteriores.

Considerar saldo final previsto nos períodos posteriores: Este parâmetro controla a exibição de valores do Previsto, seja item ou saldo (Saldo Inicial e Saldo Final). O mesmo reflete nos saldos dos períodos futuros como ocorre para a coluna Realizado.

Considerar saldo inicial conforme a coligada proprietária: Este parâmetro carrega os saldos das contas caixas globais considerando a coligada proprietária, realizando a carga do saldo inicial dos extratos de caixa de tal forma que traga os saldos dos extrato das coligadas selecionadas. 

   Importante: Os parâmetros "Considera período anterior" e "Considerar somente os valores previstos no vencimento" não podem ser marcados simultaneamente. Ao selecionar um destes, o outro fica desabilitado.

Data previsto: Permite definir a data previsto para o cálculo do valor original ou líquido no fluxo de caixa gerado.

* Data de previsão de baixa: Ao selecionar esta opção, o fluxo de caixa irá exibir as informações de registros considerando a data de previsão de baixa informada no lançamento financeiro.
* Data de vencimento: Ao selecionar esta opção, o fluxo de caixa irá exibir as informações de registros considerando a data de vencimento informada no lançamento financeiro.

Valor Previsto: Este parâmetro tem por função definir qual valor será exibido no fluxo de caixa como valor previsto. Sua influência está sobre os lançamentos financeiros, não afetando os valores provenientes de extratos e aplicações financeiras.

* Valor Original: Será utilizado o valor original, ou seja, o valor  cadastrado na base de dados sem a execução de qualquer cálculo.
* Valor líquido na data atual: Para os lançamentos abertos e parcialmente baixados, será executado o cálculo do valor líquido utilizando como referência a data do dia que está sendo gerado o fluxo de caixa.   
  Como exemplo, vamos supor que estamos gerando um fluxo de caixa na data de  10/05/2019  para o período de   a  com periodicidade diária. Os valores dos lançamentos com vencimento anterior ao dia  serão apresentado com cálculo de juros, multa, etc, e os valores dos lançamentos com vencimento igual ou posterior  a esta data terão os respectivos descontos considerados.
* Valor líquido na data do previsto: Esta opção é dependente do parâmetro Data Previsto**.** Caso a opção selecionada neste parâmetro seja "Data Vencimento", a data utilizada como referência para o cálculo do valor líquido será  a data de vencimento cadastrada no lançamento. Se a opção selecionada for  "Data de Previsão de Baixa", a data de previsão de baixa cadastrada no lançamento será utilizada como referência para o cálculo do valor líquido.

**Observação**: O valor líquido calculado será rateado pelo percentual cadastrado nos rateios do lançamento para ser exibido no fluxo de caixa.

Planejamento: Pode ser selecionado um planejamento para compor os valores planejados do fluxo de caixa gerado de acordo com os itens de planejamento cadastrados.

Filtros

**Lista conta/caixa inativa:**Este parâmetro permite definir se serão listadas as contas/caixa inativas nos filtros para seleção no fluxo de caixa. Ao marcar ou desmarcar esta opção, deverá ser atualizada a visão do filtro.

Cenário

O cenário no contexto do TOVS Gestão Financeira corresponde à imagem do fluxo de caixa em um instante no tempo, ou seja, dada uma configuração e filtros parametrizados, as informações geradas a partir destes na data de geração do fluxo de caixa representam o que queremos descrever como um cenário.

* **Inclusão de cenário**
* **Habilitar/Desabilitar configurações e filtro**
* **Exibição de cenário**
* **Editar, renomear cenário**
* **Controlar revisões de cenários**

As opções "Incluir, Excluir e Editar Cenário" terão controle de permissão de acesso através de Globais em Serviços Globais | Segurança | Perfis | Gestão Financeira | Fluxo de Caixa | Cenários. O Perfil deverá ser associado ao Usuário de acesso ao sistema.

Saldos Fluxo de CaixaSaldos

**Saldo Inicial:**É composto pela soma dos saldos nas datas base das contas/caixa selecionadas, subtraídos ou somados os valores de todos os lançamentos/extratos baixados/compensados até a data inicial do período selecionado.

**Saldo de Entradas:** É composto pelo somatório dos valores de natureza *A Receber* dentro do período informado.

**Saldo Saídas:** É composto pelo somatório de todos os valores de natureza *A Pagar* que pertençam ao período definido.

**Saldo Operacional:** Este saldo é obtido na subtração do total de *Entradas* pelo total de *Saídas*. Permite valores negativos, caso no período ocorra mais saídas do que entradas.

**Saldo Final:** É obtido pelo somatório entre *Saldo Inicial* e *Saldo Operacional*. Permite valores negativos.

Simulação Simulação 

O Fluxo de Caixa disponibiliza a Simulação sobre a planilha que permite a digitação dos valores nos campos, recalculando automaticamente os totalizadores.

DadosDados

Nessa aba serão apresentados os dados dos Lançamentos Financeiros, Extratos Financeiros e Aplicações Financeiras com as seguintes Informações: Coligada, Id. Lan., Valor, Valor Baixado/Compensado, Data de Vencimento, Data baixa/Compensação, Histórico, Nome/Razão Social e Nome Fantasia do Cliente/Fornecedor.

Observação: Com a opção [Considerar no Relatório de Fluxo de Caixa](https://tdn.totvs.com/pages/viewpage.action?pageId=421388695) habilitada, serão considerados os lançamentos financeiros e baixas na geração do fluxo de caixa. Caso a opção acima esteja desabilitada, não serão considerados os lançamentos na geração.

[DT Planejamento do Fluxo de Caixa](http://tdn.totvs.com/display/LRM/DT+Planejamento+do+Fluxo+de+Caixa)
