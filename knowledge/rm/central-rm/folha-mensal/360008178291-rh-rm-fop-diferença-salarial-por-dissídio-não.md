---
article_id: 360008178291
category: Folha Mensal
content_hash: 02433077c709e684f2e44c54ace7d9b7e02a9e3aa570a57cf49e3825cbbdc19a
fetched_at: '2026-06-28T22:47:00.315941+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Diferença salarial por dissídio não
type: support-article
updated_at: '2024-10-15T20:54:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008178291-RH-RM-FOP-Diferen%C3%A7a-salarial-por-diss%C3%ADdio-n%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24229542278935)Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**Como realizar a diferença salarial por dissídio?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para realizar o procedimento de diferença salarial, realize os seguintes passos:  
  
1. O primeiro passo para gerar a diferença salarial é fazer a alteração salarial.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6934414909207)  
  
Sendo assim, segue documentação orientando o processo de alteração global: [RH - RM - FOP - Alteração Global de Salários.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007539911)  
  
2. Logo, acesse: **Folha mensal | Lançamentos | Diferença salarial.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4461167024791)**3. Informe a competência inicial e a competência final do aumento.   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6934492592407)  
  
4. No envelope o sistema lança o evento com código de cálculo com incidência em INSS, por se tratar de uma diferença salarial por dissídio não.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6934948072343)  
  
Na ficha financeira na aba "**verbas geradas por diferença**", demonstra os eventos que tiveram valor de diferença lançados,  assim como a informação 0 se for dissídio não e 1 se for dissídio sim.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6934929243415)  
  
**Importante**Para o processo de diferença salarial, deverão ser criados dois eventos com [Código de Cálculo 37.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718613) Sendo, um com incidência em INSS e outro sem incidência. Portanto:

* **Dissídio Sim =** Eventos de código de cálculo 37 sem Incidência em INSS | Dissidio SIM
* **Dissídio Não =** Eventos de código de cálculo 37 com Incidência em INSS | Dissidio NÃO

Em relação às diferenças que estão sendo pagas no mesmo mês da rescisão, o tipo de cálculo a ser utilizado poderá ser o de diferença normal. Contudo, é imprescindível estar atento ao tipo de demissão e ao prazo de recolhimento do FGTS, uma vez que, dependendo da data de recolhimento, poderá haver a incidência de multa e juros.  
  
**Saiba Mais**  
[RH - RM - FOP - Cadastro de Dissídio de Acordo Coletivo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016287591-RH-RM-FOP-Cadastro-de-Diss%C3%ADdio-de-Acordo-Coletivo)
