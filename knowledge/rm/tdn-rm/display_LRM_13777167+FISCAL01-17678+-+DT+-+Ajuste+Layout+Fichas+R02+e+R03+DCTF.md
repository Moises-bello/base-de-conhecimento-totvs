---
content_hash: c68cda4ffa6e4922bbfc5d2ec4fa347e833058d5a7e7a037f8097cf60c5c128e
fetched_at: '2026-06-29T00:11:17.017592+00:00'
page_id: '676038473'
product: rm
source: tdn-rm
title: 13777167 FISCAL01-17678 - DT - Ajuste Layout Fichas R02 e R03 DCTF
type: documentation
url: https://tdn.totvs.com/display/LRM/13777167+FISCAL01-17678+-+DT+-+Ajuste+Layout+Fichas+R02+e+R03+DCTF
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Fiscais |
| País: | Brasil |
| Ticket: | 13777167 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17678 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar a DCTF, as fichas R02 e R03 o sistema está gerando algumas informações incorretamente e com ausência de outras. 

TESTES REALIZADOS 

Ao gerar a rotina DCTF visualizamos que na ficha R02, ordem 12, o layout está levando o código do município e não o nome do município, conforme o esperado. 

Na ficha R03 o layout está levando zeros na frente dos números de telefone (contador, responsável e geral), ao invés de espaços.

Também na ficha R03, o layout está levando o número de CRC de forma incompleta e também não levou o estado do CRC.

## **03. SOLUÇÃO**

Foi ajustado a forma de preenchimento de vazio (‘ ’) nos campos telefone, telefoneContador, TelefoneResponsavel, CRCcontador, UFCRCContador.

Preenchimento de brancos à direita.

R02 - 15: DDD do telefone

R02 - 16: Telefone

R03 - 08: DDD do telefone Representante

R03 - 09: Telefone Representante

R03 - 16: CRC - Responsável

R03 - 17: UF - Responsável

R03 - 18: DDD do telefone Responsável

R03 - 19: Telefone Responsável

Além disso o campo 16 do R03 está com o dígito do CRC.

Disponível a partir da versão 12.1.34
