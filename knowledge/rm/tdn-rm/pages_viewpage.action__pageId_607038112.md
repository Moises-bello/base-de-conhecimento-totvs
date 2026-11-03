---
content_hash: 3c10c265a729936c75888577d7ebb3c84e6b7e28a948c1593b8a502b3020d1bf
fetched_at: '2026-06-29T00:10:58.809377+00:00'
page_id: '607038112'
product: rm
source: tdn-rm
title: Parâmetro "As colunas deste registro devem ser tratadas dinamicamente como
  campos complementares"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=607038112
version: 9
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

     O Parâmetro "**As colunas deste registro devem ser tratadas dinamicamente como campos complementares**" é utilizado para realizar uma concatenação entre "**Origem**" e "**Destino**", de uma forma em que as colunas da tabela selecionada pelo usuário, será imprimida no "**Destino**", juntamente com a informação descrita pelo usuário no conexão de "**Origem**".

     Quando Selecionado o parâmetro é necessário o preenchimento de dois campos: "**Aplicação**" e "**Tabela**"

     Com Isso, será criado dois campos fixos para a nova tabela criada:

* **NOMECOLUNA:** São as colunas das tabela selecionada.
* **VALORCOLUNA:** Valor do que está sendo enviado pelo usuário na Origem.

A funcionalidade desse parâmetro é realizada somente quando utilizada na conexão de "ORIGEM".

**02. EXEMPLO DE UTILIZAÇÃO**

      Como exemplo, vamos utilizar uma conexão de Origem em arquivo texto e uma conexão de Destino também em arquivo texto.

falseConfigurando o Aplicativo Confiável no ADFS1º Passo:

Após a inclusão de um novo conceito, crie uma conexão de Origem e preencha os campos necessários como: "Nome" e "Arquivo".   
Para o campo arquivo, crie um novo arquivo.txt (que esteja em uma pasta compartilhada) e selecione o mesmo como arquivo fixo para o campo".

Em seguida na aba "**Tabelas**", crie uma nova tabela, dê um nome a ela e marque o parâmetro "**As colunas deste registro devem ser tratadas dinamicamente como campos complementares**", após a marcação do mesmo, será mostrado dois novos campos para preenchimento: "**Aplicação**" e "**Tabela**".

Para nosso exemplo foi selecionada a aplicação "**Folha de Pagamento**" e tabela "**PFCOMPL**".

Não é possível alterar o Tipo das colunas, pois o mesmo respeita o tipo definido no banco de dados.

2º Passo:

Após a criação da conexão de Origem, é necessário realizar a criação da conexão de Destino.

Crie uma conexão de Destino e preencha os campos necessários como: "Nome" e "Arquivo".   
Para o campo arquivo, crie um novo arquivo.txt (que esteja em uma pasta compartilhada) e selecione o mesmo como arquivo fixo para o campo".

Em seguida na aba "**Tabelas**", crie uma nova tabela, dê um nome a ela, em seguida crie duas colunas para receber os valores da conexão de Origem.

3º Passo:

Após a criação das conexões, é necessário realizar as ligações entre elas.

Clique na aba "Ligações" do seu conceito e arraste a tabela de Destino para o espaço em branco reservado para receber essa tabela.

Em seguida, arraste a tabela de Origem para o espaço reservado em receber essa tabela (como mostra imagem abaixo) e faça a ligação dos campos.

* NOMECOLUNA → CHAVE
* VALORCOLUNA → VALOR

4º Passo:

Feita as ligações, é necessário preencher o arquivo.txt (ORIGEM) com as informações desejadas para serem concatenadas juntamente com as colunas da tabela selecionada (PFCOMPL).

As informações para cada coluna devem ser separadas por "**Ponto e Virgula (;)".**

**ORIGEM:**

**DESTINO:**

* As informações inclusas na conexão de Origem, devem seguir o tipo da coluna definido no banco de dados.
* A quantidade de coluna mostrada no Destino, dependerá da quantidade de informações descritas na Origem.   
  Como realizado no exemplo acima, foram descritas 4 informações diferente, ou seja, foram visualizadas quatro colunas diferentes no Destino.
