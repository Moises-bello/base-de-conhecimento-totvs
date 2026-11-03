---
article_id: 115014942348
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: e0b51b36a69b385704346e211cbece5da4c312d9f646f9258ffb10e998e048b4
fetched_at: '2026-06-28T22:38:43.931380+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Agrupadores do
  Faturamento
type: support-article
updated_at: '2023-09-21T14:30:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115014942348-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Agrupadores-do-Faturamento
---

**Ocorrência**   
  
Quando vou preparar documento de saída não aparece o pedido para eu selecionar e continuar o processo, conforme imagem abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/z6pCFlnYN4Oxl3lVoKqX9dSw0/?name=inline-1034542730.png)  
  
**Causa**  
  
A pergunta Agrupadores são configurações que podem ser utilizadas para filtrar os pedidos que deseja que sejam faturados.  
Para usar esta pergunta, será necessário ter acesso ao módulo CRM, pois são duas tabelas deste módulo que são utilizadas para tratar os agrupadores, que são Controle de Entidades (CRMA220) e Agrupadores de registros (CRMA580).  
Com base nestes cadastros é que será criado o filtro para utilização da pergunta, lembrando que o acesso ao módulo crm depende da licença de cada cliente.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**  
  
Para poder  faturar pelo processo normal do sistema, deixe o campo da pergunta Agrupadores sem preenchimento algum.  
Sem o agrupamento, o sistema trará os registros conforme determinado nos demais parâmetros da seleção dos pedidos para preparação da nota, se considerar apenas as primeiras perguntas, o sistema trará todas as notas no browser de faturamento para processar.
