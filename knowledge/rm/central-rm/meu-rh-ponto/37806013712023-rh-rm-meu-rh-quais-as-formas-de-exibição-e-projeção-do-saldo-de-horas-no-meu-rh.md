---
article_id: 37806013712023
category: Meu RH - Ponto
content_hash: 5f19b81840348ff96956b6d418b61b2c45df8e5894340fa67ce4b9483a104084
fetched_at: '2026-06-28T22:47:30.236054+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Quais as formas de exibição e projeção do saldo de horas
  no Meu RH?
type: support-article
updated_at: '2026-01-20T17:42:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37806013712023-RH-RM-Meu-RH-Quais-as-formas-de-exibi%C3%A7%C3%A3o-e-proje%C3%A7%C3%A3o-do-saldo-de-horas-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37806013695895) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Quais opções o Meu RH disponibiliza para visualização e projeção do saldo de horas?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37806013696919)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**  
O dashboard saldo de horas do Meu RH disponibiliza diferentes opções para visualização e projeção do saldo de horas, conforme a parametrização definida no módulo Automação de Ponto | Configurações | Parametrizador | Iniciais | Cálculo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37806011875479)

A projeção do saldo é determinada pelo parâmetro “**Executa o cálculo até**”, que define até qual data o sistema irá considerar a movimentação do banco de horas dos funcionários.  As opções disponíveis são:

* **Fim do Período Mensal**  
  O sistema realiza o cálculo do saldo de horas considerando integralmente o período mensal.
* **A data atual**  
  O sistema projeta o saldo de horas desde a data inicial do período mensal configurado até a data atual do servidor. Caso a data atual seja posterior à data final do período mensal definido, o sistema considerará automaticamente a data final do período mensal.
* **A data atual menos 1 dia**  
  O sistema projeta o saldo de horas desde a data inicial do período mensal configurado até o dia anterior à data atual do servidor (ontem). Se essa data ultrapassar o término do período mensal definido, será considerada a data final do período mensal.

Para que as informações do saldo de horas sejam atualizadas no Meu RH, é necessário executar o [recalculo do espelho](https://RH%20-%20RM%20-%20PTO%20-%20Onde%20realizar%20o%20recalculo%20do%20ponto) após alteração dos parâmetros.

**Saiba Mais:**

[**RH - RM - Meu RH - Como exibir ou ocultar o saldo de banco de horas no Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414883509143-RH-RM-Meu-RH-Como-exibir-ou-ocultar-o-saldo-de-banco-de-horas-no-Meu-RH)

[**RH - RM - Meu RH - Como exibir o saldo do banco de horas do time para o gestor**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8741453560727-RH-RM-Meu-RH-Como-exibir-o-saldo-do-banco-de-horas-do-time-para-o-gestor)
