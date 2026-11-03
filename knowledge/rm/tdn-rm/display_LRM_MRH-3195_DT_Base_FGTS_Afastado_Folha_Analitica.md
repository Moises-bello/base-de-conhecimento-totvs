---
content_hash: 83a3fedc31400b7e47a2d95b93dfd711905fbc26cdbb51a51ff928a31dccdbc5
fetched_at: '2026-06-29T00:08:25.062051+00:00'
page_id: '270911286'
product: rm
source: tdn-rm
title: MRH-3195_DT_Base_FGTS_Afastado_Folha_Analitica
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-3195_DT_Base_FGTS_Afastado_Folha_Analitica
version: 110
---

# BASE DE FGTS DE AFASTADO SAINDO INDEVIDAMENTE NA FOLHA ANALÍTICA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Folha Analítica* |
| **Situação/Requisito:** | *Funcionário afastado pelo tipo T (Acidente de trabalho), contendo somente o evento de CC 343 (Base FGTS 13º salário) lançado no envelope de 13o.*  *Ao gerar a folha analítica do período de 13o., é exibida também a Base de FGTS Folha, onde deveria constar somente a Base FGTS do 13º salário.* |
| **Solução/Implementação:** | *Ajuste na Folha Analítica para somar o FGTS de afastado somente se no período selecionado existir Base de FGTS ou se for selecionado todos os períodos.* |
| **Chamados relacionados:** | MRH-3195 |
| **Requisito (ISSUE):** | MRH-3195 |

divs
