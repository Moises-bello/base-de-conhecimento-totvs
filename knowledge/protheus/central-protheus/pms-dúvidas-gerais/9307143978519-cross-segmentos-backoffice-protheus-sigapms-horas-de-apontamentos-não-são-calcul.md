---
article_id: 9307143978519
category: PMS - Dúvidas Gerais
content_hash: 64c621da5f67dbbe54e9e61f424ebb9925e4f597ef0e7eecc467af440b33ca88
fetched_at: '2026-06-28T22:37:17.772820+00:00'
product: protheus
section_id: 1500001539681
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAPMS - Horas de apontamentos não
  são calculadas após alteração do parâmetro MV_PRECISA '
type: support-article
updated_at: '2024-02-23T15:14:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9307143978519-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Horas-de-apontamentos-n%C3%A3o-s%C3%A3o-calculadas-ap%C3%B3s-altera%C3%A7%C3%A3o-do-par%C3%A2metro-MV-PRECISA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21567636764055) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Após alteração do parâmetro MV\_PRECISA o calculo das horas não é efetuado no apontamento de recurso (PMSA320/PMSA321).  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as versões  
  
**Causa**Isso ocorre pois após a alteração do parâmetro MV\_PRECISA para um melhor calculo de horas relacionado aos apontamentos é necessário alterar os campos das tabelas SH7 (H7\_ALOC) e SH9 (H9\_ALOC).  
  
**Solução**Após a alteração do parâmetro MV\_PRECISA realize o seguinte processo:   
1-Realizar a alteração dos campos H7\_ALOC e H9\_ALOC, conforme documentação abaixo:

* [Alteração do Campo Calendário Semanal e Calendário Diário](https://tdn.totvs.com/x/B-lc)

2-Caso existam cadastros já em uso é necessário seguir o procedimento da documentação abaixo:

* [Criação do Parâmetro MV\_ALTCLD](https://tdn.totvs.com/x/GD1ZEg)

**Saiba mais:** [MV\_PRECISA - Configurações e procedimentos para alteração](https://tdn.totvs.com/x/c5YTEQ)
