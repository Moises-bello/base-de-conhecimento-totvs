---
content_hash: fcef338351cffabb50f053f504c13face1c07a0748a12771edee3922cb3003fd
fetched_at: '2026-06-29T00:08:29.738992+00:00'
page_id: '272162111'
product: rm
source: tdn-rm
title: 590048 MRH-8132 DT DIRF
type: documentation
url: https://tdn.totvs.com/display/LRM/590048+MRH-8132+DT+DIRF
version: 108
---

# ASSISTÊNCIA A SAÚDE COMPLEMENTAR DIRF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projeto |
| **Módulo:** | Folha de Pagamento |
| **Função:** | DIRF |
| **Situação/Requisito:** | Ao realizar a geração do informe de rendimentos, o sistema não esta considerando no campo 3.1 Total dos Rendimentos(inclusive férias) o valor de previdência complementar quando existem mais de uma operadora de assistência cadastrada.  O sistema não considera o valor pois esta lendo os eventos somente de uma operadora cadastrada e não de todas as operadoras que o cliente cadastrou. |
| **Solução/Implementação:** | Foi ajustado o sistema para poder enxergar todos os eventos das operados que estão cadastrados, não somente de uma como estava sendo feito. |
| **Tickets relacionados:** | * 590048 |

divs
