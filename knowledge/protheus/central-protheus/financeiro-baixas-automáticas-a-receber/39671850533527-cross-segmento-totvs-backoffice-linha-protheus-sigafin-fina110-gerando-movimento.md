---
article_id: 39671850533527
category: 'Financeiro - Baixas Automáticas a Receber '
content_hash: 1c9dd1bf4953c7480173c7b5be2ba635b9f68d7b39e606b3004d8b6840cd1b75
fetched_at: '2026-06-28T22:37:38.774640+00:00'
product: protheus
section_id: 35057325714199
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FINA110 gerando
  movimento individualizado mesmo com MV_BXCNAB ativo
type: support-article
updated_at: '2026-04-13T17:21:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39671850533527-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FINA110-gerando-movimento-individualizado-mesmo-com-MV-BXCNAB-ativo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39671850529175) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
Por que a rotina FINA110 (Baixa Automática) gera movimentos bancários título a título mesmo quando o parâmetro MV\_BXCNAB está configurado como S (Sim)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Versões  
  
**Solução:**

Para que o sistema realize a aglutinação das movimentações bancárias na baixa automática, é obrigatório que os títulos estejam vinculados a um borderô. Caso os títulos sejam processados de forma avulsa pela FINA110 (sem borderô) as movimentações permanecerão individualizadas no extrato bancário (tabela SE5), independentemente da configuração do parâmetro.

Estes movimentos individuais, serão gerados com movimentação bancária.

O parâmetro MV\_BXCNAB atua especificamente no processo de borderô: quando ativo, o sistema gera registros de movimentação não bancária (Tipo BA) para cada título individual do borderô e cria uma linha adicional de movimento bancário com o valor total (somatória), permitindo a conciliação aglutinada.
