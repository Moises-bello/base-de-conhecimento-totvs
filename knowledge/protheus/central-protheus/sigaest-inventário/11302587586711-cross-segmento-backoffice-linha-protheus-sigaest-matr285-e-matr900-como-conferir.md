---
article_id: 11302587586711
category: SIGAEST - INVENTÁRIO
content_hash: d2f8eb9814d6a38d9e76b7880b09f7286c940fc3b554cac4d0f08f151b199e47
fetched_at: '2026-06-28T22:38:50.430567+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR285 e MATR900
  - Como conferir após o processamento do inventário os itens que foram ajustados
type: support-article
updated_at: '2025-10-13T19:52:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11302587586711-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR285-e-MATR900-Como-conferir-ap%C3%B3s-o-processamento-do-invent%C3%A1rio-os-itens-que-foram-ajustados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35604761197591) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Após o processamento do inventário, o relatório de Conferência (MATR285) não apresenta a quantidade inventariada, como devo conferir o que foi ajustado?

***Sugestão*:** Assista também o ***Webinar que apresentamos sobre o processo padrão de inventário*** no Protheus, ***[clique aqui](https://www.youtube.com/watch?v=x-UMZkr8ukA)***.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Após a digitação do inventário, emitir o relatório MATR285 para conferência dos itens que serão ajustados. Porém, após o ***processamento do inventário (MATA340)***, o relatório MATR285 não exibe mais as diferenças.

Não se trata de um erro, pois o relatório é para conferência antes do processamento do inventário, e pode ser utilizado inclusive para revisar se realmente foi contado corretamente o saldo físico, dessa forma, pode-se alterar a digitação do inventário se necessário.

Exemplo simulado abaixo:

***Saldo atual no sistema quantidade 100 e saldo físico digitado pelo usuário com quantidade 150.***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11303352435223)

***Após o processamento do inventário (MATA340) observe que não exibe mais a diferença.***

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11303459136023)

***Nesse caso, para identificar o que foi ajustado, deve utilizar o relatório MATR900 por Documento e sequência de impressão Digitação e a data que foi processado o inventário.***

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11303992767127)

***Veja o resultado abaixo. Nesse exemplo, apresenta a quantidade que foi inventariada com documento igual INVENT:***

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11303720861079)

***Dica:*** Sugerimos, antes de processar o inventário, fazer um backup do relatório MATR285 para futuras consultas.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Inventário no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033402-SIGAEST-INVENT%C3%81RIO)*
