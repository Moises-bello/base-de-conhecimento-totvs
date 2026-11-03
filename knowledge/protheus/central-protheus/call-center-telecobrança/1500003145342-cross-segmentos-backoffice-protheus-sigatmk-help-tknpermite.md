---
article_id: 1500003145342
category: Call Center - Telecobrança
content_hash: 117938bc9dedc68d82a4380fcba2fbb800d8d9fa91b5bc5c77b98ee7ba6221d7
fetched_at: '2026-06-28T22:41:28.587867+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Help TKNPERMITE
type: support-article
updated_at: '2024-04-17T13:21:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003145342-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Help-TKNPERMITE
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22866535087767) Tempo aproximado para leitura: 00:01:00 min***

**Dúvida**

Qual a solução para o Help**: TKNPERMITE?**

**![Regra Negociação 02.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22866543736343)**

**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões.  
  
**Solução**

Situações onde pode ocorrer o Help: TKNPERMITE:

1- Ao alterar a data de retorno para uma data maior, o sistema gera o Help: TKNPERMITE:

No cadastro de telecobrança/regra de negociação (**TMKA190**), há o campo **Reagendar**( **K2\_DIAREAG**), é neste campo que deve ser efetuada a inclusão da quantidade de dias para retorno:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003207701)

Se no atendimento de telecobrança (**TMKA350/ TMKA274**) a data para retorno do atendimento compreender até 90 dias, conforme a definição do campo **Reagendar**, o sistema gravará normalmente o retorno:

![Telecobran_a_reagendar_em_90_dias.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003170442)

Se no atendimento de telecobrança a data para retorno do atendimento estiver acima de 90 dias, conforme a definição do campo **Reagendar**, o sistema emitirá o help **TKNPERMITE** para a data seja ajustada:

![Telecobran_a_reagendar_acima_de_90_dias.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003207841)

2- Ao tentar conceder um desconto de juros, ocorre o Help: TKNPERMITE:

No cadastro de telecobrança/regra de negociação (**TMKA190**), há o campo **Desc.Juros**( **K2\_DSCJUR**), é neste campo que deve ser efetuada a inclusão do percentual de juros que o operador poderá conceder no título em cobrança. Se estiver zerado , no momento em que efetuar o desconto da cobrança será emitido o help em questão.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4404559313303)

![Desnconto_de_juros_sem_informar_k2_dcsjur.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4404552356503)

Para que o sistema permita a informação desconto de juros no atendimento telecobrança, informe o percentual no campo **K2\_DSCJUR**. E posteriormente no atendimento informe o desconto de juros.

![Desconto_de_juros_informando_k2_dcsjur.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4404559789719)

Obs: Sempre avaliar se o campo de  **juros (acg\_juros)** possui valor, pois o help também ocorrerá na tentativa de informar desconto de juros sobre um campo zerado.

**Saiba mais**: [Habilitar o telecobranças do Call Center (SIGATMK)](https://tdn.totvs.com/x/YWw-Dg)
