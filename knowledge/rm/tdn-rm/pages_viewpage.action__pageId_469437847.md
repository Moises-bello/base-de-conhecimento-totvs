---
content_hash: 331733b284eb5c62da79fffed0e5d33b4f43587b63d367f817fdb53a9866d548
fetched_at: '2026-06-29T00:10:16.369772+00:00'
page_id: '469437847'
product: rm
source: tdn-rm
title: TOTVS Gateway Manager (TGM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=469437847
version: 121
---

# **01. VISÃO GERAL**

O TOTVS Gateway Manager é um centralizador de requisições (ponto único de acesso), que realiza a análise, a filtragem e redirecionamento do tráfego de terceiros entre os hosts ativos.

As funções presentes no API Gateway permitem as mais diversas vantagens para quem o utiliza. Um único ponto de acesso, por exemplo, significa uma redução de esforço em administrar as "portas de entradas" dos serviços utilizados, podendo focar seus esforços em um único local.

As funções presentes no API Manager fornecem uma camada de gestão para o API Gateway. Além de definir o comportamento do API Gateway, o API Manager lida com a análise de cada requisição.

# **02. VANTAGENS E POSSIBILIDADES DO TGM**

      Haverá um ponto central de comunicação com os Serviços para requisições de portais web, sem que seja necessário implementar uma regra de balanceamento e descoberta em cada portal.

      Não é necessário mais re-configurar todas as aplicações clientes ao incrementar ou modificar o parque de Servers.

      Será possível visualizar todos os Servers disponíveis no parque,  além de poder testar a saúde de comunicação dos mesmos, é até reconfigurar cada server para que ele atenda a determinados tipos de serviços.

      **Principais características de destaque do TGM:**

* A solução é de fácil implantação, tanto para novas instalações quanto para instalações já existentes.
* O sistema é modularizável e servirá à qualquer linha de produto da TOTVS.
* Será possível que o administrador do ERP tenha uma visão completa de todo o parque de servidores.

# **03. REQUISITOS**

A partir da versão 12.1.2406 do RM, não há pré-requisitos para a instalação do TGM.

Para versões anteriores, consultar: [Dependências de execução do TGM na versão 12.1.2402 e anteriores - Linha RM - TDN (totvs.com.br)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=822245226)

# **04. INSTALANDO O TGM**

## **04.01 (MÁQUINA LOCAL)**

Abaixo iremos apresentar como instalar o TGM.

Instalador do TGM,RM.Host.ServiceManager.exe4,5yes4

A instalação do TGM pode ser feita via **TOTVS Gateway Manager (TGM)**, basta informar os campos abaixo:

Atenção

As configurações dos serviços serão inseridas no arquivo "appServerList.json" onde o mesmo será lido ao subir o serviço do TGM, adicionando as informações dos Serviços de Proxy na configuração do TGM.

Ao instalar o TGM via instalador, ao final verificar se o serviço do TGM está online.

no5

O serviço do TGM  pode ser feita via RM.Host.ServiceManager, basta marcar o campo "**Instalar TGM"** e clicar no botão **Instalar** após informar o diretório onde o TGM foi instalado.

Atenção

Caso o serviço do TGM não inicie, verifique na documentação .

**D****escrição dos Campos:**

* **Instalar TGM:** Opção para que o serviço do Totvs Gateway Manager seja instalado na maquina que está sendo utilizada. 
  + **Caminho completo do arquivo:** Caminho onde está instalado o executável do Totvs Gateway Manager.
* **Portas de eonfiguração do TGM**
  + **Porta de serviço:** Porta onde o TGM irá realizar o serviço de configuração.
  + **Porta de resiliência:**Porta onde o TGM irá realizar a resiliência do provider (NGINX).
* **Portas de escuta do TGM**
  + **Porta de WCF:** Porta onde o TGM irá receber requisições TCP e redirecionar para os Hosts cadastrados para responder TCP.
  + **Porta de WebService:** Porta onde o TGM irá receber requisições HTTP e redirecionar para os Hosts cadastrados para responder HTTP.
  + **Porta de WebApi:** Porta para disponibilização do endpoint do serviço rest para configuração do TGM**.**
  + **Connect (s):** Valor em segundos para aguardar a conexão com o Proxy.
  + **Time-out (s):** Valor em segundos para aguardar a resposta da requisição.
* **Utiliza****r TGM em outra maquina:** Opção dada ao usuário para que o Totvs Gateway Manager seja instalado em outra maquina (informando Host:Porta).

**Passo a passo para configuração do TGM (Totvs Gateway Manager):**

1. Acessar o aplicativo "RM.Host.ServiceManager.exe" e adicionar a quantidade de serviços desejada.
2. Acessar a aba "Totvs Gateway Manager" e ,marcar a opção "Instalar TGM".
3. Informe o caminho onde o TGM foi instalado anteriormente.
4. Em seguida, clique para instalar o serviço do TGM em Operações no serviço TGM.
5. Após realizada a instalação, configure as portas WebService e WebApi e clique em "Aplicar".
6. Verifique que o TGM foi instalado corretamente, como mostra a imagem disponível abaixo:

                         

Veja mais sobre a  ou como configurar o

## **04.02 EM OUTRA MÁQUINA**

Iremos apresentar como instalar o TGM em outra máquina.

Instalador da Biblioteca RM,RM.Host.ServiceManager.exe6,7yes6

Na instalação da Biblioteca o usuário poderá informar se usará o TGM, conforme parâmetro abaixo: 

no7

1. Marcar a opção "Utilizar TGM em outra maquina" e preencher o campo com "Host:Porta" da maquina que será utilizada para a instalação do TGM.
2. Alterar o arquivo "RM.exe.config", apontar as tags do host e porta para maquina que está sendo utilizada.
3. Verifique que a comunicação é feita corretamente entre as maquinas (através dos hosts ativos).

false

É necessário que seja feita a alteração no arquivo "RM.exe.config" quando utilizado o TGM em outra máquina (Alterar os tags "Port" e "Host").

false

Caso a sua empresa possua firewall e/ou restrições de acesso à internet, é necessário que o administrador da rede libere o acesso às portas configuradas.

# **05. LOG DE ERROS**

      

      Erros podem ocorrer no RM.Host ou no RM.Host.ServiceManager

TGM,RM.Host/RM.Host.Service,RM.Host.ServiceManager8,9,10yes8#dddsolidTGM

O log do TGM está centralizado no EventViewer (Visualizador de Eventos) do Windows.

---

no9#dddsolidRM.Host / RM.Host.Service

Caso hajam erros nos serviços relacionados ao TGM no RM.Host, os mesmos serão apresentados no TraceFile.

obs.: é necessário habilitar a Tag Tracefile no config (<https://tdn.totvs.com/display/LRM/Habilitar+Tag+Tracefile>)

---

no10#dddsolidRM.Host.ServiceManager

Caso hajam erros nos serviços relacionados ao TGM no RM.Host.ServiceManager, os mesmos serão apresentados na tela.

---

#ddd1solidInformações do Documento

**Versionamento**

---

Versão: v1.0

Versão: v1.1

**Links Externos**

---

[1] <https://dotnet.microsoft.com/download/thank-you/dotnet-runtime-2.2.0-windows-x64-asp.net-core-runtime-installer>

[2] <https://dotnet.microsoft.com/download/thank-you/dotnet-runtime-2.2.0-windows-x64-installer>

[3] <https://nodejs.org/en/>.

#ddd1solidInformações Gerais do TGM

**Informações do instalador**

---

Nome: TOTVS Gateway Manager - {versao}.exe

Versão: 12.1.25+

Tamanho: ~ 4mb

**Pré-requisitos**

---

* ASP.NET Core 2.2.0
* .NET Core 2.2.0
* NODE.js (Publicação - somente desenvolvedores)
