---
content_hash: 236a127ceaccf0eb83a95b35347083ebd83d293ed57ca6803c48a6e5fefc764a
fetched_at: '2026-06-29T00:12:08.407031+00:00'
page_id: '933149762'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - Shopping - Relatórios - Relatório Dinâmico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=933149762
version: 31
---

### Introdução

---

O relatório dinâmico visa de forma transparente e simples, permitir que sejam inseridos componentes que irão compor a saída do relatório, isto é, seu resultado final apresentado. Desta forma, temos uma interface que pode ser confeccionada e customizada em poucos passos, trazendo um dinamismo e maior rapidez na execução dos relatórios do sistema.  Dessa forma podem ser passados parâmetros de seleção por contratos, subunidades, cliente/fornecedor, entre outros.

### Como utilizar

---

O relatório dinâmico deve ser acessado em Shopping / Relatórios / Relatório Dinâmico. Este menu possui permissão, então o usuário deve ter a sua respectiva permissão habilitada para utilizá-lo.

É importante frisar que toda a modificação resultante na tela do relatório dinâmico deve ser primeiro realizada nos relatórios que irão fornecer os parâmetros para a exibição da tela. Abaixo vamos mostrar como realizar essa alteração.

**Tipos de Parâmetros**

**Multi Record (MRE\_)**  
Utilizado quando é necessário selecionar **mais de um registro** em um mesmo parâmetro.  
Esse tipo de parâmetro é identificado pelo prefixo **`MRE_`** e deve ser aplicado em consultas SQL que utilizem operadores como **`IN`** ou **`FILTER`**, conforme exemplificado na Tabela abaixo.

**Lookup (LKP\_)**  
Utilizado quando é permitida a seleção de **apenas um único registro** no componente.  
É identificado pelo prefixo **`LKP_`** e possui uma regra específica de uso: ao criar o relatório, o parâmetro deve ser nomeado com o prefixo **`LKP_`**, e a sentença SQL deve utilizar o parâmetro conforme o padrão definido para cada Tabela, conforme listado abaixo.

**Tabela Definição de Campos**

| Tabela | Descrição | Parâmetro MULTIRECORD (IN) | Parâmetro MULTIRECORD (FILTER) | Parâmetro LOOKUP | |
| --- | --- | --- | --- | --- | --- |
| **Parâmetro no Relatório** | **Parâmetro na Consulta SQL** |
| FCFO | Cliente / Fornecedor | MRE\_XCLIENTE\_IN | MRE\_XCLIENTE\_FILTER | LKP\_XCLIENTE | :CODCOLCFO :CODCFO |
| XALGCONTRATOADMPROPRIETARIO | Locador do Contrato de Administração | MRE\_XLOCADOR\_IN | MRE\_XLOCADOR\_FILTER | LKP\_XLOCADOR | :CODCOLCFOPROP :CODCFOPROP |
| XALGCONTRATOLOCLOCATARIO | Locatário do contrato de locação | MRE\_XLOCATARIO\_IN | MRE\_XLOCATARIOFILTER | LKP\_XLOCATARIO | :CODCOLCFOLOCATARIO :CODCFOLOCATARIO |
| FLAN | Lançamentos | MRE\_IDLAN\_IN | MRE\_IDLAN\_FILTER | LKP\_IDLAN | :CODCOLLAN :IDLAN |
| XALGIMOVEL | Imóvel | MRE\_XIMOVEL\_IN | MRE\_XIMOVEL\_FILTER | LKP\_XIMOVEL | :CODCOLIMOVEL :CODIMOVEL |
| XCONTRATOLOC | Contrato de Locação | MRE\_XCONTRATOLOC\_IN | MRE\_XCONTRATOLOC\_FILTER | LKP\_XCONTRATOLOC | :CODCOLCONTLOC :CODCONTLOC |
| XEMPREENDIMENTO | Empreendimento | MRE\_XEMPREENDIMENTO\_IN | MRE\_XEMPREENDIMENTO\_FILTER | LKP\_XEMPREENDIMENTO | :COD\_PESS\_EMPR |
| XUNIDADE | Unidades | MRE\_XUNIDADE\_IN | MRE\_XUNIDADE\_FILTER | LKP\_XUNIDADE | :COD\_PESS\_EMPR :NUM\_UNID |
| XSUBUNIDADE | Subunidades | MRE\_XSUBUNIDADE\_IN | MRE\_XSUBUNIDADE\_FILTER | LKP\_XSUBUNIDADE | :COD\_PESS\_EMPR :NUM\_UNID :NUM\_SUB\_UNID |
| XCONDITEMCOBR | Item de Cobrança | MRE\_XCONDITEMCOBR\_IN | MRE\_XCONDITEMCOBR\_FILTER | LKP\_XCONDITEMCOBR | :CODITEMCOBR |
| FCXA | Contas/Caixa | MRE\_FCXA\_IN | MRE\_FCXA\_FILTER | LKP\_FCXA | :CODCOLCXA :CODCXA |
| GCCUSTO | Centros de Custo | MRE\_GCCUSTO\_IN | MRE\_GCCUSTO\_FILTER | LKP\_GCCUSTO | :CODCOLCCUSTO :CODCCUSTO |
| TTBORCAMENTO | Natureza Orçamentária/Financeira | MRE\_TTBORCAMENTO\_IN | MRE\_TTBORCAMENTO\_FILTER | LKP\_TTBORCAMENTO | :CODCOLNATFINANCEIRA :CODNATFINANCEIRA |

