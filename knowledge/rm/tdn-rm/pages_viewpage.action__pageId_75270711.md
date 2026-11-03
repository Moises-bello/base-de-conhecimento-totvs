---
content_hash: 00e015039c634cba63f3fdf15baa4efb43d0b6c73e161be920537025af32be11
fetched_at: '2026-06-29T00:11:33.138695+00:00'
page_id: '75270711'
product: rm
source: tdn-rm
title: Serviço de host não sobe ou erro de Broker
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=75270711
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.5x, 11.8X |
| **Processo** | **:** | Serviço de Host |
| **Subprocesso** | **:** | *Verificação / Configuração do ambiente 2 ou 3 camadas* |
| **Data da publicação** | **:** | 20/09/2013 |

Sempre que ocorrer **erro de Broker,** serviço de **queda do serviço de host** sem nenhum motivo aparente, **serviço de host não sobe**, será válido algumas verificações conforme descrito abaixo:

Antes de qualquer coisa, o teste mais rápido a ser feito, é desinstalar o serviço de host (C:\totvs\CorporeRM\RM.Net RM.Host.ServiceManager.exe), deletar o arquivo \_Broker.Dat e instalar o serviço novamente.

Porém, este erro pode ser de serviço de host não iniciado ou não localizado.

- NÃO INICIADO

Os motivos deste erro podem ser:

- Antivírus bloqueando

- Firewall

- Outro programa utilizando a porta 80:50

- UAC habilitado do Server 2008, Vista e Sevem

Outras opções são:

Na pasta c:\corporerm\rm.net executar o arquivo RM.Host.ServiceManager.exe

Nesta tela você deverá desinstalar o serviço e instalar novamente.

Nesta etapa terá 3 opções  de instalação:  NetworkService, Local System ou Informando usuário e senha específicos (senha do administrador de Rede)

Caso o serviço não seja iniciado em uma das opções, testar as demais citadas.

Deverá ser verificado se na pasta RM.NET (C:\CorporeRM\RM.Net), os arquivos RM.Host.Service.exe.config e RM.Host.exe.config, estão com mesmo endereço onde está localizado os arquivos Exe RM.Host.ServiceManager.exe e RM.Host.exe.

Exemplo abaixo:

<?xml version="1.0" encoding="utf-8"?>

<configuration>

   <appSettings>

      <add key="port" value="8050" />

      <add key="actionsPath" value="C:\CorporeRM\RM.Net;C:\CorporeRM\Corpore.Net\bin" /> \*\*\* este endereço tem que estar igual a pasta física onde se encontra o exe do serviço\*\*

      <add key="JobServer3Camadas" value="true"/>

      <add key="logPath" value="C:\CorporeRM\" />

   </appSettings>

   <system.runtime.remoting>

      <customErrors mode="off" />

   </system.runtime.remoting>

</configuration

Se mesmo após todas as tentativas acima o serviço ainda não estiver iniciando, verificar antivírus, Firewall, UAC  e porta 80:50.

OBS: se estiver em 3 camadas, verificar o servidor onde está sendo executado o serviço.

Mencionando a opção de 3camdas verificar também:

- NÃO LOCALIZADO.

Se estiver tentando abrir um aplicativo, e o mesmo estiver em 3camadas, deverá ser observado se o arquivo .config (ex: RMFluxus.exe.config) está buscando informação do servidor correto.

<?xml version="1.0"?>

<configuration>

                <appSettings>

                               <add key="CommunicationStyle" value="WCF" />

                               <add key="JobServer3Camadas" value="true" />

                        <add key="Port" value="8050" />

                        <add key="Host" value="RM0005438" /> \*\* nome do servidor.

                               <add key="EnableCompression" value="true" />

                </appSettings>

                <runtime>

                               <NetFx40\_LegacySecurityPolicy enabled="true" />

                </runtime>

                <startup>

                               <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0" />

                </startup>

</configuration>

Verificar ainda, se a tag deste arquivo estiver true e no servidor de aplicação no arquivo config do serviço de host (RM.Host.Service.exe.config) estiver com a tag 3camadas false, ou vise e versa, o erro também ocorrerá.

|  |  |
| --- | --- |
|  | **Para maiores informações:**     **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha); |
