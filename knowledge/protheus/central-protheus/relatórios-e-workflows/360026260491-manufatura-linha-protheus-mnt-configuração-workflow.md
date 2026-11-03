---
article_id: 360026260491
category: Relatórios e Workflows
content_hash: 9aae4bb596eea08e40039910766e3a14fbe4d58b00374c56424c7d7206e03d0a
fetched_at: '2026-06-28T22:42:31.642176+00:00'
product: protheus
section_id: 360010992394
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Configuração Workflow
type: support-article
updated_at: '2022-12-19T18:49:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026260491-Manufatura-Linha-Protheus-MNT-Configura%C3%A7%C3%A3o-Workflow
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:04:30 min****Dúvida**Como configurar o *workflow* no módulo de **Manutenção de Ativos - SIGAMNT**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Relatórios e Workflows - Todas as versões  
  
**Solução**Para configuração do *workflow* no **SIGAMNT** é necessário a realização dos passos a seguir:  
  
1. No módulo do **Configurador - SIGACFG** acessar **Usuário/Senhas/Usuários - CFGA510**.

* Selecionar o usuário utilizado para acessar o Sistema e **Alterar**.
* No campo de **E-mail - USR\_EMAIL** preencher com um *E-mail* válido.

2. Acessar **Ambiente - Workflow - Contas de E-mail - WFC003**.

* Incluir uma conta de *E-mai*l conforme solicitado.
* Na pasta **Caixa de Correio**, no campo **Correio** incluir um nome para a conta e no campo **Endereço** informar a conta de *E-mail* utilizada pelo remetente.
* Na pasta **Receber Mensagens**, no campo **Nome** inserir o nome do servidor **POP3**, inserir **Conta** e **Senha** para *login* no servidor.
* Na pasta **Enviar Mensagens**, no campo **Nome** inserir o nome do servidor **SMTP**, inserir **Usuário** e **Senha** para autenticação no servidor.
* Na pasta **Conexão**, selecionar **TLS** e **LAN**.

3. Acessar **Ambiente - Workflow - Parâmetros Wf - WFA000**.

* Na pasta **Correio** selecionar a conta cadastrada anteriormente e selecionar os campos **Envia html** **no corpo da mensagem** e **Envio automático**.
* Na pasta **Processos** inserir **10** no campo **Execuções de retornos** **de processos por vez**, em seguida marcar o campo **Usar TRANSACAO na execução de funções RETORNO**, **TIMEOUTs**.
* Na pasta **Notificação** inserir o endereço de *e-mail* para envio de *workflow* e selecionar todas as opções.
* Na pasta **Messenger** inserir o servidor e o caminho do diretório **HTTP - \http\web** por padrão.

4. Acessar **Ambiente - E-mail/Proxy - Configurar - CFGSETMAIL.**

* Na primeira pasta incluir o servidor **SMTP** para envio de *workflow*, a conta para autenticação **SMTP**, senha e o *e-mail* **FROM** - remetente.
* Na segunda pasta selecionar **POP3 / Sim / Sim** e **Sim** respectivamente.
* Na terceira pasta selecionar e preencher as informações se utiliza *proxy*.

5. Acessar **Ambiente / Cadastros / Parâmetros - CFGX017** e configurar os parâmetros conforme descrição dos mesmos:

* **MV\_RELSERV - Nome do servidor de envio de E-mail utilizado nos relatórios.**
* **MV\_RELAPSW - Senha para autenticação no servidor de E-mail.**
* **MV\_RELACNT - Conta a ser utilizada como remetente no envio de E-mail para os relatórios.**
* **MV\_RELAUSR - Usuário para autenticação no servidor de E-mail.**
* **MV\_RELAUTH - Servidor de E-mail necessita de autenticação?**
* **MV\_RELFROM - E-mail utilizado no campo FROM no envio de relatórios por E-mail.**
* **MV\_RELTIME - Timeout no envio de E-mail.**
* **MV\_RELSSL - Define se o envio e recebimento de E-mails na rotina SPED utilizara conexão segura - SSL - Secure Sockets Layer.**
* **MV\_RELTLS - Informe se o servidor de SMTP possui conexão do tipo segura - SSL/TLS.**
* **MV\_NGWFHT - Indica o IP - Internet Protocol e a Porta para a comunicação HTTP do workflow.**
* **MV\_NGWFLG - Indica se gera log específico do processamento do workflow, 0 - Desabilita; 1 - Habilita.**
* **MV\_WFDIR - Diretório de trabalho do Workflow.**
* **MV\_WFMLBOX - Nome da caixa de mensagens do workflow.**
* **MV\_WFBRWSR - IP ou nome do servidor HTTP.**
* **MV\_WFMAIL - Conta de E-mail do Workflow. Exemplo: Workflow@siga.com.**
* **MV\_WFPOP3 - Servidor de E-mail POP3.**
* **MV\_WFPASSW - Senha da conta do Workflow.**
* **MV\_WFREMET - Remetente do Workflow.**
* **MV\_WFSMTP - Nome do servidor SMTP - envio de mensagem.**
* **MV\_PORSMTP - Porta do servidor SMTP.**
* **MV\_NGSSWRK - Identifica se no módulo de Solicitação de Serviços será utilizado envio de mensagens por workflow online aos solicitantes. Igual a S - Sim.**

6. No módulo do **Manutenção de Ativos** - **SIGAMNT**  acessar **Atualizações / Controle de Oficina / Cadastros Básicos / Funcionários - GPEA010**.

* Preencher o campo **End. E-mail - RA\_EMAIL**.

7. Acessar **Atualizações / Controle de Oficina / Manutenção / Funcionários - MNTA020**.

* Preencher o campo **E-mail**.
* Vincular ao funcionário cadastrado com usuário no campo **Cód. usuário**.

8. Acessar **Atualizações / Controle de Oficina / Cadastros Básicos / Filiais - MNTA855**.

* Selecionar a filial e o funcionário cadastrado.

9. Acessar **Atualizações / Controle de Oficina/Workflow/Grupo conta E-mail - MNTA225**.  
  
10. Acessar **Atualizações / Controle de Oficina/Workflow / Grupo conta E-mail/ Func. - MNTA235**.

* Selecionar o grupo e o funcionário com *E-mail* cadastrado.

**Saiba mais**  
Para informações complementares a respeito da rotina **MNTA855**, verifique o artigo:  
[Como é realizada a definição de destinatários para workflows](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041718353)
