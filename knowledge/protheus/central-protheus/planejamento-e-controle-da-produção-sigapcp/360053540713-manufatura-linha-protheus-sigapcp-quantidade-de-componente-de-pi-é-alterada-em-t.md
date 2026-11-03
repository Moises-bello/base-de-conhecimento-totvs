---
article_id: 360053540713
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 9b5c3f305510f09f3fbd81ae3ec69a448729836ae19cd8f12c6eddb8cf78d17c
fetched_at: '2026-06-28T22:42:45.808951+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Quantidade de componente de PI é alterada
  em todas as estruturas
type: support-article
updated_at: '2022-11-22T12:45:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053540713-Manufatura-Linha-Protheus-SIGAPCP-Quantidade-de-componente-de-PI-%C3%A9-alterada-em-todas-as-estruturas
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:26 min**  
**Dúvida**Por que ao alterar a quantidade de um componente de um **PI - Produto Intermediário** no **PCPA200 - Estrutura** é alterada em todas as estruturas que o **PI** é utilizado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Ao alterar a quantidade de um **MP - Matéria Prima** que é filho de um **PI** é alterado para as outras estruturas.  
  
Segue abaixo o exemplo onde possui estruturas dos produtos **A**, **B**, **C** e **D**, sendo que o produto **B** é um **PI**, e como pode ser observado esse **PI** pode ter quantidades diferente em várias estruturas:  
  
**Estrutura 1**  
**A** - Qtd Base 1    
|  
**B** - Qtd 1  
|  
**C** - Qtd 1  
  
**Estrutura 2**  
**D** - Qtd Base 2  
|  
**B** - Qtd 2  
|  
**C** - Qtd 1  
  
**Estrutura 3**  
**B** - Qtd Base 3  
|  
**C** - Qtd 1  
  
Porém, se alterar a quantidade do produto **C**, essa quantidade será replicada para todas as outras estruturas que utilizam o **PI** **B**, pois o componente **B** é pai do **C**.  
  
**Estrutura 1**  
**A** - Qtd Base 1    
|  
**B** - Qtd 1  
|  
**C** - Qtd 5  
  
**Estrutura 2  
D** - Qtd Base 2  
|  
**B** - Qtd 2  
|  
**C** - Qtd 5  
  
**Estrutura 3  
B** - Qtd Base 3  
|  
**C** - Qtd 5
