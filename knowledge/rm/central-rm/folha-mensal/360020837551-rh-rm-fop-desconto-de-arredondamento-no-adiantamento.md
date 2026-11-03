---
article_id: 360020837551
category: Folha Mensal
content_hash: 054a189cad057ce49f232dc1e88265f2f7d877f13b5b741f29f4409b9d62096a
fetched_at: '2026-06-28T22:46:59.548184+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Desconto de arredondamento no adiantamento
type: support-article
updated_at: '2025-01-22T18:37:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020837551-RH-RM-FOP-Desconto-de-arredondamento-no-adiantamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:01:20 min****Dúvida**  
Qual a parametrização para que o sistema não desconte o saldo devedor do funcionário no adiantamento salarial do funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Por padrão, o sistema lança o evento desconto de arredondamento (código de cálculo 21) na movimentação posterior ao lançamento do evento código de cálculo 20, se o funcionário possuir líquido positivo no envelope.  
  
Caso queira que o sistema não realize o lançamento do desconto de arredondamento no adiantamento salarial do funcionário, será necessária criar e vincular uma fórmula aos eventos código de cálculo 20 e 21, definindo o tratamento específico para o adiantamento.  
  
**Saiba Mais**  
Uma dica sobre isso, é cadastrar uma fórmula zerada para que os eventos não tenham valor e por isso não sejam considerados nos cálculos. Caso queira uma validação mais completa, a fórmula deverá ser criada.
