---
article_id: 360013332532
category: Rescisão
content_hash: 49e8a6b2fbe11b7ce0efa5850c6649c724cb83b287e753d3940a59d3effc45ac
fetched_at: '2026-06-28T22:46:55.417489+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - GRRF: Não há total a recolher'
type: support-article
updated_at: '2024-10-18T15:46:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013332532-RH-RM-FOP-GRRF-N%C3%A3o-h%C3%A1-total-a-recolher
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:01 min  
  
Ocorrência**No módulo Folha de pagamento, ao tentar realizar a emissão da GRRF na aba **Rescisão** é apresentada a mensagem de erro: **Não há Total a Recolher para Emissão da GRRF. Verifique os detalhes de Cálculo no Log de Debug.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Este incidente ocorre para funcionários que utilizam tomadores de serviços por CEI, mas que não informaram o CEI no rateio de tomador vinculado ao funcionário.  
  
**Solução**  
Para solucionar essa ocorrência, siga as instruções.  
  
1. Acesse: **Administração de Pessoal | Funcionário** e selecione o funcionário em questão e depois vá em **Anexos | Folha de Pagamento | Rateio de Tomadores**. Verifique no cadastro do rateio do tomador, se está informado corretamente o número do **CEI**. Caso negativo, preencha o valor no campo **CEI**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360009371872/mceclip0.png)  
  
2. Acesse: **Administração de Pessoal | Evento** e informe em todos os evento e marque a flag **Segue rateio de tomadores.**  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5372698731671/mceclip0.png)  
  
3. Acesse: **Encargos | SEFIP | Distribuir SEFIP** e execute a distribuição.
