---
content_hash: 7b9ee88a941a386012748f88745ae85c6fb9bb909aba0d05535381a93b3f2084
fetched_at: '2026-06-29T00:05:55.322906+00:00'
page_id: '134152970'
product: rm
source: tdn-rm
title: Balanceamento de Conexões X Servidor de Aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=134152970
version: 9
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.52 e11.82 |
| **Processo** | **:** | Balanceamento de Conexões x Servidor de Aplicação |
| **Subprocesso** | **:** | Configurações de Balanceamento |
| **Data da publicação** | **:** | 25/03/2014 |

 

Efetuando balanceamento em 3 camadas.

   
 OBJETIVO

 Demostrar de forma concisa, efetuar o balanceamento entre os servidores de aplicação, aproveitando as configurações em 3 ou 4 camadas

 PROCEDIMENTOS:

 Considerando um ambiente em 3 camadas, porém com dois servidores de aplicação, efetuaremos as seguintes configurações nos arquivos config:

 

**1.** **Configurando máquinas cliente:**

 

A máquina cliente será apontada para dois ou mais servidores de aplicação.

 

No arquivo .config do aplicativo (exemplo: C:\totvs\CorporeRM\RMLabore\RMLabore.exe.config), é necessário acrescentar as tags HOST e PORT de maneira crescente :

 

   <add key="Host" value="SERVER01" />

   <add key="Port" value="8050" />

   <add key="Host1" value="SERVER2" />

   <add key="Port1" value="8050" />

 

Lembrando que poderá ter mais de dois servidores de aplicação. Neste caso, temos que continuar acrescentando as tags HOST e PORT: Host2, Port2, Host3 e Port4.

 

**22.** **Configuração do Servidor de Aplicação.**

 

As configurações desse servidor, permanecerão como a mesma estrutura inicial, já configurada par a 3 ou 4 camadas.

 No arquivo RM.Host.Service.exe.config do servidor de aplicação, a estrutura será:

 <appSettings>

    <add key="JobServer3Camadas" value="true" />

    <add key="Port" value="8050" />

    <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />

    <add key="DefaultDB" value="CorporeRM" />

    <add key="EnableCompression" value="true" />

 </appSettings>

 Em resumo, já considerando a estrutura de 3 ou 4 camadas, apenas as maquinas client deverão ser alteradas conforme descrito acima.

 **3.**  **Configuração para o Portal Gestão de conteúdo.**

 a-      Localize o arquivo web.config da pasta C:\totvs\CorporeRM\Corpore.Net

 b-      Edite o arquivo em bloco de notas.

 c-       Localize as tagas HOST e PORT e alterando e acrescentando os novos servidores.

     <add key="SelfHosted" value="true" />

     <add key="Host" value="SERVER01" />

     <add key="Port" value="8050" />

     <add key="Host1" value="SERVER02" />

     <add key="Port1" value="8050" />     

     <!--<add key="Protocol" value="tcp"/>

     <add key="WcfProtocol" value="tcp"/>-->

     <add key="JobServer3Camadas" value="true" />

 O balanceamento será de forma automática conforme escolha do sistema. Não será possível, considerando esta configuração, determinar de forma manual para qual servidor será redirecionado os processos, ou seja, a escolha pelo sistema será de forma aleatória.

 

 DICAS:

 ·         Arquitetura em 3 camadas: <http://tdn.totvs.com/display/public/rm/Arquitetura+3+camadas>

 

|  |  |
| --- | --- |
|  | **Para maiores informações:** Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
