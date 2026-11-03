---
content_hash: 2ee5fd8c03ee68b2c3e6eda09593a993af279acb14bddba3e7022f20dba71ae2
fetched_at: '2026-06-28T21:35:22.492675+00:00'
page_id: '237376532'
product: fluig
source: tdn-fluig
title: Release 12.3.2
type: documentation
url: https://tdn.totvs.com/display/fluig/Release+12.3.2
version: 6
---

Este documento contém breves descritivos acerca das implementações e correções efetuadas no pacote **12.3.2**.

## Implementações

#### fluig ESB Plugin e fluig ESB Server

**Recurso: Plugin e Motor**

**Situação:** Quando o ESB é iniciado pelo serviço do Windows, ocorre uma inconsistência na verificação de versão, não permitindo a realização do *deploy* dos diagramas do ESB.

**Solução:** Foram efetuadas alterações no retorno do arquivo que possui a versão e a data de atualização do ESB.

**Recurso: Chamadas a *Webservices* do Tipo RPC Encoded**

**Situação:** Endereços de WSDL com letras maiúsculas não eram encontrados.

**Solução:** Foi realizado um tratamento para considerar caminhos de WSDL, diferenciando maiúsculas e minúsculas.

**Recurso: Monitor**

**Situação:** Quando informada a URL completa do monitor (<http://192.168.0.127:8085/monitor/monitor/monitor.jsf>) é necessário que seja solicitado o usuário e a senha, porém ele está acessível sem segurança.

**Solução:** Foram efetuadas alterações para que seja solicitado o usuário e a senha em todas as URLs de acesso ao monitor ESB, solucionando a inconsistência de segurança.  
Lembrando que, por padrão, o acesso ao monitor ESB é realizado pelo usuário “esbAdm” e senha “adm”.  
Estas informações estão configuradas no arquivo <diretório instalação ESB>/conf/users.xml, contendo usuário e senha criptografada em MD5. É possível incluir mais de um usuário, conforme exemplo abaixo:

xml 
 
esbAdm 
b09c600fddc573f117449b3723f23d64 
 
 
esbUser1 
b09c600fddc573f117449b3723f23d64 
 
]]>

Para auxiliar na criptografia MD5 pode ser utilizado o site: <http://www.md5online.org/md5-encrypt.html>.

**Situação:** Ao acessar as opções “View” e “View Error” do monitor ESB, ocorre a inconsistência “"Error 404 Not Found"”, não sendo exibidas as informações corretamente.

**Solução:** Foram efetuadas alterações para que o monitor exiba corretamente o conteúdo das opções “View” e “View Error”.

**Recurso: FTP Sender**

**Situação:** Componente FTP Sender não funciona corretamente quando o motor ESB está em ambiente Windows e o Server FTP em outra máquina Linux.

**S****olução:** Foram efetuadas alterações para permitir que seja definida uma estrutura de pastas internas ao FTP, mesmo estando em ambientes distintos, com o ESB em Windows e o Server FTP em Linux.

**Recurso:** **Parametrização de *Web Services***

**Situação:** Ao tentar consumir o serviço do FLUIG são apresentadas mensagens de inconsistência no LOG do ESB e do FLUIG. No ESB é exibida a mensagem de tipo AnyType não reconhecido.

**Solução:** Foram efetuadas melhorias na parametrização de *Web Services*. Agora os parâmetros passados ao *Web Service* podem ser extraídos da mensagem que está sendo processada, inclusive de atributos do XML, utilizando-se a linguagem XSLT.

**Recurso: Validação de Licenças em Linux**

**Situação:** Ao iniciar o serviço do ESB configurado para utilizar TOTVS License Server, ocorre uma inconsistência e a licença não é validada.

**Solução:** Foi realizado um tratamento para ambientes em Linux, permitindo a validação correta com o TOTVS License Server.
