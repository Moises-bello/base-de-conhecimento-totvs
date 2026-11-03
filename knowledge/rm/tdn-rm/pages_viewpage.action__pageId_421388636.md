---
content_hash: 09f542e378013ca6e0bbc73c1cfa4e881bffe9006d4d388e45a03c63a0e47a85
fetched_at: '2026-06-29T00:09:17.752895+00:00'
page_id: '421388636'
product: rm
source: tdn-rm
title: Habilitação Histórico de Alterações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388636
version: 13
---

**Histórico do Controle de Alterações de Lançamentos/ Extrato de Caixa e Baixas**

O Histórico de Alterações do Lançamento é uma funcionalidade que proporciona armazenar registro histórico para cada um dos processos realizados nos lançamentos. Também será armazenado o histórico das seguintes entidades relacionadas:

* Retenções (tributos)
* Valores de integração
* Rateio por centro de custo
* Rateio por departamento
* Vínculo entre lançamentos
* Retenção Acumulada
* Retenção Acumulada Rateio
* Retenção de IRRF
* Valores restantes a baixar

Para utilizar esta funcionalidade, deverá ser habilitado em Utilitários | "Habilita controle para todos os módulos". A visualização dos registros de histórico de alteração será através do *Anexo* | *Histórico de Alterações* na visão do Lançamento.

Com duplo clique sobre o registro, ou pelo botão "Editar", será possível visualizar os dados do histórico, acessar o detalhamento do cálculo do valor líquido (aba Histórico) e as entidades relacionadas. Vale ressaltar que Lançamentos podem ser afetados indiretamente e terem registros de histórico criados pela execução de processos sobre outro Lançamento (Vínculos).

No processo para habilitar o controle de histórico de alteração dos lançamentos, existirá três opções:

* Habilita Controle para todos os módulos.
* Habilita controle somente para TOTVS Gestão de Imóveis.
* Desabilita controle de Histórico de alteração.

**Habilita Controle para todos os módulos**

O sistema irá preencher o Histórico com a posição atual dos lançamentos (somente para os registros de lançamentos não cancelados), incluindo o primeiro registro histórico com o processo de Carga Inicial (campo Proceso com valor 0). Quando o processo é habilitado é necessário fazer logout/login para que os menus de Posição Financeira sejam exibidos.

Observação: Recomenda-se que esse processo seja executado em dia e horário de menor acesso ao banco de dados do sistema, já que o mesmo realiza uma verificação nas tabelas do lançamento. O tamanho da base também terá impacto no tempo para execução do mesmo.

O histórico do lançamento quando habilitado, controlará os seguintes campos para criação do registro:

| * Coligada * Referência do lançamento * Id do Histórico * Processo executado * Processo aplicação * Data do processo * Data da operação * Memória de Cálculo * Status do lançamento * Classificação * Filial * Centro de Custo * Departamento * Tipo de documento * Cliente/Fornecedor * Conta Caixa * Faturado ou não * Moeda * Data de emissão * Data de vencimento * Data da baixa * Data de cancelamento * Data do cheque * Valor original * Valor Baixado | * **Valor de capitalização** * Juros * **Multa** * **Desconto** * **Valores opcionais (1 a 8)** * **Valor do serviço** * **% base do IRRF** * **Valor do IRRF** * **% base do INSS** * **Valor do INSS** * **Valor do INSS em outra empresa** * **Valor do Sest/Senat** * **Valor da Nota de crédito** * **Valor do adiantamento** * **Valor da devolução** * **Valor vinculado** * **Juros de vendor** * **Valor de perda financeira** * **Valor da operação de desconto** * **Valor do desconto de duplicata** * **Valor do cheque** * **Desconto do acordo** * **Juros do acordo** * **Acréscimo do acordo** * **Valor original baixado** | * **Valor de capitalização baixado** * **Juros baixados** * **Multa baixada** * **Desconto baixado** * **Valores opcionais baixados (1 a 8)** * **Valor do IRRF baixado** * **Valor do INSS baixado** * **Valor do Sest/Senat baixado** * **Valor da Nota de crédito baixado** * **Valor do adiantamento baixado** * **Valor da devolução baixado** * **Valor das retenções baixados** * **Valor vinculado baixado** * **Juros de vendor baixado** * **Valor de perda financeira baixado** * **Fórmula Juros, Desconto, Multa e Capitalização** * **Fórmula dos Valores Opcionais (1 a 8)** * **Tipo Contábil** * **Identificador do Convênio** * **Nosso Número (Cobrança Eletrônica)** * **Código de Barra (Pagamento Eletrônico)** * **Código da Aplicação que executou o processo** * **Usuário e Data de Criação do lançamento** * **Imposto Editado** * **Código de Receita** | * **Data de Contabilização** * **Juros dia** * **Tipo Juros Dia** * **Carência Juros** * **Multa ao Dia** * **Status do Extrato** * **Tem Cheque parcial** * **Código do Indexador** * **Retenções do lançamento** * **Valores de integração** * **Valores de rateio por centro de custo** * **Valores de rateio por departamento** * **Vínculo entre lançamentos** * **Retenção Acumulada** * **Retenção Acumulada Rateio** * **Retenção de IRRF** * **Rateio Por Centro de Custo** * **Rateio Por Departamento** * **Tipo Baixa Pendente** * **Valor Devolução** * **Status Liquidação Duvidosa** * **Status de Negativação** * **Status de Terceirização** * **Tabelas opcionais (1 a 5)** |
| --- | --- | --- | --- |

