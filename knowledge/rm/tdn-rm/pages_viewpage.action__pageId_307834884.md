---
content_hash: b94c7c0ee1dfcca4ff317520e5c3a7ff9726fae3e27fff3067e5573d561ac4ec
fetched_at: '2026-06-29T00:08:43.942320+00:00'
page_id: '307834884'
product: rm
source: tdn-rm
title: Conexão de Origem/Destino Utilizando Web Services
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307834884
version: 68
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo deste documento é mostrar como é feito a criação de um Web Service para consultar e inserir dados em uma tabela do banco de dados e mostrar como utilizar este Web Service como conexões de Origem e Destino em um conceito.

# Criação do Banco de Dados:

---

**Requisitos:**

* Banco de Dados SQL
* Visual Studio 2017

   Para este exemplo, foi criada uma tabela de produto em um banco de dados SQL para que o Web Service possa retornar todos os produtos cadastrados.

   Crie a tabela produto e insira alguns dados, como mostra o exemplo abaixo:

false.Criação da Tabela

CREATE TABLE **produto** (

**id\_produto** INT IDENTITY,

**nome**VARCHAR (**100**),

**quantidade\_estoque** INT,

**preco**DECIMAL(**10,2**),

**data\_criacao**DATETIME,

PRIMARY KEY (**id\_produto**)

)

Inserção de Dados na Tabela

INSERT INTO **produto** VALUES ('Produto 01',**1,0.5**,GETDATE())

INSERT INTO **produto** VALUES ('Produto 01',**2****,1**,GETDATE())

INSERT INTO **produto** VALUES ('Produto 02',**2,1**,GETDATE());

INSERT INTO **produto** VALUES ('Produto 03',**3,2.5**,GETDATE());

INSERT INTO **produto** VALUES ('Produto 04',**4,3**,GETDATE());

INSERT INTO **produto** VALUES ('Produto 05',**5,4.5**,GETDATE());

INSERT INTO **produto** VALUES ('Produto 06',**6,5**,GETDATE());

INSERT INTO **produto** VALUES ('Produto 07',**7,6.5**,GETDATE());

INSERT INTO **produto** VALUES ('Produto 08',**8,7**,GETDATE());

INSERT INTO **produto** VALUES ('Produto 09',**9,8.5**,GETDATE());

INSERT INTO **produto** VALUES ('Produto 10',**10,9.5**,GETDATE());

# Criação do Web Service:

---

   A criação do Web Service é feita através do Visual Studio, o mesmo será utilizado para consumir e inserir dados na tabela criada anteriormente.

false.1° Passo: 

Abra o Visual Studio e selecione: **File -> New -> Project** em seguida crie um projeto do tipo "**WCF Service Application**" com o nome "**WcfService**".

|  |
| --- |

2° Passo:

Depois de criado o projeto, um serviço é criado automaticamente com os métodos "**GetData**" e "**GetDataUsingDataContract**".

Clique com o botão direito na Solution **(WcfService) -> Add -> New Item**

|  |
| --- |

3° Passo:

Na tela "Add New Item" Selecione a opção "**ADO.NET Entity Data Model**" e coloque o nome de "**ModelDB**".

|  |
| --- |

4° Passo:

Na tela "Entity Data Model Wizard" selecione a opção "**EF Designer From database**" e avance o processo.

|  |
| --- |

5° Passo:

Na tela seguinte "Choose Your Data Connection", crie uma nova conexão apontando para sua base de dados, e dê o nome de "**DBEntities**" em seguida avance o processo.

|  |
| --- |

6° Passo:

Selecione a tabela criada anteriormente e finalize a criação.

|  |
| --- |

# Criação do Método:

---

Depois de criado o Web Service, é necessário que seja criado um método no serviço "**Service1**" para retornar a lista de produtos cadastrados anteriormente. 

false.1° Passo: 

Na Interface "**IService1.cs**" adicione os métodos "**GetProdutos"** e "**PutProduto"** na interface como mostra o exemplo abaixo:

