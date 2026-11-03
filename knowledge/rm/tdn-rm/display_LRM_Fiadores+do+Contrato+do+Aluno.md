---
content_hash: 0d8579db28d67669ed8c510b66b19758d7f4e3d96a49ef574624247ec09b756d
fetched_at: '2026-06-29T00:11:18.157809+00:00'
page_id: '684009924'
product: rm
source: tdn-rm
title: Fiadores do Contrato do Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/Fiadores+do+Contrato+do+Aluno
version: 7
---

Disponível apenas para o nível de ensino **superior,** a partir do patch ****12.1.33,**** essa página irá conter os fiadores associados ao contrato que estão relacionados ao contexto selecionado pelo aluno após o login.

Somente será exibida essa funcionalidade se o contrato que está relacionado ao contexto logado do aluno tiver algum **fiador ativo associado**.

As regras básicas, relacionadas a inclusão, edição e exclusão dos fiadores, serão as mesmas que foram implementadas na tela de .

Além das funcionalidades básicas especificadas acima, nessa tela é possível executar o **processo de troca do fiador**.

Vale ressaltar que somente é possível fazer a troca em fiadores previamente **aprovados**, conforme demonstrado acima no fiador IZABELA ROCHA ANDRADE.

Fiadores em processo de troca pendente, como mostra o fiador REVISTA INFO EXAME não ficam disponíveis para serem trocados, assim que a troca for efetiva ou cancelada, a opção de troca de fiador será novamente habilitada.

A troca de fiador será sempre de um fiador para outro, sempre de um para um.

Para fazer a troca de um fiador é necessário clicar no ícone  que um pop-up será exibido para que o aluno informe os dados do fiador. Basta preencher os campos obrigatórios e salvar.

Nota-se, que a modal é similar a modal de cadastro de fiador, porém, o campo "**Motivo da alteração do Fiador**" ficará disponível, sendo obrigatório seu preenchimento.

Ao digitar o **CPF** o portal irá procurar se existe algum cliente/fornecedor com o CPF informado, se sim, uma mensagem de confirmação para o aluno será exibida, informando que já existe um cadastrado e se deseja fazer a associação, se fizer a associação o mesmo será vinculado como fiador do aluno, se clicar em não, o fiador não será criado.

Se o aluno acionar Sim na tela anterior, uma modal para informar o **motivo da alteração do fiador** será exibida.

Caso o **CPF**informado não for de nenhum cliente/fornecedor, será exibido um alerta para o aluno dizendo que não foi encontrado fiador, com isso será necessário preencher os dados e salvar. Como este **CPF** não estava vinculado a nenhum cliente/fornecedor ao salvar os dados, será criado um novo cliente/fornecedor que será vinculado como fiador deste aluno e será associado ao contrato do contexto logado.

Após a conclusão da solicitação de troca do fiador, o fiador a ser substituído ficará disponível na aba **Novo fiador**, e seus documentos na aba **Documentos do novo fiador**. Vale ressaltar que, até que a troca seja confirmada no RM, o novo fiador ficará com a situação **Em avaliação**, o antigo permanece **Aprovado**, até que a troca seja efetivada.

O usuário responsável pelos fiadores com acesso ao RM, deve aprovar ou reprovar a solicitação de troca de fiadores.

Para provar é preciso acessar o RM => Educacional => Aba "Financeiro/Contábil" =>  Contratos => Fiador

Busque pelo fiador que será trocado, como no exemplo abaixo, o novo fiador deve estar desativado, não deve ser possível alterar a matriz aplicada e o status em avalição.

Ao mudar o status para aprovado, a troca de fiador é concluída, caso seja reprovado a troca é cancelada.

Após a aprovação da troca do fiador, o fiador responsável pelo contrato é alterado, o fiador antigo muda o status para **substituído**, conforme a tela abaixo.
