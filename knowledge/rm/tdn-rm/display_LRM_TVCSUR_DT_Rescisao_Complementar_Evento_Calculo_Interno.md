---
content_hash: 2cc341cd0cd03eea1476de5f324d6ea12b639a4dbcb0feff0be1828bea2ad6c0
fetched_at: '2026-06-29T00:08:15.518432+00:00'
page_id: '244744083'
product: rm
source: tdn-rm
title: TVCSUR_DT_Rescisao_Complementar_Evento_Calculo_Interno
type: documentation
url: https://tdn.totvs.com/display/LRM/TVCSUR_DT_Rescisao_Complementar_Evento_Calculo_Interno
version: 109
---

# RESCISÃO COMPLEMENTAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Cliente questionou que ao executar o cálculo de Rescisão Complementar, são fixados alguns eventos no campo de Eventos a serem somados a todas rescisões complementares. Porém os eventos que são fixados são eventos de base de cálculo de FGTS, e isto faz com que mesmo que o evento não tenha que ser calculado (exemplo: evento de CC28 em casos de rescisao tipo 4), o sistema lança valores.* |
| **Solução/Implementação:** | *Adicionado filtro na seleção de eventos para não permitir o lançamento de evento com CC 28.* |
| **Chamados relacionados:** | *TVCSUR* |

divs
