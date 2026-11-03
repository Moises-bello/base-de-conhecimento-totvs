---
article_id: 360006992532
category: RH - Ambiente
content_hash: 39afaca4f8af0adc37db2c8991a4cebe771aa95b15ba0492593eceef6c50da91
fetched_at: '2026-06-28T22:43:09.611793+00:00'
product: protheus
section_id: 20669342808471
source: central-protheus
title: RH - Linha Protheus - GPE - Configuração Event Viewer - Inscrição de Eventos
type: support-article
updated_at: '2026-06-24T17:36:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006992532-RH-Linha-Protheus-GPE-Configura%C3%A7%C3%A3o-Event-Viewer-Inscri%C3%A7%C3%A3o-de-Eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32875650349847)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como configurar o *Event Viewer* para notificação aos usuários?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O ***Event Viewer*** funciona como uma forma de **notificação de determinados eventos** aos usuários inscritos, que pode acontecer por **email** ou **evento de notificação no Protheus.**  
As notificações através de **email** **só poderão ser enviadas para usuários que fazem parte do grupo de Administradores**, e as **notificações no Protheus** **podem ser enviadas para grupos/usuários previamente cadastrados.**  
É necessário que no cadastro do Grupo/Usuário que receberão as notificações, na aba Restrições de Acesso > Acessos > esteja marcada a opção **174 - Acesso a inscrição nos eventos do EventViewer.**  
  
Os **eventos** que podem ser cadastrados para notificação, são:  
**• 015 -** Aviso de Férias  
**• 016 -** Admissão de Funcionário  
**• 017 -** Desligamento de Funcionário  
**• 018 -** Funcionário Afastado  
**• 019 -** Funcionário Transferido  
  
Para cadastro do ***Event Viewer*** para Grupos/Usuários, basta seguir os passos abaixo:  
  
**1 -** Acessar o Configurador > Usuário > Senhas > neste exemplo, a liberação será feita para um Usuário específico, de nome **TESTE**.   
Após localizar o usuário, clique em Alterar > siga para a aba Restrições de Acesso > Acessos > **marque a opção 174** e salve.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875650350231)  
  
  
**2 -** Acesse o SIGAGPE com o usuário que deverá receber a notificação > Miscelanea > Inscr. Event Viewer > Incluir. O cadastro deve ser feito conforme abaixo:  
**- Canal:** selecione a opção 002 - Ambientes  
**- Categoria:** selecione a opção 001 - Módulos e dê um TAB no teclado  
**- Id do Evento:** neste exemplo, usaremos o 016 - Admissão de Funcionário  
O cadastro ficará desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875671662231)  
  
  
**3 -** A partir deste momento, quando um funcionário for admitido por qualquer pessoa, o usuário TESTE receberá a notificação deste evento. Para que o usuário visualize esta informação, basta que ele clique no Envelope no canto superior direito. conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875671664279)  
  
  
**4 -** A notificação ficará desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875671666199)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875650353431)  
  
  
  
  
Para enviar a notificação de um evento por **email** para usuários que pertencem ao grupo de Administradores, devem ser seguidos os passos abaixo:  
  
**1 -** Através do Configurador, é necessário que seja feita a **configuração de SMTP** conforme documentação do Framework que pode ser acessada **[aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071-Framework-Linha-Protheus-Configurar-o-SMTP-para-envio-de-relat%C3%B3rios-por-e-mail)**  
  
**2 -** No cadastro do usuário, se certifique que existe um **email informado** e que a opção **174 está marcada:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875650354327)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875650355351)  
  
  
**3 -** Acesse o SIGAGPE com o usuário que deverá receber a notificação > Miscelanea > Inscr. Event Viewer > Incluir. O cadastro deve ser feito conforme abaixo:  
**- Canal:** selecione a opção 002 - Ambientes  
**- Categoria:** selecione a opção 001 - Módulos e dê um TAB no teclado  
**- Id do Evento:** neste exemplo, usaremos o 016 - Admissão de Funcionário  
**- Email:** Sim  
O cadastro ficará desta forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875671670423)  
  
  
**4 -** A partir deste momento, quando um funcionário for admitido por qualquer pessoa, o usuário TESTE ADMIN receberá a notificação deste evento por email conforme exemplo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32875671672471)  
  
  
**Saiba Mais:**  
[Framework - Event Viewer - Inscrição de Eventos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=876240657)  
[Ponto de Entrada GPM040MAIL](https://tdn.totvs.com.br/pages/releaseview.action?pageId=185761521)
