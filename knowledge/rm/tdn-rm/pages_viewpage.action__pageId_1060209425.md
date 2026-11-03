---
content_hash: c28925185ebc8182e7e59d35fb14477eaec533dc002176d60ed9e5a9460f5d26
fetched_at: '2026-06-29T00:05:52.764402+00:00'
page_id: '1060209425'
product: rm
source: tdn-rm
title: Objeto de negócio - Lançamentos Fiscais CBS/IBS (nível item)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1060209425
version: 11
---

Conteúdo

Conteúdo

# 1. Visão Geral

O objeto de negócio de Lançamentos Fiscais CBS/IBS efetua a extração dos lançamentos fiscais e seus itens considerando os tributos CBS e IBS (IBS-E e/ou IBS-M) considerando o coligada e períodos desejados obedecendo os filtros fornecidos. Este dados serão uteis para o preparo da Apuração Assistida do IBS/CBS da Reforma Tributária então o sistema deve garantir a extração dos valores tributários considerando o detalhamento de itens das notas.

Chegamos a um nível de detalhamento nos itens/tributos dos lançamentos para garantir a precisão do imposto.

Este objeto está disponível pela ferramenta "Smart View". Serão disponibilizados pelo TOTVS Compartilhamento relatórios, tabelas dinâmicas e visões de dados que utilizam este objeto, mas também há a possibilidade de criar recursos personalizados com este objeto de negócio.

A extração de lançamentos fiscais considerando itens com tributos CBS/IBS prioriza a data de entrega e/ou emissão para fins de apropriação tributária.

É importante, para garantir o compliance, que a extração seja realizada preferencialmente em períodos já conferidos e encerrados no RM Fiscal. O objeto de negócio disponível no Smart View permite a criação de tabelas dinâmicas para conferência de valores de operação *vs*. valores de imposto.

# 2. Relatórios Disponíveis com o ON Lançamentos Fiscais CBS/IBS

## 2.1 Tabela Dinâmica

É possível ter várias perspectivas diferentes sobre suas informações ao vincular o objeto de negócio de Lançamentos CBS/IBS à uma tabela dinâmica.   
Neste exemplo, foram realizados agrupamentos aninhados por Filial, Tipo de Lançamento, Natureza e Número do Documento para obter a sumarização de seus totais.

Exemplo de tabela dinâmica

## 2.2 Visão de dados

A visão de dados permite uma visualização mais detalhada e extensa de cada informação.   
No exemplo abaixo, ao vincular o objeto de negócio de Lançamentos CBS/IBS a uma visão de dados, foram filtradas as informações referentes apenas aos valores da filial 1.

Exemplo de visão de dados

 

# 3. Parâmetros

Há quatro parâmetros a serem preenchidos, obrigatoriamente, para retornar dados neste objeto de negócio, sendo eles:

* Código da coligada;
* Mês/Ano inicial período;
* Mês/Ano final período;

* Lógica do período de recuperação dos lançamento: Aplica-se o período à Data de Previsão de Entrega (caso esteja informada no lançamento) e à Data de Emissão, isto é, se a data de previsão ou a data de emissão estiver dentro do período então o registro é considerado;
* Os parâmetros Coligada e Período (Mês/Ano inicial e final) são de preenchimento obrigatório;
* Não possui a opção de recuperação de registros multi-coligada, isto é, apenas uma coligada por vez (de acordo com a informada no parâmetro);
* Apenas lançamentos com Status "Normal";
* Apenas lançamentos/notas cujos itens tenham tributos como tipo base o CBS ou IBS.

# 4. Campos e Filtros do objeto de negócio

Atualmente, são disponibilizados os seguintes campos referentes aos lançamentos no objeto de negócio com os indicativos de quais podem ser utilizados em filtros:

Tabela de campos

