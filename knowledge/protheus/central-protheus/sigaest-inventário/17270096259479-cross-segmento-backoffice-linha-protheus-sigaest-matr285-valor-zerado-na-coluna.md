---
article_id: 17270096259479
category: SIGAEST - INVENTÁRIO
content_hash: 8f741c7280b47c0a18487b587043c20d6b158d26c93470b31f240a959ad4892c
fetched_at: '2026-06-28T22:38:50.426669+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR285 - Valor zerado
  na coluna Diferença Valor
type: support-article
updated_at: '2023-09-04T19:43:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17270096259479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR285-Valor-zerado-na-coluna-Diferen%C3%A7a-Valor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17270086472727) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao emitir o relatório de **Conferência de Inventário (MATR285)** a coluna **DIFERENÇA VALOR** esta zerada, porém o produto tem valor no campo B2\_CM1, o que devo ajustar?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17270270902167)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17270287433111)  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

Para esse cenário, verifique se o parâmetro **MV\_CUSZERO esta habilitado**, caso o mesmo esteja igual Sim e a Quantidade do produto e Valor estiverem zerados, o inventário para incluir saldo vai considerar o custo do moviemnto igual a zero, por isso apresenta no relatório dessa forma. **[Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023788792-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-zerar-custo-de-movimento-no-Protheus-?source=search)** e veja o conceito do parâmetro.  
  
Avaliar com a equipe de Custos da empresa a necessidade de manter o parâmetro Habilitado, ou simplesmente desabilitando o relatório exibe o valor como desejar.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17270461477399)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17270449970711)

***Saiba Mais:***

[Clique aqui e veja mais artigos sobre INVENTÁRIOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)
