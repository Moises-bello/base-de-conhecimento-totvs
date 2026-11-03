---
content_hash: 0bc4adfd4ffe344cf8dd8c4e0e380f9f396a582326b9c1c9052446c32dc0f3ca
fetched_at: '2026-06-29T00:11:55.649410+00:00'
page_id: '862606129'
product: rm
source: tdn-rm
title: Objeto de Negócio Dinâmico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862606129
version: 1
---

# Introdução

---

O **Objeto de Negócio Dinâmico** é um Objeto de Negócio feito utilizando os recursos do *RM Reports* que são exclusivos ao RM. Este Objeto de Negócio é gerado automaticamente ao acelerar um relatório *RM Reports* e possui informações referentes à todos os controles do relatório. Ele se diferencia dos outros já disponíveis na integração **RM x Smart View** por permitir que ferramentas não disponíveis no Smart View (Como expressão e fórmula) sejam utilizadas para gerar e retornar dados para o relatório.

## Ações do Objeto de Negócio Dinâmico

---

Entende-se como **Ações** de um *Objeto de Negócio Dinâmico* algum comando que será executado antes da execução do relatório ou de um de seus detalhes. Atualmente, é possível apenas a execução de **StoredProcedures**, tal qual suportado pelo RM Reports.

## As fontes de dados do Objeto de Negócio Dinâmico

---

O Objeto de Negócio dinâmico suporta dois tipos específicos de **Fontes de Dados**, que são atreladas ou à um controle diretamente ou a todo um objeto aninhado, simulando uma banda/detalhe do relatório.

### Fonte de Dados de Tabela

---

Essas Fontes de Dados são fontes atreladas à tabelas da base de dados do RM. Estas tabelas serão utilizadas para construir o SQL que será executado e assim, retornar os dados de acordo com seus relacionamentos e restrições específicas.

### Fonte de Dados de Consulta SQL

---

Essas Fontes de Dados utilizam do recurso '**Consulta SQL'** do RM para gerar os dados que serão retornados para o Smart View. É menos versátil que a **Fonte de Dados de Tabela**, uma vez que utiliza de uma consulta já definida ao invés de permitir que esta seja gerada em tempo de execução, de acordo com os campos do Detalhe atrelado.

## Os Detalhes do Objeto de Negócio Dinâmico

---

Detalhes são equivalentes às bandas de um relatório. Estes normalmente estão atrelados à uma fonte de dados e definem as relações que serão realizadas para busca de dados daquela fonte de dados específicas (Chaves estrangeiras e ligações). Nos Detalhes também estão contidas as **Ações** (Comandos que serão executados logo antes do início da busca de dados do Detalhe) e os **Campos do Detalhe** propriamente ditos. Detalhes também podem conter Detalhes filhos, chamados de **SubDetalhes**, gerando assim uma árvore de dados aninhados, com suas relações construídas dinamicamente, de acordo com a necessidade de dados do Objeto de Negócio.

## Os controles do Objeto de Negócio Dinâmico

---

Entende-se por **'Controle'** os campos que serão utilizados para construção de um Recurso no Smart View. Em um Objeto de Negócio Dinâmico, diversos tipos de controles são suportados. São eles:

### Controle de Fonte de Dados (DataSourceField)

É um controle atrelado à uma coluna da **Fonte de Dados** da hierarquia de Detalhes em que este controle está inserido.

Na prática, em um Detalhe atrelado à tabela **GCOLIGADA**, um **Controle de Fonte de Dados** possível seria um controle atrelado à coluna **CODCOLIGADA**.

### Controle de Expressão (ExpressionField)

É um controle referente à uma **Expressão** do RM. A expressão contida no relatório é salva durante o processo de aceleração e executada quando necessária.

### Controle de Filtro (FilterField)

Outro controle exclusivo do RM Reports, um equivalente a este não existe no Smart View e por isso, este é acelerado como um controle próprio. Nele é salvo o valor do filtro no momento da aceleração e este ficará fixo durante toda execução deste Objeto de Negócio no Smart View

### Controle de Fórmula (FormulaField)

Similar à Expressão, este controle é responsável por executar uma **Fórmula** do RM e devolver o resultado durante a obtenção de dados do Objeto de Negócio no Smart View

### Controle sem Fonte de Dados

Estes são os controles de valor fixo existentes RM Reports, como controle de **Texto** (**Label**) e afins. Estes controles, apesar de existirem também no Layout do relatório após a aceleração, tornam se necessários no Objeto de Negócio uma vez que podem estar sendo utilizados para execuções de outros controles, como Expressões por exemplo.

### Controle de Parâmetro (ParameterField)

Estes são controles responsáveis por entregar o valor de um parâmetro específico passado durante a execução do Objeto de Negócio

### Controles de Fontes de Dados Relacionais (RelationalDataSourceField)

Estes controles são responsáveis por buscar o valor de colunas referentes à Fontes de Dados que podem ser relacionadas à Fonte de Dado do Detalhe em que o controle está inserido, como o **Controle Avulso** do RM Reports. Na prática, caso o Objeto de Negócio possua por exemplo Fontes de Dados de Tabela da tabela **PFUNC** e **PPESSOA**, é possível que um **Controle de Fonte de Dados Relacional** inserido em um Detalhe que está atrelado a **PFUNC** busque colunas da **PPESSOA**, uma vez que existe um chaveamento entre essas duas tabelas (**PPESSOA.CODIGO → PFUNC.CODPESSOA**).

### Controle de Variável (variableField)

Este controle é responsável por retornar algumas informações contextuais, de acordo com a execução do relatório. e é equivalente ao controle **Variável** do RM Reports.

# Considerações Finais

---

É necessário reforçar que o Objeto de Negócio Dinâmico existe para facilitar o uso de recursos do RM em conjunto com o Smart View, porém este não funcionará como um executor em escala 1:1 em relação ao RM Reports, principalmente em relação à relatórios acelerados. Para mais informações, acesse a página de .

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2410

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