Na execução dos processos abaixo, será criado registro no histórico para o Lançamento (em parênteses o respectivo código do campo Processo):

| * Inclusão de Lançamento (1) * Alteração de Lançamento (2) * Alteração Global de lançamento (2) * Alteração do Valor do IRRF no lançamento (24) * Alteração do lançamento pelo cancelamento (21) * Alteração do lançamento pelo cancelamento da baixa (22) * Alteração do lançamento pela baixa (28) * Geração de lançamentos de IRRF (20) * Cancelamento de lançamento (3) * Cancelar Transação de Cartão de Crédito/Débito (6) * Baixa de lançamento (5) * Baixa de lançamento com fatura (5) * Baixa com Boleto (5) * Baixa com cheque (5) * Baixa por perda financeira (5) * Baixa por Acordo (Aprovação Simples) (5) * Baixa por Acordo (Ao pagar primeira parcela) (5) * Cancelamento de baixa (6) * Emissão/Recebimento de cheque (7) * Cancelamento de cheque (8) * Incluir fatura (9) * Cancelar fatura (10) * Efetivação de acordo (11) * Cancelamento de acordo efetivado (12) | * Inclusão de acordo não efetivado (32) * Reprovação de acordo (31) * Desconto de duplicata (13) * Efetivar desconto de duplicata (14) * Devolver desconto de duplicata (15) * Vincular Lançamentos  - incluir vínculos (16) * Vincular Lançamentos  - remover vínculos (29) * Remessa de pagamento (17) * Retorno bancário (18) * Inclusão de Tributo pelo EFD Fiscal (19) * Atualização de valores de integração - Integração módulo Gestão Imobiliária (33) * Alteração Conta Caixa e Convênio do Boleto (23) * Alteração Data Vencimento Boleto (23) * Edição de boleto via interface (23) * Conversão de Boletos (23) * Remover código de barras do boleto (23) * Inclusão de boleto (25) * Cancelamento Boleto (26) * Desvincular lançamentos do boleto (30) * Contabilizar baixados (27) * Liquidação duvidosa (35) * Cancelamento liquidação duvidosa (36) * Inclusão de Borderô, remessa e retorno de negativação (37) * Inclusão de Borderô, remessa e retorno de terceirização (38) |
| --- | --- |

**Histórico de Baixas**

