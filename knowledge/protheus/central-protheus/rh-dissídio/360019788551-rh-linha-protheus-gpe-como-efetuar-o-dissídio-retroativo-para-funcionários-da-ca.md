---
article_id: 360019788551
category: RH - Dissídio
content_hash: d3fd76fbd8656594613bc012d4b50d1278a77a95f1d69783495c555219404119
fetched_at: '2026-06-28T22:43:43.289528+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Como efetuar o dissídio retroativo para funcionários
  da categoria J professores aulista
type: support-article
updated_at: '2025-08-07T15:05:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019788551-RH-Linha-Protheus-GPE-Como-efetuar-o-diss%C3%ADdio-retroativo-para-funcion%C3%A1rios-da-categoria-J-professores-aulista
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34015583233303)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como o sistema faz para realizar o cálculo de dissídio retroativo para funcionários da categoria **"J"**, se os mesmos não possuem salário cadastrado no campo **RA\_SALARIO?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Versão 12.

**Solução**

As tarefas são cadastradas na tabela S070 em **Atualizações > Definições de cálculo> Manutenção de tabelas.**

Para efetuar o cálculo de dissídio retroativo referente a categoria J, é necessário atualizar as tarefas com o percentual de reajuste:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015361012)

1. Acesse Miscelânea > Reajuste> Tarefas.  
  
Defina os parâmetros de acordo com o perfil que deve ser atendido:

a pergunta atualiza tarefas deve ser executada como não, no primeiro momento, para gerar o relatório para conferência.

Quando estiver como **SIM** será atualizado os valores na tabela de tarefas S070.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18053946593175)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18053972907287)

**2. Relatório de aumento de tarefas:**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18054338944919)**

**3. Tabela S070 após atualização das tarefas:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18054474361751)

**4. Acesse Miscelânea > Reajuste> Dissídio retroativo.**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360015361492)**

Efetuar o cálculo de acordo com as configurações de perguntas da rotina :

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18055055566487)**

Em Outras ações -> Manutenção podemos verificar os cálculos realizados , baseado na folha de pagamento , tratando as verbas e valores ORIGEM, valor calculado com o reajuste e valor a pagar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18056978803095)

**Saiba Mais:**

[Artigos Dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)

[RH - Linha Protheus - GPE - Cálculo, geração e conferência do dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056146513-RH-Linha-Protheus-GPE-C%C3%A1lculo-gera%C3%A7%C3%A3o-e-confer%C3%AAncia-do-diss%C3%ADdio-retroativo)

[RH - Linha Protheus - GPE - Como parametrizar e calcular o dissídio retroativo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034578653-RH-Linha-Protheus-GPE-Como-parametrizar-e-calcular-o-diss%C3%ADdio-retroativo)
