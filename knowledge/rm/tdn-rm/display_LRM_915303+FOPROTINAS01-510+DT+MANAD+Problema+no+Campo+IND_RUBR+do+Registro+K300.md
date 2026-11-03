---
content_hash: 54fe29edf684a94c7de8b71744f29fde202ef06f5a69763a683f76edd24874af
fetched_at: '2026-06-29T00:08:35.978537+00:00'
page_id: '283399771'
product: rm
source: tdn-rm
title: 915303 FOPROTINAS01-510 DT MANAD Problema no Campo IND_RUBR do Registro K300
type: documentation
url: https://tdn.totvs.com/display/LRM/915303+FOPROTINAS01-510+DT+MANAD+Problema+no+Campo+IND_RUBR+do+Registro+K300
version: 110
---

# MANAD

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | MANAD |
| **Situação/Requisito:** | Eventos do tipo base que não possuem incidência nem estorno estão sendo impressos no MANAD com o tipo 'P' - Provento no campo 9 - IND\_RUBR do registro K300, quando é marcado para exportar eventos de base como Provento/Desconto na parametrização do processo. Entretanto, eventos sem incidência ou estorno de INSS e IRRF (que não afetam a base de INSS ou IRRF) sempre devem ser levados como 'O' - Outros, conforme orientação obtida junto ao suporte do SVA, Receita Federal. |
| **Solução/Implementação:** | Foi ajustada a geração do MANAD para sempre exportar eventos de base sem incidências/estornos como 'O' - Outros no campo 9 - IND\_RUBR, como 'P' - Provento se não possuir CC 114, 116 ou 128 e possuir alguma incidência ou exportar como 'D' - Desconto se possuir CC 114, 116 ou 128 ou possuir algum estorno. Esse comportamento ocorre apenas quando for marcado "Exportar como Provento/Desconto" no parâmetro de exportação de eventos tipo base durante a geração do MANAD. Se for marcado "Exportar como Outros", o evento será exportado como 'O' - Outros se for cadastrado como sendo do tipo base, 'P' - Provento se for um provento ou 'D' se for um desconto, independente de CC e incidências/estornos. |
| **Tickets relacionados:** | [915303](https://totvssuporte.zendesk.com/agent/tickets/915303 "Open ticket in Zendesk Support") |

divs
