---
content_hash: 8bbe085b493da91d8a4b580e319377c8f4c420d9c2ea90557c3b7a146c6503a3
fetched_at: '2026-06-29T00:11:06.851625+00:00'
page_id: '635757624'
product: rm
source: tdn-rm
title: 03 - Informar Fiador no Portal do Aluno
type: documentation
url: https://tdn.totvs.com/display/LRM/03+-+Informar+Fiador+no+Portal+do+Aluno
version: 38
---

Disponível apenas no contexto de **Ensino Superior**

**Acesse:** Novo Portal do Aluno | Matrícula Online | Etapa Fiador.

Foi disponibilizado na matrícula online do novo portal do aluno um novo passo chamado Fiador, este passo permite que aluno informe um ou mais fiadores. Vale lembrar que o passo somente será visível se o sistema atender aos critérios:

* se a parametrização por curso do aluno estiver marcado o parâmetro que **exige fiador;**
* se o [controle de validade do fiador](https://tdn.totvs.com.br/display/LRM/Fiadores#Fiadores-08.ControledeValidadedoFiador) configurado determinar que a etapa de fiadores deverá ser exibida, conforme as regras abaixo:
  + **Válido para todo o curso**: o passo do fiador na rematrícula será exibido somente quando o aluno não tiver fiador ativo previamente cadastrado;
  + **Válido por período letivo**: o passo do fiador sempre será exibido na rematrícula online;
  + **Verificar inadimplência do aluno**: se o aluno tiver alguma inadimplência ou não tiver nenhum fiador ativo previamente cadastrado, o passo de fiador será exibido, senão, o passo do fiador não é exibido.

A **quantidade máxima de fiadores** e o **controle de visibilidade dos fiadores** poderão ser parametrizados em Configurações | Parâmetros | Tesouraria.ATENÇÃO

Se o parâmetro de sistema **não exigir fiador em caso de alunos com 100% de bolsa / desconto** estiver marcado e o aluno tiver 100% de bolsa incondicional e/ou desconto incondicional, não exigido o fiador.  Esse novo parâmetro se encontra no menu Configurações → Parâmetros → RM Portal → RM Portal  → Matrícula → Portal - Matrícula / Geral 1/6.

Informar Fiador

Ao clicar em **adicionar** um pop-up será exibido para que o aluno informe os dados do fiador. Basta preencher os campos obrigatórios e salvar.

Entretanto, ao digitar o **CPF** o portal irá procurar se existe algum cliente/fornecedor com o CPF informado, se sim, uma mensagem de confirmação para o aluno será exibida, informando que já existe um cadastrado e se deseja fazer a associação, se fizer a associação o mesmo será vinculado como fiador do aluno, se clicar em não, o fiador não será criado.

Caso o **CPF**informado não for de nenhum cliente/fornecedor será exibido um alerta para o aluno dizendo que não foi encontrado fiador, com isso será necessário preencher os dados e salvar. Como este **CPF** não estava vinculado a nenhum cliente/fornecedor ao salvar os dados, será criado um novo cliente/fornecedor que será vinculado como fiador deste aluno.

Como foi o aluno quem criou este registro pelo portal, o mesmo poderá ver os dados e até atualizar se for necessário.

Para atualização do dados basta clicar no ícone  que será aberta o mesmo pop-up para inserir um novo, porém será carregado os dados do fiador. Vale ressaltar que o aluno não poderá alterar os seguintes dados do fiador: **CPF, Nome, Data nascimento e R.G**.

Caso o aluno deseje remover a associação com algum fiador específico, basta clicar no ícone , que será aberta uma pop-up de confirmação da exclusão do fiador. Vale ressaltar que o aluno não excluí o registro do fiador da base de dados, no caso, o sistema apenas **inativa o fiador do aluno**.

Caso não foi o aluno quem criou o cliente/fornecedor que foi associado ao fiador, não será possível ver e editar os dados deste fiador até que o fiador seja aprovado pela instituição. Apenas o CPF será possível visualizar.

Se exceder o máximo de fiadores cadastrados e **ativos** o portal irá exibir uma mensagem de erro ao aluno informando que o número máximo de fiadores já foi atingido.

Caso o aluno não tenha nenhum fiador e não cadastre nenhum, a matrícula não poderá ser avançada, pois a quantidade mínima exigida de fiadores sempre será de um.

Fiadores **inativos** nunca serão exibidos no portal para o aluno.

Documentos do fiador

Quando a **parametrização por curso** estiver configurada para exigir fiador e no anexo de [Documentos Exigidos do Fiador](https://tdn.totvs.com/display/LRM/Documentos+Exigidos+do+Fiador) algum documento estiver cadastrado, o sistema vai apresentar no Portal do Aluno, logo abaixo dos fiadores, uma tabela para possibilitar ao aluno a entrega dos documentos do fiador.

Para mais informações sobre os documentos do fiador [acesse aqui](https://tdn.totvs.com/display/LRM/Documentos+do+Fiador).

Se houver algum documento obrigatório de algum fiador do aluno que não foi informado, a matrícula não poderá ser avançada. Somente poderá avançar quando todos os documentos obrigatórios de todos os fiadores do aluno forem informados.

Se algum dos documentos cadastrados forem rejeitados, deverão ser novamente informados para que o aluno avance a matrícula.

Caso não foi o aluno quem criou o cliente/fornecedor que foi associado ao fiador, não será possível visualizar os documentos previamente cadastrados deste fiador, até que o fiador seja aprovado pela instituição. Nesse caso, o aluno conseguirá visualizar apenas os documentos que ele anexou.

Disponibilizar pagamento após confirmação do fiador

Foi criado o parâmetro **“Permite pagamento somente para os alunos que já tiverem o fiador ativo e aprovado”**

Poderá ser parametrizada em Configurações | Parâmetros | Tesouraria.

Quando estiver marcado e não existir Fiador para o aluno ou o Fiador não está aprovado, não será exibido as formas de pagamento no portal (boleto, pix e cartão de crédito)

Matricula no portal na finalização não será apresentado as formas de pagamento

Extrato não será habilitada as formas de pagamento
