---
article_id: 13491090836119
category: RH - Lançamentos
content_hash: e65f20304f7e28ecc21ceaf30bf9a4d704937b902645828e7e617b4d7faec541
fetched_at: '2026-06-28T22:43:31.420991+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema permite deletar lançamento futuro que ainda
  não foi feito o pagamento de nenhuma parcela
type: support-article
updated_at: '2025-04-17T19:22:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13491090836119-RH-Linha-Protheus-GPE-Sistema-permite-deletar-lan%C3%A7amento-futuro-que-ainda-n%C3%A3o-foi-feito-o-pagamento-de-nenhuma-parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26080190414103) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Sistema permite deletar lançamento futuro que ainda não foi feito o pagamento de nenhuma parcela?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Sim, o sistema permite deletar um lançamento futuro que ainda não foi feito o pagamento de nenhuma parcela diretamente pela rotina de Valores Futuros pelo caminho **>Atualizações >Lançamentos >Valores Futuros**, para isso, o campo **Nr.Parc.Paga** deve estar com 0 no lançamento em questão, pois somente lançamentos com esse campo zerado vai ser possível deletar diretamente pela rotina de Valores Futuros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13490728285079)  
  
Para lançamentos que já foi feito o pagamento de pelo menos uma parcela, o sistema não permite deletar em valores futuros, deve ser feita a suspensão ou tratamento direto pela rotina de Conta corrente valores futuros.

Saiba Mais

[RH - Linha Protheus - GPE - Como efetuar os lançamentos Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006975151-RH-Linha-Protheus-GPE-Como-efetuar-os-lan%C3%A7amentos-Futuros)

[RH - Linha Protheus - GPE - Informada verba incorreta nos Lançamentos Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059007914-RH-Linha-Protheus-GPE-Informada-verba-incorreta-nos-Lan%C3%A7amentos-Futuros)

[RH - Linha Protheus - GPE - Sistema permite deletar lançamento futuro que ainda não foi feito o pagamento de nenhuma parcela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13491090836119-RH-Linha-Protheus-GPE-Sistema-permite-deletar-lan%C3%A7amento-futuro-que-ainda-n%C3%A3o-foi-feito-o-pagamento-de-nenhuma-parcela)

[RH - Linha Protheus - GPE - Como controlar as movimentações de Lançamentos Valores Futuros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006568592-RH-Linha-Protheus-GPE-Como-controlar-as-movimenta%C3%A7%C3%B5es-de-Lan%C3%A7amentos-Valores-Futuros)

[RH - Linha Protheus - GPE - Lançamento de Valores Futuros não é carregado para a folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14175822567447-RH-Linha-Protheus-GPE-Lan%C3%A7amento-de-Valores-Futuros-n%C3%A3o-%C3%A9-carregado-para-a-folha)
