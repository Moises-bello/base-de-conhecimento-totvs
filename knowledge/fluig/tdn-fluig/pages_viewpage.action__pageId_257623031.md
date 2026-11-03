---
content_hash: 83f1c0942bafc6a8c4c6c7857e0b220a45faa5cfdc16b9f78bb8ecebc0ddfa9c
fetched_at: '2026-06-28T21:35:23.575173+00:00'
page_id: '257623031'
product: fluig
source: tdn-fluig
title: Parâmetros de configuração da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257623031
version: 37
---

Fique atento!

Esta página é válida a partir da atualização **Voyager (2.0)** do TOTVS Fluig.

Se você utiliza uma atualização anterior, acesse Quais são os parâmetros de configuração da plataforma da atualização **1.6 até 1.8.2**.

Índice

# Parâmetros de configuração

---

Veja a seguir os parâmetros disponíveis para configuração no arquivo **configuration.properties** disponível em [diretório\_instalação]\repository\wcmdir\config.

|  |  |  |  |
| --- | --- | --- | --- |
| **Parâmetro** | **Parâmetro API** | **Descrição** | **Valores aceitos** |
| webdesk/FTPPort | FTP\_PORT | Alterar a porta FTP para a publicação de documentos via FTP. A porta padrão é 21. | Inteiro de 1 à 65535. |
| webdesk/FTPPrivateFolderPort | FTP\_PRIVATEFOLDER\_PORT | Alterar a porta FTP para a pasta particular. A porta padrão é 25. | Inteiro de 1 à 65535. |
| webdesk/FTPPortRange | FTP\_PORT\_RANGE | Conjunto de portas usadas para conexão de FTP passivo, caso não seja informado é usada uma porta aleatória. | Conjunto de portas, e.g: 2000-3000,3005. |
| ``` webdesk/FTPPrivateFolderRange ``` | FTP\_PRIVATEFOLDER\_PORT\_RANGE | Conjunto de portas usadas para conexão de FTP passivo das pastas privadas, caso não seja informado é usada uma porta aleatória. | Conjunto de portas, e.g: 2000-3000,3005. |
| webdesk/LSHost | LS\_HOST | Alterar o endereço do servidor de licenças (*License Server*). | IP ou *HOSTNAME*. |
| webdesk/LSPort | LS\_PORT | Alterar a porta de comunicação com o servidor de licenças (*License Server*). | Inteiro de 1 à 65535. |
| webdesk/OOoDir | OO\_DIRECTORY | Alterar o diretório de instalação do *OpenOffice* (para a conversão dos documentos em PDF). | Caminho para instalação do *OpenOffice.* |
| webdesk/OOoPort | OO\_PORT | Alterar as portas disponíveis para o *OpenOffice*. Para informar mais de uma porta deve-se utilizar o separador “,” (vírgula). | Inteiro de 1 à 65535. |
| fluig/server.url | SERVER\_URL | Alterar a URL de acesso à plataforma. O padrão inicial é http://[endereco\_IP]:8080. | IP ou *HOSTNAME.* |
| totvs/solrHome | SOLR\_HOME | Alterar o diretório em que são armazenadas as configurações do Solr. | Caminho para configuração do Solr. |
| totvs/solrURL | SOLR\_URL | Alterar a URL do Solr. Por padrão a URL é [servidor\_fluig]:8080/solr. | IP ou *HOSTNAME.* |
| totvs/solrCloud | SOLR\_CLOUD | Ative para configurar o Solr com servidor em *Cluster*. | *true/false* |
| totvs/solrRemote | SOLR\_REMOTE | Ative para configurar o Solr em servidor separado remoto. | *true/false* |
| wcm/cacheServerAddress | CACHE\_SERVER\_ADRESS | Alterar [protocolo]:[endereco]:[porta] do servidor de cache de permissões. | LOCAL\_MAP, memcached:[host]:[port], redis:[host]:[port], redisc:[host]:[port] |
| node.chat.url | NODE\_CHAT\_URL | Alterar a URL utilizada para comunicar as notificações e publicações da plataforma em tempo real. Use o mesmo endereço (*host*) da plataforma, para evitar problemas de *Cross-Domain.* | IP ou *HOSTNAME*, com a porta. |
| node.realtime.url | NODE\_REALTIME\_URL | Alterar a URL interna do servidor de comunicação com o node.js. Use o mesmo endereço (*host*) da plataforma, para evitar problemas de *Cross-Domain.* | IP ou HOSTNAME, com a porta. |
| fluig.schedule.server.host | SCHEDULE\_SERVER\_HOST | Altera a URL do servidor de agendamentos. | IP ou HOSTNAME. |
| fluig.schedule.server.port | SCHEDULE\_SERVER\_PORT | Alterar a porta do servidor de agendamentos. | Inteiro de 1 à 65535. |
| analytics.resources.folder | ANALYTICS\_RESOURCES\_FOLDER | Alterar a pasta de recursos do Fluig Analytics. | Caminho onde fica os arquivos para envio do Analytics. |
| fluig/mail.defaultSender | MAIL\_DEFAULT\_SENDER | Habilitar o envio de *e-mail* utilizando o *e-mail* cadastrado no parâmetro mail.from. | *true/false* |
| fluig/mail.personal | MAIL\_PERSONAL | Definir um nome junto ao *e-mail* de origem, para identificar a empresa por exemplo. Tipo: NOME\_DA\_EMPRESA [adm@fluig.com.](mailto:adm@fluig.com) |  |
| fluig/mail.allNotification | MAIL\_ALL\_NOTIFICATION | Caso definido como 'true' faz com que todos os e-mails da plataforma sejam enviados a partir do *e-mail* informado no campo mail.from e não apenas os *e-mails* de sistema. | *true/false* |
| fluig/mail.from | MAIL\_FROM | Alterar o endereço de *e-mail* utilizado para envio dos *e-mails* de sistema. |  |
| webdesk/OOoEnabled **\*** | OO\_ENABLED | Habilitar/Desabilitar o serviço do *OpenOffice*. | *true/false* |
| webdesk/FTPEnabled **\*** | FTP\_ENABLED | Permite habilitar ou desabilitar o servidor FTP. | *true/false* |
| webdesk/FTPExternalAddress **\*** | FTP\_EXTERNAL\_ADDRESS | Endereço externo do servidor de FTP, necessário para expor o FTP em modo passivo se estiver usando NAT. | IP ou *HOSTNAME* do servidor externo. |
| FDN\_emailSmtpServer **\*** | SMTP\_SERVER | Alterar o *HOSTNAME* do servidor de SMTP. | IP ou *HOSTNAME.* |
| FDN\_emailSmtpPort **\*** | SMTP\_PORT | Alterar a porta SMTP para o envio de *e-mails*. A porta padrão é 25. | Inteiro de 1 à 65535. |
| FDN\_emailSecurity **\*** | MAIL\_SECURITY | Ativar/Desativar o uso de TLS na conexão SMTP. | *true/false* |
| FDN\_emailAuthentication **\*** | MAIL\_AUTHENTICATION | Ativar/Desativar autenticação no envio de *e-mail.* | *true/false* |
| FDN\_emailUser **\*** | MAIL\_USER | Login do usuário utilizado na autenticação do servidor de *e-mail.* |  |
| FDN\_emailPasswd **\*** | MAIL\_PASSWORD | Senha utilizada na autenticação do servidor de *e-mail*. |  |
| FDN\_emailSecurity **\*\*** | MAIL\_SECURITY | Protocolo de segurança utilizado na conexão SMTP. | none/tls/ssl (os valores devem ser minúsculo). |

**\*** → Parâmetro existente a partir da atualização **1.6.1**.

**\*\*** → Parâmetro existente a partir da atualização **1.6.2**.

# Configuração do JMS

---

Para obter um melhor desempenho do servidor de aplicação utilizado pela plataforma, recomenda-se a alteração do parâmetro relacionado ao JMS para não persistir as mensagens em disco.

Importante!

A alteração deste parâmetro é **opcional**. Antes de alterá-lo, não esqueça de criar um ***backup*** do arquivo **standalone.xml**.

No arquivo **standalone.xml**, armazenado na pasta [diretório\_instalação]\appserver\standalone\configuration, altere:

Eclipsestandalone.xml]]>
