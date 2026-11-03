---
article_id: 360045420974
category: ' TOTVS OMS (Linha Protheus)'
content_hash: 3d42acde33c9f33e6c6ff81f9b5eb32637f5d4a5719fa7b124818c86f5576fc2
fetched_at: '2026-06-28T22:45:48.827000+00:00'
product: protheus
section_id: 4403736822807
source: central-protheus
title: MP - OMS - HELP OMSVEIDISP
type: support-article
updated_at: '2025-02-26T17:01:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045420974-MP-OMS-HELP-OMSVEIDISP
---

**Ocorrência**Sistema apresenta o **help OMSVEIDISP** no momento da montagem da carga, mesmo que a carga anterior que esta amarrada ao veiculo já estiver finalizada.  
  
   
 **Ambiente**PROTHEUS, SIGAOMS, a partir de 11.8  
   
 **Causa**O veiculo em questão esta alocado para outra carga e a data final desta alocação esta vigente.

**Solução**- Acesse a rotina de alocação de veiculo (**OMSA230**);

- Faça a manutenção dessa alocação de veiculo, **ajustando a data final (DAN\_DATFIM) e hora (DAN\_HORFIM)** para uma data/hora anterior a data base do sistema.
