---
content_hash: d60257538fae40876cc19ceac1e474af4aa7e65ba0c76ad0acce0a649d6c43e0
fetched_at: '2026-06-29T00:11:06.336678+00:00'
page_id: '634036561'
product: rm
source: tdn-rm
title: Informações técnicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=634036561
version: 4
---

## Restrição:

Nessa primeira versão somente parâmetros configurados como **obrigatórios** no tipo de atendimento serão apresentados para preenchimento no App. A configuração dos parâmetros é realizada em: TOTVS Aprovações e Atendimento\Worflow\Tipo do atendimento.

## Pré-Requisitos

### **TOTVS****Linha RM****:**

* Versão 12.1.28 ou superior;
* Possuir licença do TOTVS Aprovações e Atendimento (RM Agilis).

### **Mobile:**

* Android 6.0 ou superior
* IOS 8.0 ou superior
* Acesso à internet
* Acesso externo ao servidor estar liberado.

Veja também : [Videos How To - App Minhas Aprovações](https://tdn.totvs.com/pages/viewpage.action?pageId=552580409)

## Configurações

### **Acesso externo ao servidor**

Para o funcionamento correto do aplicativo **Minhas Aprovações** , é necessário que o **RM.Host.config e RM.Host.Service.Config**esteja devidamente configurado, pois o mesmo terá informações necessárias para o consumo de serviços do aplicativo. 

1) Para incluir/editar as portas pelo arquivo de configuração, acesse o diretório **C:\totvs\CorporeRM\RM.Net**, e edite os arquivos **RM.Host.exe.config** e **RM.Host.Service.exe.config**.

Inclua/edite as tags abaixo, em ambos os arquivos, dentro do escopo das tags **appSettings**:

**<add key="ApiPort" value="8051" />**

**<add key="HttpPort" value="8051" />**

**<add key="DefaultDb" value="CorporeRM"/>**

**Obs.:** Neste exemplo utilizamos a porta **8051**, caso esta seja utilizada para outra finalidade o departamento de TI deverá informar outra porta para uso.

**Exemplo:**

|  |  |
| --- | --- |
| **RM.Host.exe.config** | **RM.Host.Service.exe.config** |
| <?xml version="1.0"?>  <configuration>    <**appSettings**>         <add key="JobServer3Camadas" value="false" />         <add key="Port" value="8050" />         <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />         <add key="EnableCompression" value="true" />  **<add key="ApiPort" value="8051" />**  **<add key="HttpPort" value="8051" />**  **<add key="DefaultDb" value="CorporeRM"/>**<**/appSettings**>  <runtime>  ... | <?xml version="1.0"?>  <configuration>    <**appSettings**>         <add key="JobServer3Camadas" value="false" />         <add key="Port" value="8050" />         <add key="ActionsPath" value="C:\totvs\CorporeRM\RM.Net;C:\totvs\CorporeRM\Corpore.Net\Bin" />         <add key="EnableCompression" value="true" />  **<add key="ApiPort" value="8051" />**  **<add key="HttpPort" value="8051" />**  <**/appSettings**>  <runtime>  ... |

**Importante:** Após alterar as configurações de portas é necessário reiniciar o serviço do Host.

2 ) Validação para verificar se os arquivos  **RM.Host.config e RM.Host.Service.Config**foram devidamente configurados:

 Digite a URL http://**Endereço:APIPort/api/swagger/ui/index**

    Exemplo:   
             <http://localhost:8051/api/swagger/ui/index>

 Verifique se a página abaixo foi carregada.

### Configuração TOTVS Aprovações e Atendimento para o App Minhas Aprovações

Para que o App Minhas Aprovações funcione corretamente, existem algumas configurações que devem ser realizadas no TOTVS Aprovações e Atendimento.

**1) Inserir a URL para acesso.**

**Observação:** A URL solicitada é a mesma configurada no arquivo **RM.Host.config ,**ou seja, http://**Endereço**:**APIPort**.

* **Exemplo da URL configurada**

* **Após o processo de configuração ser executado, o TOTVS Aprovações e Atendimento  informa que deve ser executado o processo  'Validar tipo de Atendimento'.**

               Para mais informações sobre esse processo acesse: 

               Veja também : [Videos How To - App Minhas Aprovações](https://tdn.totvs.com/pages/viewpage.action?pageId=552580409)

**2) Configuração do QRCode**

* **No Totvs Aprovações e Atendimento no menu principal , pode se gerar link QRCode para utilização do App Minhas Aprovações.**

**Para realizar a leitura do QRCode é necessário habilitar parâmetro que permite sua utilização informando o caminho do servidor, caso não esteja configurado a mensagem abaixo será exibida.**

**Testando as configurações em um emulador**

É possível usar emuladores para executar o aplicativo 'Minhas aprovações', isso pode ser feito de várias formas, uma delas é utilizando a extensão do Chrome para emuladores, segue abaixo o link:

<https://chrome.google.com/webstore/detail/android-online-emulator/lnhnebkkgjmlgomfkkmkoaefbknopmja?hl=pt-BR>

Após adicionar a extensão, basta fazer upload do apk do aplicativo 'Minhas aprovações'

Em seguida, é só configurar o caminho do host desejado e usar:
