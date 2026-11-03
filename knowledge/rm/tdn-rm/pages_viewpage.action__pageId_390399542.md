---
content_hash: 5ad076eb14cdbc5a9d4755db9e4d63230966f2892cd7b4f598424234f81ec2cd
fetched_at: '2026-06-29T00:09:08.622027+00:00'
page_id: '390399542'
product: rm
source: tdn-rm
title: DT Orçamento de Receita
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=390399542
version: 15
---

### Orçamento de Receita

### Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção & Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Informe a rotina. | Informe o nome técnico da rotina. |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Informe a(s) rotina(s) envolvidas. | Informe o nome técnico da(s) rotina(s) envolvidas. | |  |  | |
| **Cadastros Iniciais:** | Relacione os cadastros necessários que precisam ser preenchidos antes da utilização desse requisito. |
| **Parâmetro(s):** | Informe os parâmetros utilizados. |
| **Ponto de Entrada:** | Informe o ponto de entrada relacionado (link). |
| **Tickets relacionados** | Informe o(s) chamado(s) relacionado(s). |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-4834 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQLServer e Oracle |
| **Tabelas Utilizadas:** | TTMVEXT, TPAR, |
| **Sistema(s) Operacional(is):** | Windows. |
| **Pacote:** | Informe o [linkdopacote] |

## Descrição

### 1. Parametrização

Para o correto funcionamento da rotina de Orçamento de Receita é necessário que sejam executadas algumas parametrizações. São elas:

### 1.1 Orçamento

Alteração de tamanho dos seguintes campos da tabela TPAR para 255:

DESCRICAOORCADO  
DESCRICAOORCAMENTOREAL  
DESCRICAOORCAMENTOOPCIONAL1  
DESCRICAOORCAMENTOOPCIONAL2

Os respectivos componentes na visão de parametrização tiveram seu tamanho máximo (de digitação) alterados para 50.

Caminho: Ambiente | Parâmetros | 04.02 - Controle Orçamentário.  
Grupo: Descrição do Tipo de Orçamento  
Campos: Orçado, Real, Opcional 1 e Opcional 2.

### 1.2 Natureza Orçamentária Financeira Default:

Ao parametrizar o tipo de movimento para utilizar natureza orçamentária financeira no item (Edita, Mostra ou Edita Obrigatoriamente), será exibido o parâmetro Buscar Def. no Produto, o qual é responsável por definir se o sistema deve buscar a natureza orçamentária no cadastro do produto e qual o tipo da mesma.

### **1.3 Tipo de Orçamento**

Ao selecionar o parâmetro Controla Orçamento, é possível escolher se o orçamento é de Despesa ou Receita, lembrando que é emitido alerta dizendo:

"Selecione corretamente o Tipo de Orçamento, uma vez parametrizado não será possível altera-lo." ou seja, é irreversível a escolha.

 Ao selecionar o Tipo de Orçamento **"Despesa"**, a Ação ao Exceder o Orçamento aparecerá para seleção **"Barra, Avisa ou Bloqueia"**

Ao selecionar o Tipo de Orçamento **"Receita",**a Ação ao Exceder o Orçamento aparecerá para seleção **"Avisa, Não Avisa"**

**2. Cadastros**

**2.1 Cadastro de Produto**

Foi criado um novo loockup no cadastro de Produtos que tem por finalidade filtrar toda Natureza Orçamentária/Financeira que esteja cadastrada com o tipo "A Receber" (Receita) ou "Ambos".

**OBS:** O loockup já existente continua temporariamente filtrando todos os tipos de Natureza Orçamentaria/Financeira e em breve será modificada para que filtre somente as naturezas do tipo "A Pagar" (Despesa) ou "Ambos".

Com a criação do loockup na tela de cadastro de Produtos, foram criados dois campos na tabela TPRODUTODEF para armazenar informações da Natureza de Receita (A Receber) utilizada no produto.

Os campos são:

* TPRODUTODEF.CODCOLTBORCAMENTORECEITA
* TPRODUTODEF.CODTBORCAMENTORECEITA

**2.2 Cadastro de Orçamento**

Foi criado o campo "**Tipo de Orçamento**" na tela  "**Cadastros de Valores Orçados**", o qual tem como objetivo definir se o orçamento em questão é do tipo Receita ou Despesa.

Após a criação do registro, apenas os valores orçados podem ser alterados, ou seja, todos os campos do cabeçalho serão desabilitados para edição.

### 3. Orçamento

Na visão de Consulta de Valores de Orçamento, dois novos botões foram criados, de modo que possam ser utilizados para filtrar os registros que serão exibidos na Matriz.

São eles: 'Despesa' e 'Receita', que deverão ser usados para identificar o Tipo do Orçamento.

Caso seja selecionada a opção 'Receita', os valores exibidos na coluna 'Saldo' serão multiplicados por -1, de modo a representarem este Tipo de Orçamento.

## **3.1. Realocação orçamentária e transferência de orçamento**

Foram criadas regras para impedir a Realocação e Transferência para diferentes tipos de orçamento.

Exemplo do processo de transferência:

Exemplo do processo de realocação orçamentária:

## 4. Importação

Acrescentamos o campo TIPO no layout de importação do orçamento, o mesmo será considerado tanto na planilha quanto no arquivo texto e deve ser preenchido com o valor "R" para receita ou "D" para despesa.

Caso o campo TIPO não esteja contido nos arquivos, a importação será realizada normalmente, considerando **Despesa** como default.

Colunas da planilha Excel:

CODCCUSTO  
CODTBORCAMENTO  
DATAORCAMENTO  
VALOREFEITOORCAMENTO  
CODTBGRUPOORC (Deve ser informada no arquivo quando o sistema está parametrizado para utilizar grupo orçamentário)  
TIPO

Observação: As colunas podem ser renomeadas na planilha, no entanto, a ordem deve ser mantida. Ex:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Código do Centro de Custo | Código da Natureza Orçamentária/Financeira | Data | Valor Orçado | Grupo Orçamentário | Tipo |

Colunas do Arquivo texto:

CODCCUSTO (25 caracteres)  
CODTBORCAMENTO(40  caracteres)  
DATAORCAMENTO(10  caracteres)  
VALOREFEITOORCAMENTO(20 caracteres)  
CODTBGRUPOORC(40 caracteres) (Deve ser informada no arquivo quando o sistema está parametrizado para utilizar grupo orçamentário)  
TIPO(1 caracteres)

Exemplo:

01.1                     001                                     06/10/2018100,00              001                                     R
