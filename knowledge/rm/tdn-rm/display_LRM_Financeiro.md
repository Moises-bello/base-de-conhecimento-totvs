---
content_hash: 2e1098e632327a48204ee340041219484da95baeed4d84bf783bb80d103c2814
fetched_at: '2026-06-29T00:08:05.095619+00:00'
page_id: '235583770'
product: rm
source: tdn-rm
title: Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/Financeiro
version: 10
---

|  |  |
| --- | --- |
| Descrição | Financeiro |
| Observações | Alterações feitas no TOTVS Gestão Financeira |

# 4.1 Visão por Data Base

Foram desenvolvidas duas novas telas para consulta de registros com a visão na data base, estas telas só estão disponiveis versão com data base e revitalização a partir da versão 12.1.9.

 São elas

|  |  |
| --- | --- |
| **Posição Financeira Lançamentos** | **Posição Financeira Extratos** |
|  |  |

Foram adicionados novos status para o campo BAIXAPENDENTE na tabela FLAN. Sempre que um lançamento financeiro estiver com o campo BAIXAPENDENTE  com um valor diferente de 0 (Zero) não será possível fazer a baixa.

Os novos status foram criados para situações onde os planos de financiamento são gerados por processos do TIN e que ainda não estão efetivados.  Como não há mais a redundância de dados do TIN com o financeiro os lançamentos são criados diretamente no financeiro e enquanto seu processo de origem ainda estiver “em preparação” ficam bloqueados evitando assim possíveis baixas indevidas.

Segue abaixo a descrição e motivo do bloqueio.

* **Livre = 0**

Status que permite que o lançamento financeiro seja baixado. Este status é aplicado caso nenhum das condições abaixo se apliquem.

* **Distrato = 1**

Utilização exclusiva do financeiro.

* **Cartão Credito = 2**

Utilização exclusiva do financeiro.

* **Efetivação Acordo = 3**

Utilização exclusiva do financeiro.

* **Bloqueio Plano Financiamento Venda = 4**

As parcelas financeiras recebem este status quando forem criadas pelo processo “Gerar Plano de financiamento” **da Venda** e permanecem assim até que a venda seja efetivada e os lançamentos desbloqueados através do processo de “Desbloquear Lançamentos Financeiros” (processo existente na visão da venda).

* **Bloqueio Venda = 5**

Bloqueio realizado pelo processo de “Bloquear Venda” existente na visão da venda.

* **Bloqueio Geração Distrato = 6**

Quando uma venda possui um Distrato e ele é efetivado, o sistema aplicada o status =6 nas parcelas do plano de financiamento de venda (receber). Antes da versão de revitalização, estas parcelas era cancelas, mas devido a evolução que permite desfazer um distrato, o cancelamento não é mais aplicado. Desta forma evita-se que parcelas de recebimento de venda de um contrato distratado sejam baixadas indevidamente ou remetidas a banco.

* **Bloqueado Geração Aditivo = 7**

As parcelas financeiras recebem este status quando forem selecionadas (no click) em Aditivos de Venda do tipo Renegociação e Alteração de Vencimento.  
Ao efetivar o aditivo de renegociação as parcelas que antes estavam bloqueadas, são canceladas.  
Ao efetivar o aditivo de alteração de vencimento as parcelas são desbloqueadas, voltando para o status =0.

* **Bloqueado Plano Venda Por Distrato = 8**

As parcelas financeiras recebem este status quando forem criadas pelo processo “Gerar Plano de financiamento” **do Distrato da venda** e permanecem assim até que o distrato seja efetivado.

* **Bloqueado Plano Venda Por Aditivo = 9**

As parcelas financeiras recebem este status quando forem criadas pelo processo “Gerar Plano de financiamento” **do Aditivo da venda** e permanecem assim até que o aditivo seja efetivado.

* **Bloqueado Divergência Valores TIN = 10**

As parcelas financeiras recebem este status através da ferramenta de “divergências de Valores” que trata valores inconsistentes entre o TIN e o Financeiro, se a inconsistência não for corrigida o sistema bloqueia a parcela, se necessário o usuário deverá entrar em contato com a Central de Atendimento.

* **Bloqueado Parcela "Órfã" = 11**

São lançamentos criados de parcelas que não estavam vinculadas a lançamentos financeiros. Provavelmente no passado a carga inicial da base de dados importou as vendas e suas parcelas para efeitos de histórico mas os lançamentos financeiros correspondentes a essas parcelas não foram criados. Com a eliminação da redundância de dados a parcela deixa de existir e passa a existir apenas o lançamento financeiro, que precisa ser criado automaticamente para que essas vendas antigas fiquem corretas. Como são valores que não podem ser alterados, baixados, etc. eles nascem com o tipo de bloqueio 11.

# 4.2 Bloqueios ou travas para Data Base

Afim de garantir a integridade dos registros gravados o sistema passa a bloquear comportamentos que podem gerar conflitos nos valores base

Para habilitar a trava cronológica no financeiro, deve ser habilitado o parâmetro "Bloquear alterações de dados financeiros e baixas, quanto estiver usando Data Base e o mês competência da alteração for diferente do mês da competência do reajuste."

* Todo reajuste deve registrar no histórico financeiro a “data de reajuste” e não a data de execução;

*Este log só ocorre se o Financeiro estiver parametrizado para usar o histórico.*

* Uma parcela com baixas parciais, permitirá criar uma nova “baixa” ou “cancelamento de baixa”, se já houver uma baixa parcial com data futura.

*Este log só ocorre se o Financeiro estiver parametrizado para usar o histórico.*

*Se necessário o usuário deverá cancelar a baixa futura para fazer os processos retroativos.*

* Uma parcela com baixa parcial futura não terá reajuste retroativo.

*Esta será uma trava parametrizada no TIN, mas o relatório de ficha financeira por data base só poderá ser exibido se esta trava estiver marcada.*

*A Parcela com baixa parcial só poderá sofrer reajuste com data maior que a data de sua última baixa.*

*É possível que este comportamento de voltar a parcela com reajuste para o passado, com uma baixa parcial futura, tenha gerado valores de integração negativos.*

**Alterações de Lançamentos com reajuste Anual ou outras periodicidades**

O bloqueio se aplica a:

* Edição de Lançamentos financeiros onde o reajuste (CM ou Juros) tenha periodicidade maior que 1 mes;
* Baixa ou Geração de Boleto de lançamentos financeiros, onde o reajuste (CM ou Juros) tenha periodicidade maior que 1 mês, e o parâmetro de Reajuste On line do Financeiro esteja desabilitado.

Exemplo:

Um lançamento está sendo alterado em 03/08/2016 e ele possui dois componentes um de juros de contrato e outro de correção monetária cuja periodicidade é de 12 meses, com as seguintes datas de último reajuste e próximo reajuste.

# 4.3 Congelar Reajuste de Parcela / Descongelar Reajuste de Parcela

Para facilitar o uso do sistema e permitir que haja negociação com seu cliente, foram criados dois processos para congelar e descongelar o reajuste da parcela. (Processos-> Congelar Reajuste da Parcela ou Descongelar Reajuste da Parcela)

Ao executar o congelamento da parcela o sistema passa a ignorar o processo de reajuste apenas para esta parcela. (no banco de dados o campo XVENDAPARCELA.IGNORARREAJUSTE = 1)

Exemplo de Aplicação:

O cliente liga para a Incorporadora e faz uma negociação direta com o financeiro, sem envolver a equipe de contratos (TIN).

Nessa negociação o cliente já está em atraso com a parcela e eles chegam a um acordo que vão congelar o reajuste até o mês de fevereiro, sendo que eles estão no mês de junho. Então, o usuário executa o processo de congelar a parcela no mês de fevereiro.

Dessa forma, a baixa poderá ser executada em qualquer competência sem que a trava do financeiro bloqueia a baixa.

E ainda o usuário deixará de se preocupar com essa parcela caso alguém da equipe do imobiliário execute o reajuste para a outra competência sem avisar a equipe do financeiro.
