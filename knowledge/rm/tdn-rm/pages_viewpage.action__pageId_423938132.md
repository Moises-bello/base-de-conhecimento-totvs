---
content_hash: b18aea5603e19bbf76340af356d018e7b4e8241466a7e0e933a44fa372a82fa7
fetched_at: '2026-06-29T00:09:25.367401+00:00'
page_id: '423938132'
product: rm
source: tdn-rm
title: 04.04 - Gestão de Estoque - Gestão de Estoque, Compras e Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938132
version: 27
---

Gestão de Estoque

**Usar Módulo de Ressuprimento:**Marcando esta opção será habilitado o Módulo de Ressuprimento.

**Nível Gestão:**Informe nesta opção se o Controle de Estoque do Produto por Ressuprimento será feito por Coligada, Filial ou Local de Estoque.

Saldos de Estoque 1/2

Nesta pasta é parametrizada a forma de controle dos saldos. É possível o controle de até 10 saldos, sendo que 4 são fixos. São eles:

* Saldo de Balanço, Saldo Atual, Pedidos a Fornecedores e Pedidos a Clientes.
* Os demais são livres. Para cada um informe o nome desejado.
* Depois de informar o nome, informe se no momento em que estiver fazendo a movimentação de um produto, o sistema confira o saldo do mesmo, os controles são para quando os saldos estiverem: Menor que Zero,

Menor que Ponto de Pedido, Menor que Estoque Mínimo, Maior que Estoque Máximo. As opções são:

* Não Confere: O sistema não fará nenhum controle do saldo.
* Avisa: Para conferir e avisar qual o saldo atual.
* Barra: Para conferir e barrar a movimentação caso esteja no limite do saldo em questão.
Saldos de Estoque 2/2

Nesta pasta é parametrizada a forma de controle dos saldos. É possível o controle de até 10 saldos, sendo que 4 são fixos. São eles:

* Saldo de Balanço, Saldo Atual, Pedidos a Fornecedores e Pedidos a Clientes.
* Os demais são livres. Para cada um informe o nome desejado.
* Depois de informar o nome, informe se no momento em que estiver fazendo a movimentação de um produto, o sistema confira o saldo do mesmo, os controles são para quando os saldos estiverem: Menor que Zero,

Menor que Ponto de Pedido, Menor que Estoque Mínimo, Maior que Estoque Máximo. As opções são:

* Não Confere: O sistema não fará nenhum controle do saldo.
* Avisa: Para conferir e avisar qual o saldo atual.
* Barra: Para conferir e barrar a movimentação caso esteja no limite do saldo em questão.
Data de Fechamento

**Geral:**Informe neste campo Geral a data de fechamento do estoque. O sistema irá considerar que até esta data o controle de estoque de todos os produtos está fechado e não sofrerá mais alterações.

**Fechamento do Estoque por Saldo:**Se esta opção está marcada poderá informar uma data de fechamento de estoque por saldo. Ao regerar saldos e custos será necessário informar qual saldo está sendo regerado. Além disso, os custos financeiros somente serão atualizados quando o saldo 2 for regerado. Outra mudança é que ao realizar consistência da data de movimento serão consistidas todas as datas de fechamento dos saldos que afetam o movimento (consistência que não permite que um movimento com data anterior à data de fechamento de estoque seja inserido ou atualizado).

1
incomplete
Exemplo*:*

* Se o movimento 1.2.01 afeta os saldos 2 e 4, a data do movimento não poderá ser menor que a data de fechamento de estoque dos saldos 2 e 4.
* Se a data de fechamento de estoque do saldo 2 é 31/12/2003, somente será considerados movimentos após esta data.

IMPORTANTE

O preenchimento desta data é **obrigatório**, pois, não é possível regerar Saldos e Custos se a data de fechamento não estiver preenchida.

O sistema não permitirá a inclusão, alteração ou exclusão de movimentos que afetam o estoque (todos os saldos), com data de movimentação anterior à data de fechamento. Caso haja esta necessidade, esta data deverá ser alterada.

Durante os processos de regerar Saldos e Custos e regerar Ficha Física-Financeira, só serão recalculados os movimentos com data de movimentação posterior à data de fechamento do estoque. Logo, quanto mais recente for esta data, mais rápidos serão estes processos.

Custos

**Editar Custos no Cadastro:**Marque para editar no Cadastro do Produto os Custos Unitário, Médio e de Reposição A e B.

**Calcular Custo Unitário On-line:**Para que este custo tenha cálculo on-line quando Regerar Saldos e Custos.

**Calcular Custo Médio On-line:**Para que este custo tenha cálculo on-line quando Regerar Saldos e Custos.

**Calcular Custo de Reposição A On-line:**Para que este custo tenha cálculo on-line quando Regerar Saldos e Custos.

**Calcular Custo de Reposição B On-line:**Para que este custo tenha cálculo on-line quando Regerar Saldos e Custos.

**Nome dos Custos de Reposição A e B:**Defina um nome para os Custos.

**Consistir Saldo de Serviços:**Marque esta opção se desejar que seja feito o controle do estoque dos serviços.  
***Observação**:*O sistema verificará a parametrização para Controle de Estoque conforme abaixo:

* Se o Módulo de Estoque estiver ativo.
* Se o movimento for diferente de 3.2 (Transferência de Faturamento).
* Se o Parâmetro Geral Consistir Saldo de Serviços estiver marcado.
* Se o Parâmetro Tipo de Produto no Tipo de movimento estiver diferente de Serviços.

2
incomplete
Exemplo*:*Se determinado movimento precisar consistir Saldo de Serviços, o mesmo deverá estar configurado para (ambos ou serviço) como Tipo de item e o parâmetro Geral/Consistir Saldo de Serviços deverá estar marcado. Esta configuração é necessária, pois o Módulo de Estoque necessita de um Local de Estoque para realização dos cálculos necessários.

**Manter Custo Médio ao Zerar Saldo Físico:**Marcando esta opção sempre que o saldo físico do produto ficar igual a zero, o sistema manterá o custo médio anterior. Desmarcando, o sistema irá zerar o custo médio do produto sempre que o saldo físico for igual a zero.

**Zerar Saldo Financeiro se o Saldo Físico for Zero:**Marcando esta opção sempre que o saldo físico for zerado o financeiro também será zerado.

**Utilizar Método de Cálculo do Custo Definido no Produto:**Marcando esta opção será possível definir no cadastro de produtos campo "Cálculo do Custo" qual método será utilizado para calcular o custo do produto.

**Calcular Custo Médio Mensal:**Marcando este parâmetro a ordenação dos movimentos será a seguinte: dentro de um mesmo mês e ano virão primeiro todas as entradas (ordenadas pelo dia, no caso a data do movimento) e depois todas as saídas (ordenadas pelo dia, no caso a data do movimento).  
***Observação**:*Com essa opção marcada na emissão da Ficha Física Financeira obrigatoriamente o período inicial deverá ser o primeiro dia do mês.

**Ordem dos Movimentos ao Regerar Ficha Física-Financeira:**Indica a ordem em que um movimento afetará o estoque, disponibilizado:

* Efeito sobre o saldo: Corresponde à opção anterior ("Regerar Ficha Física-Financeira pela ordem de inclusão dos movimentos") não habilitada. Ao gerar a ficha física-financeira o sistema irá ordenar os movimentos, dentro da mesma data de emissão, pela seguinte ordem, primeiro as entradas depois as saídas.

**Ordem em que movimento afetou estoque:**Ao gerar a Ficha Física-Financeira o sistema irá ordenar os movimentos, dentro da mesma data do movimento, pela ordem em que estes afetaram o estoque (o sistema tem um controle interno sequencial de gravação dos movimentos que afetam estoque). Se o movimento foi alterado após ter sido incluído, a sua ordem de "afetar" o estoque continuará a mesma.

**Custo por Filial:**Este não poderá ser alterado pelo usuário e será exibido marcado quando a base for convertida para Custo por Filial.

**Manter Custo por Local Gerencial:**Este será exibido marcado quando a base for convertida para custo por filial, porém pode ser alterado pelo usuário. Quando estiver marcado, o sistema fará as movimentações baseadas em custo por filial, mas manterá o custo por local em caráter gerencial, podendo ser verificado na consulta de saldos e custos.

Reserva

**Usar Reserva de Saldo Físico:**Marque está opção, para trabalhar com reserva de saldos dos produtos.

**Tipo de Movimento de Solicitação de Compras para Reserva:**Informe o tipo de movimento que será gerado pelo RM Factor para a reserva de produtos caso não haja saldo disponível suficiente em estoque.  
***Observações**:* O recurso de reserva de saldos é utilizado na integração com o RM Factor através do Planejamento Mestre de Produção e Ordem de Produção. A reserva solicitada internamente pelo RM Factor é efetuada da seguinte forma:

* O saldo disponível em estoque é reservado e caso não seja suficiente é feita a reserva da quantidade restante vinculada às solicitações (parametrizada no RM Factor) que ainda não foram baixadas, e finalmente caso não seja suficiente é gerado um movimento (solicitação ou pedido, de acordo com a parametrização) com a quantidade restante.
* O saldo de estoque reservado e disponível pode ser visualizado pela consulta de saldos e custos do produto.
* Não será possível desmarcar o parâmetro Usar Reserva de Saldo Físico no TOTVS Gestão de Estoque, Compras e Faturamento quando no RM Factor estiver habilitado qualquer parâmetro da pasta Reserva em Opções/Parâmetros/Produção. Na validação será apresentada a mensagem de consistência: "Parâmetro Usa Reserva de Saldo Físico não pode ser desmarcado, pois o RM Factor está utilizando o conceito de reserva".
Definições de Inventário 1/3

**Utilizar código sequencial:**Este parâmetro indica se o código do inventário será gerado de forma automática com um código sequencial ou se o código do inventário será informado pelo usuário ao se inserir registro de inventário.

Marcando essa opção o sistema gerará o código do inventário sem necessidade do usuário informá-lo. Ao marcá-lo é atribuído ao campo **Máscara do código do inventário** a máscara definida para o código sequencial (####.##.##### que significa Ano.Mês.Código sequencial) e o campo da máscara fica desabilitado para edição.

Desmarcando tal parâmetro então é necessário que o usuário informe o código do inventário e que este esteja válido de acordo com a máscara informada no parâmetro **Máscara do código do inventário** (logo abaixo). Ao desmarcá-lo o campo de máscara é habilitado para edição.

**Máscara do Código de Inventário:**Neste campo informe a máscara do código do Inventário.

**Tipo do Inventário Default:**Selecione qual será o tipo de inventário padrão ao incluir um novo Inventário:

* Produto: somente produtos.
* Grade Numerada: produtos com controle de grade numerada(antiga).
* Lote: produtos com controle de lote.

Número de Série: produtos controlados por número de série.

**Tipos de Movimento de Acerto de Entrada:**Deverá indicar um tipo de movimento que depois de encerrado o inventário, serão geradas movimentações de acerto de estoque dos produtos. Neste caso, o Tipo de Movimento de Ajuste de Inventário tem que ser que aumente o estoque.

**Tipo de Movimento de Acerto de Saída:**Deverá indicar um tipo de movimento que depois de encerrado o inventário, serão geradas movimentações de acerto de estoque dos produtos. Neste caso, o Tipo de Movimento de Ajuste de Inventário tem que ser que diminua o estoque.

Definições de Inventário 2/3

**Tipos de Movimento de Acerto de Entrada:**Deverá indicar um tipo de movimento que depois de encerrado o inventário, serão geradas movimentações de acerto de estoque dos produtos. Neste caso, o Tipo de Movimento de Ajuste de Inventário tem que ser que aumente o estoque.

**Tipo de Movimento de Acerto de Saída:**Deverá indicar um tipo de movimento que depois de encerrado o inventário, serão geradas movimentações de acerto de estoque dos produtos. Neste caso, o Tipo de Movimento de Ajuste de Inventário tem que ser que diminua o estoque.

Definições de Inventário 3/3

**Tipos de Movimento de Acerto de Entrada:**Deverá indicar um tipo de movimento que depois de encerrado o inventário, serão geradas movimentações de acerto de estoque dos produtos. Neste caso, o Tipo de Movimento de Ajuste de Inventário tem que ser que aumente o estoque.

**Tipo de Movimento de Acerto de Saída:**Deverá indicar um tipo de movimento que depois de encerrado o inventário, serão geradas movimentações de acerto de estoque dos produtos. Neste caso, o Tipo de Movimento de Ajuste de Inventário tem que ser que diminua o estoque.
