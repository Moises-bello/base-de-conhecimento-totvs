---
content_hash: 7f6f51117d15b2839347a9967f34757adeeef501c5deb0950b6bd8ff98ea4e86
fetched_at: '2026-06-29T00:05:58.293912+00:00'
page_id: '185748495'
product: rm
source: tdn-rm
title: DataServers RM - Problemas comuns durante a codificação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185748495
version: 4
---

# Erro: *“Ocorreu um erro ao efetuar a leitura do registro: There is no row at position 0.”*

---

O problema em questão ocorre quando as tabelas do DataServer estão nulas ou a contagem das Rows é igual a zero. Quando o código tenta acessar as tabelas não encontra linhas na tabela, gerando a exceção. Alguns dataservers RM não possuem esta validação, pois já se pressupõe que os dados venham devidamente preenchidos nas tabelas ainda no lado cliente.

**Solução/Sugestão de Ajuste:** Efetuar o tratamento verificando se existem rows e tabelas preenchidas no DataSet:

false

if(dataSet.Tables["VTUAVCONH"] != null &&

dataSet.Tables["VTUAVCONH"].Rows.Count > 0){...}

# Erro: *“Missing the DataColumn 'FILTROALUNOS' in the DataTable 'VTurmas' for the SourceColumn 'FILTROALUNOS'”*

---

Tal situação ocorre quando é enviada uma mensagem SOAP para o DataServer via WebService, e na mensagem não são acrescentadas todas as colunas exigidas pelo DataServer. As colunas aqui se referem àquelas definidas pelo DataSet utilizado pelo DataServer, no caso, o dataset ‘VTurmas’.

**Solução/Sugestão de Ajuste:** Basta adicionar à mensagem SOAP as colunas e seus valores exigidos pelo DataServer. Para saber quais colunas são exigidas pelo dataserver basta efetuar uma requisição do *ReadView* e obter a estrutura XML. Quando a estrutura não for suficiente, basta adicionar a coluna exigida ao XML e o valor.

# Erro:*“A coluna 'CODCOLIGADA' não pertence à tabela VTurmas”*

---

 Semelhante à situação acima, o erro é decorrente à falta de uma coluna específica na estrutura de gravação do registro.

**Solução/Sugestão de Ajuste:** Basta acrescentar a coluna no XML para envio da mensagem.

# Erro:*“Violação de chave estrangeira”*

---

Essa é uma clássica Violação de chave estrangeira, como ocorre no sistema. No SoapUI torna-se difícil a análise de quais campos violam a chave, por não possuir uma interface amigável para este fim.

**Solução/Sugestão de Ajuste:** Para esta situação, basta avaliar a mensagem de erro e identificar entre quais tabelas está gerando a violação de chave.

# Erro: **“***Violação de concorrência: UpdateCommand afetou 0 dos registros 1 esperados.”*

---

Este é um caso onde tentamos efetuar um UPDATE cujo registro possui tabela filha, tal como uma tabela complementar. Algumas estruturas de SaveRecord exigem a atualização de suas tabelas filhas. O que ocorre é que o SELECT que verifica a existência do registro na base estava incorreto, e não retorna registro algum, invalidando o UPDATE. As colunas que estão preenchidas incorretamente e que invalidam o UPDATE são as colunas de controle.

**Solução/Sugestão de Ajuste:** Sugere-se verificar se os datasets estão com chave primária definida e se as tabelas do banco de dados também tem chave primária definida. Essa exceção pode ocorrer por concorrência ou outra coisa que pode estar alterando o dataset ou a query, fazendo com que a mesma não execute.

# Erro: *“Ocorreu um erro ao efetuar a leitura do registro: A tabela [VTurmas] da Relation Pai não possui nenhum registro”.*

---

Esta situação ocorre quando se tenta efetuar a atualização de um registro cujo dataset carrega uma tabela pai e outra filha.

**Solução/Sugestão de Ajuste:** Internamente já é realizado o tratamento desta situação. Entretanto pode ocorrer que o sistema obrigue a inserção dos dados filhos antes dos dados pai. Portanto sugere-se uma maior investigação, por parte do produto, para encontrar o agente causador do problema.

# Erro:*“A cadeia de caracteres de entrada não estava em um formato incorreto.”*

---

Esta inconsistência se dá quando o dado de algum campo não se encontra no formato esperado pelo DataServer (String, Int16, DateTime...), e por sua vez não possibilita a inserção ou manutenção do registro.

**Solução/Sugestão de Ajuste:** Localizar e efetuar o ajuste do dado no XML para o formato exigido pelo DataServer.

# Erro:*“Coluna 'CODCOLIGADA' é somente leitura.”*

---

Tal mensagem de erro pode ocorrer em fontes do Conector, pois não esperado que a coluna no ponto de Inserção/Edição (via *SaveRecord*) esteja como *“Somente Leitura”*, gerando assim a exceção ao tentarmos incluir dados no sistema.

**Solução/Sugestão de Ajuste:** Sugere-se verificar os dataservers (ReadRecord, xsd, DataProps) afim de encontrar alguma regra que esteja modificando a Propriedade ReadOnly da Coluna CODCOLIGADA, ou qualquer outra nesse mesmo cenário.
