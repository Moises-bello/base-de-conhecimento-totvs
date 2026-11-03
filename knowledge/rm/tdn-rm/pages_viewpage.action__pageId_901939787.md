---
content_hash: abc93c62fb408696d88fe20ca79cc113da0f3da27fe974c06ae90b3349f56759
fetched_at: '2026-06-29T00:12:02.396083+00:00'
page_id: '901939787'
product: rm
source: tdn-rm
title: Objeto de Negócio - Relatório ISS (Lançamentos Entrada/Saída)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=901939787
version: 14
---

Conteúdo

Conteúdo

# 1. Visão Geral

O objeto de negócio ISS Lançamentos Municipais Entrada/Saída retorna os dados dos lançamentos cadastrados dentro do período desejado agrupados por tipo de recolhimento que não tenham sido Cancelados.  
Este objeto está disponível pela ferramenta "Smart View". Serão disponibilizados pelo TOTVS Compartilhamento relatórios, tabelas dinâmicas e visões de dados que utilizam este objeto, mas também há a possibilidade de criar recursos personalizados com este objeto de negócio.

Cabe lembrar que este objeto de negócio possui o controle de segurança por perfil o que significa que o usuário deve possuir permissão no item "Encerrar período de apuração" (Gestão fiscal | Obrigações principais | Apuração | Período de apuração | Encerrar período de apuração) para conseguir acessar relatórios, tabelas dinâmicas e/ou visões de dados que utilizem este objeto de negócio.

# 2. Relatórios Disponíveis para o ISS

## 2.1 Tabela Dinâmica

É possível ter várias perspectivas diferentes sobre suas informações ao vincular o objeto de negócio de Lançamentos à uma tabela dinâmica.

Exemplo de tabela dinâmica

## 2.2 Visão de dados

A visão de dados permite uma visualização mais detalhada e extensa de cada informação.

Exemplo de visão de dados

## 2.3 Relatórios

250

# 3. Campos do objeto de negócio

Atualmente, são disponibilizados os seguintes campos referentes aos lançamentos no objeto de negócio:

Tabela de campos

| Nome | Tipo | Coluna |
| --- | --- | --- |
| Data de Entrada/Saída | Data | DLAF.DATAES |
| Data Emissão | Data | DLAF.DATAEMISSAO |
| Número | Inteiro | DLAF.DOCINI |
| Código do Cliente/Fornecedor | Literal | FCFO.CODCFO |
| Nome do Cliente/Fornecedor | Literal | FCFO.NOME |
| UF do Cliente/Fornecedor | Literal | FCFO.CODETD |
| Numero do Item | Inteiro | -- |
| Produto | Literal | TPRODUTO.NOMEFANTASIA |
| Tipo Recolhimento | Literal | DTRBITEM.TIPOTRIBUTACAO |
| Base de Cálculo | Decimal | DTRBITEM.BASETRN |
| Alíquota | Decimal | DTRBITEM.ALQTRB |
| Valor do Imposto | Decimal | DTRBITEM.VALORTRB |
| Isento/Não Tributada | Decimal | DTRBITEM.VLRISENTO |

# 4. Outras informações

### Permissão

Para utilizar este Objeto de Negocio é necessário que o usuário tenha permissão em "*Gestão fiscal | Obrigações principais | Apuração | Período de apuração | Encerrar período de apuração*"

### Parâmetros de entrada

Os parâmetros abaixo serão solicitados ao executar o Objeto de Negócios e todos são obrigatórios.

* Código da coligada;
* Código da filial;
* Data inicial período;
* Data final período;
* Tipo do lançamento

### Seleção de Lançamentos

A seleção dos Lançamentos Fiscais de Entrada e Saída será feita de acordo com os parâmetros informados no *TOTVS Gestão Fiscal  | Processo 03.02.03 | Etapa “Apur. ISS por Filial” | Datas Apuração doISS*.

O Objeto de Negócio irá gerar dados considerando as opções *Data de Emissão* ou *Data de Entrada/Saída* definidos no parâmetro.

⚠ **Atenção:**

* Caso a opção de parâmetro seja configurada como **Data de Vencimento**, o relatório **não exibirá dados**.
* Este Objeto de Negócio **não considera lançamentos com status de cancelado**.
