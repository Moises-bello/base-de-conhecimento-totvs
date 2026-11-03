---
article_id: 360036290853
category: eSocial - Gerar XML/ Integração Evento
content_hash: 24ad4451eae9fbb71709d2ffd9098dc32fc956d7b2aa2a865afb872abd79044a
fetched_at: '2026-06-28T22:47:11.847920+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - Erro ao transmitir S-1200: A data informada devera ser maior
  ou igual ao período de apuração informado'
type: support-article
updated_at: '2026-05-26T20:07:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036290853-RH-RM-FOP-Erro-ao-transmitir-S-1200-A-data-informada-devera-ser-maior-ou-igual-ao-per%C3%ADodo-de-apura%C3%A7%C3%A3o-informado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21152610237463) Tempo aproximado para leitura: 00:03:00 min**

**Ocorrência**  
Ao transmitir o evento S-1200 para o governo é retornado a inconsistência: **A data informada deverá ser maior ou igual ao período de apuração informado em #39;perApur#39;**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial  - Todas as Versões  
  
**Causa**  
A tag **comAcConv**é responsável por informar a data indicada no erro, esta tag informa a competência em que é devida a obrigação de pagar os efeitos remuneratórios de lei, acordo coletivo, convenção coletiva ou sentença normativa. A competência deve ser maior ou igual ao período de apuração indicado na tag **perApur**. 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047643573)

**Solução**  
Para solução deste erro, realize os passos abaixo:  
1. Acesse **Folha de Pagamento | eSocial | Acordo Coletivo / Reajuste por Lei** e edite o acordo utilizado para lançamento das verbas;  
2. Valide a competência acordada para pagamento, deverá ser igual ou maior ao período de apuração;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046776594)

3. Após ajustar a data acordada para pagamento, gere novamente o XML, integre e transmita.  
  
**Saiba mais**  
Para mais informações acesse:   
[RH - RM - FOP - eSocial - Informar verbas geradas por dissídio no eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004806532-RM-eSocial-Informar-verbas-geradas-por-diss%C3%ADdio-no-eSocial?source=search)
