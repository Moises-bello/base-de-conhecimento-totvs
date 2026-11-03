---
article_id: 360016459011
category: RH - Calculo Autonomo/Prolabore
content_hash: 6e2f80feae107e6fa6ae8a289ef3f762073baba5def4492bb0fc978c96ae1275
fetched_at: '2026-06-28T22:43:15.121804+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo para roteiro AUT apenas para matrículas
  com lançamentos na RGB - lançamentos por funcionário ou por verbas
type: support-article
updated_at: '2025-04-17T19:20:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016459011-RH-Linha-Protheus-GPE-C%C3%A1lculo-para-roteiro-AUT-apenas-para-matr%C3%ADculas-com-lan%C3%A7amentos-na-RGB-lan%C3%A7amentos-por-funcion%C3%A1rio-ou-por-verbas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25169282087319) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Como realizar cálculo para roteiro **AUT** apenas para as matrículas com eventos existentes na rotina de **Lançamentos Por Funcionários**, tabela **RGB**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para que o sistema execute o cálculo da folha de **Autônomos** e **Pró-labores** vinculados ao roteiro **AUT, somente** considerando os lançamentos informados (RGB), é necessário

**1.** Acessar módulo **Configurador,** selecione as opções **Base de Dados > Dicionário > Base de Dados** e localize o parâmetro **MV\_AUTOSRC.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31493259155095)  
  
2. Altere** o conteúdo do parâmetro para **.T.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/31493259155607)**  
**3.** Realizar o cálculo do roteiro AUT.  
  
**Importante**A ideia é  para agilizar o cálculo da folha de pagamento do roteiro AUT.  
Quando o parâmetro estiver com .T. e for solicitado cálculo para o roteiro AUT sem que existam lançamentos na RGB, o sistema irá emitir a mensagem:**"Nenhum Funcionário Processado nessa Requisição".**

**Saiba Mais:**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
