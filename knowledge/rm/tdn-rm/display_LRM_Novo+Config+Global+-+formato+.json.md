---
content_hash: 23983da51a8587b5b8fde9608551d1aa61ddb5361cba552078127954ff7decc7
fetched_at: '2026-06-29T00:10:30.249853+00:00'
page_id: '519710228'
product: rm
source: tdn-rm
title: Novo Config Global - formato .json
type: documentation
url: https://tdn.totvs.com/display/LRM/Novo+Config+Global+-+formato+.json
version: 16
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

A partir da versão 12.1.27 foi reformulada a forma de se utilizar o arquivo de configuração global, com o intuito de facilitar a sua criação, manutenção e visualização do ambiente.

As vantagens de manter um arquivo único de configuração foram mantidas, tais como simplificar a maneira de administrar os arquivos de configurações das estações de trabalho, utilizando uma única interface para visualizar, incluir, excluir e alterar as configurações de qualquer estação mesmo estando desligada.

Novidades da melhoria:

* O arquivo é montado em **JSON**, não mais em XML;
* **No mesmo arquivo** podem ser cadastrados os **Alias** do ambiente, não necessitando mais da manutenção do Alias.dat. No modelo antigo o Alias não era cadastrado nesse arquivo;
* Podem ser criados agrupamentos de **Alias** **diferentes** para determinados **grupos de hosts.**
* Podem ser criados **agrupamentos de configuração** para os diferentes aplicativo da linha RM, como hosts que executam jobs, hosts locais, RM.exe e outros.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para utilizar essa configuração é necessário ter o arquivo de configuração em uma pasta compartilhada na rede.

Nos arquivos de configuração do Host (service ou .exe) e RM, de cada estação, dentro de <**appSettings**> devem ser adicionadas as tags:

* ***CONFIGGLOBALADDRESS*** com o diretório de rede compartilhado onde está o arquivo de configuração, com o nome do arquivo. Ex.: \\bhd050101853\Compartilhada\ConfigGlobal\configGlobal.json. Preenchimento obrigatório.
* ***CONFIGGLOBALAPPKEY*** com o nome do agrupamento do AppConfig. Exemplo: pode ser criado um AppConfig para o host, outro para o RM.exe. Preenchimento obrigatório.
* ***CONFIGGLOBALDBKEY*** com o nome do agrupamento do DbConfig, que é a configuração de campo. Preenchimento opcional, caso esteja vazio será considerado o DbConfig Default.

      Exemplos dos arquivos de configuração:

150150

Abaixo um exemplo de como ficarão os arquivos de configurações em cada estação:

| Máquina que não utiliza o arquivo de configGlobal | Máquina que utiliza o arquivo de configGlobal | Máquina que utiliza o serviço do TGM e o arquivo de configGlobal |
| --- | --- | --- |
| <?xml version="1.0"?> <configuration> <appSettings> <add key="JobServer3Camadas" value="false" />     <add key="Port" value="8050" />     <add key="Host" value="localhost" />    <add key="LibPath" value="C:\totvs\CorporeRM\RM.Net" /> </appSettings> </configuration> | <?xml version="1.0"?> <configuration> <appSettings> <add key="CONFIGGLOBALADDRESS" value="\\bhd050101853\Compartilhada\ConfigGlobal\configGlobal.json" /> <add key="CONFIGGLOBALAPPKEY" value="RM" /> <add key="CONFIGGLOBALDBKEY" value="Bases" /> </appSettings> </configuration> | <?xml version="1.0"?> <configuration> <appSettings> <add key="CONFIGGLOBALADDRESS" value="<http://localhost:8040/api/globalconfig>" /> <add key="CONFIGGLOBALAPPKEY" value="RM.Host.Service" /> </appSettings> </configuration> |

        Exemplos do arquivo de configuração Global:

150

Esse arquivo possui dois agrupadores principais: **AppConfig** e **DbConfig.**

* Dentro de AppConfig são cadastradas as configurações de aplicativos, como o RM.Host.Service, RM.Host.Service1, RM.Host, RM.exe, etc.
* Dentro e DbConfig são cadastrados os alias e agrupamentos de alias. Caso não seja definido no arquivo de configuração do aplicativo qual DbConfig usar, será utilizado o agrupamento "Default".

Os nomes para os AppConfigs ou DbConfigs não são fixos. Podem ser criados livremente desde que seja um alfanumérico e ponto ("."), sem os demais caracteres especiais. Esse nome deve ser referenciado no arquivo de configuração dos aplicativos, nas tags CONFIGGLOBALAPPKEY e CONFIGGLOBALDBKEY.

Exemplo:

Obs.: As barras invertidas ("\") no arquivo json, seja para determinar diretórios, ou bases de dados, devem ser trocadas pela barra simples ("/") ou utilizadas em duplicidade, ex.: "\\\\BFG050101854\\Compartilhada" ou "//BFG050101854/Compartilhada"

 Após realizar estas configurações o ambiente está preparado para utilizar o arquivo Global de configuração.
