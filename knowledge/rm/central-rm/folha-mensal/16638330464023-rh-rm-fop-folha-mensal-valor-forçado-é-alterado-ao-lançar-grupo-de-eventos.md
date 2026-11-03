---
article_id: 16638330464023
category: Folha Mensal
content_hash: ae53a86924e45494b23468a7e866af0800f616ed2cfc910ef320671da3bd8dbb
fetched_at: '2026-06-28T22:46:58.187043+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Folha Mensal: Valor forçado é alterado ao lançar grupo de
  eventos '
type: support-article
updated_at: '2025-02-12T18:22:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16638330464023-RH-RM-FOP-Folha-Mensal-Valor-for%C3%A7ado-%C3%A9-alterado-ao-lan%C3%A7ar-grupo-de-eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16638352237847) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**Quando há um evento com valor forçado já lançado no envelope, ao realizar o processo de Lançamento Grupo de Eventos novamente, o evento com valor forçado é alterado para outro valor. Por qual motivo isso pode ocorrer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**1. Para que o valor do evento que foi forçado não seja alterado, é necessário acessar: **Folha Mensal | Lançamentos | Grupo de Eventos** conforme a imagem abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16637941056279)

2. Logo após, acesse a aba "Eventos do grupo" para verificar qual é o comportamento que está vinculado aos eventos forçados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16638064402199)

3. Se os eventos forçados estiverem com o comportamento "Substituir", é necessário alterar para "Ignorar". Veja o exemplo abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16638095365271)

4. Após alteração, ao lançar o grupo de eventos, o valor forçado será mantido e ficará da forma desejada. 

**Importante:** Para melhor entendimento da coluna "Comportamento", veja abaixo as explicações referente a cada ação:   
  
**Ignorar:** Mantém o valor do evento caso ele já exista;

**Somar:** Soma o valor constante no movimento com o valor do evento já lançado, caso o evento já exista;

**Substituir:** Substitui o valor do evento já lançado, caso o evento já existia.

**Saiba Mais:**

[RH - RM - FOP - Lançamento do Grupo de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014011632-RH-RM-FOP-Lan%C3%A7amento-do-Grupo-de-Eventos)
