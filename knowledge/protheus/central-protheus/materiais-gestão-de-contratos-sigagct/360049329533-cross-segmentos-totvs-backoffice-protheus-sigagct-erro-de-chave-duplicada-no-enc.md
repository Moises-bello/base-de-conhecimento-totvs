---
article_id: 360049329533
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: b453c20b2da4b63540bf8cb386e68ff2285c4f268e2ba357024d97182783c899
fetched_at: '2026-06-28T22:37:22.737985+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Erro de chave duplicada
  no Encerramento da Medição - Cannot insert duplicate key row in object SE2 - Parâmetro
  MV_NMEDTIT = 2
type: support-article
updated_at: '2022-05-19T21:12:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049329533-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Erro-de-chave-duplicada-no-Encerramento-da-Medi%C3%A7%C3%A3o-Cannot-insert-duplicate-key-row-in-object-SE2-Par%C3%A2metro-MV-NMEDTIT-2
---

**Ocorrência**

Erro de chave duplicada no Encerramento da Medição - Cannot insert duplicate key row in object SE2 - Parâmetro MV\_NMEDTIT = 2

**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Solução**

Quando o parâmetro MV\_NMEDTIT está com o conteúdo = 2 a Numeração do título, será igual a Numeração da Medição, dessa forma se no encerramento da medição for gerado mais de um título o erro será gerado, pois, o sistema não aceita 2 títulos com a mesma numeração.  
Ajuste o parâmetro MV\_NMEDTIT = 1 para que a numeração possa ser gerado pela numeração sequencial.
