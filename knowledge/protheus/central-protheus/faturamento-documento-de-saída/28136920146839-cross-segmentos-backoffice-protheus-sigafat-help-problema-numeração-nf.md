---
article_id: 28136920146839
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: df32347aa89c3da91ffeda8876cf7e1d833d2bffc3e21cea7ef5474b3ef2417e
fetched_at: '2026-06-28T22:38:44.064526+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGAFAT - Help: "Problema Numeração
  NF"'
type: support-article
updated_at: '2024-11-28T20:09:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28136920146839-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Help-Problema-Numera%C3%A7%C3%A3o-NF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28136914337815) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como resolver o Help: "Problema Numeração NF"?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Causas:**1 - A numeração/série selecionada existir nas tabelas: SF3, SF2, SE1 ou SF1 (não basta não existir na SD2)

2 - Supondo que o passo 1 esteja correto, a numeração escolhida já existe nas tabelas acima, ele tentará 200 vezes encontrar a numeração mais próxima acima para gravar a nota fiscal, se ainda assim não enconstrar, também dará o HELP.

3 - A tabela SX5 não existe na filial do erro ou está inconsistente (o sistema não conseguiu encontrar)

**Soluções**

1 - Ajustar a numeração, pois ela pode existir nas tabelas citadas acima nos campos "F3\_NFISCAL", "F2\_DOC", "E1\_NUM", "F1\_DOC" e "D2\_DOC", além disso, há 200 números seguintes da numeração desejada que não são possíveis seu uso (o sistema faz 200 tentativas de gravar em alguma numeração sequencial acima).

2 - Certificar que o compartilhamento das tabelas SF3, SF2, SE1 ou SF1 estão adequadas conforme as séries na tabela SX5.

3 - Certificar que a tabela SX5 não esteja corrompida e no padrão (default).
