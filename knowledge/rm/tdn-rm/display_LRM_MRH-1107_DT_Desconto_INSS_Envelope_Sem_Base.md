---
content_hash: 29a8048f9a986f582b7caffa184fcbdd6102d2feb37b89515fea6b4e9c047289
fetched_at: '2026-06-29T00:08:21.701126+00:00'
page_id: '269069207'
product: rm
source: tdn-rm
title: MRH-1107_DT_Desconto_INSS_Envelope_Sem_Base
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-1107_DT_Desconto_INSS_Envelope_Sem_Base
version: 113
---

# LANÇAMENTO DO DESCONTO EM ENVELOPE SEM BASE DE INSS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *INSS* |
| **Situação/Requisito:** | *No cálculo .Net o sistema realiza o desconto de INSS mesmo que no período não tenha base de INSS.*  *No Delphi o comportamento era diferente, onde o desconto só era lançado se no envelope corrente existisse valor de base de INSS, mesmo que no cálculo seja considerada a base completa da competência.* |
| **Solução/Implementação:** | *Tratar no cálculo .Net para que o comportamento fique igual o Delphi.*  *Assim, o desconto do INSS só será lançado no envelope que tiver valor de base de INSS, mesmo que no cálculo seja considerada a base completa da competência.* |
| **Chamados relacionados:** | MRH-1107 |
| **Requisito (ISSUE):** | MRH-1107 |

divs
