---
content_hash: d823e30923b7189df156e2199a0e5a8a0ae10e0ecae0cc5e86d7cdea14c1192e
fetched_at: '2026-06-29T00:08:44.036754+00:00'
page_id: '307838301'
product: rm
source: tdn-rm
title: Conexão de Origem/Destino Utilizando DLL .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307838301
version: 17
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo deste documento é mostrar como é feito a criação de uma DLL .Net para consultar e inserir dados em uma tabela do banco de dados, e mostrar como utilizar esta DLL .Net como conexões de Origem e Destino em um conceito.

# Criação do Banco de Dados:

---

**Requisitos:**

* Banco de Dados SQL
* Visual Studio 2017

   Para este exemplo, foi criada uma tabela de produto em um banco de dados SQL para que a DLL .Net possa retornar todos os produtos cadastrados.

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

# Criação da DLL .Net:

---

       A criação da DLL .Net é feita através do Visual Studio, o mesmo será utilizado para consumir e inserir dados na tabela criada anteriormente.

false.1° Passo: 

Abra o Visual Studio e selecione: **File -> New -> Project** em seguida crie um projeto do tipo "**Class Library**" com o nome "**ConceitoDll**".

Em seguida clique com o botão direito na Solution (ConceitoDll) -> Add -> New Item

|  |
| --- |

2° Passo:

Na tela "Add New Item" Selecione a opção "**ADO.NET Entity Data Model**" e coloque o nome de "**ModelDB**".

|  |
| --- |

3° Passo:

Na tela "Entity Data Model Wizard" selecione a opção "**EF Designer From database**" e avance o processo.

|  |
| --- |

4° Passo:

Na tela seguinte "Choose Your Data Connection", crie uma nova conexão apontando para sua base de dados, e dê o nome de "**DBEntities**" em seguida avance o processo.

|  |
| --- |

5° Passo:

Na tela "Choose Your Version", Selecione a versão 6.x do Entity Framework.

|  |
| --- |

6° Passo:

Selecione a tabela criada anteriormente, dê o nome de "DBModel" e finalize a criação.

|  |
| --- |

7° Passo:

Após o processo, uma conectionString com o nome "**DBEntities**" será criada no arquivo "**App.Config**".

|  |
| --- |

8° Passo:

Para que o RM possa acessar tal endereço durante a execução do conceito, a mesma deve estar presente nos arquivos de configuração do "**Host**" descritos abaixo:

* RM.Host.exe.config
* RM.Host.Service.exe.config
* RM.Host.JobRunner.exe.config

|  |
| --- |

9° Passo:

Crie uma classe com o nome "**Controle.cs**", e crie os métodos "**GetProdutos"** e "**PutProduto"** para listar os produtos e inserir um novo produto respectivamente.

Algumas observações sobre a classe e seu métodos:

* A classe a ser utilizada deverá ser pública e instânciável, ou seja não pode ser uma classe estática
* Os métodos devem conter o atributo Browsable(true) para serem reconhecidos pelo RM
* Para a **Conexão de Origem**, o método deve retornar um enumerado genérico **IEnumerable<T>**, de uma classe qualquer
* Para a **Conexão de Destino**, o método deve receber uma classe qualquer.

    [Browsable(true)]

public List<produto> GetProdutos()

    {

using (DBEntities entitie = new DBEntities())

      {

return entitie.produto.ToList();

      }

    }

    [Browsable(true)]

public bool PutProduto(produto Produto)

    {

using (DBEntities entitie = new DBEntities())

      {

        entitie.produto.Add(Produto);

        entitie.SaveChanges();

return true;

      }

    }

|  |
| --- |

A conexão DLL .Net está criado e consumindo uma tabela do banco de dados.

Compile a DLL .Net e a coloque na pasta de instalação da Biblioteca (RM.NET).

falseCópia de referências:

Além de cópiar a dll principal do projeto, também serão necessárias as dlls de terceiros das quais o seu projeto é dependente.

Para esse exemplo, devemos copiar também as dlls "EntityFramework.dll" e "EntityFramework.SqlServer.dll"

falseObservação:

Após colocar a DLL .Net no ambiente, é necessário reiniciar o Host.

# Conexão de Origem:

---

        Crie um conceito que terá como Conexão de Origem a DLL .Net criada anteriormente.

false.1° Passo: 

Acesse o módulo Integração, abra o cadastro do Conceito e clique em Novo.

Na tela de inclusão, preencha o campo nome com "**ConceitoDLLNetOrigem****"**

|  |
| --- |

2° Passo:

No menu de Conexões adicione uma Conexão de Origem do tipo "**DLL .Net**" e preencha com os seguintes dados:

* **Nome:** OrigemDll
* **DLL:** ConceitoDll.dll
* **Tipo:** ConceitoDll.Controle
* **Método:** GetProdutos

|  |
| --- |

3° Passo:

A conexão de Origem foi criada listando as propriedades do Objeto **produto**, retornado como lista na DLL .Net.

|  |
| --- |

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

Após a criação da Conexão de Origem, crie um conceito que terá como Conexão de Destino o Web Service para inserir um produto (**PutProduto**).

false.1° Passo: 

Acesse o módulo Integração, abra o cadastro do Conceito e clique em Novo.

Na tela de inclusão, Preencha o campo nome com "**ConceitoDLLNetDestino****"**

|  |
| --- |

2° Passo:

Crie um arquivo texto com a seguinte informação:

* A;Produto Novo;10;10,50;18/10/2017 01:00:00

|  |
| --- |

As informações estão separadas por ; onde:

* **A:** Identificador da Tabela
* **Produto Novo:** Coluna Nome
* **10:** Coluna quantidade\_estoque
* **10,50:** Coluna preço
* **18/10/2017 01:00:00:** Coluna data\_criação
3° Passo:

No menu de Conexões adicione uma Conexão de Origem do tipo "**Arquivo Texto"** e preencha com os seguintes dados:

* **Nome:** Origem
* **Arquivo:** Aponte para o arquivo criado anteriormente

|  |
| --- |

4° Passo:

Ainda na tela de inclusão da conexão Arquivo Texto, acesse a aba "Tabelas" e adicione uma tabela com o identificador O (mesmo do arquivo criado anteriormente) contendo 4 colunas e preencha seus respectivos nomes e tipos.

|  |
| --- |

5° Passo:

Agora adicione uma Conexão de Destino do tipo "**DLL .Net**" e preencha os seguintes dados:

* **Nome:** DestinoDll
* **DLL:** ConceitoDll.Dll
* **Tipo:** ConceitoDll.Controle

|  |
| --- |

6° Passo:

A Conexão de Destino foi criada listando o método "**PutProduto**" como uma tabela e listando as propriedades do objeto Produto.

|  |
| --- |

7° Passo:

Selecione a aba Ligações e realize as ligações da tabela de destino com a tabela de origem.

|  |
| --- |

8° Passo:

Após salvar o Conceito, volte a tela de cadastro de conceito e execute o processo em "Processos | Processar Novo Conceito". Em seguida realize a consulta na tabela no banco de dados e verifique que o produto foi inserido corretamente como mostra a imagem abaixo:

|  |
| --- |

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Conexão de Web Services

falsefalse

**Status:** Finalizado

false

**Data:** 19/10/2017

false

**Autores:**
