---
content_hash: fd4ad2d47a7567ca460227d6e9ba0c97491dff078b60aa5c074a5cef692c8c28
fetched_at: '2026-06-29T00:08:58.648783+00:00'
page_id: '360453955'
product: rm
source: tdn-rm
title: Webservices.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=360453955
version: 1
---

Os serviços WebService identificarão a base de dados a ser utilizada através da tag **DefaultDB**, que informa o Alias que será utilizado no acesso. Essa tag deve existir no arquivo de configuração do Host (RM.Host.Service.exe.config ou RM.Host.exe.config):

**<add key=”DefaultDB” value=”<ALIAS\_DO\_BANCO\_RM>**

A variável ***<ALIAS\_DO\_BANCO\_RM>*** deverá ser substituída pelo nome do alias cadastrado para acesso ao banco de dados.

Exemplo:

|  |
| --- |
| `<?``xml` `version``=``"1.0"``?>` `<``configuration``>` `<``appSettings``>` `<``add` `key``=``"JobServer3Camadas"` `value``=``"false"` `/>` `<``add` `key``=``"Port"` `value``=``"12120"` `/>` `<``add` `key``=``"ActionsPath"` `value``=``"C:\totvs\CorporeRM\RM.Net;"` `/>` `<``add` `key``=``"LibPath"` `value``=``"C:\totvs\CorporeRM\RM.Net"` `/>` `<``add` `key``=``"EnableDynamicLocalization"` `value``=``"false"` `/>` `<``add` `key``=``"EnableCompression"` `value``=``"false"` `/>` `<``add` `key``=``"LocalizationLanguage"` `value``=``"pt-BR"` `/>` `<``add` `key``=``"HttpPort"` `value``=``"8051"` `/>` `<``add` `key``=``"DefaultDB"` `value``=``"CorporeRM"` `/>` `</``appSettings``>` `<``runtime``>` `<``NetFx40_LegacySecurityPolicy` `enabled``=``"true"` `/>` `<``generatePublisherEvidence` `enabled``=``"false"` `/>` `</``runtime``>` `<``startup` `useLegacyV2RuntimeActivationPolicy``=``"true"``>` `<``supportedRuntime` `version``=``"v4.0"` `sku``=``".NETFramework,Version=v4.0"` `/>` `</``startup``>` `</``configuration``>` |

A porta **8051** é padrão no sistema e caso seja alterada na tag **HttpPort** no arquivo de configuração do Host, precisa ser alterada no link acima.

Liberação de acesso a porta do Host Service

Caso o Host utilizado seja o **RM.Host.Service.exe** é necessário a execução do comando, abaixo, para liberação da porta configurada na tag **HttpPort**, via prompt de comando:

* Adicionar

**netsh http add urlacl url=http://+:8051/ user=NetworkService**

* Apagar

**netsh http delete urlacl url=http://+:8051/**

* Exibir

**netsh http show urlacl**

Para que o sistema carregue corretamente os parâmetros do sistema no momento de utilização do WebService, é necessário que sejam inclusas as informações do contexto: **Coligada, Filial, Tipo de curso e Código do Sistema.**

Essas informações devem ser separadas pelo caractere ***";"***.
