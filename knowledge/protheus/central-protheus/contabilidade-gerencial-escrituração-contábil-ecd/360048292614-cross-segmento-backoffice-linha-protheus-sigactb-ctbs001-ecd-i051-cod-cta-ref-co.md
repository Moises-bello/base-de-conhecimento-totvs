---
article_id: 360048292614
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: f62d2fa655add875d369533f1468db8508d581f003fb076b1b902de82355705a
fetched_at: '2026-06-28T22:40:44.379624+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001  : ECD I051:
  COD_CTA_REF ; Conta não existe no plano de contas referencial informado no registro
  0000 (COD_PLAN_REF).'
type: support-article
updated_at: '2024-04-11T19:55:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-I051-COD-CTA-REF-Conta-n%C3%A3o-existe-no-plano-de-contas-referencial-informado-no-registro-0000-COD-PLAN-REF
---

**Dúvida**

3 - COD\_CTA\_REF ; Conta não existe no plano de contas referencial informado no registro 0000 (COD\_PLAN\_REF).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072459633)  
  
**Ambiente**   
Protheus – Contabilidade gerencial – A partir da versão 12.1.17

**Solução**

* Através do validador é possível clicar sobre o erro

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071281994)**

* O validador apresenta mensagem que a Conta é invalida

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071282094)**

* Ao clicar sobre  a conta veja que a conta não existe na relação de contas do PGE

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071282194)**

**O PGE considera a contas referencial existente na**[Tabelas Dinâmicas e Planos de Contas Referenciais](http://sped.rfb.gov.br/arquivo/show/4273)

* Com isso acesse a tabela e veja se a conta que esta apresentando erro existe na tabela dinâmica . Neste exemplo a conta 1.01.01.02.00  não existe na aba L100A
* Necessário verificar nas demais abas se a conta existe

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071282974)

* Cada empresa possui o seu plano de contas referencial L100A,P100....P150B, verifique qual se enquadra a sua empresa , com base nessa informação busque a conta na tabela dinâmica

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071282634)

* Com isso erro esta sendo apresentado pois os o plano de contas referencial utilizado não esta atualizado conforme o plano referencial da receita
* A receita é responsavel por liberar o plano referencial para entregas das obrigações.Diante obtenha o plano referencial atualizado junto a receita e posteriormente atualize o plano referencial utilizado no sistema
* [Veja como Como importar Plano referencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007547712-MP-SIGACTB-Como-importar-Plano-referencial-?source=search)
* preencher o parâmetro abaixo .

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22729622849815)

Saiba mais

[MP - SIGACTB : ECD I050 E I051: GERAR CONTA BLOQUEADA , SEM SALDO ANTERIOR E OU SEM MOVIMENTO NO PERIODO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047812633-MP-SIGACTB-ECD-I050-E-I051-GERAR-CONTA-BLOQUEADA-SEM-SALDO-ANTERIOR-E-OU-SEM-MOVIMENTO-NO-PERIODO?source=search)

[MP - SIGACTB : ECD COMO GERAR OS REGISTROS I050 E I051: PLANO DE CONTAS E PLANO DE CONTAS REFERENCIAL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022515312-MP-SIGACTB-ECD-COMO-GERAR-OS-REGISTROS-I050-E-I051-PLANO-DE-CONTAS-E-PLANO-DE-CONTAS-REFERENCIAL?source=search)
