---
content_hash: e5897a55c9a3f6023673dfdaf6613a7157a279c77a75edd06e4adce6a74128af
fetched_at: '2026-06-29T00:11:38.969340+00:00'
page_id: '786545512'
product: rm
source: tdn-rm
title: Objeto de negócio - Lançamentos Fiscais e de Ajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=786545512
version: 55
---

Conteúdo

Conteúdo

# 1. Visão Geral

O objeto de negócio de Lançamentos Fiscais e de Ajuste retorna os dados dos lançamentos cadastrados dentro do período desejado.  
Este objeto está disponível pela ferramenta "Smart View". Serão disponibilizados pelo TOTVS Compartilhamento relatórios, tabelas dinâmicas e visões de dados que utilizam este objeto, mas também há a possibilidade de criar recursos personalizados com este objeto de negócio.

# 2. Relatórios Disponíveis com o ON Lançamentos Fiscais e de Ajuste

## 2.1 Tabela Dinâmica

É possível ter várias perspectivas diferentes sobre suas informações ao vincular o objeto de negócio de Lançamentos à uma tabela dinâmica.   
Neste exemplo, foram realizados agrupamentos aninhados por Filial, Tipo de Lançamento, Natureza Sintética e Número do Documento para obter a sumarização de seus totais.

Exemplo de tabela dinâmica

## 2.2 Visão de dados

A visão de dados permite uma visualização mais detalhada e extensa de cada informação.   
No exemplo abaixo, ao vincular o objeto de negócio de Lançamentos a uma visão de dados, foram filtradas as informações referentes apenas aos valores do ICMS.

Exemplo de visão de dados

## 2.3 Relatórios

Segue exemplos dos relatórios em PDF.

Exemplos de relatóriosRegistro de ApuraçãoTipoleftEntrada

Clique para visualizar a imagem:

Imagem

Download Registro de Apuração ICMS - Entrada:

150

Saída

Clique para visualizar a imagem:

Imagem

Download Registro de Apuração IPI - Saída:

150

Atualmente, existem 4 relatórios deste tipo, todos seguindo o mesmo padrão:

* Relatório do Registro de Apuração - ICMS - Entrada
* Relatório do Registro de Apuração - ICMS - Saída
* Relatório do Registro de Apuração - IPI - Entrada
* Relatório do Registro de Apuração - IPI - Saída
Resumo de ApuraçãoTipoleftIPI

Clique para visualizar a imagem:

Imagem

250

Download Resumo de Apuração IPI:

250

ICMS

Clique para visualizar a imagem:

Imagem

250

Download Resumo de Apuração ICMS:

250

Em **Outros Créditos** serão somados os valores dos lançamentos de ajustes que possuam os seguintes subtipos:

* Tipo Extemporâneo
* Recebimento de crédito
* Transferência de Débito
* Ressarcimento ST

Em **Outros Débitos** serão somados os valores dos lançamentos de ajustes que possuam os seguintes subtipos:

* Recebimento de Débito
* Transferência de Crédito
* Ressarcimento de Crédito

Atualmente, existem 2 relatórios deste tipo, todos seguindo o mesmo padrão:

* Relatório do Resumo de Apuração - ICMS
* Relatório do Resumo de Apuração - IPI
Registro de Entradas/Saídas

Clique para visualizar a imagem:

Imagem

Download Registro de Entradas - ICMS - Entrada:

150

Atualmente, existem 4 relatórios deste tipo, todos seguindo o mesmo padrão:

* Relatório do Registro de Entradas - ICMS
* Relatório do Registro de Saídas - ICMS
* Relatório do Registro de Entradas - IPI
* Relatório do Registro de Saídas - IPI

Para ver corretamente os valores das colunas "Saldo Tributo Anterior" e "Saldo Tributo Atual", deve ser filtrado o período de apenas um mês e o Período de Apuração deve estar Encerrado.

Para visualizar com precisão os valores do relatório, é fundamental selecionar a empresa correspondente aos dados que se deseja incluir no relatório.

