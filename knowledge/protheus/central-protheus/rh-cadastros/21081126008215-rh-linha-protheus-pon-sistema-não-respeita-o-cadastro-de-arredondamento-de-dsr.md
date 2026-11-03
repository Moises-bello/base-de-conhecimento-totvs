---
article_id: 21081126008215
category: RH - Cadastros
content_hash: 9a924f0cd0edca288b927ab57fc4dc629123dec99b4ae4988178fa8e5d3b12f1
fetched_at: '2026-06-28T22:44:53.119468+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Sistema não respeita o cadastro de Arredondamento
  de DSR
type: support-article
updated_at: '2025-12-10T12:46:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21081126008215-RH-Linha-Protheus-PON-Sistema-n%C3%A3o-respeita-o-cadastro-de-Arredondamento-de-DSR
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21081125971863) Tempo aproximado para leitura: 00:01:30 min********Dúvida****Mesmo existindo um cadastro de Arredondamento de DSR parcial, após o Cálculo Mensal o sistema gera verba de desconto de DSR nos Resultados.  
  
****Ambiente****TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
****Causa****O sistema **não irá validar** cadastros de faixas de Arredondamento de DSR, quando o parâmetro **MV\_DSRPROP** estiver com conteúdo **S**.  
  
****Solução****Neste caso, será utilizado como base para o desconto, **a quantidade de horas/minutos de apontamento que o funcionário teve na semana**, para que a verba de desconto de DSR seja gerada de forma proporcional.  
  
Segue abaixo um exemplo de cenário:  
  
Conteúdo do parâmetro **MV\_DSRPROP = S:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21081125973911)  
  
Cadastro de **Arredondamento de DSR:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21081124564503)  
  
  
**Regra de Apontamento** **- Aba Apuração**, mostrando que a apuração de DSR é Semanal:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21081124566551)  
  
  
No período de 01 à 31.01.2024, o funcionário teve apenas um atraso de 11 min, ou seja, **menor** que a quantidade inicial informada no cadastro de Arredondamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21081125978903)  
  
  
Cadastro do **Evento** de Atraso e Desconto DSR:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21081125981591)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21081124581911)  
  
Após o Cálculo Mensal, o sistema gerou a verba do desconto de Atraso + Desconto de DSR, pois como explicado, quando o **MV\_DSRPROP = S,** o sistema vai **desprezar** o cadastro de **Arredondamento** e gerar a verba de Desconto de DSR proporcional:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21081432120599)  
  
Se o conteúdo do **MV\_DSRPROP estiver como N**, o sistema geraria apenas a verba de desconto do Atraso, pois a quantidade gerada na semana foi inferior a quantidade inicial informada no Arredondamento:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21081447496599)  
  
  
**Saiba Mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como efetuar o desconto do DSR no Ponto Eletrônico quando existe Falta, Atraso ou Saída Antecipada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004970391-RH-Linha-Protheus-PON-Como-efetuar-o-desconto-do-DSR-no-Ponto-Eletr%C3%B4nico-quando-existe-Falta-Atraso-ou-Sa%C3%ADda-Antecipada)
