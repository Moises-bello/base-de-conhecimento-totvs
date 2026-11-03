---
article_id: 7006150518551
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: d4f371ab1994f51a1bd5deca1604c82e8b74905a61375f674e6d058e2971e673
fetched_at: '2026-06-28T22:43:32.409362+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: 'RH - Linha Protheus - GPE - Mensagem ao gerar GRRF: Funcionário recebeu antecipação
  de 13º salário gerando valores de FGTS a recuperar'
type: support-article
updated_at: '2025-06-26T13:33:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7006150518551-RH-Linha-Protheus-GPE-Mensagem-ao-gerar-GRRF-Funcion%C3%A1rio-recebeu-antecipa%C3%A7%C3%A3o-de-13%C2%BA-sal%C3%A1rio-gerando-valores-de-FGTS-a-recuperar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33069318741143) Tempo aproximado para leitura: **00:01:00 min** **Ocorrência**Mensagem ao gerar GRRF: Funcionário recebeu antecipação de 13º salário gerando valores de FGTS a recuperar.  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.1.27.  
  
**Causa**  
Mensagem ocorre pois na rescisão foi calculado o ID 0292-FGTS a recuperar.  
  
**Solução**Essa mensagem é apenas informativa, para ressaltar que na rescisão foi calculado o ID 0292:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7005501477655)

Esse ID é uma verba de base que é calculada quando por algum motivo foi calculado FGTS a maior, um exemplo é quando o funcionário recebe a 1ª parcela do 13º, mas é demitido e na rescisão a 2ª parcela é calculada com um valor a menor do que a 1ª parcela.  
O valor dela não será considerado na GRRF, caso queira a recuperação do valor de FGTS depositado a maior, deverá entrar em contato direto com a CEF para verificar como realizar essa recuperação, pois no *layout* da GRRF não existe campo para esse valor.

**Saiba mais:**

[RH GRRF (Guia de Recolhimento Rescisório FGTS)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781714-RH-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-FGTS)
