---
content_hash: 956c16011e20b9a9f80d06332bfffaa2d3764c5a9396c172fae67baa47a11690
fetched_at: '2026-06-29T00:09:34.646305+00:00'
page_id: '425459210'
product: rm
source: tdn-rm
title: Layout de Importação de Exemplares
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459210
version: 2
---

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **ORDEM** | **NOME** | **DESCRIÇÃO** | **OBRIGATÓRIO** | **TIPO** | **VALIDAÇÃO/MÁSCARA** |
| 1 | CODPUBLIC | Código da publicação à qual o exemplar pertence | Sim | Inteiro | Ver tabela LPUBLIC (referência 2) |
| 2 | NUMTOMBO | Número do tombo do exemplar | Depende de parametrização | Inteiro |  |
| 3 | NTOMBO | Número do tombo antigo | Não | Texto(30) |  |
| 4 | DTREGISTRO | Data do registro | Sim | Data | DD/MM/AAAA |
| 5 | DTBAIXA | Data da baixa | Não | Data | DD/MM/AAAA |
| 6 | LOCALIZACAO | Localização do exemplar (número de chamada) | Não | Texto(30) |  |
| 7 | TIPOAQUISICAO | Tipo de aquisição do exemplar | Sim | Texto(1) | C - Compra D - Doação I - Incorporação P - Permuta O - Consignação M - Multa A - Assinatura |
| 8 | VALORAQUISICAO | Valor pago pelo exemplar | Não | Numerico(10,2) | 99999999,99 |
| 9 | NEXEMPLAR | Número do exemplar | Não | Texto(10) |  |
| 10 | MOEDA | Moeda da compra | Não | Texto(10) |  |
| 11 | JUSTIFICATIVABAIXA | Justificativa da baixa | Não | Texto(254) |  |
| 12 | BLOQEMP | Bloquear exemplar para empréstimo | Não | Texto(1) | T - Sim, F - Não |
| 13 | ANO | Ano | Não | Texto(10) |  |
| 14 | NPAGINA | Número de páginas | Não | Texto(20) |  |
| 15 | EDICAO | Edição | Não | Texto(20) |  |
| 16 | EDTCOMPL | Complemento da edição | Não | Texto(60) |  |
| 17 | VOLUME | Volume | Não | Texto(80) |  |
| 18 | DTCOMPRA | Data da compra | Não | Data | DD/MM/AAAA |
| 19 | NFISCAL | Nota fiscal de compra | Não | Inteiro |  |
| 20 | OBSAQUISICAO | Observação sobre a aquisição | Não | Texto(100) |  |
| 21 | MATERIALANEXO | Material anexo ao exemplar | Não | Texto(150) |  |
| 22 | NOBRA | Número da obra | Não | Inteiro |  |
| 23 | NEXEMPPER | Número do exemplar de periódico | Não | Inteiro |  |
| 24 | MÊS | Mês de publicação do exemplar de periódico | Não | Texto(20) |  |
| 25 | COMPRIMENTO | Comprimento do exemplar | Não | Numerico(10,2) | 99999999,99 |
| 26 | UNCOMP | Código da unidade de medida de comprimento do exemplar | Não | Texto(5) | Ver tabela TUND (referência 3) |
| 27 | ALTURA | Altura do exemplar | Não | Numerico(10,2) | 99999999,99 |
| 28 | UNALT | Código da unidade de medida da altura do exemplar | Não | Texto(5) | Ver tabela TUND (referência 3) |
| 29 | LARGURA | Largura do exemplar | Não | Numerico(10,2) | 99999999,99 |
| 30 | UNLARG | Código da unidade de comprimento da largura do exemplar | Não | Texto(5) | Ver tabela TUND (referência 3) |
| 31 | PESO | Peso do exemplar | Não | Numerico(10,2) | 99999999,99 |
| 32 | UNPESO | Código da unidade de medida do peso do exemplar | Não | Texto(5) | Ver tabela TUND (referência 3) |
| 33 | CODFILIAL | Código da filial que será cadastrado o exemplar | Não | Inteiro |  |
| 34 | CODUNIDADE | Código da unidade que será cadastrado o exemplar | Não | Inteiro |  |
