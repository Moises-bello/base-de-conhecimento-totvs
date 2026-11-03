---
article_id: 360034654694
category: RH - Rescisão
content_hash: f108f2fa7ff0df8bcf2d346fc24b852edec855be47da5578756f6154ca835b2f
fetched_at: '2026-06-28T22:43:48.369889+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE -  Como simular rescisão e efetivar cálculo de rescisão
  simulada
type: support-article
updated_at: '2025-09-09T13:22:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034654694-RH-Linha-Protheus-GPE-Como-simular-rescis%C3%A3o-e-efetivar-c%C3%A1lculo-de-rescis%C3%A3o-simulada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34806448451735) Tempo aproximado para leitura: **00:01:30 min**  
**Dúvida**Como simular rescisão e efetivar cálculo de rescisão simulada?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para executar o cálculo da simulação de uma rescisão, na rotina de **Rescisão**, pelo caminho **>Miscelânea >Cálculos >Rescisão**, posicione no funcionário e clique em Incluir:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12782805650327)  
  
No cabeçalho do cálculo, altere o campo **Resc. Efetiv.** para **Não** e calcule a rescisão clicando em **F6** ou em **>Outras Ações >Calcular Rescisão**:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12782886270231)  
  
Confirme o cálculo, no *grid* superior o funcionário permanecerá com o *status* verde pois continua ativo e no *grid* inferior o *status* ficará azul, de rescisão simulada:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12782968924567)  
  
Para efetivar a rescisão, ainda na rotina de Rescisão, posicione no funcionário simulado, clique em Incluir, e no campo **Resc. Efetiv.** altere para **SIM**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12783091670295)  
  
Clique em **Confirmar**, sistema apresentará a mensagem abaixo, clique em **SIM**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12783166307607)  
  
Rescisão será efetivada, tanto no *grid* superior quanto no *grid* inferior, a situação do funcionário será alterada para demitido (*status* vermelho):  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12783194551703)

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
