---
content_hash: 8e32cdb0486df6b52675234769280e0a1690bdadcfc57968cfa6bbc8c78b0ab4
fetched_at: '2026-06-29T00:09:30.371600+00:00'
page_id: '425458451'
product: rm
source: tdn-rm
title: Grupos de Emails
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupos+de+Emails
version: 22
---

**Grupos de Emails**   
 O usuário cadastra um endereço de e-mail e um grupo de atendentes.

Quando o serviço de envio de e-mails do TOTVS Aprovações e Atendimento for executado, ele irá percorrer a caixa de entrada do e-mail cadastrado e transformar cada e-mail em um atendimento. Este atendimento será gerado de acordo com um modelo de atendimento selecionado no cadastro de grupo de e-mails e será encaminhado para um determinado atendente (fixo ou grupo de atendentes), de acordo com o que for definido no próprio cadastro de grupo de e-mails.   
   
Existem dois tipos de autenticação:

**Padrão:**

Na autenticação padrão, o usuário informa e-mail e senha. Com isso o sistema consegue conectar-se à caixa de entrada do e-mail informado e ler as mensagens. O e-mail informado deve aceitar conexão com o protocolo informado nos parâmetros de serviço (podendo ser POP ou IMAP), e a senha utilizada deve ser uma senha de um aplicativo cadastrado na conta de e-mail utilizada.

Link dos parâmetros de serviço:

**OAuth 2.0 (Exchange)**

Contas de e-mail que utilizam a autenticação OAuth 2.0, não aceitam acesso de aplicativos usando usuário e senha. Portanto, nesse caso deve-se informar o ID do aplicativo cadastrado na conta de e-mail (ClientID) e a URL de direcionamento. Após isso, o botão Autenticar deve ser acionado e uma página para o usuário informar e-mail e senha será exibida, e após autenticar corretamente será exibido do lado direito do botão Autenticar, um ícone verde indicando que a autenticação foi bem-sucedida. Então o registro do grupo de email que utiliza esse tipo de autenticação poderá ser salvo. Para um exemplo (passo a passo) de como cadastrar um aplicativo e obter os dados necessários para a autenticação OAuth 2.0 (ClientID e URL de direcionamento), vide link abaixo:

**Importante:**

O Microsoft Exchange não suporta mais a autenticação básica (usuário e senha), então, usuários desse serviço devem configurar a autenticação OAuth 2.0.

Os demais campos independem do tipo de autenticação, são eles:

* **Criação de atendimentos a partir dos e-mails da caixa postal.**

Lê as mensagens da caixa de entrada do e-mail informado e transforma todas em atendimentos,

* **Atualização do histórico do cliente a partir de resposta aos mailings do módulo de Marketing**

Lê as mensagens da caixa de entrada do e-mail informado, identifica quais mensagens possuem determinada TAG que as identifica como resposta ao envio de mailing do módulo de marketing e registra quaisquer respostas no histórico do cliente.

* **Registro na discussão (do texto de e-mail) e inserção de arquivos anexos a partir de resposta aos e-mails de atendimentos**

Lê as mensagens da caixa de entrada do e-mail informado, identifica quais mensagens possuem determinada TAG que as identifica como ligadas ao atendimento, e registra quaisquer respostas na discussão do atendimento, bem como inclui no atendimento os arquivos anexos ao e-mail..

* **Atendimento Modelo**

Modelo usado no atendimento criado pelo serviço de Gerar atendimentos por grupo de e-mails.

* **Atendente responsável**

Define o atendente que será responsável pelos atendimentos criados pelo serviço de Gerar atendimentos por grupo de e-mails.

* **Grupo de Atendentes**

Define um grupo de atendentes responsável pelos atendimentos criados por meio do serviço de Gerar atendimentos por grupo de e-mails. Necessário informar, caso a opção escolhida como atendente responsável seja "Repasse para grupo de atendentes".
