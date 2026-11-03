---
content_hash: fe0a1a4c464b2a40ae08d1e43f2bea375b1b79bd2f18e371988c1eb52945dea6
fetched_at: '2026-06-29T00:08:47.051934+00:00'
page_id: '318603312'
product: rm
source: tdn-rm
title: 07.1 Plano de Pagamento
type: documentation
url: https://tdn.totvs.com/display/LRM/07.1+Plano+de+Pagamento
version: 28
---

**Este Menu está disponível apenas para o contexto ENSINO BÁSICO.**

Este step tem como objetivo de exibir os planos de pagamentos para que o aluno/responsável possa visualizar ou alterar o plano de pagamento para aquela matrícula.

Essa tela será exibida na rematrícula, caso o parâmetro "Visualizar/Alterar plano de pagamento" seja habilitado.

 **Educacional| Configurações| Parâmetros| RM Portal| Matrícula| Contrato financeiro 1/4**

**Exibição dos planos de pagamento para os alunos/responsáveis dependendo da parametrização:**

Plano de pagamento default vinculado na "Parametrização por curso"

Ao vincular um plano de pagamento default na parametrização por curso, esse plano será exibido já marcado para o aluno/responsável, será possível alterar para outro plano de pagamento disponível:

Plano de pagamento já vinculado no "Contrato" do aluno

Ao vincular um plano de pagamento no contrato da matrícula deste aluno, o plano será exibido já marcado para o aluno/responsável, será possível alterar para outro plano de pagamento disponível:

Vale lembrar que se este contrato estiver **cancelado**, o plano de pagamento que virá marcado, será o plano de pagamento default da parametrização por curso.

Se o aluno possuir dois contrato ativos, o plano de pagamento que virá selecionado também será o que estiver configurado na parametrização por curso. Por outro lado, se possuir um **ativo** e outro **cancelado**, virá marcado o do contrato ativo.

Mesmo se o plano de pagamento vinculado ao contrato estiver **vencido** ele será exibido podendo ser alterado, exceto no caso do contrato já possuir algum lançamento gerado referente ao plano de pagamento, nesse caso, ele será exibido porém ficará desabilitado para alteração.

Se o parâmetro para **"Visualizar/Alterar plano de pagamento" estiver desmarcado** e o contrato financeiro da matrícula do aluno **não tem um plano associado**, o sistema aplicará o **plano de pagamento default** configurado no curso. No entanto, se o contrato **já possuir um plano** vinculado, ele **não será alterado** para o default.

Aluno com parcelas do plano de pagamento já geradas na matrícula

Ao gerar os lançamentos das parcelas do plano de pagamento vinculado ao aluno na matrícula, somente será exibido na matrícula o plano de pagamento das parcelas geradas sem a possibilidade de alteração desse plano:

Se o responsável financeiro do aluno estiver com status de inativo, o sistema irá emitir uma mensagem de erro nesse step como na imagem abaixo, e não irá permitir ao aluno prosseguir com a rematrícula online até que o responsável financeiro seja ativado ou o aluno seja associado à um responsável financeiro ativo.

No Cadastro do responsável financeiro do aluno o cadastro do cliente/fornecedor deve estar ativo.

Plano de pagamento e bolsa associado ao prospect

Para informações referentes à prospecções, clique [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=702373785).

[Sistema Indústria](https://tdn.totvs.com/pages/releaseview.action?pageId=527384229)
