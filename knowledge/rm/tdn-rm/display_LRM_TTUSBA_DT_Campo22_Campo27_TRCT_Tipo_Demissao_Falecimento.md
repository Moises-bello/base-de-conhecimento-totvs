---
content_hash: 7e95b1741feb35b797ea8c343d678fa6dd3a1fe9a430a6f34b808c54e7a462d4
fetched_at: '2026-06-29T00:06:20.060423+00:00'
page_id: '221547225'
product: rm
source: tdn-rm
title: TTUSBA_DT_Campo22_Campo27_TRCT_Tipo_Demissao_Falecimento
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUSBA_DT_Campo22_Campo27_TRCT_Tipo_Demissao_Falecimento
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
| **Chamados relacionados:** | TTUSBA |
| **Versões/Release:** | *12.1.9* |

divs
