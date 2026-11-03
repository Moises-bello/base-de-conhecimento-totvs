---
article_id: 360022391971
category: CRM - Dúvidas Gerais
content_hash: 300da8dc7fabc167855fc735055a0eeefce03faa4b3b4e1678ed0f42f2c2e9d1
fetched_at: '2026-06-28T22:40:27.702900+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Integração do Cadastro de
  Atividades com Exchange Server
type: support-article
updated_at: '2024-04-25T11:54:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022391971-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Integra%C3%A7%C3%A3o-do-Cadastro-de-Atividades-com-Exchange-Server
---

**Dúvida**

Sincronização do Cadastro de Atividades com Exchange Server  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12

**Solução**

**1. Configure os parâmetros do Exchange Server ( SIGACFG )**

• MV\_EXGAUT = 1 ( NTLM )  
• MV\_EWS2010/ MV\_EWS2007 = Informe a Url do Exchange. (Exemplo: [https://servidor/ews/exchange.asmx](https://mail.totvs.com.br/ews/exchange.asmx) )  
• MV\_VEREXCH = Informe a versão do Exchange que está sendo utilizada.

**2. Configuração de Envio de Email ( SIGACFG )**

**2.1.** Em Ambiente/ E-mail Proxy/ Configurar, informe os parâmetros necessários para o envio de relatórios e clique em Avançar.  
**2.2.** Preencha as configurações de E-mail e Proxy e clique em Avançar.  
**2.3.** Preencha as informações para a configuração do Proxy e clique em Finalizar.

**3. Configurar SSL para comunicação ( Binário )**

Para configurar o SSL, será necessário gerar um certificado e uma chave (com senha) e adicioná-los no appserver.ini.

Sobre a geração do Certificado SSL para Exchange: A TOTVS não fornece suporte para este processo. Contate seu time de TI para providenciar este requisito.

Mais informações nos links abaixo:  
<http://tdn.totvs.com/pages/viewpage.action?pageId=6064865>  
<http://tdn.totvs.com/pages/viewpage.action?pageId=6065065>

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

**4. Configurar o usuário do CRM para integração com Exchange Server**

No Cadastro de Usuário do CRM, preencha todos os campos da pasta Integração Exchange, conforme o Help de campo.

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

**Observação:**

* Verificar se URL do Web Services do Exchange Server é HTTPS. Em caso afirmativo, a configuração do SSL é imprescindível.
* Versões do Exchange Server homologadas: **2007**, **2010** e **2013**.
* Utilizar o parametro lógico **MV\_FATEXDS** para informar se o Exchange Server está em horário de verão.
