---
article_id: 360011514111
category: Encargos
content_hash: 933b3f70d7933002648b6b05fe1267acf1c53133b5cfd2b9a9a0b44b14d55733
fetched_at: '2026-06-28T22:46:53.404735+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: 'RH - RM - FOP - SEFIP: Erro 320649 Para movimentação I1, I2, I3, I4 ou L'
type: support-article
updated_at: '2025-03-05T18:50:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011514111-RH-RM-FOP-SEFIP-Erro-320649-Para-movimenta%C3%A7%C3%A3o-I1-I2-I3-I4-ou-L
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Na importação da SEFIP de uma Rescisão Complementar e ao importar essa situação no programa do SEFIP é apresentado mensagens de erros do **SEFIP** como:  
  
***3020623 - Data de movimentação deve ser informada dentro do mês de competência ou mês anterior.***  
ou  
***320649 - Para movimentação I1, I2, I3, I4 ou L a data de movimentação deve ser informada no mês da competência, mês anterior ou mês posterior.*** **320649 - Para movimentação I1, I2, I3, I4 ou L a data de movimentação deve ser informada no mês da competência, mês anterior ou mês posterior.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**O erro acontece nas importações da Sefip quando houver **Rescisões Complementares** após dois meses da rescisão original e quando na geração é marcado o parâmetro **Dissídio Não**.  
  
**Solução**  
Para solucionar essa ocorrência, siga as orientação abaixo:  
  
O próprio programa da Sefip não aceita **Rescisão Complementar** como **Dissídio Não,** caso tenha sido pago em competências após dois meses da rescisão original. Sendo assim, caso a **Rescisão Complementar** ocorra nesta situação, deverá ser gerada como **Dissídio Sim** e ao gerar o SEFIP deverá utilizar o código de recolhimento **650**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10961293785111)  
  
**Saiba mais**  
[COMO FAZER - Diferença Salarial e SEFIP por Dissídio](https://tdn.totvs.com/pages/releaseview.action?pageId=126714055)