**Tipos de Parâmetros Compatíveis**

Os tipos de parâmetros listados abaixo são compatíveis e podem ser utilizados como **componentes na geração de relatórios dinâmicos**.

| Tipo de Parâmetro | Descriçao |
| --- | --- |
| Decimal | Utilizado para valores numéricos com casas decimais e alta precisão. |
| Float | Utilizado para valores numéricos decimais de ponto flutuante. |
| Duplo (Double) | Utilizado para valores numéricos decimais com maior precisão que o Float. |
| DateTime | Utilizado para data e hora. |
| Texto (String) | Utilizado para informações textuais. |
| Int (Inteiro) | Utilizado para valores numéricos inteiros. |

**Exemplos de Utilização**

Multi Record (MRE\_)

Utilize o **Multi Record** quando o parâmetro permitir a seleção de **vários registros**.

**Parâmetro Inserido no Relatório:**  
MRE\_XCONTRATOLOC\_IN

**Cenário:**  
O usuário deseja selecionar um ou mais contratos.

**Exemplo de SQL:**

sqlDJango1Select

**Atenção:** o uso do operador **`FILTER`** pode impactar o desempenho, dependendo da complexidade da sentença SQL e da quantidade de registros retornados para aplicação do filtro.

Lookup (LKP\_)

Utilize o **Lookup** quando o parâmetro permitir a seleção de **apenas um registro**.

**Parâmetro Inserido no Relatório:**  
LKP\_GCCUSTO

**Cenário:**  
O usuário precisa filtrar por um centro de custos.

**Exemplo de SQL:** Na sentença SQL tem que usar os parâmetros definidos para Lookup na tabela acima na coluna "**Parâmetro na Consulta SQL**".

sqlDJango1SelectJuntos (Multirecord e Lookup)

**Parâmetros Inseridos no Relatório:**  
MRE\_IDLAN\_IN e LKP\_GCCUSTO

**Cenário:**  
O usuário necessita filtrar os dados por um **centro de custos específico** e, simultaneamente, selecionar **um ou mais lançamentos** associados ao centro de custos informado.

**Exemplo de SQL:**

sqlDJango1Select

**Resumo Comparativo**

| Tipo | Prefixo | Quantidade de Registros | Uso no SQL |
| --- | --- | --- | --- |
| Multi Record | MRE\_ | Múltiplos | IN / FILTER |
| Lookup | LKP\_ | Único | = |

Recomendações de configuração

É fundamental verificar sempre o tipo do parâmetro informado e garantir que ele seja compatível com o relatório dinâmico utilizado.

### Como fazer (Relatório com Sentença SQL IN e Componente MultiRecord)

---

Dada as tabelas acima, eu quero que o meu relatório me permita escolher vários contratos de locação que irão fazer parte do resultado dele. Este relatório possui uma sentença SQL com uma clausula IN, então neste caso devemos proceder da seguinte maneira

Para isso então estou dizendo que deve existir o parâmetro MRE\_XCONTRATOLOC\_IN no relatório como mostra a imagem abaixo:

Na minha cláusula **WHERE** eu preciso utilizar obrigatoriamente a função *string\_split*. dessa forma, passamos os parâmetros como abaixo:

sql

Para entender mais sobre essa função, consulte a página abaixo:

[Central de Atendimento - Consultas com IN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15817743667223-Cross-Segmentos-Backoffice-RM-BI-Cl%C3%A1usula-IN-em-consulta-SQL)

O resultado da tela do relatório dinâmico será a seguinte, possibilitando a seleção de vários contratos de locação que irão compor a saída do relatório:

Em bases Oracle, há uma diferença, onde devemos primeiro criar uma função que "imite" a string\_split diretamente no banco de dados:

sql

Após a criação da função, a cláusula **WHERE** da consulta SQL deve obrigatoriamente seguir o padrão:

sql

### Como fazer (Relatório com Sentença SQL FILTER e Componente MultiRecord)

---

Para esse relatório dinâmico ser criado, deve existir o parâmetro MRE\_XCONTRATOLOC\_FILTER no relatório como mostra a imagem abaixo:

O resultado da exibição no relatório dinâmico será o mesmo da exibição quando temos um componente IN, entretanto o resultado da consulta SQL do relatório será filtrada de acordo com os contratos selecionados. Não é necessário utilizar a função split.

### Como fazer (Relatório com Componente Lookup)

---

Neste exemplo, eu quero que o meu relatório me permita escolher somente um contrato de locação que irão fazer parte do resultado dele através de uma lookup. Então neste caso devemos proceder da seguinte maneira.

Para isso então estou dizendo que deve existir o parâmetro LKP\_XCONTRATOLOC no relatório como mostra a imagem abaixo:

Na consulta SQL deste relatório, devemos também passar na cláusula WHERE o parâmetro em questão:

sql

Dessa forma, ao executar o relatório dinâmico, teremos o seguinte resultado:

Importante

* Caso seja utilizado algum componente cujo tipo de parâmetro é Multirecord e Filter, os campos devem obrigatoriamente estar na consulta SQL do relatório. Caso não estejam, não será possível gerar o filtro de forma adequada. O sistema irá emitir uma mensagem de alerta nestes casos.
* Para evitar problemas de compatibilidade do relatório dinâmico e as consultas é imprescindível que o relatório e a consulta sejam confeccionados na mesma Coligada.
