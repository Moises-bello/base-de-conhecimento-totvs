---
article_id: 4418635977239
category: Férias
content_hash: 2357312f99e4ce32c1c8d80ac6897b0295fc05f31bcc7e1506959137ce71cf4a
fetched_at: '2026-06-28T22:46:56.338631+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Recesso de Estagiário
type: support-article
updated_at: '2025-01-22T18:36:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418635977239-RH-RM-FOP-Recesso-de-Estagi%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29425336376727) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como realizar o lançamento do recesso de estagiário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
  
1. Para que o TOTVS Folha de Pagamento realize a administração dos períodos aquisitivos, dias de recesso e seus cálculos, é necessário que o parâmetro **Considera tratamento para Recesso de Estagiário** esteja marcado. Este parâmetro está localizado no **Configurações | Parametrizador | Férias | Controle.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/29425336379543)  
  
2. Utilizando o parâmetro **Considera tratamento para Recesso de Estagiário**, será necessário incluir os cadastros dos eventos a seguir:  
  
[Código de Cálculo – 332 - Recesso de Estágio -](https://tdn.totvs.com/pages/releaseview.action?pageId=452719754#:~:text=Evento%20valor%20do%20tipo%20provento,as%20incid%C3%AAncias%20parametrizadas%20pelo%20usu%C3%A1rio.) Evento **valor** do tipo **provento**. Destinado ao cálculo de recesso de estagiário, sendo os descontos de acordo com as incidências parametrizadas pelo usuário.  
  
[Código de Cálculo – 333 - Recesso de Estágio Vencido](https://tdn.totvs.com/pages/releaseview.action?pageId=452718760) - Evento **valor** do tipo **provento**. Destinado ao cálculo de recesso de estagiário vencido, sendo os descontos de acordo com as incidências parametrizadas pelo usuário.  
  
[Código de Cálculo – 334 - Recesso de Estágio Proporcional -](https://tdn.totvs.com/pages/releaseview.action?pageId=452718761) Evento **valor** do tipo **provento**. Destinado ao cálculo de recesso de estagiário proporcional, sendo os descontos de acordo com as incidências parametrizadas pelo usuário.  
  
3. Logo, será necessário realizar o cadastro do recesso. O cadastro do período de gozo do recesso estagiário será realizado na mesma interface utilizada para o cadastro de férias. Portanto, acesse: **Administração de Pessoal | Funcionários | ícone Férias**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29425315791895)  
  
4. Feito isso, irá ser aberta a tela período de gozo.   
  
![](https://v2uploads.zopim.io/3/Y/h/3YhhAljRQojs3mXfAHLtQZRLS5ueXJam/e05b999f549130891ab5739cd034d0fe21cc4b66.png)  
  
**Importante**Quando o sistema é parametrizado para que as férias do Estagiário seja tratada como Recesso o sistema não possui um Recibo de Férias para ele. Portanto, na rotina padrão de férias não irá aparecer o botão **Calcular**, mas somente **Lançar** e **Finalizar**  
  
O cálculo será feito no momento do lançamento caindo diretamente no envelope do estagiário. Portanto, no momento em que você informar a data de início, a quantidade de dias e lançar, apenas é necessário atualizar a tela dos funcionários que ocorrerá a alteração do status para G.  
  
![](https://v2uploads.zopim.io/3/Y/h/3YhhAljRQojs3mXfAHLtQZRLS5ueXJam/1906fcbb3b7498086c6fc1abbcde66b71b7f6d0b.png)  
  
![](https://v2uploads.zopim.io/3/Y/h/3YhhAljRQojs3mXfAHLtQZRLS5ueXJam/1ed601c1fe81f1fd4a5ab0bec1899f8c707b3514.png)  
  
5. Logo, ao finalizar, a situação do funcionário voltará para o status **A**.  
  
**Saiba Mais**  
[RH - RM - FOP - Férias: Finalizar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012328752-RH-RM-FOP-F%C3%A9rias-Finalizar-?source=search)  
[Recesso Estagiário](https://tdn.totvs.com/display/public/LRM/DT_Recesso_Estagiario)
