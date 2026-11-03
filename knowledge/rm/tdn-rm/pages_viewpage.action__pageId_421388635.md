---
content_hash: 34b1ce494f7c0b9c30f3eab42c90d29dd869fc221789a06d86528d3d7c11a396
fetched_at: '2026-06-29T00:09:17.740070+00:00'
page_id: '421388635'
product: rm
source: tdn-rm
title: Histórico de Alterações do Extrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388635
version: 3
---

O Histórico de Alterações do Extrato é uma funcionalidade que proporciona armazenar um registro histórico para cada um dos processos realizados diretamente e indiretamente.  
Para ativar esta funcionalidade, é necessário habilitar a opção Utilitários|Controle de Histórico de Alterações/ Habilita Controle para todos os módulos, processo que irá parametrizar o sistema para realizar o controle e gera o primeiro registro do Histórico de **Carga Inicial.**Quando o processo é habilitado é necessário fazer logout/login para que os menus de Posição Financeira sejam exibidos.

Será criado um registro de histórico para cada extrato de caixa não cancelado. O processo é executado para todas as coligadas do sistema.  
 Para cada processo executado no extrato que altere alguma informação relacionada, é gravado um registro no histórico. Será armazenado o processo executado e uma cópia dos dados do extrato, ou seja, o registro de histórico será uma cópia do extrato após a execução da operação.

* O Histórico do extrato controlará os seguintes campos:
* Coligada
* Referência extrato
* Id do Histórico
* Processo executado
* Data do processo
* Data da operação
* Número do Documento
* Tipo
* Centro de Custo
* Coligada da Conta/Caixa
* Coligada da Natureza Orçamentária Financeira
* Coligada da Conta/Caixa de Transferência
* Coligada do Extrato de Transferência
* Conta/Caixa
* Conta/Caixa de Transferência
* Departamento
* Filial
* Natureza Orçamentária Financeira
* Compensado
* Data
* Data de Cancelamento
* Data de Compensação
* Data de Estorno
* Data de Reconciliação
* Data de Vencimento
* Extrato Estornado
* Extrato Reconciliado
* Extrato de Transferência
* Valor
* Forma de Pagamento

A execução de um dos seguintes processos irá criar um Registro de Histórico no extrato:

* Inclusão
* Inclusão de extrato de transferência
* Alteração
* Alteração Global
* Cancelamento
* Exclusão
* Compensação
* Cancelamento compensação
* Conciliação
* Cancelamento conciliação
* Emissão de cheque
* Cancelamento de cheque

Para visualizar os registros de histórico de alteração acessar o Anexo|Histórico de Alterações na visão do extrato. Vale ressaltar que extratos podem ser afetados indiretamente e terem registros de histórico criados pela execução de processos sobre outro extrato (estorno no cancelamento, inclusão de mútuo, quebra de vínculo de mútuo e transferência na exclusão), ou sobre um lançamento financeiro (liberação de período).  
 No processo de Liberação de Período serão excluídos os registros de histórico do extrato de caixa com data menor ou igual à data liberada.

**Posição Financeira de extratos**

Através do menu  Movimentações Bancárias | Controle Bancário | Posição Financeira, é possível pesquisar a posição dos extratos de caixa numa data especifica baseado no histórico de alterações. Será selecionado o último registro de histórico por extrato com data menor ou igual à pesquisa.

**Observação:**

Este processo tem a mesma funcionalidade da posição financeira do lançamento.

Foram criadas novas funções de fórmula para trazer a Posição financeira do extrato numa data específica, sendo elas:

* TABEXTRATOPF: Valor de um campo do extrato numa determinada data.
* VALOREXTRATOPS: Valor do extrato numa determinada data.
* VALORCOMPENSADOPS: Valor compensado do extrato numa determinada data.

 As funções de fórmula acima receberão como o parâmetro, além daqueles relacionados à sua regra, a data da posição financeira desejada. O retorno será sempre sobre os dados da tabela de histórico.   
 Para opção *"**Desabilita Controle de Histórico de alteração**"*, irá desabilitar o Flag de controle, ou seja, o sistema não irá mais criar registros de histórico, além disso, excluirá todos os registros de histórico existentes.
