---
article_id: 28080603161879
category: Financeiro - Movimentação Bancária
content_hash: 14d7cac2f446e901bf8d914a74930cf7d61ba82638573a2ce29df48c0f3fb017
fetched_at: '2026-06-28T22:38:19.376963+00:00'
product: protheus
section_id: 1500001550402
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN – Help: FA100NAT'
type: support-article
updated_at: '2025-01-24T20:19:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28080603161879-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Help-FA100NAT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28080641459863) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao efetuar a baixa a pagar de um título com um banco em moeda 2, ocorre o erro: **Help: FA100NAT.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28080641460887)  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.2310  
  
**Causa**Este help ocorre quando, na natureza financeira, houver algum campo com valor igual a **"S-Sim"**, o que resulta no cálculo do imposto, mesmo que a porcentagem do campo de imposto esteja igual a 0,00.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28080603145239)

**Solução**Necessário alterar o cadastro da **natureza financeira** em **Atualizações -> Cadastros -> Naturezas**, informando os campos de imposto como **"N-Não"** para desativar o cálculo do imposto.
