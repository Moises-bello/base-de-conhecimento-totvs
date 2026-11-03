---
article_id: 4754343266967
category: Encargos
content_hash: 18b49c0974a198c5bd72e5d6181e5e8324e99bd766e8f87696afdc4e707f0834
fetched_at: '2026-06-28T22:46:53.178967+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Geração de Encargos
type: support-article
updated_at: '2025-03-07T18:18:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4754343266967-RH-RM-FOP-Gera%C3%A7%C3%A3o-de-Encargos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Dúvida**  
Como realizar a geração de encargos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para geração dos encargos da Folha de Pagamento acesse: **Encargos | Geração de Encargos**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10486406446359)  
  
O sistema traz como default o mês e ano de competência atual e período igual ao atual. Mas tanto a competência quanto o período poderá ser definido pelo usuário. 

**O campo Período é flexível no caso de contabilizar um ou mais de um período a ser selecionado, sendo que será apresentado um campo onde os períodos deverão ser separados por vírgula.**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10486408119831)  
  
O parâmetro **Permite valores negativos para fórmulas,** permite que o sistema faça a geração de encargos com valores negativos gerados por fórmula, ou seja, somente para os encargos cujo tipo é A **Valor calculado através de fórmula**.  
   
O parâmetro **Calcula somente rateio de encargos** é utilizado para o caso de alteração no rateio de encargos e seja necessário apenas o cálculo do rateio de encargos.  
   
O parâmetro **Considera duas casas decimais p/fórmulas** Com este parâmetro marcado os encargos calculados por fórmula serão gerados considerando apenas duas casas decimais, caso o parâmetro esteja desmarcado será gerado considerando quatro casas decimais. Na visualização dos históricos de encargos serão exibidos quatro casas decimais, caso os encargos tenham sido gerados com o parâmetro marcado as duas últimas casas decimais irão aparecer zeradas.  
   
A **Seleção de Encargos Ativos para Contabilização** serve para indicar quais os grupos de encargos **código de encargos ativos** devem ser processados.  
  
**Importante**  
O sistema de folha de pagamento somente gera os rateios por cento de custo no histórico de encargos na rotina de contabilização quando parâmetro **Usa histórico de rateio de encargos na contabilização retroativa** estiver marcado nos parâmetros do sistema.  
  
**Saiba mais**[RH - RM - FOP - Encargos: Criação de códigos ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021841391-RH-RM-FOP-Encargos-Cria%C3%A7%C3%A3o-de-c%C3%B3digos-ativos)  
[Encargos - Folha de Pagamento](https://tdn.totvs.com/display/public/LRM/Encargos+-+Folha+de+Pagamento)
