---
content_hash: aeaaaeb9704cc9122d1fd22a36a37bf32b08fec4aa50a4e850d9a3723996bb2c
fetched_at: '2026-06-29T00:06:21.950826+00:00'
page_id: '223906299'
product: rm
source: tdn-rm
title: TTYCZ7_Envio_Email_InscricaoesProva_Tags_Incorretadas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTYCZ7_Envio_Email_InscricaoesProva_Tags_Incorretadas
version: 122
---

# ENVIO DE EMAILS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Envio de emails* |
| **Situação/Requisito:** | *Foi identificado que ao enviar um email do tipo "Inscrições de prova" o sistema carrega um modelo com as tags INSCRICAO\_TESTIS, DATA\_PROVA E HORARIO\_PROVA, porém as tags não são preenchidas e não possuem a opção de ser inseridas caso o texto seja alterado.* |
| **Solução/Implementação:** | *Foi identificado que as tags INSCRICAO\_TESTIS, DATA\_PROVA E HORARIO\_PROVA realmente não faz mais parte das opções, foi feito o ajuste no modelo para não serem exibidas e a tag correta é a PROVA\_TESTIS, que já contém os dados necessário da prova.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.9* |
| **Versão Corrigida:** | *12.1.9* |
| **Versão Expedida:** | **12.1.9** |

divs
