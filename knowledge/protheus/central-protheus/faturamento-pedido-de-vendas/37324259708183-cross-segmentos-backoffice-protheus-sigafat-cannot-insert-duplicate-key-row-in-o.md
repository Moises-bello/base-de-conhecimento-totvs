---
article_id: 37324259708183
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: bc3320aab62f5568ef628834d60829bf091dfe14006de9168d429b939a12c0e9
fetched_at: '2026-06-28T22:38:39.670153+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Cannot insert duplicate key
  row in object  'dbo.XXX010
type: support-article
updated_at: '2025-12-29T20:19:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37324259708183-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Cannot-insert-duplicate-key-row-in-object-dbo-XXX010
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37324259700247) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Quando o sistema esta realizando o processamento de gravação de registro e o sistema apresenta o erro.log **Cannot insert duplicate key row in object**  **'dbo.XXX010**'  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - todas as versões.  
  
  
**Causa**  
O erro ocorre quando o sistema tenta gravar um registro que que já existe no banco de dados da chave única. Isso geralmente está relacionado à inconsistência na numeração automática da tabela ou à definição incorreta da chave única no dicionário de dados.  
  
**Solução**  
Para corrigir o problema, siga uma das alternativas abaixo:

1- Ajustar a numeração automática da tabela  
Verifique qual foi o último número gravado na tabela e realize o ajuste da numeração automática por meio do SIGACFG: 

2- Validar a chave única no dicionário de dados  
Confirme no dicionário padrão da tabela se a definição da chave única está correta no SX2.
