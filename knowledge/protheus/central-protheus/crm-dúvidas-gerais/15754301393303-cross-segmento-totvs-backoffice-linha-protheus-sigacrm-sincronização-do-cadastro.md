---
article_id: 15754301393303
category: CRM - Dúvidas Gerais
content_hash: 5425de7f0de58e964d5890a28fdf13379987753fafd1989dfa01e6dd64fd3bae
fetched_at: '2026-06-28T22:40:27.637493+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Sincronização
  do Cadastro de Atividades com Exchange Server
type: support-article
updated_at: '2024-09-02T17:09:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15754301393303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGACRM-Sincroniza%C3%A7%C3%A3o-do-Cadastro-de-Atividades-com-Exchange-Server
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15949702032663) Tempo aproximado para leitura: **00:05:00 min****Dúvida:**

Sincronização do Cadastro de Atividades com Exchange Server

**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACRM - Todas as versões.  
  
**Solução:**

**1. Configuração de Envio de E-mail ( SIGACFG )**

1. Em Ambiente/ E-mail Proxy/ Configurar, informe os parâmetros necessários para o envio de relatórios e clique em Avançar.  
2. Preencha as configurações de E-mail e Proxy e clique em Avançar.  
3. Preencha as informações para a configuração do Proxy e clique em Finalizar.  
  
Configuração do SMPT:

[MP - FRAME - Configurar o SMTP para envio de relatórios por e-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025393071-MP-FRAME-Configurar-o-SMTP-para-envio-de-relat%C3%B3rios-por-e-mail)

Caso utilize servidor de E-mail Gmail, saiba que é utilizado a configuração de senhas de aplicativo: 

