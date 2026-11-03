---
article_id: 33700310339735
category: eSocial - Gerar XML/ Integração Evento
content_hash: 2869c488ae61f70a6691f3f4ea81162e4723b2aafcafb8cac6158c8bb340ed2e
fetched_at: '2026-06-28T22:47:13.106186+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Reintegração: Ajuste no Evento S-1200 para Desconsiderar
  Valores da Rescisão'
type: support-article
updated_at: '2025-07-25T13:09:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33700310339735-RH-RM-FOP-eSocial-Reintegra%C3%A7%C3%A3o-Ajuste-no-Evento-S-1200-para-Desconsiderar-Valores-da-Rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33700280320791) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Na geração do XML do evento S-1200 referente ao mês de reintegração do funcionário, o sistema estava considerando, de forma indevida, os valores do complemento juntamente com os valores já pagos no evento de rescisão, ocasionando duplicidade de informações no envio ao eSocial.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - A partir dos patches: 12.1.2402.255, 12.1.2406.199, 12.1.2410.130 e superiores   
  
**Solução**  
Foi ajustada a geração do evento **S-1200** para considerar **somente o lançamento do complemento no mês da reintegração**.  
A rotina agora valida o mês da reintegração e **desconsidera os envelopes lançados com data de pagamento de até 10 dias após a data de desligamento**, conforme informado no cadastro do funcionário;

Exemplo no Cadastro do Funcionário: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33700612104087)

Saiba mais:   
[Mapeamento Evento S-1200](https://tdn.totvs.com/display/public/LRM/Evento+S-1200)
