---
article_id: 360028985851
category: RH - Recibos e Cheques
content_hash: e24026a1351f6a97f4c8298ffc1f70c61b17bf2099216ba97105e69ad2f9fc1e
fetched_at: '2026-06-28T22:43:29.488063+00:00'
product: protheus
section_id: 360011909573
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar o recibos de pagamento e outros
  relatórios por e-mail
type: support-article
updated_at: '2026-04-09T11:02:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028985851-RH-Linha-Protheus-GPE-Como-configurar-o-recibos-de-pagamento-e-outros-relat%C3%B3rios-por-e-mail
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25131002272919) Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**  
Como configurar o Sistema para enviar recibos de pagamento / holerite / demonstrativo de pagamento por *e-mail*?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
Para configurar o envio do recibo de pagamento por *e-mail*, execute o seguinte procedimento:  
  
Acesse o cadastro do funcionário através do menu **Atualizações > Funcionários > Funcionários (GPEA010):**  
Na aba **Cadastrais**, preencha da seguinte forma:  
No campo**"Email Princ."** Informe o *e-mail* do empregado ao qual será enviado o recibo de pagamento.  
No campo**"Receb.E-Mail"** Informe sim para que o empregado possa receber *e-mails*.  
No campo**"Tipo E-Mail"** informe o formato do *e-mail* que será enviado: **HTML**.  
  
Para configurar os parâmetros de envio de *e-mail*, acesse o Módulo **SIGACFG** (Configurador) pelo menu **Ambiente > Cadastros > Parâmetros (CFGX017):**

**MV\_EMCONTA:** Indica qual a conta utilizada para o envio de *e-mails*, o que não necessariamente deve ser o *e-mail* do empregado informado no cadastro de funcionários;  
**MV\_EMSENHA:** Indica qual a senha da conta utilizada para envio de *e-mails* automáticos pelo Sistema;  
**MV\_RELSERV:** Indica o nome do servidor de envio de *e-mail* utilizado nos relatórios;  
**MV\_RELAUTH:** Servidor de EMAIL necessita de Autenticação? Utilize .T. para Sim ou .F. para não  
**MV\_RELACNT:** Conta a ser utilizada no envio de *e-mail* para os relatórios;  
**MV\_RELPSW:**Senha da Conta de *e-mail* para envio de relatórios;  
**MV\_RELAPSW:** Senha para autenticação no servidor de *e-mail*;  
**MV\_RELFROM:** *E-mail* utilizado no campo *FROM* no envio de relatórios por *e-mail;*  
**MV\_RELAUSR:** Usuário para Autenticação no Servidor de *E-mail*  
**MV\_PORSMTP:** Indica a porta do servidor SMTP;  
**MV\_RELFIL:** Indica se permite a utilização de filtros nos relatórios do sistema. (1=Sim/2=Não);  
MV\_RELGAR**T****:** *User Function* que Imprime o relatório gerencial da garantia estendida;  
**MV\_RELSSL:** Define se o envio e recebimento de *e-mails* na rotina SPED utilizará conexão segura (SSL);  
**MV\_RELSUG:** Indica a rotina de impressão da sugestão de Lista de Presentes;  
**MV\_RELT:** Diretório especificado para impressão de relatórios  
**MV\_RELTIME:** *Timeout* no Envio de *e-mail*;  
**MV\_RELTLS:** Informe se o servidor de SMTP possui conexão do tipo segura ( SSL/TLS );  
**MV\_RHSERV:** Servidor de *e-mail* para envio de mensagens. Ex.: microsiga.com.br   
**MV\_RHAUTEN:** Determina se o servidor de *e-mail* requer autenticação. Conteúdo .T. requer, .F. não requer autenticação. Conteúdo padrão: .F.

Abaixo segue exemplo de preenchimento:  
**MV\_EMCONTA**: XXXXX[@totvs.com.br](mailto:luciana.firme@totvs.com.br)   
**MV\_EMSENHA**: XXXXX (informe a senha do email)  
**MV\_RELSERV**: smtp.gmail.com:587; (informe logo em seguida porta do servidor, que no exemplo mencionado é a 587)  
**MV\_RELAUTH**: .T.                                                                     
**MV\_RELACNT**: XXXXX[@totvs.com.br](mailto:luciana.firme@totvs.com.br)  
**MV\_RELPSW**: XXXXX(informe a senha do email)  
**MV\_RELAPSW**: *sem preenchimento*  
**MV\_RELFROM**: XXXXX[@totvs.com.br](mailto:luciana.firme@totvs.com.br)   
**MV\_RELAUSR**: *sem preenchimento*  
**MV\_PORSMTP**: 587 (mesma porta informada no parâmetro **MV\_RELSERV)**  
**MV\_RELFIL**: 1  
**MV\_RELGART**: U\_LOJR600A                                                                                                                 
**MV\_RELSSL**:  .F.   
**MV\_RELSUG**: *sem preenchimento*  
**MV\_RELT**: \SPOOL\                                                                                                                                   
**MV\_RELTIME**: 120  
**MV\_RELTLS**: .T.  
**MV\_RHSERV**: *sem preenchimento*  
**MV\_RHAUTEN**: .F.  
  
Ainda no ambiente **SIGACFG** (Configurador), acesse o menu **Ambiente > E-Mail/Proxy > Configurar (CFGSETMAIL):**  
  
Verifique se as informações estão conforme exemplo abaixo, pois dependendo da configuração informada nos parâmetros acima, farão diferença nas telas a seguir:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30878875865879)  
  
[​![](https://centraldeatendimento.totvs.com/hc/article_attachments/30878875873815)​![](https://totvssuporte.zendesk.com/attachments/token/gT0mbLLNonAEsjSBrG0LBFzYq/?name=inline853547263.png)​![](https://totvssuporte.zendesk.com/attachments/token/FPh8jBpSYYHI86PLKQiD5xrij/?name=inline-320636105.png)](http://tdn.totvs.com/x/whRbB)

Concluídas as configurações, acesse a rotina de **Recibos de Pagamento** no **SIGAGPE** através do menu **Relatórios > Recibos/Cheques > Recibos de Pagamento (GPER030)**, preencha os parâmetros de acordo com necessidade e selecione uma das opções de envio por *e-mail,* sendo elas:

- ***e-Mail*** **HTML**: Onde as informações do recibo estarão descritas no corpo do *e-mail;*  
- ***e-Mail*** **PDF**: É enviado um arquivo anexo em PDF com as informações do recibo de pagamento do funcionário:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013959821)

Após a confirmação dos parâmetros será demonstrada tela de progresso e por fim uma tela de *status* de envio do *E-mail***![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500013683222)**

**IMPORTANTE:** O acesso ao Configurador é restrito **apenas** para usuários que possuem acesso ou fazem parte do grupo de **administradores** do Sistema.

Caso você utilize o **Gmail** como **servidor** de e-mail, é necessário ativar a **permissão de aplicativos menos seguros** através do link: <https://myaccount.google.com/lesssecureapps>.

Você deverá fazer login com o e-mail cadastrado para envio dos recibos de pagamento (**MV\_EMCONTA**) para habilitá-la.

![](https://totvssuporte.zendesk.com/attachments/token/r2cYd4O7oGjXlMfgPmBHKXBN8/?name=inline-1187386498.png)

**Saiba mais:**

[**RH - Recibos e Cheques**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909573-RH-Recibos-e-Cheques)
