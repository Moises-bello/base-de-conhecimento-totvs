---
article_id: 360018234351
category: RH - Rescisão
content_hash: af7b10495347e2a98e3c0055dc5bea31c3d707d929e9923537c267fe69ec3ac3
fetched_at: '2026-06-28T22:43:49.721022+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Funcionário com afastamento no mês da rescisão,
  o campo 50 do TRCT carrega valor incorreto
type: support-article
updated_at: '2025-04-16T18:22:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018234351-RH-Linha-Protheus-GPE-Funcion%C3%A1rio-com-afastamento-no-m%C3%AAs-da-rescis%C3%A3o-o-campo-50-do-TRCT-carrega-valor-incorreto
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26556259312663)***Tempo aproximado para leitura: **00:*****01:00 min***

**Ocorrência**No módulo Gestão de Pessoal, quando funcionário tem afastamento no mês da rescisão traz saldo de dias corretamente no cálculo, porém no TRCT o **campo 50** carrega valor incorreto.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) GPE - Gestão de Pessoal - A partir da versão 12  
  
**Solução**Quando uma das verbas da rescisão estava com a configuração do campo **Tipo de Verba** com o valor **Horas**, o sistema exibia a quantidade incorreta do saldo de dias no campo 50. Foi realizado ajuste para impressão correta do campo 50, com essas configurações do sistema.  
  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Realize o *backup* prévio;  
2. Aplique o pacote de correção;  
3. Refaça o teste.

Link para acesso de pacotes de atualizações:  
<https://suporte.totvs.com/portal/p/10098/download#000006>

**Saiba mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
