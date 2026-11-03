---
content_hash: 91611e89862497514cb5ed36d12b4556c9cf95d9e49b49434045841563dde808
fetched_at: '2026-06-29T00:11:04.628115+00:00'
page_id: '627995830'
product: rm
source: tdn-rm
title: Rascunho_EDU0011 - Cadastro de bolsista
type: documentation
url: https://tdn.totvs.com/display/LRM/Rascunho_EDU0011+-+Cadastro+de+bolsista
version: 46
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Educacional & Fluig |
| **Versões:** | 12.1.9 |
| **Ocorrência:** |  |
| **Ambiente:** | ORACLE |
| **Passo a passo:** | Cadastro de Bolsista  **Descrição**  Possibilita ao usuário gerenciar seus processos referentes ao cadastro do bolsista, permitindo realizar o cadastro, submeter a análise e avaliação utilizando-se do processo de aprovação através de FLUIG.  Preciso primeiro ter aprovado e finalizado um Projeto Extensão  1º)   É necessário ter um projeto cadastrado e aprovado (SPROJPROJETO.APROVADO = ‘S’) e que esteja em execução (SPROJPROJETO.SITUACAO = 4).  O usuário (CODPESSOA) do RM.exe, vinculado ao usuário logado no FLUIG, deve ser o coordenador do projeto (SPROJPROJETO.CODPESSOACOORDENADOR).  A data final do projeto (SPROJPROJETO.DATAFINAL) deve ser maior ou igual a data atual.  O projeto deve ter participantes ativos (SPROJPARTICIPANTES.ATIVO = ‘S’) e que tenham plano de trabalho associado (SPROJPLANOTRABALHO). Utilizar os usuários do RM.exe vinculados aos usuários do FLUIG que foram criados para os testes desse fluxo.    Esta informação é inserida no Projeto em Equipes .. Mas é preciso o Cadastro de Plano de trabalho também para que possa se utilizar o cadastro de Bolsista    **Informar quantidade de Bolsas**  Esta informação é cadastrada no próprio Edital      Obs: O Valor das Bolsas do Edital não pode ultrapassar o informado no cadastro do mesmo acima.  Anexos > Bolsas de Pesquisa / Extensão ( pagamento )      Inseridos os dados referentes ao cadastro de Bolsa para o Edital ( Edital Projeto Extensão 2 )  Quantidade de Bolsa no Edital =  ( 400 )  Quantidade de Bolsa no Projeto = ( 400 )      Inserida quantidade de bolsas que serão utilizadas  **Após finalizar e aprovar o Cadastro de Projeto Extensão :**  Realizar o cadastro dos dados solicitados no formulário, lembrando dos pré-requisitos informados anteriormente.   * O campo “RA” não é obrigatório visto que o pesquisador/Extensionista pode ser de fora da instituição. * Caso o bolsista seja menor de idade, o campo “RA” deverá ser preenchido para que seja recuperado o responsável acadêmico desse bolsista. Caso o Pesquisador/Extensionista não seja um aluno, portanto não tenha RA, não será possível cadastrá-lo como bolsista. * Ao marcar o campo “Voluntário” o painel “Bolsas (pagamento)” deve desaparecer, pois sendo voluntário, não é possível receber bolsas. * Caso o bolsista não seja voluntário, será necessário informar ao menos uma bolsa.   Logar no FLUIG utilizando o usuário que está vinculado ao papel de “Pesquisador” e que é coordenador do projeto que será selecionado. Iniciar uma nova solicitação do cadastro de bolsista.    Logando com Fluig          Educacional | Inovação , Pesquisa e Extensão | Bolsista | Cadastro de Bolsista | Cadastro de Bolsista       usuário deverá preencher o tipo de fomento e se o mesmo for “Externo” deverá ser informado também o órgão de fomento.    Nessa etapa do fluxo o usuário poderá escolher uma das duas opções .   * Confirmar * Cadastro Recusado   Neste exemplo foi escolhido a opção: “Confirmar”. Clique em Salvar/Enviar.  Caso o usuário selecione “Cadastro Recusado” o campo SITUAÇÃO será alterado para “I” e o fluxo será concluído.  Nesse momento, se o pesquisador/Extensionista for menor de idade, o fluxo será direcionado para seu responsável acadêmico. Para essa evidência foi escolhida a opção onde o pesquisador/Extensionista é maior de idade, ou seja, o fluxo será enviado diretamente para ele.      Movimentar processo    Logar com o usuário coordenador do projeto, nesse exemplo o usuário astoni, e realizar a aceitação do termo de aceite.    Coordenador do Projeto dando seu Aceite aos Termos  Projeto Finalizado para Cadastro de Bolsista |
| **Observações:** |  |

divs
