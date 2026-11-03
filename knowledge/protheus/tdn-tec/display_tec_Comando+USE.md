---
content_hash: df78a2a44643f983abbb2af64c37bdb375a1cbf24d083766ba113073f1ebd076
fetched_at: '2026-07-02T19:24:24.958001+00:00'
page_id: '492707035'
product: protheus
source: tdn-tec
title: Comando USE
type: documentation
url: https://tdn.totvs.com/display/tec/Comando+USE
version: 2
---

### Sintaxe mínima

```
USE
```

* Veja informações adicionais da documentação.

### Sintaxe completa

```
USE [ <cTabela> [ALIAS <cAlias>] <SHARED|EXCLUSIVE> [READONLY] [NEW] [VIA <cRDD>] ]
```

### Parâmetros

| Cláusula | Tipo | Obrigatório | Descrição |
| --- | --- | --- | --- |
| <cTabela> | C | S | Expressão caractere, constante ou variável, que contém o nome da tabela a ser aberta. |
| ALIAS <cAlias> | C | N | Expressão caractere, constante ou variável, que contém o nome do *Alias* – ou apelido – que a tabela será aberta. Caso não especificado, o nome da tabela será usado como o *Alias* . |
| SHARED | EXCLUSIVE |  | S | Apenas uma das cláusulas pode ser especificada. Elas indicam o modo de abertura do arquivo em questão. Em modo SHARED (ou compartilhado) uma tabela pode ser aberta por mais de um processo, desde que não exista nenhum processo com a tabela em modo exclusivo. |
| READONLY |  | N | Caso especificado, indica que a tabela será aberta apenas para leitura. Por padrão, caso esta cláusula não seja especificada, a tabela é aberta em modo de leitura e escrita. |
| NEW |  | N | Caso especificado, indica que uma nova área de trabalho (WorkArea) deve ser criada para a abertura da tabela. Caso não especificado, a área de trabalho atual será usada, e se houver uma tabela aberta na área de trabalho atual, a mesma será fechada. |
| VIA <cRdd> | C | N | Indica qual será o Driver utilizado para abrir a tabela informada. Caso este não seja especificado, será usado o Driver default do Protheus configurado para arquivos locais – vide configuração do Application Server. |

* A sintaxe mínima do comando USE – sem nenhum parâmetro – fecha a tabela aberta na área de trabalho atual, do mesmo modo que a função
* Uma vez especificada uma tabela a ser aberta, usando a sintaxe completa, este comando será traduzido internamente para chamar a função
* Recomendamos fortemente, como uma boa prática de programação, utilizar o comando USE sempre especificando a cláusula **NEW**, para deixar o código mais claro e evitar o fechamento indesejável ou acidental de um alias aberto nela. Quando houver a necessidade do fechamento de um Alias, realize esta operação explicitamente. –  usando o comando USE sem parâmetros ou a função
* Este comando foi concebido para receber os parâmetros do tipo caractere sem a utilização de aspas. Quando necessário ou desejável utilizar o conteúdo de uma variável do tipo caractere como parâmetro, a variável deve estar cercada por parênteses. Veja mais detalhes nos exemplos.
* Como a chamada do comando é traduzida em tempo de compilação para a função , acesse a documentação da mesma para verificar os demais comportamentos e informações adicionais da função.

### Exemplos
