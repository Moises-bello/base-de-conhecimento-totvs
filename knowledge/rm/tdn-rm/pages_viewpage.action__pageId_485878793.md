---
content_hash: 35ec302dbd49091e8bf8a247de16314a799ca9f02fd2cd7c2a231eb95fa5a216
fetched_at: '2026-06-29T00:10:20.129179+00:00'
page_id: '485878793'
product: rm
source: tdn-rm
title: Exemplo de Utilização de Conceito Utilizando a Conexão de Origem Data Server
  (N Tabelas)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=485878793
version: 36
---

# Índice:

---

.\*ndice:

# Objetivo:

---

        Esta página tem por objetivo apresentar um exemplo de Conceito utilizando a Conexão de Origem Data Server (N tabelas) e Conexão Destino arquivo texto.

# Exemplo Prático:

---

        Neste exemplo, iremos exportar dados da tabela de produto utilizando a Conexão Origem Data Server e Conexão Destino arquivo texto.

falseCadastrando Conceito11° Passo

Cadastre o Conceito utilizando os dados abaixo:

* **Nome:** Origem DataServer | Destino TXT - Tabela Produtos
* **Sistema:** T
* **Descrição:** Origem DataServer | Destino TXT - Tabela Produtos
22° Passo

Crie uma Conexão Origem do tipo Data Server RM.NET, conforme imagem abaixo:

Depois de feita a seleção da opção acima, apresentará uma janela para o usuário. Nesta, vamos configurar a conexão.

**Nome:** Origem\_DataServer  
**Servidor:** EstPrdDataBR (Produtos)

falseImportante/Saiba Mais

 Para consultar o nome do DataServer/Action de determinado cadastro no RM, acesse a visão de cadastro e pressione as teclas Ctrl + Alt + F9. Uma janela abrirá contendo a informação do DataServer/Action.

33° Passo

Depois de criada a Conexão Origem temos acesso a diversas tabelas ligadas ao DataServer.

44° Passo

Agora, vamos configurar a Conexão Destino. Crie uma conexão do tipo Arquivo Texto, conforme imagem abaixo:

Na janela que será aberta, preencha os seguintes campos:

* **Nome:** Destino\_TXT
* **Tipo de Arquivo:** Arquivo separado por delimitador
* **Delimitador:** |
* **Aquivo:** Diretório: C:\TBC\

Aba Tabelas

* Adicione uma Tabela
  + **Nome:** Produtos
* Adicione as colunas
  + IDPRD
  + CODIGOPRD
  + DESCRICAO
  + TEMPOMAX

Depois de realizar o cadastro, a Conexão Destino retornará a seguinte estrutura:

55° Passo

A próxima etapa será realizar a lição entre a Conexão Origem e a Conexão Destino. Acesse a aba Ligações, localizada no lado esquerdo superior do cadastro do conceito.  
Ao acessar a aba, a mensagem “Arraste uma tabela de destino aqui” será apresentada. Clique na tabela de destino, segure e arraste para a mensagem mencionada.

Para incluir os campos da tabela de origem, primeiramente selecione a tabela TPRODUTO e arraste para a parte superior direita da tabela acima.

Os campos podem ser associados através do recurso arraste e solte.

O único campo que não estará presente na tabela TPRODUTO é o TEMPOMAX.

66° Passo

Para buscarmos a informação deste grupo, vamos utilizar a ferramenta Operações | Lookup, presente no lado direito inferior do conceito.

Ao selecionar a opção Lookup, uma janela será apresentada.

Preencha os campos conforme abaixo:

77° Passo

Com o Lookup devidamente configurado, volte na aba Ligações.

Arraste o operador Lookup para o campo Origem do TEMPOMAX.

88° Passo

Ao realizar o procedimento acima, teremos que associar as chaves primárias para que o campo TEMPOMAX seja retornado corretamente.

Na sequencia, salve o conceito.

99° Passo

Na visão do cadastro do Conceito, selecione o registro do exemplo criado, clique em Processos | Processar Novo Conceito. Avance no assistente de execução até finalizá-lo.

Verifique o arquivo criado na pasta TBC

Nas versões atuais do sistema, é possível configurar a quantidade de registros por transação. Essa configuração interfere na opção de Continuar execução em caso de erros. Para mais informações, consulte: .

Na conexão DataServer a configuração para parar ou não a execução do conceito em caso de erros é sobreposta pela configuração feita no conceito.

**Novidades!**

* A partir dos patches mais recentes da versão 12.1.28 estão disponíveis os parâmetros **Permitir Paginação**e **Tamanho da página** na conexão origem**.**

Quando estão habilitados, a leitura na base será feita de forma paginada. Ou seja, em vez de fazer a leitura de todos os dados de uma vez, o sistema buscará a quantidade de registros determinado no campo Tamanho da página, podendo ser de 10 em 10, por exemplo.

O uso do recurso de paginação reduzirá a quantidade de memória usada pelo processo de extração de dados pela conexão de origem.

# Parâmetros e Filtro

Selecionando a aba de Parâmetros serão apresentadas opções para definição de um Parâmetro relacionado ao Data Server ou definir um Filtro Fixo

Ao selecionar a opção Fixo, será apresentada a tela padrão de Definição do Filtro, onde pode ser gerada uma expressão.

Versão 2402

A partir da versão 12.1.2402, patch 106  
As colunas adicionadas na expressão serão acrescentadas com o Alias da tabela, conforme apresentado no texto exibido ao passar o mouse sobre o campo em negrito em Coligada.  
Isto para evitar erro na execução da query quando em tabelas relacionadas existe mais de uma coluna com o mesmo nome.

Exemplo:

Antes desta versão poderia ocorrer um erro na execução do conceito, como: **"Ambiguous colunm name 'CODCOLIGADA'"**, pois na query o filtro estaria sem o Alias, por exemplo:  
Where CODCOLIGADA = 1

Sendo que o correto deve ser conforme exibido no texto sobre o campo Coligada com o Alias adicionado, por exemplo:  
Where FLAN.CODCOLIGADA = 1

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Conexão Data Server (N Tabelas)

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
