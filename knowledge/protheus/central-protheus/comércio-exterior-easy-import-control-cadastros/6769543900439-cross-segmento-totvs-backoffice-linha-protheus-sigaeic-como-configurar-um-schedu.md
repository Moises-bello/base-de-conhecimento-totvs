---
article_id: 6769543900439
category: Comércio Exterior - Easy Import Control - Cadastros
content_hash: 2359c450a02528e0bedea551f5447d674f8efb6c6733f00d35b612bf0f6bcf41
fetched_at: '2026-06-28T22:39:52.175117+00:00'
product: protheus
section_id: 1500001549382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como Configurar
  um Schedule no Totvs Comex Conteúdo
type: support-article
updated_at: '2022-06-14T20:52:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6769543900439-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-Configurar-um-Schedule-no-Totvs-Comex-Conte%C3%BAdo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

É possível configurar um Schedule no Totvs comex conteúdo?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control*– Todas versões

**Solução**Segue abaixo os procedimentos necessários para efetuarem a schedule da integração da NCM e da Taxa:

 Agendamento para integração NCM e Ex-NCM.  
1. No Configurador (**SIGACFG**), acesse Ambiente/Schedule/Schedule (**CFGA010**).  
2. Em Schedule / Agendamentos / Cadastro, clique em Incluir.  
3. No campo Rotina (XX1\_ROTINA), informe a função **CD100SchNCM**.  
4. Clique em Recorrência e informe a periodicidade. Clique em Confirmar.  
5. Clique em Ok. O registro é gravado com sucesso.  
6. O sistema executará a integração de NCM e Ex-NCM conforme agendamento.  
  
Agendamento para integração Taxas de Moedas.  
1. No Configurador (SIGACFG), acesse Ambiente/Schedule/Schedule (**CFGA010**).  
2. Em Schedule / Agendamentos / Cadastro, clique em Incluir.  
3. No campo Rotina (XX1\_ROTINA), informe a função **CD100SchTX**.  
4. Clique em Recorrência e informe a periodicidade. Clique em Confirmar.  
5. Clique em Ok. O registro é gravado com sucesso.  
6. O sistema executará a integração de Taxas de Moedas conforme agendamento.

**Saiba mais**

[Integração TOTVS Comex Conteúdo x Easy Import Control](https://tdn.totvs.com/display/public/PROT/TULMK4_DT_Integracao_TOTVS_Comex_Conteudo)
