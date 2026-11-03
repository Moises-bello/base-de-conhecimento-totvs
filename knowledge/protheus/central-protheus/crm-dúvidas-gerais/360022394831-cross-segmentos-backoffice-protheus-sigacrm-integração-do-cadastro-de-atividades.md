---
article_id: 360022394831
category: CRM - Dúvidas Gerais
content_hash: a06c8a018c175c34c1a123e4ce7f5e28c0bf6ed9f6db2545cd5eb37f71e70b6f
fetched_at: '2026-06-28T22:40:27.472097+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Integração do Cadastro de
  Atividades com Exchange Online (Office 365)
type: support-article
updated_at: '2024-03-21T14:20:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022394831-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Integra%C3%A7%C3%A3o-do-Cadastro-de-Atividades-com-Exchange-Online-Office-365
---

**Dúvida:**

Sincronização do Cadastro de Atividades com Exchange Online

**Ambiente:**  
Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da versão 12.  
  
**Solução:**

**1. Configure os parâmetros do Exchange Online ( SIGACFG )**

• MV\_EXGAUT = 2 ( Basic Authentication )  
• MV\_EWS2010/ MV\_EWS2007 = Informe a Url do Exchange. (Exemplo:  [https://outlook.office365.com/ews/exchange.asmx](https://outlook.office365.com/EWS/Exchange.asmx))  
• MV\_VEREXCH = 2016

**2. Configuração de Envio de Email ( SIGACFG )**

1. Em Ambiente/ E-mail Proxy/ Configurar, informe os parâmetros necessários para o envio de relatórios e clique em Avançar.

Exemplo:  
Nome do Servidor smtp: [https://outlook.office365.com](https://outlook.office365.com/)  
Conta a ser utilizada para autenticação: [email@dominio.com.br](mailto:email@dominio.com.br)  
Senha da conta: senha  
Necessita de autenticação: Sim

2. Preencha as configurações de E-mail e Proxy e clique em Avançar.

3. Preencha as informações para a configuração do Proxy e clique em Finalizar.

**3. Configurar SSL para comunição ( Binário )**

Para configurar o SSL, será necessário gerar um certificado e uma chave (com senha) e adicioná-los no appserver.ini

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

Atenção: As chaves `CertificateClient` e `KeyClient` devem conter o caminho para o certificado e a chave respectivamente e a chave “PassPhrase” com a senha da chave.

**4. Configurar o usuário do CRM para integração com Exchange Online**

No Cadastro de Usuário do CRM: CRMA210, preencha todos os campos da pasta Integração Exchange, conforme o Help de campo.

Para office 365, no campo Usuário Exc (AO3\_EXGUSR) preencher o usuário composto por @..... (ou seja, o e-mail completo)

**5. Sincronizar o cadastro de Atividades com Exchange Online**

1. Em Atualizações/ Vendas/ Atividades/ Atividades, clique em Outras Ações -> Sincronizar.  
2. Preencha os parâmetros conforme a sua necessidade.  
3. Clique em OK.  
4. Lembrando se a sincronização automática estiver habilitada a autenticação do usuário no Exchange Online será uma única vez.

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
5. Verifique a sincronização da atividade com Exchange Online.
6. Acessa a Caixa de Entrada dos respectivos e-mails informados como participante. E verifique a agenda dos mesmos.
7. Faça o cancelamento do compromisso e verifique que no Protheus o mesmo foi excluído.

**Teste 2 – Inclusão de Tarefas**

1. Em Atualizações/ Vendas/ Atividades/ Atividades, clique em Incluir.
2. Selecione a opção Tarefa.
3. Preencher os principais campos como: Assunto, Descrição e Data / Hora.
4. Confirma o formulário
5. Verifique a sincronização da atividade com Exchange Online.
6. Acessa a Caixa de Entrada e verifica que a tarefa foi sincronizada.
7. Faça a exclusão da mesma pela Caixa de entrada e verifica que no Protheus a mesma foi excluída.

**Teste 3 – Envio de e-mail**

1. Em Atualizações/ Vendas/ Atividades/ Atividades, clique em Incluir.
2. Selecione a opção Email.
3. Preencher os principais campos como: Destinatário, Assunto, Corpo do E-mail
4. Acessa a Caixa de Entrada e verifica que o e-mail foi enviado.

**Observação**:

* Verificar se URL do Web Services do Exchange Online é HTTPS. Em caso afirmativo, a configuração do SSL é imprescindível.

**Saiba mais:**

[Sincronização do Cadastro de Atividades com Exchange Online ( Office 365 ).](https://tdn.totvs.com/pages/releaseview.action?pageId=274655153)

[Sincronização do Cadastro de Atividades com Exchange Server](https://tdn.totvs.com/pages/releaseview.action?pageId=272712174)