[How To | MP-SIGAFAT Alteração na conf. de e-mails do Protheus](https://www.youtube.com/watch?v=wGikJth4dN0)

**2. Configure os parâmetros do Exchange Server ( SIGACFG )**

* MV\_EXGAUT = 1 ( NTLM )
* MV\_EWS2010/ MV\_EWS2007 = Informe a Url do Exchange. (Exemplo: [https://servidor/ews/exchange.asmx](https://mail.totvs.com.br/ews/exchange.asmx) ).
* MV\_VEREXCH = Informe a versão do Exchange que está sendo utilizada.
* MV\_RELACNT = Inclua o e-mail com domínio user@empresa.com.br
* MV\_RELAPSW = senha do e-mail
* MV\_EMCONTA = Inclua o e-mail com domínio user@empresa.com.br
* MV\_EMSENHA = senha do e-mail
* MV\_RELAUSR = Inclua o e-mail com domínio user@empresa.com.br
* MV\_RELAUTH = .T.
* MV\_RELFROM = user@empresa.com.br (Quando é utilizado um servidor autenticado, não é permitido enviar mensagens com o campo "FROM" de outra conta)
* MV\_RELPSW = senha do e-mail
* MV\_RELSSL = .F.
* MV\_RELTLS = .T.

**3. Configurar o Usuário para integração com Exchange Server**

         
  Usuário sistema no Configurador informar o E-mail:

![a1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15754296094359)

Configurar os campos de integração na rotina Usuário de CRM- CRMA210 na aba Integração Exchange:

![a2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15754438391319)

Configurar os campos de integração na rotina Vendedor- CRMA520 na aba Integração Exchange:

![a3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15754468592407)

Na aba Outros na rotina Vendedor- CRMA520 o E-mail:

![a4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/15754468594327)

**4. Configurar SSL para comunicação ( Binário )**

Para configurar o SSL, será necessário gerar um certificado e uma chave (com senha) e adicioná-los no appserver.ini.

Sobre a geração do Certificado SSL para Exchange: A TOTVS não fornece suporte para este processo. Contate seu time de TI para providenciar este requisito.

Mais informações nos links abaixo:  
[http://tdn.totvs.com/pages/viewpage.action?pageId=6064865](https://tdn.totvs.com/pages/viewpage.action?pageId=6064865)  
[http://tdn.totvs.com/pages/viewpage.action?pageId=6065065](https://tdn.totvs.com/pages/viewpage.action?pageId=6065065)

Para gerar a chave e o certificado, é possível utilizar o openssl (download: <https://www.openssl.org/>) executando o comando: req -x509 -newkey rsa:4096 -keyout serverkey.pem -out servercert.pem

Esse comando irá gerar os arquivos cert.pem e key.pem. Será necessário substituir a chave PassPhrase pela a senha preenchida durante a geração da chave\certificado.

Configurando o certificado e senha SSL no ini do Server do Protheus:

Exemplo de configuração da seção:

[SSLCONFIGURE]  
HSM=0  
SSL2=1  
SSL3=1  
TLS1=1  
BUGS=1  
CertificateClient=C:\P12\12.1.7\ProtheusPadrao\bin\appserver\servercert.pem  
KeyClient=C:\P12\12.1.7\ProtheusPadrao\bin\appserver\serverkey.pem  
Verbose=0  
PassPhrase=hardPassword

**Atenção:**As chaves `CertificateClient` e `KeyClient` devem conter o caminho para o certificado e a chave respectivamente e a chave “PassPhrase” com a senha da chave.

**5. Sincronizar o cadastro de Atividades com Exchange Server**

1. Em Atualizações/ Vendas/ Atividades/ Atividades, clique em Outras Ações -> Sincronizar.  
2. Preencha os parâmetros conforme a sua necessidade.  
3. Clique em OK.  
4. Lembrando se a sincronização automática estiver habilitada a autenticação do usuário no Exchange Server será uma única vez.

**Teste 1 – Inclusão de Compromisso com participantes com e-mail externo**

1. Em Atualizações/ Vendas/ Atividades/ Atividades, clique em Incluir.
2. Selecione a opção Compromisso.
3. Preencher os principais campos como:
   1. Participante: adicionar os e-mails dos participantes do compromisso separados por ponto e vírgula (;). Se o e-mail do participante for @gmail, por exemplo, este participante receberá um invite em sua caixa de e-mail.
   2. Assunto
   3. Local
   4. Descrição
   5. Data / Hora.
4. Confirma o formulário
5. Verifique a sincronização da atividade com Exchange Server.
6. Acessa a Caixa de Entrada dos respectivos e-mails informados como participante. E verifique a agenda dos mesmos.
7. Faça o cancelamento do compromisso e verifique que no Protheus o mesmo foi excluído.

**Teste 2 – Inclusão de Tarefas**

1. Em Atualizações/ Vendas/ Atividades/ Atividades, clique em Incluir.
2. Selecione a opção Tarefa.
3. Preencher os principais campos como: Assunto, Descrição e Data / Hora.
4. Confirma o formulário
5. Verifique a sincronização da atividade com Exchange Server.
6. Acessa a Caixa de Entrada e verifica que a tarefa foi sincronizada.
7. Faça a exclusão da mesma pela Caixa de entrada e verifica que no Protheus a mesma foi excluída.

**Teste 3 – Envio de e-mail**

1. Em Atualizações/ Vendas/ Atividades/ Atividades, clique em Incluir.
2. Selecione a opção Email.
3. Preencher os principais campos como: Destinatário, Assunto, Corpo do E-mail
4. Acessa a Caixa de Entrada e verifica que o e-mail foi enviado.

**Observações:**

1 - Verificar se URL do Web Services do Exchange Server é HTTPS. Em caso afirmativo, a configuração do SSL é imprescindível.  
2 - Versões do Exchange Server homologadas: 2007, 2010 e 2013.  
3 - Utilizar o parâmetro lógico MV\_FATEXDS para informar se o Exchange Server está em horário de verão.

**Importante:** Para a segurança da conexão do Envio de E-mail no Protheus, foi implementado na release 12 do Protheus, a verificação em duas Etapas e a senha Aplicativo pelo Provedor de E-mail, Para o sistema validar a senha disponibilizada pelo Provedor no parâmetro, com isso realizando o envio do E-mail.

**GMAIL**

[Alterações necessárias para uso do envio de e-mails com o Gmail](https://tdn.totvs.com/pages/releaseview.action?pageId=687162208)

**OUTLOOK**

[Autenticação em duas etapas](https://support.microsoft.com/pt-br/office/autentica%C3%A7%C3%A3o-em-duas-etapas-f4ac126a-f6eb-464e-abdc-ec956e279e10)

[Gerenciar senhas de aplicativo para verificação em duas etapas](https://support.microsoft.com/pt-br/account-billing/gerenciar-senhas-de-aplicativo-para-verifica%C3%A7%C3%A3o-em-duas-etapas-d6dc8c6d-4bf7-4851-ad95-6d07799387e9)

**Para realizar a configuração, saiba mais:**

[Application Server - E-mail](https://tdn.totvs.com/display/tec/Application+Server+-+E-mail)

[Integração de Exchange com a Área de Trabalho do Representante](http://tdn.totvs.com/pages/releaseview.action?pageId=234610307)

**[Sincronização do Cadastro de Atividades com Exchange Server](https://tdn.totvs.com/pages/releaseview.action?pageId=272712174)**

**[Sincronização do Cadastro de Atividades com Exchange Online ( Office 365 ).](https://tdn.totvs.com/pages/releaseview.action?pageId=274655153)**
