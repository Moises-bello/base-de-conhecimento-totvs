---
content_hash: 7803369eb888b97c90f90cbc4a4cc07c219f89df67e71e5bc1a6a160b0bf6b6e
fetched_at: '2026-06-29T00:08:20.938592+00:00'
page_id: '268796701'
product: rm
source: tdn-rm
title: TVWHJF_DT_FGTS_Rescisao_Complementar
type: documentation
url: https://tdn.totvs.com/display/LRM/TVWHJF_DT_FGTS_Rescisao_Complementar
version: 2
---

# FGTS DA RESCISÃO COMPLEMENTAR NA MESMA COMPENTENCIA DA ORIGINAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Quando está sendo calculada a rescisão complementar na mesma competência da rescisão original, os eventos de FGTS (CC's 26 e 31) da rescisão complementar estão considerando a base de FGTS da rescisão original, e assim duplicando o valor a ser depositado.*  *E consequentemente o valor do CC 28 (FGTS Artigo 22) também está ficando incorreto.* |
| **Solução/Implementação:** | *Ajuste no cálculo do FGTS para tratar o caso de rescisão complementar na mesma competência da rescisão original.*  *Neste caso não pode considerar a base total da competência.* |
| **Chamados   relacionados:** | *TVWHJF, TWCFQM* |
| **Versões/Release:** | *11.82.46, 12.1.14* |
