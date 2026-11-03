---
article_id: 31234428339607
category: Integrações - Conceito e WebService
content_hash: 048b206557584fbaef114977b0c63b10515f15f61dbbf04c2f25c8c10d1c059b
fetched_at: '2026-06-28T22:46:44.886095+00:00'
product: rm
section_id: 1500000834721
source: central-rm
title: RH - RM - RHU - Cadastro de Pessoa via WebService/API utilizando o DataServer
  RhuPessoaData
type: support-article
updated_at: '2026-05-14T20:33:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31234428339607-RH-RM-RHU-Cadastro-de-Pessoa-via-WebService-API-utilizando-o-DataServer-RhuPessoaData
---

**Dúvida**Como cadastrar uma pessoa no módulo Gestão de Pessoas utilizando API / Web Service via SoapUI ou Postman    
  
**Ambiente**

* TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Solução**

Para cadastrar uma pessoa no RM via WebService/API, utiliza-se o **DataServer** RhuPessoaData. Para mais detalhes sobre esse DataServer, consulte a documentação oficial:

🔗 [**[RhuPessoaData - Documentação Oficial]**](https://apitotvslegado.z15.web.core.windows.net/RhuPessoaData.html?Objeto=RhuPessoaData)

Antes de cadastrar uma nova pessoa, recomenda-se **consultar os dados de uma pessoa já existente**. Isso retorna um XML ou JSON pronto, que pode ser utilizado como base para o cadastro de uma nova pessoa.

Abaixo, exemplificamos esse processo utilizando as ferramentas **SoapUI** e **Postman**:

[1- Consulta e cadastro via SoapUI](#h_01JR8MA8YSZ2KZCY0SPEVTVQPJ)

[2- Consulta e cadastro via Postman](#01JR8RZWRBC5SAWP6630Q3PYMN)

### 1. Consulta e cadastro via **SoapUI**

#### Passo 1 – Realizar um ReadRecord

Para realizar a leitura dos dados de uma pessoa já cadastrada, utilize o método **ReadRecord**, fornecendo as seguintes informações:

* **DataServer:** RhuPessoaData

**Chaves primárias:**

* **CODCOLIGADA** (código da coligada da pessoa)
* **CODPESSOA** (ID da pessoa que será consultada)

**Parâmetros de contexto:**

* **CODCOLIGADA**
* **CODUSUARIO**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31234428309655)

OBS: Lembre-se de colocar a autenticação (basic), no canto inferior esquerdo

        2. Em seguida, será necessário obter o **XML** gerado após o consumo do **DataServer**. Para isso, deve-se acessar a aba **XML** e extrair as informações disponíveis na tag **"ReadRecordResult"**, conforme o exemplo abaixo:

![Gravar_2025_04_07_15_02_43_245-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31234428310935)

       3. Após copiar o XML, vamos acessar o método SaveRecord e informar o DataServer em questão (RhuPessoaData), o XML que copiamos e também o contexto da mesma forma que fizemos no ReadRecord, conforme o exemplo a baixo:

OBS: Não se esqueça de fechar as chaves no final do XML.

![Gravar_2025_04_07_15_14_24_471-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31234441823639)

      4. Em quarto passo você deve alterar as informações base para as informações da nova pessoa que será cadastrada, se atente ao formato que as tags pedem para serem inseridas, conforme está na documentação do DataServer.

### 2. Consulta e cadastro via Postman

1. Assim como no **SOAP**, o primeiro passo é obter as informações do **JSON** base para realizar o envio. Para isso, deve-se utilizar a **URL** do exemplo abaixo e informar o **DataServer** correspondente no método **GET**.

   Além disso, é necessário aplicar um filtro por **ID**, pois, caso o **GET** seja executado sem filtros, todos os funcionários serão retornados por padrão. Isso pode impactar o desempenho e resultar em alguns campos sendo carregados como **nulos**. Portanto, a aplicação de um **filtro por ID** é essencial para garantir que todos os campos sejam retornados corretamente, com as informações completas para nossa base.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31234428312471)

          2. Após essa etapa, copie apenas as informações que antecedem a chave **"{"** da tag **"id"** e finalize a cópia ao final dessa chave. É importante extrair apenas os dados da **PPESSOA**, sem incluir outras tabelas, como **VLCOMPL** ou **PFCOMPL**, pois essas não precisam ser copiadas.

![Gravar_2025_04_07_15_22_56_670-ezgif.com-video-to-gif-converter.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/31234441826711)

         3. Após copiar os dados base utilizando o método **GET**, é necessário alterar o método para **POST** e informar no **body** o **JSON** base copiado.

Diferente do **GET**, no **POST** **não** é necessário informar o **ID** nem aplicar um **filtro**.

Ao finalizar a estrutura do **JSON**, certifique-se de incluir a chave de fechamento corretamente e garantir que não haja uma vírgula antes dessa chave, evitando erros de formatação.

Segue um exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31234428316311)

         4. Em quarto passo você deve alterar as informações base para as informações do novo funcionário que será cadastrado, se atente ao formato que as tags pedem para serem inseridas, por isso tomamos como base o Json de outro funcionário. Feito as alterações pode consumir normalmente.

**Saiba mais**

[Cross Segmentos - Backoffice RM - Integração - WebServices - Lista de DataServers Web Services](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5275823964567-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Lista-de-DataServers-Web-Services)

[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007851192-Cross-Segmentos-Backoffice-RM-Integra%C3%A7%C3%A3o-WebServices-Utilizando-o-SoapUI-para-consumir-DataServers-RM-via-WebServices](https://centraldeatendimento.totvs.com/hc/pt-br/articles/Cross%20Segmentos%20-%20Backoffice%20RM%20-%20Integra%C3%A7%C3%A3o%20-%20WebServices%20-%20Utilizando%20o%20SoapUI%20para%20consumir%20DataServers%20RM%20via%20WebServices)
