---
content_hash: 41a68151f367681e76a4238a256741e6bd6d7fba714f687148295996e3b957b3
fetched_at: '2026-06-29T00:11:05.909029+00:00'
page_id: '63275100'
product: rm
source: tdn-rm
title: Habilitar Tag Tracefile
type: documentation
url: https://tdn.totvs.com/display/LRM/Habilitar+Tag+Tracefile
version: 7
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.XX |
| **Processo** | **:** | Host |
| **Subprocesso** | **:** | Tag Tracefile |
| **Data da publicação** | **:** | 21/01/2015 |

Com a finalidade de gerenciarmos o processo de execução do RM Host necessitamos habilitar a tag "tracefile" nos arquivos do RM Host.

Para  habilitar o tracefile nos Servidores que executam processos, siga as orientações abaixo:

A tag é:

**<add key ="tracefile" value="true"/>**

**1.** **Acesse** **o diretório** **"C:\totvs\CorporeRM\RM.Net".**  
 **2.** **Edite** **os** **arquivos** **"RM.Host.exe.config"** **e "RM.Host.Service.exe.config"** **utilizando** **o bloco** **de** **notas.**  
 **3.** **Inclua** **no** **contexto** **do** **arquivo** **a** **tag** **"****<add** **key="tracefile"** **value="true"** **/>****".****Abaixo** **segue** **exemplo** **do contexto** **original** **e** **alterado.****4.** **Reinicie** **o serviço** **do** **RM** **Host** **para** **que** **esta** **alteração** **seja** **computada.**

Após habilitar a tag, assim que ocorrer a inconsistência, localize o arquivo na pasta Log e envie-nos uma cópia para análise via chamado.

Após enviar-nos o arquivo, pode-se apagar essa tag dos arquivos config para não gerar perda de performance em seu ambiente.

Após isso, o log irá para o caminho C:\totvs\CorporeRM\RM.Net\Processos\Logs

O caminho é:

C:\totvs\CorporeRM\RM.Net\Processos\Logs\Broker

|  |  |
| --- | --- |
| **ANTES** **(Contexto** **Original)** | **DEPOIS** **(Depois** **da** **alteração)** |
| <?xml version="1.0"?>   <configuration>   <appSettings>   <add key="JobServer3Camadas" value="false" />   <add key="Port" value="8050" />   <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\B in"   />   <add key="EnableCompression" value="true" />   </appSettings>   <runtime>   <NetFx40\_LegacySecurityPolicy enabled="true" />   </runtime>   <system.runtime.remoting>   <customErrors mode="Off" />   </system.runtime.remoting>   <startup>   <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0" />   </startup>   </configuration> | <?xml version="1.0"?>   <configuration>   <appSettings>   <add key="JobServer3Camadas" value="false" />   <add key="Port" value="8050" />   <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\B in"   />   <add key="EnableCompression" value="true" />   **<add** **key="tracefile"** **value="true"** **/>**   </appSettings>   <runtime>   <NetFx40\_LegacySecurityPolicy enabled="true" />   </runtime>   <system.runtime.remoting>   <customErrors mode="Off" />   </system.runtime.remoting>   <startup>   <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0" />   </startup>   </configuration> |

Importante

A partir da versão 12.1.24, o arquivo de Log será limitado ao tamanho de 500MB. Serão geradas 5 cópias a medida que os arquivos atingirem o tamanho máximo.

O conteúdo do arquivo começa a ser sobrescrito após a quinta cópia.

Ex.:

RMSBroker-Host-Port\_8915-636869642632303892.txt

RMSBroker-Host-Port\_8915-636869642632303892.txt1

RMSBroker-Host-Port\_8915-636869642632303892.txt2

RMSBroker-Host-Port\_8915-636869642632303892.txt3

RMSBroker-Host-Port\_8915-636869642632303892.txt4

RMSBroker-Host-Port\_8915-636869642632303892.txt5
