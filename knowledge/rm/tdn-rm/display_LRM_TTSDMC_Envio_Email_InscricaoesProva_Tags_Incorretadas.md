---
content_hash: eba8eb6ce43d82596f09cba2dc7a5a70f006d696877b1ec6f93d376f2b10c4aa
fetched_at: '2026-06-29T00:06:21.945954+00:00'
page_id: '223906288'
product: rm
source: tdn-rm
title: TTSDMC_Envio_Email_InscricaoesProva_Tags_Incorretadas
type: documentation
url: https://tdn.totvs.com/display/LRM/TTSDMC_Envio_Email_InscricaoesProva_Tags_Incorretadas
version: 116
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
| **Versões/Release:** | *11.83.55* |
| **Versão Corrigida:** | *11.83.55* |
| **Versão Expedida:** | *11.83.55* |

divs
