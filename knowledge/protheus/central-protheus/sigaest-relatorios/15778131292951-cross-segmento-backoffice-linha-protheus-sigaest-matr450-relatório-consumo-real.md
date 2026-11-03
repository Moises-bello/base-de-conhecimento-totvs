---
article_id: 15778131292951
category: SIGAEST - RELATORIOS
content_hash: a50f34e71c191046f48b22241ff1e78f8dd3a69e19bc1ccf0ba44be7cdc6a42f
fetched_at: '2026-06-28T22:39:06.154630+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR450 - Relatório
  Consumo Real vs Standard não está aglutinando os produtos
type: support-article
updated_at: '2023-07-04T19:35:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15778131292951-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR450-Relat%C3%B3rio-Consumo-Real-vs-Standard-n%C3%A3o-est%C3%A1-aglutinando-os-produtos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15778089658519) Tempo aproximado para leitura: **00:03:12 min** **Dúvida**Relatório Consumo Real X Standard não está aglutinando os produtos. O que fazer?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

O Relatório Consumo Real vs Standard, a partir da sua atualização de 26/05/2023, mudou o conceito de aglutinação de produtos.

**Diferenças entre os relatórios MATR450 antes e MATR450 depois de 26/05:**

No relatório antigo:  
Requisições: Req1, Req2, Req3  
Ordem de Produção: OP1  
   
Relatório antigo agrupava todas as requisições em uma linha só:  
OP1 - Req1, Req2, Req3  
   
No relatório novo:  
Requisições: Req1, Req2, Req3  
Ordem de Produção: OP1  
   
O relatório novo quebra cada linha para cada requisição, discriminando assim cada requisição para OP:  
OP1 - Req1  
OP1 - Req2  
OP1 - Req3  
   
Dessa forma, no novo relatório, cada requisição é apresentada em uma linha separada, permitindo uma visualização mais detalhada das requisições associadas a uma determinada Ordem de Produção.

**Exemplos práticos**

 Portanto, antes o relatório agrupava todas as requisições de um produto para OP em uma linha só, veja exemplo onde isso discrimina claramente quando a pergunta 1 (Relação Por = Ordem de Produção):  
   
Exemplo de uma OP que tiveram varias requisições do produto MP-0020:  
![](https://totvssuporte.zendesk.com/attachments/token/jkFkiMqd2ltnABZklZJERb8jl/?name=image.png)  
   
Relatório antigo agrupava todas as requisições em uma linha só (parecido quando o usuário deixa a pergunta 1  - Relação por" = Ordem de Produção):  
![](https://totvssuporte.zendesk.com/attachments/token/YrW87tGTLDqFnpsUXVrkFPbGr/?name=image.png)  
   
Relatório novo quebra cada linha para cada requisição:  
![](https://totvssuporte.zendesk.com/attachments/token/bHcclqrGJNzyVm0XOvLQyK0h3/?name=image.png)  
   
   
Esta foi uma mudança no fonte padrão, do qual realmente se tornou o comportamento atual.

**Qual a saída contorno para obter o comportamento que tinha antes no relatório?**

A primeira seria a possibilidade de deixar a pergunta "Relação por" = Ordem de Produção. Desta forma ele tem um comportamento similar de aglutinação, se o produto tenha sido consumido varias vezes em uma OP.

Caso mesmo assim não seja o suficiente, outra saída seria baixando o fonte para adequar a esta necessidade. Veja mais em: [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Fontes de relatórios Estoque para alteração ou customização fora do padrão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058126794-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Fontes-de-relat%C3%B3rios-Estoque-para-altera%C3%A7%C3%A3o-ou-customiza%C3%A7%C3%A3o-fora-do-padr%C3%A3o)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
