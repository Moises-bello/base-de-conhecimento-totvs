---
content_hash: bb8b92bbca917dfa7a70b3c3da42bc50c87d682e8d33cf0200375ad2bf0ab0ad
fetched_at: '2026-06-29T00:11:33.149341+00:00'
page_id: '75271283'
product: rm
source: tdn-rm
title: Configuração de Tag 3 camadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=75271283
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.xx |
| **Processo** | **:** | 3 camadas |
| **Subprocesso** | **:** | Configuração de Tag 3 camadas |
| **Data da publicação** | **:** | 23/09/2013 |

**O** **contexto** **original** **do** **arquivo** **seria** **o exemplo** **abaixo.**

**As** **tags** **que estão** **em** **negrito** **devem** **ser** **alteradas** **caso** **o sistema** **esteja** **sendo utilizado** **em** **ambiente** **de** **três** **camadas.**

<?xml version="1.0"?>  
 <configuration>  
 <appSettings>  
 <add key="CommunicationStyle" value="WCF" />  
 **<add** **key="JobServer3Camadas" value="false"** **/>**  
 <add key="Port" value="8050" />  
 **<add** **key="Host"** **value="localhost"** **/>**  
 <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />  
 <add key="LibPath" value="C:\totvs\CorporeRM\RM.Net" />  
 <add key="EnableCompression" value="true" />  
 </appSettings>  
 <runtime>  
 <NetFx40\_LegacySecurityPolicy enabled="true" />  
 </runtime>  
 <startup>  
 <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0" />  
 </startup>  
 </configuration>

**Abaixo** **segue** **exemplo** **de** **como** **seria** **configuração** **caso** **o ambiente fosse** **utilizado** **em** **três** **camadas.**

**As** **tags "JobServer3Camadas"** **e** **"Host" receberam** **os** **valores** **de** **true** **para** **execução** **em** **três** **camadas** **e** **o** **nome** **do servidor** **vai** **para** **a** **tag** **host,** **este** **será** **o responsável** **pela** **execução** **dos processos.**

<?xml version="1.0"?>  
 <configuration>  
 <appSettings>  
 <add key="CommunicationStyle" value="WCF" />  
 **<add** **key="JobServer3Camadas" value="true"** **/>**  
 <add key="Port" value="8050" />  
 **<add** **key="Host"** **value="SERVERELETRO"** **/>**  
 <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />  
 <add key="LibPath" value="C:\totvs\CorporeRM\RM.Net" />  
 <add key="EnableCompression" value="true" />  
 </appSettings>  
 <runtime>  
 <NetFx40\_LegacySecurityPolicy enabled="true" />  
 </runtime>  
 <startup>  
 <supportedRuntime version="v4.0" sku=".NETFramework,Version=v4.0" />  
 </startup>  
 </configuration>

Para maiores informações:

Consulte o [Wikihelp](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.LogAuditoria.aspx) TOTVS.

**COMUNIDADE** [@FRAMEWORK](https://totvs.byyou.com/?space=rframework)

**Canais de Atendimento:**

**Telefônico:** 4003-0015 escolhendo as opções 02 – dois (Software), 02 – dois (Suporte Técnico), 03 – três (RM), 09 – nove (Demais Áreas), 04 – quatro (BI) e 03 – três (Gerador de Relatórios e Planilha);

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)
