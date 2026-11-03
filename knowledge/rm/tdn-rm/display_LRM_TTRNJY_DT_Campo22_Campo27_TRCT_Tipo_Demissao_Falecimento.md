---
content_hash: 2c2aeadaf127179a7ff3d40b517a1d0512892e6f56afcf9bcc620dab4a2b5764
fetched_at: '2026-06-29T00:06:20.057220+00:00'
page_id: '221547149'
product: rm
source: tdn-rm
title: TTRNJY_DT_Campo22_Campo27_TRCT_Tipo_Demissao_Falecimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTRNJY_DT_Campo22_Campo27_TRCT_Tipo_Demissao_Falecimento
version: 1
---

# TRCT - CAMPOS 22 E 27 IGUAL A FT1 QUANDO TIPO DEMISSÃO FOR IGUAL A 8 OU F

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gerar TRCT de acordo com a Portaria 1.057* |
| **Situação/Requisito:** | Ao realizar uma Rescisão do Tipo F - Falecimento p/ acidente de trabalho e gerar o TRCT, o sistema não leva informações no campo 22 – Causa do afastamento e leva no campo 27 – Cód. Afastamento o valor F, sendo que, de acordo com a Portaria 1.057 deveria ser FT1. |
| **Solução/Implementação:** | Quando o Tipo Demissao for igual a "8 - Falecimento" ou "F - Falecimento p/ acidente de trabalho" o campo 22 do TRCT é preenchido com "FT1" e o campo 27 é preenchido com "Rescisão do contrato de trabalho por falecimento do empregado". |
| **Chamados relacionados:** | TTRNJY |
| **Versões/Release:** | *11.82.42* |

divs
