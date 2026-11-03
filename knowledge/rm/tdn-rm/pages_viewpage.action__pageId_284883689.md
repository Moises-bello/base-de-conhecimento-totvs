---
content_hash: 5658b5878b9d5e2062e0c2bce0baf265bf62f2348dec14d0318bf1bc19ebb445
fetched_at: '2026-06-29T00:08:37.745315+00:00'
page_id: '284883689'
product: rm
source: tdn-rm
title: Anexo - Mensagem de Notificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284883689
version: 44
---

ÍndiceEnvio de e-mail alterando remetente

Quando é utilizado o SMTP da Google o e-mail enviado não é enviado com o remetente definido no processo, será enviado com remetente utilizado nas parametrizações do envio de e-mail do RM.

O SMTP da Google não permite enviar e-mail alterando o remente, para tal comportamento seguir as possíveis saídas no passo **"Importante 3" no link:**

Novas mensagens de notificação

* O novo tipo de mensagem de notificação "Confirmação da matrícula no TOTVS Educacional", somente está disponível a partir da versão 12.1.31.100
* O novo tipo de mensagem de notificação "Enviar token para a validação da assinatura do contrato de matrícula" somente está disponível a partir da versão 12.1.31.121

Com intuito de facilitar o envio de mensagens, foram disponibilizados alguns tipos de mensagens que poderão ser utilizados para a notificação de usuários.  Essas mensagens poderão ser criadas utilizando um texto padrão que poderá ser composto por um texto normal ou um texto *HTML*..

No formato de texto *HTML,* o usuário poderá utilizar diversos recursos como imagens, vídeos e tabelas para estruturar o texto do e-mail através de vários recursos de formatação.

Ao definir o tipo da mensagem serão disponibilizadas *tags* para compor o texto padrão, que poderão ser utilizadas através do botão "*Tags disponíveis*". Essas *tags* serão substituídas por seus respectivos valores no momento do envio do e-mail.

Tipos de mensagens para notificação por e-mail disponibilizados:

* **Enviar e-mail para o candidato com sua senha de acesso ao portal de inscrições;**
* **Enviar e-mail para o candidato com a confirmação do cadastro no portal de inscrições;**
* **Confirmação da matrícula no TOTVS Educacional;**
* **Enviar token para a validação da assinatura do contrato de matrícula \***

\* Mensagem de notificação que está disponível somente para Área de interesse ofertada, ou default.

Dica - Mensagem temporal

