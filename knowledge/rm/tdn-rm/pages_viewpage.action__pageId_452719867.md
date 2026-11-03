---
content_hash: 480060157120462d2f0f6dd45e14022083f03ee8e2e889e7732b71eb00715c1f
fetched_at: '2026-06-29T00:10:10.534425+00:00'
page_id: '452719867'
product: rm
source: tdn-rm
title: Incluir em Processo de Movimentação de Pessoal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719867
version: 3
---

**Incluir em Processo de Movimentação de Pessoal**

O processo tem por objetivo realizar as alterações dos dados funcionais do funcionário pela vinculação da requisição de aumento de quadro ou de substituição em um funcionário.

No processo de vinculação serão verificados os parâmetros relacionados às configurações do controle de lotação e da obrigatoriedade do CPF. Caso a requisição de substituição tenha sido gerada a partir do desligamento de um funcionário PCD, será verificado também se o funcionário ao qual está sendo vinculada a requisição é PCD também.

Ao selecionar o funcionário e acessar o processo "Incluir em processo de movimentação de pessoal", será exibida a tela para que seja feita a vinculação da requisição de aumento de quadro ou de substituição.

Neste processo de vinculação da requisição o sistema compara a seção, função e salário atuais do funcionário selecionado, com os dados da requisição vinculada. Se os dados atuais de um funcionário forem iguais aos dados da requisição o usuário será notificado por mensagem sobre a impossibilidade de prosseguir com o processo, pois neste caso não houve nenhuma alteração de dados funcionais. Porém, se os dados diferem dos dados da requisição vinculada, o sistema procederá de acordo com uma das seguintes formas:

* Alteração somente da seção: Como a lotação de destino proposta difere daquela em que o funcionário está lotado atualmente, esta operação dará origem a uma requisição filha de transferência com status "Pendente" baseada nos dados da requisição "Pai" de origem. Tanto o requisitante quanto o chefe da seção de origem serão notificados por e-mail sobre o processo de vinculação da requisição e da geração da requisição filha de transferência.

* Alteração somente da função ou salário: Como a proposta da função ou salário difere dos dados atuais do funcionário, esta operação dará origem a uma requisição de alteração de dados funcionais com status "Pendente" baseada nos dados da requisição "Pai" de origem. Tanto o requisitante quanto o chefe da seção de origem serão notificados por e-mail sobre o processo de vinculação da requisição e da geração da requisição filha de alteração de dados funcionais.

* Alteração da seção, função ou salário: Como a lotação de destino e a proposta salarial diferem dos dados atuais do funcionário, esta operação dará origem a uma requisição de transferência com alteração de dados funcionais com status "Pendente" baseada nos dados da requisição "Pai" de origem. Tanto o requisitante quanto o chefe da seção de origem serão notificados por e-mail sobre o processo de vinculação da requisição e da geração da requisição filha de transferência com alteração de dados funcionais.

**Observações**

* Este processo somente ficará habilitado quando um dos parâmetros "Requisição obrigatória para alterar cargo e/ou salário", "Requisição obrigatória para transferir funcionário" ou "Requisição obrigatória para transferir e alterar dados funcionais" estiverem marcados.
* Após a seleção da requisição os demais campos serão preenchidos automaticamente com os dados desta, caso o parâmetro "Permitir alterar dados da requisição vinculada" esteja marcado os dados da requisição poderão ser alterados. Se o usuário confirmar a alteração dos dados o sistema obrigatoriamente irá gerar uma requisição de alteração de dados no qual constará o registro do usuário logado, a justificativa fornecida e as alterações realizadas. Além disso, será enviado e-mail para o requisitante, o Gestor do RH e todos os participantes do fluxo comunicando a situação da requisição.
* Não será possível vincular mais de uma requisição em um mesmo funcionário. Caso seja necessário vincular uma nova requisição deve-se desvincular o funcionário da requisição atual e realizar o novo procedimento de vinculação. Para verificar o processo de desvinculação acesse: Gerência de RH | Requisições | Aumento de quadro | Pessoas Selecionadas | Remover Pessoas da Seleção ou Gerência de RH | Requisições | Substituição | Pessoas Selecionadas | Remover Pessoas da Seleção.
* Para a vinculação da requisição de substituição apenas um funcionário poderá ser selecionado, pois este tipo de requisição gera apenas uma vaga disponível.
* Não será permitida a vinculação de uma requisição para alteração de dados funcionais em funcionários que já possuem requisições, deste tipo, vinculada.
* Caso seja gerada uma nova requisição advinda da requisição de substituição, o requisitante desta deverá ser o chefe responsável pelo funcionário na requisição de origem (requisição de substituição).
* Ao final do processo será enviado um e-mail para o Gestor do Depto. de Pessoal comunicando a efetivação do procedimento.
