---
content_hash: 465bf5f3d97920ee60d7424360b746b3c51d500584cc6699d77937805c2009e6
fetched_at: '2026-06-29T00:06:30.032529+00:00'
page_id: '235309266'
product: rm
source: tdn-rm
title: TUNOHR_DT_Cutter_Sem_TituloPrincipal
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNOHR_DT_Cutter_Sem_TituloPrincipal
version: 121
---

# PUBLICAÇÃO - CUTTER PHA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Publicação - geração de Cutter/PHA sem título principal* |
| **Situação/Requisito:** | *Ao tentar gerar o *Cutter/PHA* de uma publicação que não tenha título principal o sistema retorna um erro informando que o objeto é inválido.* |
| **Solução/Implementação:** | *Foi identificado que o erro era causado pela tentativa de validar se o título era iniciado com valor número sendo que o título estava vazio. Foi feito o ajuste na validação para verificar antes se o título está vazio.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUNRYF* |
| **Requisito (ISSUE):** | *N/A* |

divs
