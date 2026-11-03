---
content_hash: dd145fa4811421847257f3e81438c2db495f00c54059bcb07998c017f93a9695
fetched_at: '2026-06-29T00:05:55.692708+00:00'
page_id: '145363622'
product: rm
source: tdn-rm
title: Configurando HttpPort e ApiPort
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurando+HttpPort+e+ApiPort
version: 17
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**
   1. **Configurando HttpPort e ApiPort via RM.Host.ServiceManager.exe**
   2. **Alterando HttpPort e ApiPort via arquivos de configuração**

## **01. VISÃO GERAL**

Para utilizar o RM é possível configurar portas de comunicação com serviços WebServices (HttpPort) e serviços de WebAPI (ApiPort).

Até a versão **12.1.24**, WebServices e APIs respondem pela mesma porta. É utilizado o valor configurado na tag 'HTTPPort' no arquivo de configuração do host.

A partir da versão **12.1.25**, é possível utilizar portas diferentes para requisições WebService e de WebAPI.  
Basta configurar as tags 'HttpPort' e 'ApiPort' no arquivo de configuração do Host.   
As portas também podem ser configuradas pelo RM.Host.ServiceManager.exe.

Lembrete:

Não é obrigatório que as portas sejam diferentes. Por default, ambas responderão na porta 8051.

Atenção

**As portas devem estar devidamente reservadas na rede. Mais informações sobre essa configuração,**

## **02. EXEMPLO DE UTILIZAÇÃO**

**Configurando HttpPort e ApiPort via RM.Host.ServiceManager.exe:**

Para configurar as portas pelo **RM.Host.ServiceManager.exe**(**C:\totvs\CorporeRM\RM.Net**), basta abrir o aplicativo e com um duplo clique na porta desejada, altere o valor.

Por default os valores das portas do primeiro host são:

* Porta WCF: 8050
* Porta WebService: 8051
* Porta WebApi: 8051

**Importante:** Após alterar as configurações de portas é necessário reiniciar o serviço do Host.

**Alterando HttpPort e ApiPort via arquivos de configuração:**

Para incluir/editar as portas pelo arquivo de configuração, acesse o diretório **C:\totvs\CorporeRM\RM.Net**, e edite os arquivos **RM.Host.exe.config** e **RM.Host.Service.exe.config**.

Inclua/edite as tags abaixo, em ambos os arquivos, dentro do escopo das tags **appSettings**:

**<add key="ApiPort" value="8051" />  
<add key="HttpPort" value="8051" />**

**Obs.:** Neste exemplo utilizamos a porta **8051**, caso esta seja utilizada para outra finalidade o departamento de TI deverá informar outra porta para uso.

**Exemplo:**

|  |  |
| --- | --- |
| **RM.Host.exe.config** | **RM.Host.Service.exe.config** |
| <?xml version="1.0"?>  <configuration>    <**appSettings**>         <add key="JobServer3Camadas" value="false" />         <add key="Port" value="8050" />         <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />         <add key="EnableCompression" value="true" />  **<add key="ApiPort" value="8051" />**  **<add key="HttpPort" value="8051" />** <**/appSettings**>  <runtime>  ... | <?xml version="1.0"?>  <configuration>    <**appSettings**>         <add key="JobServer3Camadas" value="false" />         <add key="Port" value="8050" />         <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />         <add key="EnableCompression" value="true" />  **<add key="ApiPort" value="8051" />**  **<add key="HttpPort" value="8051" />**  <**/appSettings**>  <runtime>  ... |
|  |  |

**Importante:** Após alterar as configurações de portas é necessário reiniciar o serviço do Host.

---
