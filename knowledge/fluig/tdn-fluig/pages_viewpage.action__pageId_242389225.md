---
content_hash: 9ef3cb0f47704aac1faa5051aa65f07d054e088df7a0654ab803ef34dc5c137a
fetched_at: '2026-06-28T21:35:22.909083+00:00'
page_id: '242389225'
product: fluig
source: tdn-fluig
title: Configurações sugeridas em ambientes Linux
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242389225
version: 26
---

# Índice

4true.\*ndicenone

# Introdução

---

Nesta página são listadas configurações do sistema operacional que podem afetar a experiência de uso da plataforma. Os comandos abaixo são compatíveis com distribuições baseadas no Red Hat Enterprise Linux.

Importante!

Por questões de segurança orientamos não expor sua plataforma diretamente à internet. Para isso, será necessário [criar uma rede DMZ](http://tdn.totvs.com/x/MZIbCQ) juntamente com o [protocolo HTTPS](http://tdn.totvs.com/x/vdMgFQ).

# Pré requisitos

---

* Conhecimento em Linux.

# Configuração do host local

---

Em alguns casos, de acordo com a configuração padrão da distribuição ou a instalação realizada, o servidor pode não resolver o nome do próprio *host* corretamente. Para evitar problemas, inclua o *hostname* do servidor no arquivo **/etc/hosts** apontando para o endereço IP local do servidor.

text/etc/hosts

# Limite de arquivos abertos

---

O limite padrão de algumas distribuições Linux é de 1024 arquivos abertos. Porém, a plataforma pode ultrapassar com certa facilidade esse limite devido ao processamento paralelo realizado durante o uso do servidor de aplicação.

Os arquivos abertos são a quantidade de descritores para um recurso alocado para um processo. Os recursos alocados podem ser arquivos no sistema operacional ou outros recursos como, por exemplo, conexões de rede.

No caso da plataforma, temos os arquivos temporários, conexões aos clientes que fizeram a requisição (navegador), conexões de rede para os serviços dos quais depende (banco de dados, LDAP, consultas a serviços externos), arquivos do volume e outros recurso sob controle da JVM, como arquivos JAR carregados no *classpath* e utilizado nos *classloaders*.

Esse número não é limitado e pode variar, por isso você deve ajustar o limite máximo se estiver passando do valor configurado atualmente.

Para aumentar o limite de arquivos execute o comando abaixo:

bash> /etc/sysctl.conf
sysctl -p]]>

Mais informações: [RedHat](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/5/html/Tuning_and_Optimizing_Red_Hat_Enterprise_Linux_for_Oracle_9i_and_10g_Databases/chap-Oracle_9i_and_10g_Tuning_Guide-Setting_File_Handles.html).

## Sistemas de Arquivos

---

Recomendamos o uso do **sistema de arquivos Ext4**, pois ele não tem um limite de subdiretórios imediatos dentro de um único diretório.

# Ajuste de processos e arquivos abertos para Fluig Indexer (Solr)

---

A partir da atualização 1.7.0, a plataforma passa a funcionar sobre a versão embarcada [**openJDK 11**](https://adoptopenjdk.net/). Por este motivo as mensagens de alerta, abaixo citadas, referentes ao serviço Fluig Indexer (SOLR) durante a inicialização do Fluig, podem ser exibidas.

bashMidnightSolr warnings

Trata-se de variáveis de ambiente Linux utilizadas para definir um limite de arquivos aberto e um número máximo de processos rodando.

O valores default no Linux para estas variáveis não são os ideais para alta performance do Fluig Indexer (Solr), por isso são sugeridos os valores desejáveis nestas mensagens.

Para realizar essa configuração, é necessário editar o arquivo /etc/security/limits.conf, e ao final dele inserir os seguintes valores:

bashMidnight/etc/security/limits.conf

Após a configuração e o reinício do servidor a mensagem não será mais exibida no log da plataforma.

# Codificação de caracteres do sistema

---

Para evitar problemas no armazenamento de formulários por conta da codificação de caracteres do sistema, certifique-se de que a variável LC\_ALL está configurada. Isso pode ser feito inserindo a variável LC\_ALL na variáveis do usuário.

Inclua no *script* de inicialização mais adequado (.bashrc, .bash\_profile, /etc/environment, etc...) a linha abaixo:

bash

# Desabilitar SELinux

---

O SELinux é uma ferramenta de segurança desenvolvida pela NSA para proteger informações do governo americano e é ativada por padrão em algumas distribuições. Em contrapartida à segurança oferecida, o nível de detalhe para configuração do SELinux é muito grande.

Por conta disso, em ambientes onde não há um administrador com experiência na ferramenta, é sugerida a configuração no modo *Permissive*, através do procedimento abaixo:

* Edite o arquivo /etc/selinux/config;

* Na linha que declara o valor SELINUX, altere para SELINUX=permissive;

* Reinicie o sistema operacional.

Mais informações: [RedHat](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Security-Enhanced_Linux/sect-Security-Enhanced_Linux-Working_with_SELinux-Changing_SELinux_Modes.html#sect-Security-Enhanced_Linux-Enabling_and_Disabling_SELinux-Permissive_Mode)

# Configurações MySQL

---

Para maiores informações sobre como configurar o banco de dados MySQL em um ambiente Linux, acesse [Configuração do banco de dados MySQL.](http://tdn.totvs.com/x/qAVbDw)

# Usuário para inicialização do serviço do Fluig

---

A instalação do Fluig deve ser realizado com o usuário root. Porém, deve ser utilizado um usuário comum para inicialização do serviço do Fluig. Acesse  para mais detalhes.
