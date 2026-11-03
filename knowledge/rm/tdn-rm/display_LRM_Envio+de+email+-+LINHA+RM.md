---
content_hash: 4015b1490c23081c74363a5b863fb03cbda77b76fb9d39603c4cf6ee69728398
fetched_at: '2026-06-29T00:11:21.582312+00:00'
page_id: '69763106'
product: rm
source: tdn-rm
title: Envio de email - LINHA RM
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+email+-+LINHA+RM
version: 28
---

# Índice:

---

true

# Objetivo:

---

Este documento possui orientações sobre a tela Opções\Parâmetros\Globais\Envio de E-Mails.

Esta tela define a configuração para comunicação com o servidor SMTP utilizado no processo de envio de e-mails pelos módulos do sistema. Cada servidor SMTP pode exigir uma configuração diferente para comunicação e percebemos que existem usuários que desconhecem estas configurações e não sabem o que o servidor exige e o que ele não permite.

Infelizmente existem fatores externos que podem influenciar neste processo, como conexão com a internet, firewall, antivírus, e outras aplicações que podem bloquear processos de envio de e-mail.

Fica a cargo do cliente analisar estes bloqueios externos e liberar que o aplicativo possa realizar o procedimento.

**IMPORTANTE:** O RM necessita da configuração de relay habilitada, pois irá autenticar no servidor de e-mail com o usuário que está nas configurações globais e enviar como remetente outro usuário(definido nas configurações de parâmetros globais).

**OBSERVAÇÃO:** Em ambiente **N camadas**, o servidor de Jobs é o responsável pela execução dos processos, incluindo a rotina de processos que enviam e-mail. Dessa forma, considerando esse tipo de ambiente, deve-se realizar o teste de envio de e-mail no servidor de Jobs, e realizar as devidas liberações, quando for necessário bem como no servidor de aplicação.

Em ambiente **local** todas as máquinas de usuários que forem realizar o envio de e-mail, devem receber as liberações de segurança (Firewall, antivírus, proxy, e quaisquer outros aplicativos/configurações de segurança).

Atenção

Existe um mecanismo de cache para melhorar a performance do sistema, onde após alterar as configurações de E-mail, o mesmo demorará 5 minutos para ser replicado para os outros serviços do Host. Caso necessário aplicar a alteração imediatamente será necessário reiniciar todos os serviços do Host do ambiente.

# Configuração da tela de envio de e-mails:

---

**Acesse a GUIA Envio de e-mails**

A tela possui parâmetros da coligada atual (define as configurações que serão utilizadas na coligada que o usuário está logado no momento) e da coligada global (define as configurações que serão usadas pela coligada global). Geralmente configuramos as mesmas informações para a coligada global e a atual, dependendo da necessidade da empresa estes dados poderão ser separados.

Obs.: Referente ao item 6 - Considerar como remetente padrão de envio de e-mail a opção 'E-mail do usuário corrente':

Para que seja apresentado o nome do usuário do RM ao receber o e-mail, no campo 2 (usuário/senha) deve ser informado o e-mail completo do usuário validador, exemplo: [mestre@totvs.com.br](mailto:mestre@totvs.com.br)

Caso não preencha desta forma, será apresentado o nome do usuário validador.

Exemplo:

  

IMPORTANTE

A partir dos patches informados abaixo, ao selecionar o parâmetro “Remetente Parâmetros Globais” no processo de envio de e-mails, caso a opção “E-mail da Coligada atual” esteja marcada nos parâmetros globais, o sistema passará a utilizar o nome fantasia da coligada como remetente.  
Esse comportamento será semelhante ao da opção “Utilizar usuário de e-mail como remetente”.  
Antes dessa alteração, era utilizado o nome da coligada. Após a implementação do patch, o comportamento passa a seguir a mesma lógica da opção “E-mail da Coligada global” definida nos parâmetros globais.  
  
Patches referente a alteração:

* 12.1.2506.257
* 12.1.2510.178
* 12.1.2602.101 e superiores

# Testando envio de e-mails:

---

Para verificar se as configurações foram efetuadas com sucesso, podemos testar **enviando um e-mail de teste** clicando na opção em destaque:

Digite um endereço de e-mail para que a mensagem de teste seja entregue, depois clique em **Enviar**.

Após clicar em enviar, a mensagem abaixo será exibida informando que um e-mail de teste foi enviado com êxito.

APLICATIVO TESTA EMAIL

Além do teste acima é possível fazer um outro teste de envio de e-mails para saber quais configurações e parametrizações utilizar no Envio de E-mail.

O aplicativo abaixo (Anexo) irá tentar enviar e-mail com todas as combinações possíveis de envio de e-mail, informando assim o que o servidor exige e o que ele não permite (dentro do conjunto de possibilidades da tela).

No final do processo, o sistema irá exibir um log que mostra o resultado do processo de envio. Neste log constará as combinações que enviaram com sucesso e as combinações que não foi possível enviar.

Clique abaixo para efetuar o download do aplicativo Testa E-mail Global 

**IMPORTANTE 2:** O Office 2016 está homologado à partir da versão 12.1.17 do RM. O Office 365 é um serviço de assinatura que garante que você tenha as ferramentas mais recentes da Microsoft, ou seja, você poderá estar sempre atualizado na versão mais recente do mesmo, como por exemplo o Office 2016.  
Tendo a assinatura do Office 365 e o Office 2016, em conjunto com a versão 12.1.17 (ou superior) poderá utilizar o envio de e-mail do RM, conforme orientações do documento. **Dica:** Avaliar a necessidade de ativar o recurso Aplicativos Integrados nas configurações de seu Provedor de E-mail:

Link de documentação da Microsoft sobre o recurso Aplicativos Integrados: <https://docs.microsoft.com/pt-br/office365/admin/misc/integrated-apps?view=o365-worldwide>

**IMPORTANTE 3:** O SMTP da Google para prevenir Spoofing não permite envio direto de emails alterando o remetente.  
Para tal comportamento são possíveis 2 saídas:

* Adicionar os endereços/alias no email configurado no SMTP
  + <https://support.google.com/mail/answer/22370?hl=pt-BR>
* Configurar um SMTP Relay no GSuite
  + <https://support.google.com/a/answer/2956491>

Ambas soluções são de configuração por parte do cliente.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM) e 9 – (Demais Áreas)

falsefalse

**Produto:** Framework

false

**Versão:** todas

false

**Processo:** Parâmetros Globais email

**Subprocesso:** Parametrização de envio de email

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**
