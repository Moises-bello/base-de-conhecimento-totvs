---
content_hash: e7681f3549301618700ac38f67339292528d19a176d180e2430559771d89d9c1
fetched_at: '2026-06-29T00:10:19.629265+00:00'
page_id: '484679075'
product: rm
source: tdn-rm
title: DT Retorno de pagamento do banco Crefisa
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+Retorno+de+pagamento+do+banco+Crefisa
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Baixa |
| Função: | Retorno de pagamento |
| Ticket: | [4381144](http://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%224381144%22 "4381144") |
| Requisito/Story/Issue: | [FINANCEIRO01-10648](http://jiraproducao.totvs.com.br/browse/FINANCEIRO01-10648) |

## **01. DESCRIÇÃO**

Implementado o retorno de pagamento do banco Crefisa, conforme layout:

**Header**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo/Tamanho** | **Posição** | **Conteúdo** | **Comentário** |
| TIPO REGISTRO | TEXTO (01) | 001-001 | ‘H’ | ‘H’ – Header |
| NRO ARQUIVO | TEXTO (07) | 002-008 |  | Formato : NNNnnnn – Vide Obs. 1 – Idem à remessa (o mesmo nro.?) |
| DATA ARQUIVO | TEXTO (08) | 009-016 |  | Formato : aaaammdd – Data de geração do Retorno |
| SISORIGEM | TEXTO (10) | 017-026 |  | Sistema de Origem do arquivo – (da requisição?) |
| FILLER | TEXTO (322) | 027-348 |  | Espaços |
| SEQUENCIAL | TEXTO (07) | 348-355 |  | Sequencial = 0000001 |

**Detalhe**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo/Tamanho** | **Posição** | Conteúdo | Comentário |
| TIPO REGISTRO | TEXTO (01) | 001-001 | ‘D’ | ‘D’ – Detalhe |
| NOSSO\_NUMERO | TEXTO (48) | 002-049 |  | P/ Tipo liq. : DOC : NSU\_DOC                       Titulo : CMC7                       Transf. CC/CC : NroMovimento                                                    do débito                       Débito : NroMovimento                       Crédito : NroMovimento                       DARF:NSU\_DARF |
| LIVRE | TEXTO (20) | 050-069 |  | Campo Livre p/ utilização do Sist. de Origem |
| DATA PAGAMENTO | TEXTO (08) | 070-077 |  | Formato : aaaammdd |
| VALOR | NUM (13, 2) | 078-092 |  | Formato : 13 Inteiros e 2 decimais, sem edição                                 – alinhamento  numérico |
| STATUS RETORNO | TEXTO (01) | 093-093 | ‘0’ ‘1’ ‘2’ ‘3’ ‘4’ ‘5’ ‘6’ ‘7’ ‘8’ | Status do Retorno :   0 - Importado   1 – Processado   2 – Rejeitado no Proc.   3 – Devolvida pelo SPB.   4 – “Rejeitada pelo SPB. Motivo: “ou “Rejeitada pelo SPB. Motivo não identificado.”   5 - Cancelamento de Lançamento Pendente.   6 - Cancelada no E-bank.   7 - Cancelada pelo SPB.   8 - Devolvida pelo SPB em outro dia |
| MOTIVO REJEICAO | TEXTTO(255) | 094-348 |  |  |
| SEQUENCIAL | TEXTO (07) | 349-355 |  | Sequencial a partir de 0000001 |

**Trailler**

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Descrição** | **Tipo/Tamanho** | **Posição** | Conteúdo | Comentário |
| TIPO REGISTRO | TEXTO (01) | 001-001 | ‘T’ | ‘T’ – Trailler |
| VALOR TOTAL | NUM (13, 2) | 002-016 |  | Formato : 13 Inteiros e 2 decimais, sem edição – alinhamento  numérico |
| FILLER | TEXTO (332) | 017-348 |  |  |
| SEQUENCIAL | TEXTO (07) | 349-355 |  | Sequencial a partir de 0000001 |
