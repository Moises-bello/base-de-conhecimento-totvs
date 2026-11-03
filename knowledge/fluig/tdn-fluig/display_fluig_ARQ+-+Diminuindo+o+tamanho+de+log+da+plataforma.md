---
content_hash: 94821d8bc2f6af961cad1634fde53837e7d6f779c769c03ab3b7495e0371afe8
fetched_at: '2026-06-28T21:35:22.251568+00:00'
page_id: '235329215'
product: fluig
source: tdn-fluig
title: ARQ - Diminuindo o tamanho de log da plataforma
type: documentation
url: https://tdn.totvs.com/display/fluig/ARQ+-+Diminuindo+o+tamanho+de+log+da+plataforma
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.5.7, 1.6, 2.0

**Ambiente:** Linux ou Windows

# Ocorrência

O log da plataforma está ocupando muito espaço em disco.

# Causa

A configuração padrão do log da plataforma está definida como "INFO", fazendo que sejam registradas informações de qualquer ação realizada pelos usuários. Com isso o log acaba ficando com um tamanho considerável quando a plataforma possui uma grande utilização.

# Solução

falseVersão1A partir da 2.0

* Pare o serviço do Fluig.

* Faça um *backup* do arquivo de configuração: **[diretório\_instalação]\appserver\standalone\configuration\standalone.xml** em um diretório de sua preferência.

* Abra o arquivo [diretório\_instalação]\appserver\standalone\configuration\standalone.xml e efetue as configurações abaixo:
* + Procure por "<console-handler name="CONSOLE">" e altere "<level name="INFO"/>" para "<level name="WARN"/>"
  + Procure por "<root-logger>" e altere "<level name="INFO"/>" para <level name="WARN"/>
  + Procure a tag logger cuja propriedade "category" seja igual a "com.totvs.technology.foundation.common.Chrono", e altere o "<level name="INFO"/>" para "<level name="DEBUG"/>"
  + Acima da tag "<root-logger>", adicione as tags abaixo:

    xml






    ]]>
* Salve as alterações e inicie novamente o serviço do Fluig.

Hey, cuidado!

Após salvar as alterações, é necessário verificar se a estrutura do XML está ok. Para isso, é possível abrir o standalone.xml no navegador. Caso a estrutura do arquivo XML não esteja ok, o navegador mostrará uma mensagem e a linha do arquivo que está com inconsistência.

Após realizar as configurações acima, somente as mensagens de erro ou advertência de eventos da plataforma (documentos, processos, social, etc) mensagens de *deploy* de componentes do WCM serão exibidas. Caso você possua componentes que registrem informações no *log*, será necessário criar um novo "<logger>" no seu arquivo de configuração standalone.xml.

21.6 até 1.8.2

* Pare o serviço do fluig.

* Faça um backup do arquivo de configuração: **[diretório\_instalação]\appserver\domain\configuration\domain.xml** em um diretório de sua preferência.

* Abra o arquivo [diretório\_instalação]\appserver\domain\configuration\domain.xml e efetue as configurações abaixo:
  + Procure por "<console-handler name="CONSOLE">" e altere "<level name="INFO"/>" para "<level name="WARN"/>"
  + Procure por "<root-logger>" e altere "<level name="INFO"/>" para <level name="WARN"/>
  + Procure a tag logger cuja propriedade "category" seja igual a "com.totvs.technology.foundation.common.Chrono", e altere o "<level name="INFO"/>" para "<level name="DEBUG"/>"
  + Acima da tag "<root-logger>", adicione as tags abaixo:

    xml






    ]]>

* Salve as alterações e inicie novamente o serviço do fluig.

Hey, cuidado

Após salvar as alterações, é necessário verificar se a estrutura do XML está ok. Para isso, é possível abrir o domain.xml no navegador. Caso a estrutura do arquivo XML não esteja ok, o navegador mostrará uma mensagem e a linha do arquivo que está com problema.

Após realizar as configurações acima, somente as mensagens de erro ou advertência de eventos da plataforma (documentos, processos, social, etc) mensagens de deploy de componentes do WCM serão exibidas. Caso você possua componentes que registrem informações no log, será necessário criar um novo "<logger>" no seu arquivo de configuração domain.xml.

21.5.7 a 1.5.13

* Pare o serviço do Fluig.

* Faça um backup do arquivo de configuração **[diretório\_instalação]\jboss\standalone\configuration\standalone.xml** em um diretório de sua preferência.

* Abra o arquivo **[diretório\_instalação]\jboss\standalone\configuration\standalone.xml** e efetue as configurações abaixo:
* + Procure por "<console-handler name="CONSOLE">" e altere "<level name="INFO"/>" para "<level name="WARN"/>"
  + Procure por "<root-logger>" e altere "<level name="INFO"/>" para <level name="WARN"/>
  + Procure a tag logger cuja propriedade "category" seja igual a "com.totvs.technology.foundation.common.Chrono", e altere o "<level name="INFO"/>" para "<level name="DEBUG"/>"
  + Acima da tag "<root-logger>", adicione as tags abaixo:

    xml






    ]]>
* Salve as alterações e inicie novamente o serviço do Fluig.

Hey, cuidado

Após salvar as alterações, é necessário verificar se a estrutura do XML está ok. Para isso, é possível abrir o standalone.xml no navegador. Caso a estrutura do arquivo XML não esteja ok, o navegador mostrará uma mensagem e a linha do arquivo que está com problema.

Após realizar as configurações acima, somente as mensagens de erro ou advertência de eventos da plataforma (documentos, processos, social, etc) mensagens de deploy de componentes do WCM serão exibidas. Caso você possua componentes que registrem informações no log, será necessário criar um novo "<logger>" no seu arquivo de configuração standalone.xml.
