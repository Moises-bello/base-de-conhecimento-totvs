---
content_hash: c5fcfc51a3209dcd2b7a0befb65ecd6e1a2b31bff9c14e1ca133952e33b7b607
fetched_at: '2026-06-29T00:08:03.774066+00:00'
page_id: '235324907'
product: rm
source: tdn-rm
title: TUOL53_DT_Envio_Email_Inscricao_Periodo_Incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOL53_DT_Envio_Email_Inscricao_Periodo_Incorreto
version: 118
---

# ENVIO DE E-MAIL DE INSCRIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Avaliação e Pesquisa* |
| **Função:** | *Envio de e-mail de inscrição* |
| **Situação/Requisito:** | *Quando uma prova possui mais de um período e o candidato está cadastrado para o segundo período da prova, ao enviar um email de configuração de inscrição que contenha a Tag do período o sistema sempre considera a data do primeiro período da prova, não a que está no cadastro do candidato.* |
| **Solução/Implementação:** | *Foi identificado uma inconsistência no momento de carrega o período, sendo assim, foi feito um ajuste para que ao carregar a prova o sistema valide o periodo correto, após, a data do período no e-mail de confirmação passou a ser feita corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUPASQ* |
| **Requisito (ISSUE):** | *N/A* |

divs
