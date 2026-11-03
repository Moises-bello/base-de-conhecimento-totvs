---
content_hash: d0152bb6818d01fecfde5b377fe911f12f89d03b08db2520c8ceec5ee06f724e
fetched_at: '2026-06-29T00:08:44.393340+00:00'
page_id: '307849663'
product: rm
source: tdn-rm
title: DT Armazenar todos os registros lidos do arquivo de retorno
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Armazenar+todos+os+registros+lidos+do+arquivo+de+retorno
version: 5
---

# ARMAZENAMENTO ARQUIVO DE RETORNO BANCÁRIO

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| ****Segmento Executor:**** | Construção e Projetos | | |
| **Módulo:** | Totvs Gestão Financeira | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Retorno Bancário.* | *Importação de arquivo de retorno bancário.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | |  |  | | | |
| **Chamado:** |  | | |
| **Requisito (ISSUE):** | FINANCEIRO01-2990*.* | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** |  | | |

## Objetivo

Inserir no banco de dados todos as linhas importadas no retorno bancário de pagamento, cobrança e débito automático.

## Definição da Regra de Negócio

É necessário ter todas as informações que foram lidas no arquivo de retorno gravadas no banco de dados (tabela FRETORNOBANCARIOITEM). Existem dois objetivos na evolução desse processo. O primeiro é manter um log dos registros lidos nos retornos bancários. O outro é permitir que o processo seja quebrado em duas fases: importação do arquivo no banco de dados e processamento do mesmo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Retorno de Cobrança | Alteração | Movimentações Bancárias -> Retorno Bancário | - |
| Retorno de Pagamento | Alteração | Movimentações Bancárias -> Retorno Bancário | - |
| Retorno de Débito Automático | Alteração | Movimentações Bancárias -> Retorno Bancário | - |

* Foram criados dois novos campos na tabela de Item de Retorno Bancário. O primeiro é o Sequencial do Item de Retorno (SEQITEMRETORNO) que irá compor, juntamente com o campo IDRETORNO, a chave primária da tabela FRETORNOBANCARIOITEM. A chave anterior composta por IDRETORNO, LINHA, CODCOLIGADA e IDLAN não faz mais sentido já que agora todas as linhas de detalhe do arquivo serão armazenadas e não apenas aquelas processadas com sucesso. O segundo campo, CHAVELAN, armazenará a chave de identificação do lançamento na linha detalhe do arquivo importado, o valor da mesma é usado para identificar a qual lançamento/boleto aquela linha está relacionada.
* Todos os registros de detalhe lidos do arquivo de importação de retorno de cobrança, pagamento ou débito automático serão armazenados na tabela de Item de Retorno Bancário mesmo que ocorra erros no processo. As linhas importadas terão o campo CHAVELAN preenchidas.
* Anteriormente o processo de checagem dos dados do retorno em relação aos lançamentos relacionados criava mais de uma linha na tabela de Item de Retorno Bancário caso o boleto identificado vinculado a mais de um lançamento. Esse comportamento não mais existirá, somente uma linha ficará gravada e na mesma armazenada somente o **Identificador do boleto** e os campos de valor (Valor Baixado, Multa, Juros, Desconto e Opcional 1 a 8), com exceção de **Valor Líquido** que terá os valores somados de todos os lançamento envolvidos, conterão os valores lidos do arquivo.
* O campo de identificação do lançamento na tabela de Item de Retorno Bancário (IDLAN) somente será preenchido caso o retorno não seja por boleto. Assim, se o Identificador do Boleto (IDBOLETO) for preenchido, a Referência do Lançamento (IDLAN) ficará com valor nulo.

**Tabelas Utilizadas**

* FRETORNOBANCARIO – Retorno Bancário
* FRETORNOBANCARAIOITEM – Item de Retorno Bancário.

## Dicionário de Dados

**Arquivo ou Código do Script:** FS.2017.10\_06, FS.2017.10\_07 e FS.2017.10\_08.

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | PKFRETORNOBANCARIOITEM (IDRETORNO, SEQITEMRETORNO) |

|  |  |
| --- | --- |
| **Campo** | SEQITEMRETORNO |
| **Tipo** | Inteiro |
| **Tamanho** |  |
| **Mandatório** | Sim ( x ) Não (  ) |
| **Descrição** | Sequencial do Item de Retorno |
| **Título** | Seq. Retorno |
| **Help do Campo** | Sequencial dos registro de item de retorno bancário lidos do arquivo. |

|  |  |
| --- | --- |
| **Campo** | CHAVELAN |
| **Tipo** | String |
| **Tamanho** | 42 |
| **Mandatório** | Sim ( ) Não ( x ) |
| **Descrição** | Chave do lançamento |
| **Título** | Chave do lançamento |
| **Help de Campo** | Chave de identificação do lançamento na linha detalhe importada do arquivo de retorno. |