As informações do *Histórico de Baixa* do lançamento financeiro, onde se incluem os valores da baixa, valores de integração, rateio por centro de custo, rateio por departamento e tributos, serão armazenadas na criação do registro de [histórico de lançamento](http://tdn.totvs.com/display/LRM/ER_Historico_Alteracao_Lancamentos).    
Observação: O Histórico *d*e Baixa de lançamento financeiro controla os mesmos campos do Histórico de Alteração.

Fórmulas de Baixa

As funções de fórmula exibem a posição financeira da Baixa do Lançamento em uma data específica, baseadas nos dados das tabelas de *Histórico de Baixa*com o registro selecionado como indicado na [Posição Financeira](http://tdn.totvs.com/display/LRM/ER_Historico_Alteracao_Lancamentos).

TABLANBAIXAPF: Valor de um campo do item de baixa do lançamento numa determinada data.  
TABLANBAIXARATCCUPF: Valor de um campo do rateio por centro de custo do item de baixa do Lançamento numa determinada data.  
*TABLANBAIXARATDEPPF*: Valor de um campo do rateio por Departamento do item de baixa do lançamento numa determinada data.  
VALORTRBLANBAIXAPF: Valor do tributo do item de baixa do lançamento numa determinada data.  
VALORINTEGRACAOLANBAIXAPF: Valor para um campo de integração do item de baixa do lançamento numa determinada data.

Observação: As funções de fórmula acima, terão o mesmo conjunto de parâmetros de entrada da sua correspondente, que traz os dados do estado atual do lançamento acrescentando somente o parâmetro de data da posição financeira desejada. O retorno será sempre sobre os dados das tabelas de histórico correspondente. O contexto utilizado determina o resultado que a fórmula irá retornar na execução.

**Posição Financeira de Lançamentos**

A posição financeira é o estado de um lançamento numa data específica, ou seja, os valores para o lançamento naquele momento, sobre um processo de Baixa ou sobre uma data informada.  
Através do Menu Contas a Pagar/Receber | Operações Financeiras | Posição Financeira, é possível pesquisar a posição dos lançamentos numa data específica baseado no Histórico de Baixas. Será selecionado o último registro de histórico por lançamento com data menor ou igual à pesquisa. Na visão exibida será possível chamar o cálculo do valor líquido, exibindo no resultado o Total Original, Total Algébrico e Total Líquido.

Exemplo:

01/03 (data da operação): realizada uma baixa com data 01/03 (data do processo), Id Processo 1 -> Status "baixado"

05/03: realizado o cancelamento da baixa com data 05/03, Id Processo 2 -> Status "em aberto"

08/03: realizada uma baixa com data 20/02, Id Processo 3 -> Status "baixado"

10/03: realizado o cancelamento da baixa com data 09/03, Id Processo 4 -> Status "em aberto"

Posição

Dia 25/02: status "baixado"

Dia 05/03: status "baixado"

Dia 08/03: status "baixado"

Dia 09/03 ou posterior: status "em aberto"

Observação: Se a posição tivesse sido solicitada no dia 05/03, quando a operação realizada no dia 08/03 ainda não existia, a posição seria "em aberto".

**Informações Importantes**

* Quando ocorrer a liberação de período no TOTVS Gestão Financeira, devem ser excluídos todos os registros das tabelas de histórico de baixa, juntamente com o histórico de alteração do lançamento. O processo é chamado através do menu *Utilitários | Liberação de Período*.
* No processo de exclusão do lançamento serão excluídos todos os registros das tabelas histórico de alteração do lançamento.
* Para cada processo executado no lançamento, ou em uma das entidades vinculadas, que altere alguma informação ou Baixe um lançamento, é gravado uma linha no Anexo de Histórico. Será armazenado o processo executado e uma cópia dos dados do lançamento, ou seja, o registro de histórico será uma cópia do lançamento e de todas as outras entidades controladas, desde que o registro para a mesma exista, no momento e após a execução da operação. Irá gerar uma linha para cada lançamento atualizado pelo processo de retorno bancário.
* Quando da exclusão do lançamento financeiro todo o seu histórico também será excluído.
* Se o lançamento possuir mais de uma baixa (baixas parciais ou vários meios de pagamento), o processo de cancelamento de baixa deve ser realizado da baixa mais recente retroagindo até aquela que se deseja cancelar, para que os valores da Posição Financeira não fiquem inconsistentes. Por exemplo, se for feito um pagamento com dois cartões, a baixa do segundo cartão deve ser estornada antes da baixa do primeiro.

**Habilita Controle somente para TOTVS Gestão de Imóveis**

O sistema irá preencher o Histórico com a posição atual dos lançamentos, somente para os registros do Gestão de Imóveis não cancelados, incluindo o primeiro registro histórico com o processo de Carga Inicial,controlando os mesmos campos de registro de histórico da opção 'Habilita Controle para todos os módulos'. Esta opção não gera histórico para Extratos financeiro.  
Não será exibido o menu de posição financeira.

Importante:

Essa opção estará sempre disponível mesmo para quem já utiliza o histórico geral habilitado e que estejam no novo modelo revitalizado do TOTVS Gestão de Imóveis.   
Ao marcar a opção "Habilitar somente para TOTVS Gestão de Imóveis*"* todos os registros de histórico que já existiam na base, e que não sejam do TOTVS Gestão de Imóveis, serão removidos de forma irreversível.

**Desabilita Controle de Histórico de alteração**

Essa opção desabilita o Flag de controle, ou seja, o sistema não irá mais criar registros de histórico, além disso, excluirá todos os registros de histórico existentes.   
O controle de histórico de alteração é global, independente de coligada, uma vez habilitado irá funcionar para todas elas.

Observação: ao realizar a troca de controle do histórico, é aconselhável que entre novamente no financeiro para a leitura dos parâmetros.

Veja Também

* [DT - Histórico das tabelas da Baixa de Lançamentos Financeiros](http://tdn.totvs.com/x/b93uDQ)
