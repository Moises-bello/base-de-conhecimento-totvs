---
article_id: 360048293454
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 0811bebfbe09344dc370a306df5ffaee85d0cff41380be2f84e2c2a609bc40bb
fetched_at: '2026-06-28T22:40:44.413608+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 : ECD I051 COD_PLAN_REF
  O registro I051 é obrigatório quando existe código do plano de contas referencial
  informado no registro '
type: support-article
updated_at: '2021-12-03T15:07:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048293454-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-I051-COD-PLAN-REF-O-registro-I051-%C3%A9-obrigat%C3%B3rio-quando-existe-c%C3%B3digo-do-plano-de-contas-referencial-informado-no-registro
---

**Dúvida**O registro I051 é obrigatório quando existe código do plano de contas referencial informado no registro 0000 (COD\_PLAN\_REF).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071285254/mceclip0.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072464313/mceclip3.png)  
**Ambiente**  
Protheus – Contabilidade gerencial – A partir da versão 12.1.17  
  
**Solução**

* O validador esta apresentando erro na linha 249 , veja que o registro I051  não foi gerado para essa conta

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072464333/mceclip4.png)

* Através do validador é possível clicar sobre o erro

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072464153/mceclip2.png)

* O validador demonstra que a conta referencial não foi gerada

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072464053/mceclip1.png)

* Diante disso se faz necessário verificar o porque a conta referencial não foi gerada para essa conta , para realizar essa analise [Veja COMO GERAR OS REGISTROS I050 E I051: PLANO DE CONTAS E PLANO DE CONTAS REFERENCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022515312-MP-SIGACTB-ECD-COMO-GERAR-OS-REGISTROS-I050-E-I051-PLANO-DE-CONTAS-E-PLANO-DE-CONTAS-REFERENCIAL?source=search)

Saiba mais

[MP - SIGACTB : ECD I050 E I051: GERAR CONTA BLOQUEADA , SEM SALDO ANTERIOR E OU SEM MOVIMENTO NO PERIODO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047812633-MP-SIGACTB-ECD-I050-E-I051-GERAR-CONTA-BLOQUEADA-SEM-SALDO-ANTERIOR-E-OU-SEM-MOVIMENTO-NO-PERIODO?source=search)
