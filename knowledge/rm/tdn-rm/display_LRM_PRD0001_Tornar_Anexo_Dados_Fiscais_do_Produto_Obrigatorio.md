---
content_hash: 1806117f349c77d381b97fedf6444e15b94bda0a162949a5c3aa26d2aaca98ef
fetched_at: '2026-06-29T00:08:10.578711+00:00'
page_id: '240306407'
product: rm
source: tdn-rm
title: PRD0001_Tornar_Anexo_Dados_Fiscais_do_Produto_Obrigatorio
type: documentation
url: https://tdn.totvs.com/display/LRM/PRD0001_Tornar_Anexo_Dados_Fiscais_do_Produto_Obrigatorio
version: 4
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Versões:** | 12.1.10 ou posteriores |
| **Ocorrência:** | Tornar o anexo Dados Fiscais do Produto Obrigatório |
| **Ambiente:** | Cadastro de Produto |
| **Passo a passo:** | Objetivo Este documento tem por finalidade tornar o anexo de dados fiscais do produto obrigatório. Assim, na inserção ou na edição de um produto, o sistema consistirá o preenchimento do cadastro. Passo a Passo 1º - Deverá acessar a tela de Dados Fiscais do Produto e marcar como obrigatório os campos aos quais deseja torná-los obrigatórios:  *Clicar sobre o campo com o botão direito do mouse e marcar a opção **Preenchimento obrigatório***      2º - Após tornar os campos obrigatórios deverá cadastrar o **Anexo de uma Action** desejada para que a mesma fique disponível em Preferências de Anexos, onde iremos determinar se a mesma será obrigatória. Para isso deverá acessar o módulo de Serviços Globais e ir no menu Serviços – Opção **Actions Anexas**    Solicitar um novo registro    O cadastro deverá respeitar as informações abaixo:  Action Principal: **EstPrdAction**  Action Anexo: **FisPrdDadosFiscaisAction**  Nome do Grupo: **Dados Fiscais do Produto**      **IMPORTANTE**: Se a action desejada não apresentar na lista, deverá rodar o processo de Atualização de Actions Cadastradas conforme documento abaixo:      3º - Após o cadastro de Actions Anexas, deverá no mesmo módulo acessar o menu **Preferências de Anexos,** para tornar o Anexo Dados Fiscais do Produto obrigatório.  Ao clicar no menu, será aberta a seguinte tela:      Dentro deste cadastro, na aba Permissões Gerais (Perfil ou usuário), será necessário incluir uma nova preferência:      O cadastro deverá respeitar as informações abaixo:  Id: **É o cadastro realizado no passo 2 (EstPrdAction/FisPrdDadosFiscaisAction)**  Campos Mestre: **TPRODUTODEF.CODCOLIGADA;TPRODUTO.IDPRD**  Campos Detalhe: **TPRDFISCAL.CODCOLIGADA;TPRDFISCAL.IDPRD**  Marcar a Flag **Obrigatório**  Ativo****Sim****    Obs.: Após realizar a configuração deverá ser feito o logout e login novamente Descrição do Processo   Para realizar a validação do passo a passo, deverá criar um novo produto sem informar os dados fiscais. Ao salvar, o sistema deve obrigatoriamente apresentar a mensagem abaixo:      Para poder preencher as informações deste cadastro, o sistema irá criar uma nova aba dentro do produto. Esta aba chama-se **INFORMAÇÕES ADICIONAIS**      Podemos notar que foi criado o link Dados Fiscais do Produto, e ao clicar sobre o mesmo é aberto o anexo conforme abaixo:      Desta forma, enquanto o usuário não informar valor para o campo **Situação da Mercadoria** o produto não poderá ser salvo. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |
