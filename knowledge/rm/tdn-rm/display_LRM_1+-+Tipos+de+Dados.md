---
content_hash: 254c90d7fc5b0d37828758984df597719e85b654fb00bbbab54abda73f2c1e09
fetched_at: '2026-06-29T00:11:02.594283+00:00'
page_id: '61932971'
product: rm
source: tdn-rm
title: 1 - Tipos de Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/1+-+Tipos+de+Dados
version: 24
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      O objetivo deste documento é facilitar a identificação de possíveis relacionamentos dos tipos entre os bancos de dados Oracle/SQL Server com os tipos de dados da linguagem de programação do sistema. Facilitando a utilização posterior deste recurso na definição dos dados utilizados nos cadastros.

**02. EXEMPLO DE UTILIZAÇÃO**

      Após identificar o tipo de dados desejado, cadastre-o informando o Nome, tipo de dados SQL e Oracle e o tipo de dados da linguagem. 

**O cadastramento correto do tipo de dados repercute no sucesso ou não da criação do projeto de metadados.**

 Veja alguns exemplos de tipos de dados padrões que podem ser criados, conforme tabela abaixo:

| Nome | Tipo SQL | Tipo Oracle | Tipo Linguagem |
| --- | --- | --- | --- |
| Inteiro | int | number \*\* | System.Int32 |
| Inteiro Curto | smallint | number \*\* | System.Int16 |
| String | varchar \* | varchar2\* | System.String |
| Char | char | char | System.Char |
| Data | datetime | date | System.DateTime |
| Float | float | double | System.Double |
| Moeda | money | number \*\* | System.Decimal |
| Decimal | decimal \*\* | number \*\* | System.Decimal |
| Numeric | numeric \*\* | number \*\* | System.Decimal |
| Memo | text | clob | System.String |
| Imagem | image | blob | System.Byte[] |
| Booleano | bit | boolean | System.Boolean |
| TimeSpan | time | interval day to second | System.TimeSpan |

**\***  Campos que exigem o parâmetro TAMANHO para ser criado. (Tamanho)

**\*\*** Campos que exigem os parâmetros TAMANHO e ESCALA para serem criados. (Tamanho, Escala)

****Apenas tipos básicos podem ser definidos na Tela de Tipo de dados, exemplos:****

**Parâmetros na Tabela**

Importante

**Antigamente era é possível definir um tipo de dados fixo, mas essa funcionalidade foi retirada. Tipos de dados deverão ter seu tamanho e/ou escala definidas apenas na Tela de Tabelas ou na Tela de Modelo de Negócio.**

**Os tipos de dados cadastrados ficarão disponíveis para serem usados posteriormente nas tabelas.**

 

Para mais informações consulte o  [Vídeo demonstrativo.](http://wikihelp.totvs.com.br/WikiHelp/videos/metadados2.html)
