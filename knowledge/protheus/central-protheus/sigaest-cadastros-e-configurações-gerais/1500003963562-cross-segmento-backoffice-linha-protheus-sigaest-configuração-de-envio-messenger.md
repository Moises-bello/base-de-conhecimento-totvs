---
article_id: 1500003963562
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 0ff02bf4fce86074e90f76806bd966300515f19ea5c6d4fc43d98995bfd59af5
fetched_at: '2026-06-28T22:39:07.983569+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Configuração de envio
  Messenger para ID de eventos do Estoque
type: support-article
updated_at: '2025-10-02T18:47:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003963562-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-envio-Messenger-para-ID-de-eventos-do-Estoque
---

**Dúvida**Como configurar o Protheus para envio de e-mail por eventos do módulo do **Estoque?**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Em primeiro lugar, verificar se o ambiente possui as últimas atualizações disponíveis abaixo:

**Atualização APPSERVER**

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/)

**Atualização LIB**

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/)

**Atualização DBACCESS**

[Clique aqui](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)

Caso não esteja atualizado, efetuar as atualizações e prosseguir com os testes a seguir. (**obs**: todo e qualquer procedimento, primeiro deve ser realizado em base de homologação. Efetuar sempre o Backup antes de qualquer atualização).

**-------**

**Passo1:** Verificar junto ao seu provedor de e-mails, qual a correta configuração do e-mail, como SMTP, TLS, Protocolos, senha etc.

-------

**Passo2:** Acesse o módulo do configurador SIGACFG e prossiga até o seguinte caminho:

**Ambiente > E-mail/proxy > Configurar**, após inclua as configurações de envios conforme indica seu provedor de e-mail, abaixo utilizaremos um e-mail genérico do domínio @gmail.com

![Passo2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103281354)

![](https://centraldeatendimento.totvs.com/hc/pt-br/article_attachments/13135881814679/30898911e0449b0191e1431cc723df88329fccb43616943972122cbc20d28b80.png)

**-------**

**Passo3:** Inserir o E-mail no Cadastro de Usuário em **​Configurador > Usuário > Senhas > Usuários,** no cadastro do usuário, inserir o E-mail no campo **(E-mail)USR\_EMAIL**

**![Passo3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004469802)**

**-------**

**Passo4:**Vamos efetuar um teste de recebimento do e-mail, afim de validar se as configurações foram feitas corretamente, em **​Configurador > Usuário > Senhas > Usuários > Outras Ações > Imprimir,** selecione o tipo E-mail e no campo **Impressão(CEMAIL)** e insira o e-mail de destino, após clique em **Imprimir,** será aberto uma nova aba **"Nova Mensagem"** insira os dados de Titulo e descrição e outros caso queira, e clique em **Ok.**

**![Passo4.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004610621)**

*Se as configurações do e-mail estiverem corretas, você recebera um novo pop-up confirmando que o envio foi um sucesso, do contrario será apresentado uma tela de **Usuário e senha**, isso indica que as configurações **estão erradas**, e vai ser preciso acertar conforme o **Passo2** junto ao seu provedor de e-mail.*

***-------***

**Passo5:** Agora iremos configurar os principais parâmetros, para que o envio do e-mail funcione corretamente com os "Eventos" cadastrados e escolhidos pelo usuário**.**

**Configurador > Base de Dados > Dicionário > Base de Dados,** após expanda a seleção, clique em parâmetros, depois na lupa de busca, e filtrei os parâmetros a seguir, com as informações corretas em cada campo.

**MV\_EMCONTA:** insira seu e-mail cadastrado.  
**MV\_RELACNT:** insira seu e-mail cadastrado.  
**MV\_RELAUSR:** insira seu e-mail cadastrado.  
**MV\_RELSERV:** insira as configurações de SMTP(talvez já estejam preenchidas, por conta da configuração inicial do Passo2).  
**MV\_EMSENHA:** insira a senha do e-mail.  
**MV\_RELAPSW:** insira a senha do e-mail.

![Passo5.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004469842)

***Obs:** A senha é publica, quem tiver acesso a tabela SX6 poderá ver mediante o parâmetro.*

*-------*

**Passo6:** Acesso o sistema, e entre no módulo SIGAEST, **Miscelanea > Inscr. Event Viewer > Incluir,** vamos cadastrar um evento para disparar e-mail, com a criação de um novo produto, o evento 033.

Canal: Ambientes, Categoria: 001 (ao inserir a categoria, pressione a tecla TAB caso o campo de id do Evento esteja bloqueado), id do Evento: 033, pressione Confirmar.

![Passo6.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360103281434)

**-------**

**Passo7: Vamos agora,** Inserir o evento que deseja receber o e-mail, amarrando ao usuário: **Atualizações > Cadastros > Messenger,** selecione o retângulo de Usuários para ficar azul, e clique em incluir, após selecione o usuário em em questão, adicione o **Cod. Evento 033** e clique em Incluir.

![Passo7.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004469882)

**-------**

**Passo8:** Após todos os passos anteriores feitos com sucesso, vamos testar o evento, e verificar o envio de e-mail ao efetuar um cadastro de produto (de acordo com o evento 033).

Na rotina de Estoque/Custos acesse: **Atualização > Cadastros > Produto > Produtos**, e inclua um novo produto, após verifique sua caixa de entrada. (**Obs:** só será apresentado alguma mensagem, em caso de erro no envio).

![Passo8.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500004610681)

**-------**

**Atenção**: **cada módulo é responsável pelos eventos a ele destinados, sendo por parte do ESTOQUE/ CUSTOS averiguar inconsistências nos seguintes eventos:**

001 - Produto atingiu ponto de pedido

002 - Produto atingiu estoque negativo.  
008 - Lote de produto vencido.  
021 - Log de Processamento do Refaz Acumulados.  
022 - Log de Processamento do Saldo Atual.  
023 - Termino do Recalculo do Custo Médio.  
033 - Inclusão de Produtos.

042 - Inclusão de Solicitação ao Armazém.  
045 - Produto atingiu lote mínimo/quantidade por embalagem.  
046 - Inicio de Proc. da Rotina de Recalculo do Custo Médio.

### **Importante:**

* As rotinas que enviam e-mail de acordo com evento cadastrado, utilizam a função do messenger: ***MEnviaMail***que consta dentro do fonte **MATXFUNC.**
* Reinicie o serviço caso haja alguma alteração na configuração.
* Erros genéricos que podem ser apresentados como: *Authentication failed, There was no response from the server e Operation\_failed,* deve-se verificar internamente as configurações corretas do seu provedor de e-mail.
* A estrutura de e-mails enviadas pelo Messenger, segue um padrão, caso o layout em seu provedor sob algum disparo dos eventos estejam desalinhados, validar juntamente ao provedor responsável pelo recebimento.

**Obs:**

A rotina M-messenger (MATA045) foi descontinuada em 31/10/2024.

**Rotina Substituta:**  
[CFGA040 - Event Viewer](https://tdn.totvs.com/x/76s4E)

**Saiba mais:**

[*Clique aqui e veja mais sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033382-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
