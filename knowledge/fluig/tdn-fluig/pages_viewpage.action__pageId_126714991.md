---
content_hash: 195677891fb40c3d822f932e6aad30325ef0607f43b188703fbc348b249bcea6
fetched_at: '2026-06-28T21:35:17.729273+00:00'
page_id: '126714991'
product: fluig
source: tdn-fluig
title: Criando um aplicativo para enviar notificações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=126714991
version: 34
---

# Índice

true.\*ndicenone

# Objetivo

---

No TOTVS Fluig Plataforma é possível criar novas formas de envio de notificações para os usuários. Isto pode ser feito através de aplicativos que podem ser instalados no Fluig Plataforma. A partir daí o sistema utilizará o aplicativo para enviar notificações. Este guia visa orientar e mostrar passo-a-passo como criar, instalar e utilizar um aplicativo de envio de notificações no Fluig Plataforma.

# Projeto de exemplo

---

Para facilitar o entendimento e desenvolvimento de aplicativos, foi gerado um projeto de exemplo. Neste projeto, foi implementado um aplicativo que mostra no LOG a mensagem recebida. Para testá-lo, basta seguir os passos abaixo:

1. Baixar o projeto:  (projeto "alert-sender-sample").
2. Compilar o projeto (é um projeto padrão maven, para compilar, executar "mvn clean install" na raíz do projeto)
3. Fazer *deploy*do arquivo "/alert-sender-sample-server/target/alert-sender-sample-server.ear" em um servidor com o Fluig instalado
4. Acessar a plataforma Fluig e gerar eventos que enviem notificações (ex. apoiar um post).  
   Deverá aparecer no LOG do Fluig os dados do alerta.

Este projeto de exemplo pode servir de base para implementação de aplicativos reais de envio de notificações.

# Cadastro de aplicativos no Fluig Plataforma através da API de Notificações

---

Para que um aplicativo possa ser utilizado pelo TOTVS Fluig Plataforma para enviar notificações, este deve ser cadastrado na **Central de Notificações** do sistema. Para isto, é necessário postar uma mensagem em uma fila JMS. Abaixo um exemplo de código que realiza esta chamada, que pode ser encontrado em **alert-sender-sample/impl/src/main/java/com/fluig/StartupLoader.java**:

java values = new HashMap();
// Código do aplicativo.
values.put("applicationKey", "alert.app.sender.sample");
// Chave da descrição do aplicativo.
values.put("descriptionKey",
"alert.app.sender.sample.description");
// ID do tenante.
values.put("tenantId", TENANT\_ID);
ObjectMessage msg = session.createObjectMessage();
msg.setObject(values);
msg.setStringProperty("action", "registerAlertAppSender");
sender.send(msg);
log.info("Inicialização do aplicativo OK");
} finally {
if (sender != null) {
sender.close();
}
if (session != null) {
session.close();
}
if (connection != null) {
connection.close();
}
}
} catch (NamingException ex) {
log.error("Nao foi possivel registrar o serviço de notificação via whatsapp");
ex.printStackTrace();
} catch (JMSException ex) {
log.error("Nao foi possivel registrar o serviço de notificação via whatsapp");
ex.printStackTrace();
}
}
}]]>

Os parâmetros necessários são:

1. **applicationKey:** É uma string que será o identificador único para o aplicativo. Através desta string a Central de Notificações fará todo o gerenciamento do aplicativo.
2. **descriptionKey:** É a descrição do aplicativo. Pode ser um texto plano ou uma chave para tradução (ex: app.my.application). Para que seja feita a tradução, a chave deve estar previamente cadastrada no módulo I18n, no bundle "foundation\_alert". Caso seja inserido um texto plano, este será exibido sem tradução.
3. **tenantId:** O id do tenant onde o aplicativo será instalado.

Uma boa prática é fazer o cadastro do aplicativo no momento do *deploy* no servidor ou no momento da criação de um novo tenant. O projeto de exemplo já contém código com este comportamento.

# Configurações de envio de notificações por usuário

---

Quando um novo aplicativo for instalado na Central de Notificações, todos os usuários do tenant poderão configurar se desejam ou não receber notificações através do aplicativo. Isto pode ser feito na tela de configurações. Por padrão, ao instalar um novo aplicativo, todos os usuários do tenant passarão a receber notificações através daquele aplicativo. Abaixo o exemplo da tela de configurações depois de instalado o projeto de exemplo.

# Enviando notificação através do aplicativo

---

Para que a Central de Notificação do TOTVS Fluig Plataforma invoque o aplicativo para enviar notificações, o aplicativo deve obrigatoriamente criar um MDB que ouve a fila registrada. Abaixo temos um exemplo simples de MDB:

java) obj);
if (log.isDebugEnabled()) {
log.debug("AlertSenderSampleQueue.onMessage - FIM");
}
} catch (final JMSException ex) {
log.error(ex.getMessage(), ex);
}
}
}
}
]]>

Quando o usuário receber um alerta, a Central de Notificações vai validar se aquele usuário está configurado para receber notificações por este aplicativo. Caso esteja, a Central postará uma mensagem na fila cadastrada para o aplicativo.

# Desabilitando aplicativos de envio de Notificações

---

É possível desabilitar qualquer aplicativo de envio, exceto a própria Central de Notificações da plataforma Fluig. Atualmente este serviço está disponível na [API Pública](http://api.fluig.com/) da plataforma Fluig. Uma vez desabilitado, o sistema não invocará mais o aplicativo para envio de notificações, e também não o exibirá mais na tela de configurações.
