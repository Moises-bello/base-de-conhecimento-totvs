---
article_id: 360022314291
category: CRM - Dúvidas Gerais
content_hash: f735a585a27c0abd26d6e6187d7346fe265e29e89b5881a1f9a6f91c31c8ec7a
fetched_at: '2026-06-28T22:40:27.516525+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - CRM - Integração de Exchange
  com a Área de Trabalho
type: support-article
updated_at: '2024-09-02T17:10:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022314291-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-CRM-Integra%C3%A7%C3%A3o-de-Exchange-com-a-%C3%81rea-de-Trabalho
---

**Dúvida**

Configurar a integração do Exchange - já em funcionamento - com o Protheus para sincronismo de TAREFAS e COMPROMISSOS pelas Atividades do CRM na Área de Trabalho do Representante / Work área - FATA320  
  
**Ambiente**  
Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGACRM – A partir da versão 11.80  
  
  
**Solução**

**Implementação Atenção**:

O suporte não orienta em implementação. Este material é unicamente objeto de apoio, e orientamos firmemente que seja solicitado analista in loco para implementar a ferramenta e homologar o uso em produção.

A implementação deve ser realizada primeiramente em ambiente de homologação padrão atualizado e, posteriormente em Produção respeitando os devidos backups preventivos.

**O Exchange Server e o Protheus:**

O Exchange Server é o servidor de mensagens e colaboração da Microsoft. É um software que funciona em servidores que permitem envio e recebimento de e-mails e outras formas de comunicação interativa através da rede de computadores.  
Em sumo, o Exchange é o **SERVIÇO DE GESTÃO DO ENVIO DE E-MAILS** que pode ser utilizado pelo domínio do Cliente.

O Protheus homologou esta funcionalidade à qual se integra com o serviço de gestão de e-mail Exchange (A partir da versão 2007 do Exchange) para envio de TAREFAS e COMPROMISSOS pelas Atividades do CRM.

**Obs**: Além de Tarefas e Compromissos, há também no CRM a Atividade Envio de E-mail, porém, esta não requer integração com Exchange; utiliza a configuração SMTP / POP3, a mesma utilizada para envio de relatórios por e-mail no Protheus (suportado para as classes de tmailmanager e tmailmessage ). Para isto, realizar as configurações abaixo ignorando os parâmetros de Exchange. Mais informações: [SMTP para envio de relatórios por e-mail](http://tdn.totvs.com/pages/viewpage.action?pageId=271166884)

A funcionalidade de Integração Exchange é ativada apenas quando o domínio de e-mail utilizado, utiliza o Exchange Server para sua gestão de envio de e-mail.

**Exemplo**:   
O domínio @[totvs.com.br](http://totvs.com.br/) utiliza Exchange Server para sua gestão de envio de e-mail. Neste caso, é possível utilizar a Conta [fulano@totvs.com.br](mailto:fulano@totvs.com.br) no Protheus para efetuar a sincronização.  
Já:

* @[gmail.com](http://gmail.com/)
* @[yahoo.com.br](http://yahoo.com.br/)
* @[uol.com.br](http://uol.com.br/)
* ETC

são domínios de empresas que utilizam o próprio serviço para gestão de envio de e-mails, e não o serviço da Microsoft Exchange Server.

**Então, neste caso, não é possível utilizar contas fulano@gmail ou fulano@yahoo ou fulano@uol, etc no Protheus para efetuar a sincronização visto que a funcionalidade se integra com o Serviço Exchange**

**Obs**: esses domínios @[gmail.com](http://gmail.com/) / @[yahoo.com.br](http://yahoo.com.br/) / @[uol.com.br](http://uol.com.br/) / ETC podem ser apenas receptores. Ou seja, a conta [fulano@totvs.com.br](mailto:fulano@totvs.com.br) devidamente configurada para a integração, pode inserir na Atividade/ Compromisso "n" participantes que possuem contas de outros domínios para receberem o comunicado do agendamento.

**OBS**: O próprio OFFICE 365 não se integra com o Protheus: <http://www.tdn.totvs.com.br/display/tec/Office+365> e <http://tdn.totvs.com/display/tec/SmartClient+-+Office>

A integração é com o Exchange. A ferramenta  Office 365 não é um SERVIÇO DE GESTÃO DO ENVIO DE E-MAILS, e sim, apenas um Client que intermedia o serviço. Desta forma, independente do uso da ferramenta Office 365, é preciso avaliar para uso da integração Exchange, se o domínio de E-mail utiliza, ou não, o serviço da Microsoft: Exchange Server para sua gestão de envio.

**Importante:** Para a segurança da conexão do Envio de E-mail no Protheus, foi implementado na release 12 do Protheus, a verificação em duas Etapas e a senha Aplicativo pelo Provedor de E-mail, Para o sistema validar a senha disponibilizada pelo Provedor no parâmetro, com isso realizando o envio do E-mail.

**GMAIL**

[Alterações necessárias para uso do envio de e-mails com o Gmail](https://tdn.totvs.com/pages/releaseview.action?pageId=687162208)

**OUTLOOK**

[Autenticação em duas etapas](https://support.microsoft.com/pt-br/office/autentica%C3%A7%C3%A3o-em-duas-etapas-f4ac126a-f6eb-464e-abdc-ec956e279e10)

[Gerenciar senhas de aplicativo para verificação em duas etapas](https://support.microsoft.com/pt-br/account-billing/gerenciar-senhas-de-aplicativo-para-verifica%C3%A7%C3%A3o-em-duas-etapas-d6dc8c6d-4bf7-4851-ad95-6d07799387e9)

**Para realizar a configuração, saiba mais:**

[Application Server - E-mail](https://tdn.totvs.com/display/tec/Application+Server+-+E-mail)

[Integração de Exchange com a Área de Trabalho do Representante](http://tdn.totvs.com/pages/releaseview.action?pageId=234610307)
