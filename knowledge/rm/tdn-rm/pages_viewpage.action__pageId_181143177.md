---
content_hash: 2552c2290ca720fb752d1762e6e56b78d1beb297af9a36a12fac7819968c4f19
fetched_at: '2026-06-29T00:05:57.651144+00:00'
page_id: '181143177'
product: rm
source: tdn-rm
title: Configuração para simular 3 camadas - JobServer
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=181143177
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework                       **Versão:**11.xx |
| **Processo** | **:** | JobServer |
| **Subprocesso** | **:** | Configuração para simular 3 camadas |
| **Data da publicação** | **:** | 15/12/2014 |

**SIMULANDO 3 CAMADAS EM SEU AMBIENTE**

**·    Siga os passos abaixo para configuração do jobserver em seu ambiente: Favor verificar os arquivos com extensão CONFIG da pasta:**

****c:\totvs\CorporeRM\RM.Net:****

**Configuração**

* Abra o arquivo com o bloco de notas e verifique o valor da tag abaixo:

**<**add key="JobServer3Camadas" value="false" />

* **Obs: O Valor (FALSE OU TRUE) deve ser o mesmo para todos os arquivos .CONFIG**

O valor setado como False é para instalações no modo "Local". O valor setado como TRUE é para ambientes 3 camadas.

* Verifique também os arquivos. config da PASTA DE TODOS OS APLICATIVOS:

**( Exemplo abaixo : RMFluxus.exe.config) - Altere o valor da tag para "true"**

<add key="JobServer3Camadas" value="true" />

Obs.: Caso utilize o RM Portal, proceda conforme abaixo:

Acesse a pasta Corpore.Net (C:\totvs\CorporeRM\Corpore.Net) e abra o arquivo Web.config no bloco de notas.

Edite este arquivo de modo que o valor da tag “JobServer3Camadas” seja verdadeiro (true), como segue modelo abaixo.

<!--Configurações de Remoting-->

    <add key="RemoteLoad" value="false"/>

    <add key="SelfHosted" value="false"/>

    <add key="Host" value="localhost"/>

    <add key="Port" value="8050"/>

    <add key="JobServer3Camadas" value="true" />

    <add key="ServerUrl" value="http://localhost/RM.net/"/>

Volte na pasta RM.Net e acesse o executável RM.AliasManager.exe. Neste aplicativo, na ABA SERVIÇOS, será necessário habilitar a opção de Processamento de Job e definir um valor de execuções simultâneas.

Para dividir esse processamento, poderá ser feita a mesma configuração em outras máquinas, porém com a opção de “Executar apenas Jobs Locais” Desmarcada. A vantagem é que essas máquinas não serão de uso exclusivo para execução de processos e o usuário poderá trabalhar normalmente.

* Realizadas as alterações nos arquivos .**config** , acesse : **C:\totvs\CorporeRM\RM.Net\ RM.Host.ServiceManager.exe:**

a)      Clicar no botão Desinstalar

b)      Apagar o arquivo \_Broker.dat da pasta RM.Net

c)       Clicar em instalar e esperar que o serviço esteja iniciado.

Após essas configurações, o ambiente já estará apto para executar processos, sem que seja necessário startar o Modo Server no aplicativo Delphi.

Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)