# 3. Campos do objeto de negócio

Atualmente, são disponibilizados os seguintes campos referentes aos lançamentos no objeto de negócio:

Tabela de campos

| Nome | Tipo | Filtrável?¹ | Coluna |
| --- | --- | --- | --- |
| Código Coligada | Literal | Sim | DLAF.CODCOLIGADA, DLDC.CODCOLIGADA |
| Nome Coligada | Literal | Sim | GCOLIGADA.NOME |
| Código Filial | Literal | Sim | DLAF.CODFILIAL, DLDC.CODFILIAL |
| Nome Filial | Literal | Sim | GFILIAL.NOME |
| Id Lançamento Fiscal | Literal | Sim | DLAF.IDLAF |
| Data Entrada/Saída | Data | Sim | DLAF.DATAES |
| Código Documento | Literal | Sim | DLAF.CODTDO |
| Série | Literal | Sim | DLAF.SERIEDOC |
| Documento Inicial | Literal | Sim | DLAF.DOCINI |
| Data Emissão | Data | Sim | DLAF.DATAEMISSAO |
| Emitente/Fornecedor | Literal | Sim | DLAF.EMITENTECFO |
| Nome (Cli/For) | Literal | Sim | FCFO.NOME |
| Código Estado | Literal | Sim | FCFO.CODETD |
| Status | Literal | Sim | DLAF.STATUSLF |
| Valor Documento | Decimal | Sim | DLAF.VALORCONT |
| Valor Lançamento Ajuste | Decimal | Sim | DLDC.VALORLDC |
| Id Natureza | Inteiro | Sim | DLAF.IDNAT |
| Descrição Natureza | Literal | Sim | DCFOP.NOME |
| Código Natureza | Literal | Sim | DCFOP.CODNAT |
| Código Sintético Natureza | Literal | Não | -- |
| Código Tributo | Literal | Não | -- |
| Base ICMS | Decimal | Sim | DLAF.BASEICMS |
| Base Redução ICMS | Decimal | Sim | DLAF.BASEREDICMS |
| Valor ICMS | Decimal | Sim | DLAF.VALORICMS |
| Isento ICMS | Decimal | Sim | DLAF.ISENTOICMS |
| Outros ICMS | Decimal | Sim | DLAF.OUTROSICMS |
| Valor FECP Próprio | Decimal | Sim | DLAF.VALORFCPPROPRIO |
| Alíquota ICMS | Decimal | Sim | DLAF.ALIQICMS |
| Fator ICMS | Decimal | Sim | DLAF.FATORICMS |
| ICMS Diferido | Decimal | Sim | DLAF.ICMSDIFERIDO |
| Base IPI | Decimal | Sim | DLAF.BASEIPI |
| Valor IPI | Decimal | Sim | DLAF.VALORIPI |
| Valor IPI Sem Crédito | Decimal | Sim | DLAF.VALORIPISEMCREDITO |
| Isento IPI | Decimal | Sim | DLAF.ISENTOIPI |
| Outros IPI | Decimal | Sim | DLAF.OUTROSIPI |
| Id Regra ICMS | Inteiro | Sim |  |
| Id Regra IPI | Inteiro | Sim |  |
| Tipo Lançamento | Literal | Sim | DLAF.TIPOLF, DLDC.TIPOLDC |
| Valor ICMS/ICMSST | Decimal | Sim | DLAFAJUSTESPED.VALORICMSICMSST |
| Tipo Ajuste | Literal | Sim |  |
| Número Documento | Literal | Sim | DLDC.NUMDOC |
| CPF/CNPJ Coligada | Literal | Sim | GCOLIGADA.CGC |
| Inscrição Estadual Coligada | Literal | Sim | GCOLIGADA.INSCRICAOESTADUAL |
| CPF/CNPJ Filial | Literal | Sim | GFILIAL.CGC |
| Inscrição Estadual Filial | Literal | Sim | GFILIAL.INSCRICAOESTADUAL |
| Saldo Tributo Anterior | Decimal | Sim | DPERIODO.SALDOTRBANT |
| Saldo Tributo Atual | Decimal | Sim | DPERIODO.SALDOTRBATUAL |
| Ressarcimento de Crédito | Inteiro | Não | DLDC.SUBTIPOLDC |