Essas mensagens de notificação são definidas em dois tipos fixas ou temporais. As fixas são mensagens enviadas no momento em que há uma alteração ou algum processo é executado. Já as temporais são enviadas através de um processo especifico ***(Ler: [Processo de Envio de Mensagens de Notificações Temporais](https://tdn.totvs.com/x/bv1bGQ))***. Esta informação é somente para visualização não pode ser alterada.

Existem dois caminhos de acesso ao cadastro de mensagens de notificação, que pode ser realizado através do menu principal do sistema ou através do anexo da visão do cadastro do processo seletivo:

Nos dois momentos, envio de senha e confirmação de cadastro, o sistema irá verificar se existe uma mensagem de notificação cadastrada para o processo seletivo e se não existir será buscada uma mensagem realizada no cadastro padrão. A mensagem padrão será utilizada todas as vezes em que o processo seletivo não possuir uma mensagem cadastrada.

**Observação**: *Ao utilizar a tag "**\_NOMESOCIAL\_ (Nome Social)**" e este campo não esteja informado (preenchido), será utilizado o campo Nome completo na substituição dessa tag. Esse comportamento facilita na criação do mensagem de e-mail, pois caso se utilize do Nome Social, e este não estiver informado o sistema utiliza o Nome completo na substituição.*

Importante - Notificação de senha de acesso ao portal de inscrições

* Para o envio de uma notificação com as informações de acesso para o candidato inscrito em um processo seletivo, que poderá será executada ao se clicar no botão ***"Enviar login ao candidato",*** através da tela de inscrição do candidato, com a utilização da mensagem cadastrada no anexo do processo seletivo.
  + Caminho: *Cadastros | Processo seletivo | Anexos | Mensagens de notificação*

* Para envio de uma notificação para um usuário do Processo Seletivo que utilizará a mensagem de notificação cadastrada no menu do sistema. Essa mensagem será disparada ao se clicar no botão ***"Alterar/Enviar senha do usuário"*** do cadastro do usuário, que irá gerar uma nova senha e permitir que ela seja enviada para o seu endereço de e-mail.
  + Caminho: *Cadastros| Notificações | Mensagens de notificação*

***PS**.: Caso o cadastro de usuário do Processo Seletivo seja aberto a partir do campo **"Pessoa (Novo portal)"***da tela de inscrição do candidato, ao clicar no botão ***"Alterar/Enviar senha do usuário",***o sistema irá buscar a mensagem de notificação cadastrada através do caminho "*Cadastros | Processo seletivo | Anexos | Mensagens de notificação",* considerando o processo seletivo no qual ele foi inscrito.

## **Confirmação da matrícula no TOTVS Educacional**

Somente matrícula via central do candidato

Caso a matrícula via central do candidato esteja configurada para gerar contrato, será enviado, no anexo do e-mail, o relatório do contrato em formato PDF que foi lido e aceito pelo candidato ou responsável.

Importante: 

Apesar do tipo de mensagem de ***confirmação de matrícula*** possibilitar o envio de uma notificação por e-mail e para o eduCONNECT, o arquivo com o contrato assinado **somente** é enviado por **e-mail**.

## **Pagamento da inscrição através do e-mail de Confirmação de Inscrição**

Foi criada uma *tag* que redireciona para o pagamento por cartão e pagamento por boleto com *login* automático ou *login* manual para serem enviada pelo e-mail de Confirmação de inscrição. Dessa forma, o candidato não precisa abrir o Novo Portal para a realização do pagamento da inscrição. Também, foi criado um layout default para o e-mail de confirmação de inscrição. Esse layout pode ser encontrado no diretório ***"C:\totvs\CorporeRM\ObjetosGerenciais\Central Comunicação"***, necessitando abrir esse arquivo no cadastro de Mensagem de notificação, através do botão ***"Abrir"***na criação da mensagem.

**Tag's com Login automático**

Ao clicar no link que foi enviado pelo e-mail, contendo a *tag **"\_PAGTOBOLETOAUT\_"***, a página será redirecionada automaticamente para a página de pagamento e seus dados serão carregados, sem precisar que o usuário insira seu login.

Importante

A *tag* deve ser inserida como ***Hiper-Link***.

Após o candidato realizar a inscrição e informar um e-mail, a mensagem de confirmação de inscrição será enviada automaticamente para o candidato.

Dica

A mensagem de confirmação de inscrição só será enviada, caso o candidato informe um e-mail no preenchimento do formulário de inscrição.

**Tag's com Login manual**

Ao clicar no link que foi enviado pelo e-mail contendo a *tag **"\_PAGTOBOLETOMANUAL\_"***, a página será redirecionada para a página login, necessitando que o candidato insira seu login e senha para depois realizar o pagamento pelo cartão ou boleto.

## **Envio de token/chave de segurança**

A partir da **versão 12.1.31.121**, foi disponibilizado um novo tipo de mensagem, que somente estará disponível para cadastro no menu Mensagem de notificação default e no anexo de área de interesse, que irá funcionar conforme os outros tipos de mensagem acima, por prioridade, primeiro o sistema verifica se a área ofertada que o candidato está tentando se matrícula, possui uma mensagem de token para envio, caso não possua, será verificado no cadastro default de mensagens de notificação.

Para utilização da mensagem de notificação, no anexo na Área ofertada, é necessário:

* O usuário tenha a permissão de perfil para cadastro de mensagens de notificações:
  + Permissão: ***Processo Seletivo | 02 - Cadastros | 02.04 - Notificações***

* O processo seletivo esteja configurado para utilizar o novo portal e não utilize o Venda Online.
* A área ofertada esteja configurada para utilização da matrícula on-line.

Na mensagem de notificação acima **"Enviar token para a validação da assinatura do contrato de matrícula"** é possível informar qual o texto que será enviado no e-mail para os candidatos/responsável da inscrição, tendo a possibilidade de utilizar duas tags:

* **\_NOMECANDIDATO\_** - Nome do candidato que será realizado a matrícula.
* **\_TOKEN\_** - Token/Chave de segurança gerado para assinatura do contrato da matrícula.

  Melhoria nas Tags - Versão 12.1.2510

  A partir da versão **12.1.2510** foram incluídas novas tags de personalização na mensagem de notificação **"Enviar token para a validação da assinatura do contrato de matrícula"**,permitindo inclusão das tags abaixo para inserir dados mais específicos dos candidatos e seus responsáveis.

  + **\_NOMEPAI\_** - Nome do pai do candidato que será matriculado.
  + **\_NOMEMAE\_** - Nome da mãe do candidato.
  + **\_NOMERESPONSAVELACADEMICO\_** - Nome do responsável financeiro do candidato.
  + **\_NOMERESPONSAVELFINANCEIRO\_**- Nome do responsável acadêmico do candidato.
  + **\_NOMECURSO\_** - Nome do curso no qual o candidato será matriculado.
  + **\_HABILITACAO\_** - Nome da habilitação relacionada à matrícula.
  + **\_TURNO\_** - Turno em que o candidato será matriculado.
  + **\_CODPERLET\_** -  Código do período letivo em que o candidato será matriculado.

  Tags que fazem referência a informações **não cadastradas para o candidato** no momento da matrícula não serão exibidas no e-mail enviado. Ou seja, caso os dados correspondentes a uma tag utilizada na mensagem de notificação **não estejam preenchidos na matrícula**, essa tag será omitida no e-mail, não sendo exibida para o destinatário.

  Exemplo:

  **Print 1:** Exemplo de mensagem de notificação parametrizada com todas as tags disponíveis.

  **Print 2:** E-mail recebido após matrícula realizada utilizando apenas os dados do candidato, do pai e do responsável financeiro.

## **Envio de e-mail informando que a assinatura do contrato será validada com Totvs Assinatura Eletrônica**

A partir da **versão 12.1.34** foi disponibilizado uma nova mensagem de notificação. Trata-se da nova opção **"Enviar e-mail informando que a assinatura do contrato será validada com Totvs Assinatura Eletrônica"** que estará disponível no menu mensagem de notificação default, no anexo do processo seletivo e no anexo de área de Interesse ofertada. Por prioridade, o sistema verificará se a área de interesse ofertada possui a mensagem de assinatura com Totvs Assinatura Eletrônica para envio, caso não possua, será verificado no processo seletivo, caso também não possua, será verificado no cadastro default de mensagem de notificação.

O objetivo desta mensagem é indicar ao aluno que ele receberá um e-mail para realizar a assinatura do contrato ao concluir a matrícula pela central do candidato.

Importante

A partir da versão **12.1.2410.276**  o e-mail com a mensagem de notificação será enviado somente para o responsavel financeiro, seja ele o aluno ou não. Sendo assim caso não exista um responsavel financeiro cadastrado não será possivel prosseguir com a matricula.

**Observação**: *Caso o campo "**Nome Social**" esteja informado no cadastro do aluno, pai, mãe, responsável acadêmico ou responsável financeiro, o sistema irá utilizar o nome social ao realizar a substituição das tags correspondentes ao nome.*

Importante

Caso o parâmetro **"Utiliza Totvs Assinatura Eletrônica para assinatura do contrato"** esteja marcado na área de interessa ofertada será OBRIGATÓRIO que esta mensagem de notificação seja adicionada.

Uma vez utilizando o parâmetro será necessário informar um e-mail para realizar a assinatura do contrato ao concluir a matrícula pela central do candidato. Caso contrário, o aluno não conseguirá prosseguir com sua matrícula pela central do candidato devido a seguinte validação.

Importante

A partir da versão **12.1.2410.276** o e-mail com a mensagem de notificação será enviado somente para o responsavel financeiro, seja ele o aluno ou não. Sendo assim caso não exista um responsavel financeiro cadastrado não será possivel prosseguir com a matricula.
