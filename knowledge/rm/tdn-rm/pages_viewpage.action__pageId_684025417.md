---
content_hash: d091b2a582e76a5c41d0b5cc4eeb9d4e9ecb32fc60d0e95439f9283126a1ce3b
fetched_at: '2026-06-29T00:11:18.214529+00:00'
page_id: '684025417'
product: rm
source: tdn-rm
title: Gerenciador de Movimento - Lançamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=684025417
version: 9
---

Através do Lançaemtno do Gerenciador de Movimento para a Folha de Pagamentro, os eventos são consolidadros e gravados na Ficha Financeira (PFFINANC) e/ou na Ficha Financeira por Centro de Custo (PFMOVCC)

**Considerações**

Será durante o cálculo que o sistema irá atualizar os dados do ‘Empréstimo’ no cadastro de funcionário e realizar o cálculo do valor a ser descontado.

Para isso, o sistema deverá identificar quais são os eventos de empréstimo gravados na Movimentação de Eventos do Funcionário.  A identificação será através do campo do código de empréstimo da tabela PFENTMOV.

Em seguida consultar as informações do ‘Empréstimo’ no cadastro de funcionário, e calcular o valor para cada linha de empréstimo encontrada na Movimentação de Eventos (seja parcela fixa ou através de utilização de fórmula).

Em seguida consolidar o valor total a ser descontado e gravar na PFFINANC ou PFMOVCC e na PFEMPRT.

false

Quando o empréstimo é lançado para a Movimentação de Eventos do Funcionário é inserida uma linha para cada empréstimo processado.

Neste momento os dados do ‘Empréstimo’ no cadastro de Funcionário não são atualizados e a fórmula de cálculo não é executada, independente se utiliza fórmula ou parcelas fixas, ou seja, não grava no valor na Movimentação de Eventos do Funcionário.

*Exemplo***:**

No cadastro do funcionário existem os seguintes empréstimos cadastrados:

| **Evento** | **Código Empréstimo** | **Valor** | **Parcela** |
| --- | --- | --- | --- |
| 9999 | XXXX | R$500,00 | 10 |
| 9999 | ZZZZ | R$600,00 | 10 |

Ao processar o lançamento de grupo de eventos selecionando a opção para lançar ‘Empréstimo’ o sistema NÃO irá atualizar a tabela PFEMPRT e irá gravar duas linhas na tabela PFENTMOV, sendo:

| **Código Empréstimo** | **Valor** | **Evento** |
| --- | --- | --- |
| XXXX | R$0,00 | 9999 |
| ZZZZ | R$0,00 | 9999 |

Ao processar a importação do movimento o sistema irá gravar mais uma linha, sendo:

| **Código Empréstimo** | **Valor** | **Evento** |
| --- | --- | --- |
|  | R$100,00 | 9999 |

Ao processar o lançamento do ‘Gerenciador de Movimento’ o sistema irá gravar o histórico de empréstimo dos códigos XXXX e ZZZZ, subtraindo o saldo devedor e o nº de parcelas e irá gravar na tabela PFFINANC o valor de R$210,00 (referente aos valores dos 3 empréstimos).

false

Caso exista uma linha com o código do evento de empréstimo, porém não exista cadastro de ‘Empréstimo’ no funcionário, o sistema irá somar aos demais valores.

A movimentação do cadastro da pensionista é atualizada todo momento que o cálculo é acionado.

Sempre que no Envelope de Pagamento estiver com o evento alterado (Campo ALTERADOMANUAL =1 da Tabela PFFINANC), o processo retornarar um aviso no log e não substituirá (ou recalcularar) o evento considerando o valor/referencia lançados na Movimentação de Eventos do Funcionário.

Terá situação em que existirá evento da folha de pagamento no envelope do funcionário, porém o evento não estará na Movimentação de Eventos do Funcionário. como os eventos de encargos (INSS, IRRF, Restituições) os eventos de base de calculo múltiplos vínculos, médias de salário maternidade, etc;

Os eventos lançados automaticamente pelo sistema estarão apenas no Envelope de Pagamento (PFFINANC) com o campo Origem do Movimento (ORIGEMMOV) =0.

No momento do lançamento, caso exista o mesmo evento com data de pagamento diferente mas com o mesmo caixa, o sistema assumirar a maior data. Caso o caixa seja diferente, o sistema enviarar uma mensagem de erro para o log e não lançarar nenhum evento para o funcionário.

Quando o campo Origem Movimento da Movimentação do Funcionário for igual 9 (Lançamento de Férias) o sistema informarar o campo PFFINANC.VERBAFERIAS para 1 (um).

Quando o período estiver bloqueado, o sistema não poderá permitir nenhuma alteração ou inclusão.

Quando existir eventos lançados após a rescisão através do Grupo de Eventos, os mesmo serão lançados para o envelope através do processo 'Lançamento' do Gerenciador de Movimento, marcando a opção 'Lança Movimento Demitido mês'.

**Envelope de Pagamento**

Os eventos exisitentes na Movimentação de Eventos do funcionário serão lançados no Envelope de pagamento com a origem de movimento = 11 (Gerenciador de Movimento)

Não será permitida nenhuma ação ‘Incluir, Editar e Excluir’ no envelope de pagamento, sendo disponibilizado o recurso para 'Forçar Valor' do evento no envelope de pagamento.

Quando o mesmo for alterado, o sistema registrarar as alterações na aba Log dos Valores Alterador do envelope (tabela PFVALORALTERADO), com o valor anterior a alteração:

O registro do evento apresentarar em negrito no envelope com a flag 'Valor forçado' marcado. Caso queira retornar ao valor orginal, basta remover o valor forçado através do recurso 'Remover Valor Forçado':

**Ficha Financeira**

Somente em meses anteriores a competência atual será permitido fazer qualquer ação na ficha financeira. Para o mês igual ou posterior a competência atual não será permitido nenhuma ação.

false

Qualquer ação realizada na Ficha Financeira o sistema registrar na tabela PFVALORALTERADO.

**Cancelamento do Movimento**

No cancelamento de Movimento, será disponibilizado a opção 'Cancelar eventos de origem do Gerenciador de Movimento', que quando marcado irá cancelar os eventos de origem movimento = 11 lançadas no envelope de pagamento.

false

Sempre que processar o cancelamento de movimento deverá gravar os dados na tabela PFVALORALTERADO, independente da ORIGEMMOV.