[OperationContract]

List<produto> GetProdutos();

[OperationContract]

void PutProduto(produto Produto);

|  |
| --- |

2° Passo:

Em seguida na classe "**Service1.svc**" implemente os métodos da interface, como mostra o exemplo abaixo:

public List<produto> GetProdutos()

    {

using (DBEntities entitie = new DBEntities())

      {

return entitie.produto.ToList();

      }

public void PutProduto(produto Produto)

    {

using (DBEntities entite = new DBEntities())

      {

        entite.produto.Add(Produto);

        entite.SaveChanges();

      }

    }

|  |
| --- |

3° Passo:falseObservação:

Observe que nas definições do objeto produto, as propriedades **quantidade\_estoque**, **preco** e **data\_criacao** são do tipo **Nullable<T>**, ou seja, elas permitem receber o valor nulo.

|  |
| --- |

4° Passo:

Ao executar o projeto, a tela do "**WCF Teste Client**" será exibida, e os métodos criados serão visualizados.

Para testar o método "**GetProdutos**", dê um duplo clique no mesmo e clique no botão "Invoke", o método será chamado e retornará a lista de produtos cadastrados no início do processo.

|  |
| --- |

falseObservação:

Na lista de "**My Service Projects"**, clique sobre o "**Service1.svc"** e selecione a opção "**Copy Address"**, salve este endereço pois ele será ele utilizado na conexão com o Conceito. (No exemplo acima, o endereço copiado foi: **<http://localhost:52286/Service1.svc>**)

# Conexão de Origem:

---

Após a criação do Método, crie um conceito que terá como Conexão de Origem o Web Service da lista de produtos (**GetProdutos**).

false.1° Passo: 

Acesse o módulo Integração, abra o cadastro do Conceito e clique em Novo.

Na tela de inclusão, preencha o campo nome com "**ConceitoWebServiceOrigem"**

|  |
| --- |

2° Passo:

No menu de Conexões adicione uma Conexão de Origem do tipo "**Web Service**" e preencha com os seguintes dados:

* **Nome:** Service1
* **Endereço WSDL:** Endereço copiado anteriormente na criação do WebService (No nosso exemplo: [**http://localhost:52286/Service1.svc**](http://localhost:52286/Service1.svc)**)**
* **Protocolo:** SOAP
* **Método:** Selecione o método criado anteriormente "**GetProdutos"**
* **Time Out:** Tempo de espera para a resposta da mensagem (Minimo: **100seg**. Máximo: **5000seg**)

|  |
| --- |

3° Passo:

A conexão de Origem foi criada listando as propriedades do Objeto produto, retornado como lista no Web Service.

Observação:

A lista de propriedades será listada somente nos casos em que o WSDL tiver um retorno do tipo complexo (s:complexType).

Os webservices existentes hoje no RM não possuem o WSDL do tipo complexo, ou seja, não podem ser usados dessa forma, por isso é recomendado utilizar a conexão de DataServer para usar os dados do RM.

falseObservação:

Como as propriedades **quantidade\_estoque**, **preco** e **data\_criacao** podem receber nulo, o Web Service cria sua respectiva propriedade do tipo "**bool**" acrescentando a palavra "**Specified"** para informar se o valor é nulo ou não.

4° Passo:

No menu Conexões adicione uma Conexão de Destino do tipo "**Arquivo Texto**" e preencha com os seguintes dados:

* **Nome:** ArquivoDestino
* **Arquivo:** Parâmetro

|  |
| --- |

5° Passo:

Ainda na tela de inclusão da conexão Arquivo Texto, acesse a aba "Tabelas" e adicione uma tabela com 5 colunas.

|  |
| --- |

6° Passo:

Volte ao conceito, selecione a aba "Ligações" e realize as ligações da tabela de destino com a tabela de origem, como mostra o exemplo abaixo:

|  |
| --- |

7° Passo:

Após salvar o Conceito, volte a tela de cadastro de conceito e execute o processo em "Processos | Processar Novo Conceito". Selecione o arquivo de destino e em seguida poderá ver o resultado no arquivo texto gerado. 

|  |
| --- |

# Conexão de Destino:

---

Após a criação da Conexão de Origem, crie um conceito que terá como Conexão de Destino o Web Service para inserir um produto (**PutProduto**).

false.1° Passo: 

Acesse o módulo Integração, abra o cadastro do Conceito e clique em Novo.

Na tela de inclusão, Preencha o campo nome com "**ConceitoWebServiceDestino"**

|  |
| --- |

2° Passo:

Crie um arquivo texto com a seguinte informação:

* O;Produto Novo;10;10,50;18/10/2017 01:00:00

|  |
| --- |

As informações estão separadas por ; onde:

* **O:** Identificador da Tabela
* **Produto Novo:** Coluna Nome
* **10:** Coluna quantidade\_estoque
* **10,50:** Coluna preço
* **18/10/2017 01:00:00:** Coluna data\_criação
3° Passo:

No menu Conexões adicione uma Conexão de Origem do tipo "**Arquivo Texto"** e preencha com os seguintes dados:

* **Nome:** Origem
* **Arquivo:** Aponte para o arquivo criado anteriormente

|  |
| --- |

4° Passo:

Ainda na tela de inclusão da conexão Arquivo Texto, acesse a aba "Tabelas" e adicione uma tabela com o identificador O (mesmo do arquivo criado anteriormente) contendo 4 colunas e preencha seus respectivos nomes e tipos.

|  |
| --- |

5° Passo:

Agora adicione uma Conexão de Destino do tipo "**Web Service**" e preencha os seguintes dados:

* **Nome:** DestinoService1
* **Endereço WSDL:** Endereço copiado anteriormente na criação do WebService (No nosso exemplo: [**http://localhost:52286/Service1.svc**](http://localhost:52286/Service1.svc)**)**
* **Protocolo:** SOAP
* **Time Out:** Tempo de espera para a resposta da mensagem (Padrão: 100 segundos)
* **Gerar erro para os códigos das respostas HTTP (400 e 500):** Por padrão somente as respostas HTTP de código 401 a 499 e 501 a 599 são gerados erros no conceito. Esta opção gera erro para as respostas do WebService de código HTTP 400 e 500 e exibe no Log a resposta que o WebService enviou. Para uma lista completa dos códigos HTTP acesse: <https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html>

|  |
| --- |

6° Passo:

A Conexão de Destino foi criada listando o método "**PutProduto**" como uma tabela e listando as propriedades do objeto Produto.

falseObservação:

Como as propriedades **quantidade\_estoque**, **preco** e **data\_criacao** podem receber nulo, o Web Service cria sua respectiva propriedade do tipo "bool" acrescentando a palavra "**Specified"** para informar se o valor é nulo ou não.

|  |
| --- |

7° Passo:

Selecione a aba Ligações e realize as ligações da tabela de destino com a tabela de origem.

falseObservação:

Como as colunas **quantidade\_estoque**, **preco** e **data\_criacao** podem receber nulo, temos que informar no seus respectivos campos "**Specified"** o valor **True** para que a informação seja enviada para o nosso Web Service.

|  |
| --- |

8° Passo:

Após salvar o Conceito, volte a tela de cadastro de conceito e execute o processo em "Processos | Processar Novo Conceito". Em seguida realize a consulta na tabela no banco de dados e verifique que o produto foi inserido corretamente como mostra a imagem abaixo:

|  |
| --- |

O conceito não dá suporte a WSDLs cujas tags XML são interpretadas como arrays (ex. tag "choice"). Isso ocorre pois o conceito trabalha utilizando tabela de/para (parametrização 1 para 1). Headers de envelope SOAP também não são suportados pela ferramenta.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Conexão de Web Services

falsefalse

**Status:** Finalizado

false

**Data:** 18/10/2017

false

**Autores:**