¹: Campos que podem ser filtrados diretamente no objeto de negócio.

# 4. Outras informações

Há quatro parâmetros a serem preenchidos para retornar dados neste objeto de negócio, sendo eles:

* Código da coligada;
* Código da filial;
* Data inicial período;
* Data final período;

O Código da coligada e o Código da filial são opcionais, enquanto os parâmetros de datas são obrigatórios.  
  
É importante considerar o conteúdo de cada campo antes de aplicar um filtro diretamente no objeto de negócio. Por exemplo, o Código do Estado deve ser filtrado com "MG" ao invés de "Minas Gerais". Caso contrário, não serão retornados dados do objeto de negócio.  
Especificamente para a coluna de "Tipo Lançamento", deve ser utilizada o nome ou numeração do tipo de lançamento, sendo elas:

| Descrição | Nome/Numeração |
| --- | --- |
| Entrada | Entrada |
| Saída | Saída |
| Não se Aplica | 0 |
| Outros Débitos | 1 |
| Estorno Débitos | 2 |
| Outros Créditos | 3 |
| Estorno Créditos | 4 |
| Deduções | 5 |
| Débito Especial | 6 |

Cada "Tipo Lançamento" possui seus respectivos "Subtipos":

| **Descrição** | **Numeração** | **Tipo de Lançamento** |
| --- | --- | --- |
| Não se aplica | 0 | Todos |
| Transferência de Crédito | 1 | 1 |
| Recebimento de Crédito | 2 | 3 |
| Ressarcimento de Crédito | 3 | 1 |
| Ressarcimento ST | 4 | Todos |
| Transferência de Débito | 5 | Todos |
| Recebimento de Débito | 6 | 1,3 |
| Compensação de Crédito | 7 | 5 |
| Extemporâneo | 8 | 3 |
| Crédito Ativo Imobilizado | 9 | 3 |
| Valores FECP | 10 | Todos |
| Antecipação | 11 | Todos |
| Incentivo à Cultura | 12 | 5 |
| Diferencial de Alíquota | 13 | Todos |
| Período anterior (DAPI/MG) | 14 | Todos |
| FECP - Débitos Op. Internas | 15 | Todos |
| FECP - Débitos Op. Importação | 16 | Todos |
| FECP - Débitos Op. Dif. Alíquota | 17 | Todos |
| FECP - Débitos Op. Sub. Tributária | 18 | Todos |
| FECP - Dedução Op. Internas | 19 | Todos |
| FECP - Dedução Op. Sub. Tributária | 20 | Todos |
| Crédito Outorgado | 21 | 3 |
| Crédito Prodepe Automático | 22 | Todos |
| FECP Consumidor Final | 23 | Todos |
| FECP ICMS ST | 24 | Todos |
| FECP ICMS ST Consumidor Final | 25 | Todos |
| DIFAL – Origem\Destino | 26 | Todos |
| FECP ICMS Próprio | 27 | Todos |
| FECP Destino | 28 | Todos |
| Segregação Crédito Presumido | 29 | Todos |
| Segregação Débitos com Crédito Presumido | 30 | Todos |
| Segregação do Crédito Decorrente do Pagamento Antecipado | 31 | 1 |
| Crédito relativo Substituição Tributária | 36 | 3,4,5 |

**Observação**: O subtipo “Crédito Ativo Imobilizado” poderá ser gerado automaticamente quando o parâmetro "Considera Operação Ativo - Outros Créditos" estiver habilitado ou manualmente no cadastro de “Outros Débitos/Créditos”. O subtipo “Incentivo à Cultura” só é gerado para Filiais no Estado “MG”.
