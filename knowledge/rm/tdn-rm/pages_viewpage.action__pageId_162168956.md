---
content_hash: 58e7d780de9632f023cdc054a97cf36aa6582c32967372d88c75ccbb68a7605f
fetched_at: '2026-06-29T00:05:57.093767+00:00'
page_id: '162168956'
product: rm
source: tdn-rm
title: Configuração do Portal RM e Portal FrameHTML em WebFarm
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=162168956
version: 15
---

## **Índice**

---

Índice

## **VISÃO GERAL**

---

       Em situações onde o cliente utiliza WebFarms, é essencial que seja realizada uma configuração específica nas instâncias do arranjo para que a aplicação funcione corretamente. Segue um resumo dessas configurações.

       Essa documentação expõe os pré-requisitos da nossa aplicação para funcionar com WebFarm.

       A configuração do LoadBalance não é abordada neste documento, pois é uma questão de infraestrutura e pode ser composta por diferentes tecnologias. Segue documentação da microsoft para configuração do WebFarm com IIS: [https://docs.microsoft.com/en-us/iis/web-hosting/scenario-build-a-web-farm-with-iis-servers/configure-a-web-farm-with-iis-servers](https://www.google.com/url?q=https://docs.microsoft.com/en-us/iis/web-hosting/scenario-build-a-web-farm-with-iis-servers/configure-a-web-farm-with-iis-servers&sa=D&source=hangouts&ust=1565873638393000&usg=AFQjCNHrgC17LhgpYYRxDND7f45SE-wE_Q) 

**Importante:** Para portais específicos, como o Portal do Aluno, é necessário consultar a respectiva documentação de instalação para ver a necessidade de adicionar as tags no arquivo de web.config; de forma geral, será necessário quando o portal criar dependência do contexto da aplicação.

Configuração:

**Não** prestamos suporte à este tipo de configuração por se tratar de ajuste de ambiente, o documento serve apenas como guia.   
Para a realização de tal configuração, é necessária a atuação de um profissional capacitado.

## **EXEMPLO DE UTILIZAÇÃO**

---

       **1 - Web.config:** Configuração do atributo machineKey em todas os nós do arranjo

     Se não realizado, a aplicação retornará a mensagem: **"Validation of viewstate MAC failed. If this application is hosted by a Web Farm or cluster, ensure that configuration specifies the same validation Key and validation algorithm. AutoGenerate cannot be used in a cluster. "** Quando uma mesma requisição for atendida por um nó. Diferente dose predecessor. Com a alteração, o MAC passa a não mais ser utilizado para composição das chaves de criptografia, utilizando as informadas no parâmetro para tal.

 <system.web>  
<machineKey  
validationKey="2572D9348893391032D8D6B626932E5C132D70EFEFB3E3C49A077607852CA31CD884BBC4A1DCA0BB1C66CE865C8559E623B6E5A2F388F0DF2ECA738A0262E1EF"  
decryptionKey="A40745131B1163D6C0A857D8B2AD876CB4A9CF16AC92859F17025CDEB3820911"  
validation="SHA1" decryption="AES" />  
<trust level= "Full" legacyCasModel="true" /> 

     Para gerar uma chave aleatória, utilize a ferramenta abaixo (opção ASP.NET 2.0):

<http://www.developmentnow.com/articles/machinekey_generator.aspx>

      **2 - IIS:** Configuração dos IDs da aplicação devem ser idênticos para a mesma aplicação em todos os nós

      A chave do gerenciamento de sessão considera o ID da aplicação para ser construída. Logo, se houver divergência entre esse parâmetro, o cliente passará pela experiência de perder o estado de sessão sempre que houver troca de nós para atender sua requisição. Ajustar essa configuração no IIS em configurações avançadas da aplicação (em todos os nós):

      **3 - Web.config:**Configuração do atributo session State em todos os nós do arranjo

      Se houver divergência entre esse parâmetro, o cliente passará pela experiência de perder o estado de sessão sempre que houver troca entre nodos para atender sua requisição. Nesse caso, deve ser utilizado um dos modos: SQLServerou ServerState

* **SQLServer:**

      1 - Eleger um host instalando o SQL Server 2008R2 Express (Gratuito mesmo para uso comercial). É necessário que o Microsoft .net Framework 4.0 também seja instalado nessa mesma máquina.   
      1.1 – Criar uma base de dados e configurar a mesma para exercer a função de SesssioStateProvider para a aplicação [asp.net](http://asp.net). Considerando que o host onde a base ASPSTATE instalada é o DBSERVER, usuário sa e senha saPasswd 1@3 C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet\_regsql.exe -ssadd -d ASPSTATE -sstype c –SDBSERVER -U sa -P masterkey saPasswd 1@3

      Considerando que o host onde a base ASPSTATE instalada é o DBSERVER, usuário sa e senha saPasswd 1@3

**C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet\_regsql.exe -ssadd -d ASPSTATE -sstype c –S DBSERVER -U sa -P masterkey saPasswd 1@3**

      1.2 – Alterar o atributo sessionState em todas as máquinas do arranjo para utilizarem serverState apontado para a máquina eleita:

<sessionState  
mode="SQLServer"  
allowCustomSqlDatabase="true"  
sqlConnectionString="Data Source=DBSERVER;Initial Catalog=ASPSTATE;User  
ID=sa;Password=saPasswd1@3"  
cookieless="false"  
timeout="20"  
/>

      **Obs.:** Após alterar as configurações, é necessário reciclar todos os ApplicationPool's do arranjo para validar as alterações.

      Desenho básico da arquitetura proposta :
