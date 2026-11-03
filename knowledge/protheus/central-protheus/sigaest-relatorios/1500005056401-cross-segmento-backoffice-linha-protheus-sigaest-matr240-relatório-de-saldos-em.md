---
article_id: 1500005056401
category: SIGAEST - RELATORIOS
content_hash: b5e54961360b9b7417bd758c27bdb2acc363b194f9758c655fd667c0086bac7e
fetched_at: '2026-06-28T22:39:06.060096+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR240 - Relatório
  de Saldos em Estoque imprimindo com Armazém com **
type: support-article
updated_at: '2022-08-08T12:12:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005056401-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR240-Relat%C3%B3rio-de-Saldos-em-Estoque-imprimindo-com-Armaz%C3%A9m-com
---

**Dúvida**Ao emitir o relatório MATR240 - Saldos em Estoque Sintético - A coluna do Armazém (almoxarifado) é impressa com 2 asteriscos (\*\*). Como corrigir para que seja impresso o código do Armazem?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**O relatório Estoque Sintético (MATR240) apresenta o código do armazém somente quando a pergunta  "**Aglutina por**" está = **Armazém**. Quando selecionada as opções "Filial" ou "Empresa", é somado o valor total e quantidade do produto em estoque para os armazéns informados no range dos parâmetros e apresentado no relatório com asterisco, simbolizando assim que o saldo não pertence a um armazém específico, mas sim a todos.  
  
Segue um exemplo em ambiente padrão:  
  
**Aglutina por filial:**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007047801/mceclip0.png)**

**Resultado:**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007047921/mceclip1.png)**

**Aglutina por armazém:**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006861502/mceclip2.png)**

**Resultado:**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006861602/mceclip3.png)**

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)*
