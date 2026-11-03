---
article_id: 360020289992
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 3ec5fcbff04c13cf44d65f6acd0283038b5ef9c626035ab82e635cbf019a8b3c
fetched_at: '2026-06-28T22:45:20.993629+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Integração - O valor 'xxx' informado
  na tag tpInsc não existe na base de dados
type: support-article
updated_at: '2026-02-23T16:52:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020289992-RH-Linha-Protheus-TAF-eSocial-Integra%C3%A7%C3%A3o-O-valor-xxx-informado-na-tag-tpInsc-n%C3%A3o-existe-na-base-de-dados
---

**Dúvida**

Ao integrar os eventos para o TAF é rejeitado com a mensagem: O valor 'xxx' informado na tag tpInsc não existe na base de dados;

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF -Todas as versões

**Solução**

1 - Acesse a rotina de estabelecimentos no TAF, localize o número de inscrição informado no erro, clique em visualizar e confirme se existe número de recibo na aba "Número do recibo". Caso o campo de protocolo esteja em branco, transmita o evento S-1005 ou faça o ajuste de recibo se o evento já constar no esocial.

[RH - Linha Protheus - TAF - eSocial - Eventos de Tabelas - S-1005 - Como acessar a rotina de estabelecimentos, obras ou órgãos públicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037760133)

[RH - Linha Protheus - TAF - eSocial - Funcionalidades - Como realizar ajuste de recibo do e-Social no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019678672-RH-Linha-Protheus-TAF-eSocial-Funcionalidades-Como-realizar-ajuste-de-recibo-do-e-Social-no-TAF?source=search)

Se o protocolo estiver preenchido, confirme a data de inicio deste S-1005 pois a mesma deverá ser igual ou anterior a data do evento que está tentando integrar.

Após os ajustes refaça a integração do registro que apresentou o erro inicialmente.