| Nome | Tipo | Filtrável?¹ | Coluna |
| --- | --- | --- | --- |
| Código Coligada | Inteiro | Sim | DLAF.CODCOLIGADA, |
| Código Filial | Inteiro | Sim | GFILIAL.CODFILIAL |
| Nome Filial | Literal |  | GFILIAL.NOME (NOMEFILIAL) |
| Código Filial SCP | Inteiro |  | FILIALSCP.CODFILIAL (CODFILIALSCP) |
| Nome Filial SCP | Literal |  | FILIALSCP.NOME (NOMEFILIALSCP) |
| Id Lançamento Fiscal | Inteiro |  | DLAF.IDLAF |
| Id do Agrupamento de Lançamento | Inteiro |  | DLAFAGRUP.IDLAFAGRUP |
| Data Entrada/Saída | Data |  | DLAF.DATAES |
| Data Emissão | Data | Sim | DLAF.DATAEMISSAO |
| Data prevista/previsão entrega | Data | Sim | DLAF.DATAENTREGA |
| Código tipo documento | Literal | Sim | FTDO.CODTDO |
| Descrição tipo documento | Literal |  | FTDO.DESCRICAO (DESCRICAOTDO) |
| Documento Inicial | Literal |  | DLAF.DOCINI |
| Documento Final | Literal |  | DLAF.DOCFIM |
| Coligada Cli/For | Inteiro |  | FCFO.CODCOLIGADA  (CODCLIGADACFO) |
| Código Cli/For | Literal | Sim | FCFO.CODCFO |
| Nome Cli/For | Literal |  | FCFO.NOME (NOMECFO) |
| Id Natureza | Inteiro |  | DCFOP.IDNAT |
| Descrição Natureza | Literal |  | DCFOP.NOME (NOMENAT) |
| Código Natureza | Literal | Sim | DCFOP.CODNAT |
| Tipo Lançamento | Literal | Sim | DLAF.TIPOLF |
| Número do item | Inteiro |  | DITEM.NUMITEM |
| Identificador do produto | Inteiro | Sim | TPRODUTO.IDPRD |
| Código do produto | Literal |  | TPRODUTO.CODIGOPRD |
| Nome do produto (nome fantasia) | Literal |  | TPRODUTO.NOMEFANTASIA (NOMEPRD) |
| Tipo do produto (produto ou serviço) | Literal |  | DCLASSIFBENSSERVICO.TIPO TIPOPRD |
| NCM do produto | Literal |  | DCLASSIFBENSSERVICO.NUMERO (NCM) |
| NBS do produto | Literal |  | DCLASSIFBENSSERVICO.NBS |
| Código do tributo | Literal | Sim | DTRBITEM.CODTRB |
| Código Situação Tributária (CST) | Literal | Sim | DTRBITEM.SITTRIBUTARIA |
| Classificação tributária (cCLASSTRIB) | Literal | Sim | DTRBITEM.CLASSTRIB |
| Base de Cálculo Tributo | Decimal |  | DTRBITEM.BASETRB |
| Valor do tributo | Decimal |  | DTRBITEM.VALORTRB |
| Alíquota do Tributo | Decimal |  | DTRBITEM.ALIQTRB |
| Chave de acesso | Literal |  | DLAF.CHAVEACESSONFE |
| UF da Operação | Literal |  | DVIEWMUNICIPIOS.CODETDMUNICIPIO |
| Munícipio da Operação | Literal |  | DVIEWMUNICIPIOS.NOMEMUNICIPIO |
| Código Munícipio da Operação | Literal |  | DVIEWMUNICIPIOS.CODIFICACAO |
| UF / Munícipio Operação | Literal |  | DLAF.CHAVEACESSONFE |

¹: Campos que podem ser filtrados diretamente no objeto de negócio.

Filtros (exemplos)

É importante considerar o conteúdo de cada campo antes de aplicar um filtro diretamente no objeto de negócio. Por exemplo os campos que são "Código" devem ser informados os códigos propriamente dito ao invés de suas descrições caso contrário não serão retornados dados do objeto de negócio.
