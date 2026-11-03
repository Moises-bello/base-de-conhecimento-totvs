---
content_hash: 6ea20769f4beadc610c551e2c87e144bd2f104eb76941676aa740ff4c4c69d17
fetched_at: '2026-06-29T00:05:57.692383+00:00'
page_id: '181961676'
product: rm
source: tdn-rm
title: TBC -  Integração com o WebService do Totvs Mashups
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=181961676
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Framework     **Versão :**11.5x, 11.8x , 12.1x |
| **Processo** | **:** | TBC |
| **Subprocesso** | **:** | Integração com o WebService do Totvs Mashups |
| **Data da publicação** | **:** | 26/12/2014 |

# Introdução

O serviço do Totvs Mashups permite a integração de qualquer aplicativo de qualquer sistema operacional e linguagem de programação.   
 A sua implementação foi feita em cima da WCF (Windows Communication Foundation) utilizando padrão WS-\*, XML e SOAP para a comunicação. Mas expansível a outros padrões suportados pela WCF, da plataforma Microsoft.NET.  
 Neste documento estão detalhados todos os métodos disponíveis e classes usadas para a comunicação com o WebService.   
 A definição do WebService está disponível em:  
 [http://mashups.totvs.com.br/TotvsSO\_Hlt197145182\_Hlt197145183A.Host/SOAManager.svc?wsdl](http://mashups.totvs.com.br/TotvsSOA.Host/SOAManager.svc?wsdl)   
  **Métodos Disponíveis no WebService**

## GetServiceTypes

Através desta função é possível obter uma lista dos tipos de Mashups disponíveis. Na arquitetura do Totvs Mashups, podem ser criados vários tipos diferentes Mashups, tais como:  
 MashupStudioService – Mashups criados com a ferramenta Mashup Studio  
 MetadataService – Serviços de informações dos Mashups  
 WebServices – Mashups baseados em WebServices   
 **Parâmetros:** (SOAConnectionData)  
 **Resultados:** Array de strings com a lista de ServiceTypes.

### Classe: SOAConnectionData

* ClientID: String – ID do Client do Totvs Mashups
* UserName: String – Nome do usuário do Totvs Mashups
* Password: String – Senha do usuário

## GetServiceNames

Através desta função é possível obter uma lista dos Mashups disponíveis para o ServiceType selecionado. Cada ServiceType pode ter vários Mashups publicados.  
 **Parâmetros:** (SOAConnectionData; ServiceType: String)  
 **Resultados:** Array de strings com a lista de Mashups.

## GetServicesInfo

Através desta função é possível obter uma lista com detalhes dos Mashups disponíveis para o SearchType e SearchValue informados. Esta função retorna diversas informações sobre os Mashups que estão definidas na classe SOAServiceInfo.  
 **Parâmetros:**

* SOAConnectionData
* SearchType: Enumerado (All, ServiceName, ServiceTitle, Description, Provider, Tag)
* SearchValue: String

**Resultados:** Array de SOAServiceInfo.

### Classe: SOAServiceInfo

* ServiceType: String – Tipo de serviço do Mashup
* ServiceName: String – Nome do Mashup
* ServiceVersion: Integer – Versão do Mashup
* ServiceTitle: String – Título do Mashup
* ServiceProvider: String – Provedor dos dados do Mashup
* ServiceDescription: String – Descrição detalhada do Mashup
* ServiceTags: Strings – Tags relacionadas ao Mashup
* ServiceDate: DateTime – Data da publicação/alteração do Mashup

## GetService

Através desta função é iniciado o processo de execução do Mashup, ela retorna todas as informações de execução do Mashup como Parâmetros e Resultados da execução do Mashup.   
 **Parâmetros:** (SOAConnectionData; ServiceType: String; ServiceName: String; ServiceVersion: Integer)  
 **Resultados:** SOAServiceData.

### Classe: SOAServiceData

* ServiceExecutionID: String – ID da execução do Mashup
* ServiceType: String – Tipo de serviço do Mashup
* ServiceName: String – Nome do Mashup
* ServiceVersion: Integer – Versão do Mashup
* ServiceTitle: String – Título do Mashup
* CurrentState: String – Estado da execução do Mashup
* CurrentStateDescription: String – Descrição do estado da execução do Mashup
* Data: Array de SOAData – Dados da execução do Mashup

### Classe: SOAData

* DataKind: Enumerado – Tipo do dado do Mashup:
  + Param: Indica que o dado é um parâmetro do Mashup
  + Info: Indica que o dado é uma informação a ser mostrada do Mashup
  + Result: Indica que o dado é um resultado da execução do Mashup
  + Internal: Indica que é um dado para uso interno do Mashup
* DataType: Enumero – Indica o tipo de dado do valor
  + Boolean: Indica um dado do tipo boolean (True, False);
  + Integer: Indica um dado de tipo número inteiro;
  + Number: Indica um dado de tipo número (Double), deve ser usado o separador de decimal "." (Ponto) e sem separador de milhar;
  + DateTime: Indica um dado no formato data/hora canônico (aaaa-MM-dd hh:mm:ss), caso o valor indicar somente hora, a data deve ser igual a "01/01/0001";
  + String: Indica um dado do tipo texto;
  + List: Indica um dado que contem uma lista de valores/descrições;
  + Image: Indica um dado que contem uma imagem (JPEG com Codificação Base64);
  + Table: Indica um dado que contem uma tabela de valores detalhada abaixo;
* Name: String – Nome do dado do Mashup
* Description: String – Descrição do dado do Mashup
* StateName: String – Indica o nome do estado referente ao dado (somente para parâmetros)
* Value: String – Contém o valor do dado de acordo com o tipo de dado.
* ListItems: Array de SOADataListItem (válido somente para o DataType = List)
* Columns: Array de SOAData (válido somente para o DataType = Table)
* Required: Boolean – Indica se o parâmetro é obrigatório para a execução do Mashup

### Classe: SOADataListItem

* Code: String – Código do valor do item da Lista
* Description: String – Descrição do item da Lista

## Execute

Através desta função é feita a execução do estado atual do Mashup, após a chamada da função GetService e de preenchido os parâmetros obrigatórios do Mashup, deve-se chamar a função Execute para iniciar a execução.   
 **Parâmetros:** (SOAConnectionData; SOAServiceData)  
 **Resultados:**

* SOAServiceData – Dados da execução do Mashup
* ResultType: Enumerado – Indica o resultado da execução do Mashup
  + Continue – Indica que a execução do Mashup não chegou ao final e que deve ser preenchido os parâmetros do estado atual.
  + Finished – Indica que o Mashup terminou a sua execução com sucesso.
  + Error – Indica que houve um erro na execução do Mashup e a mesma deve ser interrompida.
  + Warning – O mesmo que um erro, também implica no fim da execução do Mashup.
  + InvalidParam – Indica que um parâmetro informado não é válido, o parâmetro deve ser informado corretamente e a execução do Mashup pode ser continuada.
* ResultMessage: String – Contém a mensagem de erro quando o ResultType é Error, Warning ou InvalidParam.
* ResultMessageCode: Integer – Contém um código relativo a mensagem de erro.

### Tipo de dado: Table

Quando o tipo de dado é do tipo Table, o string do valor contém uma estrutura com os dados da tabela. O XML é formado da seguinte maneira:   
 <?xml version="1.0" encoding="utf-8">  
 <TotvsMashupTable SelectedIndex=0>  
 <Schema>  
 <Column>  
 <Name>Nome da Coluna</Name>  
 <DataType>Tipo de dados da Coluna (SOADataType)</DataType>  
 </Column>  
 </Schema>  
 <Data>  
 <Row>  
 <Nome da Coluna 1>Valor da Coluna 1</Nome da Coluna 1>  
 <Nome da Coluna 2>Valor da Coluna 2</Nome da Coluna 2>  
 </Row>  
 </Data>  
 </TotvsMashupTable>   
 A propriedade SelectedIndex do nó TotvsMashupTable deve ser informada com o índice da Row selecionada pelo usuário quando a tabela é um parâmetro do Mashup.   
 A tabela tem a sua definição informada no Nó Schema, para cada coluna da tabela, existe uma entrada de <Column> no Schema.   
 Para cada <Row> é informado o valor de acordo com o tipo de dado da coluna.

# Passo a passo para execução do Mashup

A execução do Mashup deve seguir um passo a passo que deve ser obrigatoriamente da seguinte Maneira:

1. É feita uma chamada a função GetService;
2. Deve-se verificar se existe algum dado do tipo Info e o mesmo deve ser apresentado ao usuário juntamente com os parâmetro para o CurrentState, deve-se verificar se os parâmetros obrigatórios para o CurrentState foram informados.
3. É feita uma chamada a função Execute passado os dados preenchidos, todos os dados devem ser enviados na chamada exceto os do tipo Info.
4. Após a execução, deve-se verificar o resultado da execução (ResultType) e de acordo com o resultado:
   1. Continue – A execução deve voltar ao passo 2 para continuar a execução do próximo State do Mashup;
   2. Finished – A execução foi finalizada, os dados de Resultado estarão preenchido;
   3. Error, Warning – Deve ser apresentada a mensagem de erro ao usuário, a execução é finalizada neste ponto;
   4. InvalidParam – Deve ser apresentada a mensagem de erro ao usuário e voltar a ao passo 2 para continuar a execução do Mashup;

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
