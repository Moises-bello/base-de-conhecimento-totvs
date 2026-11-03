---
content_hash: e19651a6bef2eb53c1b58dc34ec1aa6ab01d6a6cebfe9a13585a5f7e5dfa3577
fetched_at: '2026-06-29T00:08:24.770196+00:00'
page_id: '270902711'
product: rm
source: tdn-rm
title: MRH-3078_DT_FGTS_Afastado_Aba_Incidencias_Envelope
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3078_DT_FGTS_Afastado_Aba_Incidencias_Envelope
version: 111
---

# FGTS DE AFASTADO NA ABA DE INCIDÊNCIAS DO ENVELOPE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Envelope* |
| **Situação/Requisito:** | *Funcionário possui dois afastamentos do tipo 'T- Afastamento por acidente de trabalho' totalizando 16 dias.*  *Quando lança o evento de adiantamento, o sistema está gerando na aba incidências do envelope 1 dia de FGTS referente ao afastamento.*  *Porém no envelope do funcionário não possui nenhum evento que incide em FGTS, portanto não deveria ser informado o valor do FGTS.* |
| **Solução/Implementação:** | *Ajuste na aba de incidências do envelope para informar o FGTS de afastado somente se no período selecionado existir Base de FGTS.* |
| **Chamados relacionados:** | MRH-3078 |
| **Requisito (ISSUE):** | MRH-3078 |

divs
