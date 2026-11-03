---
article_id: 10544883310231
category: Históricos
content_hash: 4b1cd8315968a5147b6a8dfae61412dd5da0ad226dfc01e5c3c968e12e72fa41
fetched_at: '2026-06-28T22:46:45.533609+00:00'
product: rm
section_id: 1500000834701
source: central-rm
title: RH - RM - FOP - Histórico Salarial - Campo % Variação Salarial
type: support-article
updated_at: '2024-09-16T18:58:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10544883310231-RH-RM-FOP-Hist%C3%B3rico-Salarial-Campo-Varia%C3%A7%C3%A3o-Salarial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:27 min****Dúvida**Como é calculado o campo "% Variação Salarial" no Histórico Salarial do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

O campo é calculado internamente e é uma variação entre o salario anterior e atual levando em consideração a data de processamento e não o percentual de alteração salarial.  
  
**Exemplo de calcular a variação do percentual:**

Para variação percentual: aumento e diminuição percentual, dos valores.  
Para calcular a variação percentual entre os valores A e B, use a seguinte fórmula:

```
=(B-A)/A que é igual variação percentual
```

Ao aplicar esta fórmula para dados reais, é importante que você determine corretamente qual valor é **A** e qual é **B**.  
  
Segue um exemplo para facilitar o entendimento.  
  
2551,54 - 1553,04 = 998,50 / 1553,04  
0,6429325709576057 \* 100  
64,29325709576057  
  
![](https://totvssuporte.zendesk.com/attachments/token/irgUAwggvyghr7MSkfdV7C5Mc/?name=inline1405028139.png)
