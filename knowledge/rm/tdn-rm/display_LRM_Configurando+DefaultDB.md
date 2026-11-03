---
content_hash: 70835904da5ad897b68cb039b442b16f6b99fc44d0a79ae0b56b248029371a0c
fetched_at: '2026-06-29T00:05:55.677428+00:00'
page_id: '145360049'
product: rm
source: tdn-rm
title: Configurando DefaultDB
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurando+DefaultDB
version: 11
---

# Configurando DefaultDB

Para inclusão da tag DefaultDB acesse a máquina ou servidor que está executando o seu RM Host.  
 Vá ao diretório **C:\totvs\CorporeRM\RM.Net** e edite os arquivos **RM.Host.exe.config** e **RM.Host.Service.exe.config**.

Inclua a tag **<add key="DefaultDB" value="CorporeRM" />** em ambos os arquivos dentro da limitação **appSettings**.

O valor a ser atribuído a tag **DefaultDB** deve ser idêntica ao nome do alias que aponta para a base de dados utilizada. No nosso exemplo que citamos atribuímos o valor "**CorporeRM**" ao alias e respectivamente ao **DefaultDB**.

Exemplo;

|  |  |
| --- | --- |
| **RM.Host.exe.config** | **RM.Host.Service.exe.config** |
| <?xml version="1.0"?>   <configuration>    <**appSettings**>         <add key="JobServer3Camadas" value="false" />         <add key="Port" value="8050" />         <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />         <add key="EnableCompression" value="true" />   **<add key="DefaultDB" value="CorporeRM" />**   <**/appSettings**>   <runtime>         <NetFx40\_LegacySecurityPolicy enabled="true" />   </runtime>         <system.runtime.remoting>         <customErrors mode="Off" />         </system.runtime.remoting>   <startup>         <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0" />   </startup>   </configuration> | <?xml version="1.0"?>   <configuration>    <**appSettings**>         <add key="JobServer3Camadas" value="false" />         <add key="Port" value="8050" />         <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />          <add key="EnableCompression" value="true" />   **<add key="DefaultDB" value="CorporeRM" />**   <**/appSettings**>   <runtime>   <NetFx40\_LegacySecurityPolicy enabled="true" />   </runtime>   <system.runtime.remoting>   <customErrors mode="Off" />   </system.runtime.remoting>   <startup>   <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0" />   </startup>   </configuration> |

Para que estas configurações sejam computadas será necessário reiniciar o serviço do RM Host.

---

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
