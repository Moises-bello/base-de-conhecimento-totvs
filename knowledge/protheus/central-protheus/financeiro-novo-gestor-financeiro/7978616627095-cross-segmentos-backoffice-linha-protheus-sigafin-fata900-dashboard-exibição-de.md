---
article_id: 7978616627095
category: Financeiro - Novo Gestor Financeiro
content_hash: 25e7a514da369ef19ccef8b477022785fee0b5ffc94a4bb10bb65adcec703be4
fetched_at: '2026-06-28T22:37:41.454606+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FATA900 - DASHBOARD
  - Exibição de todas as moedas para Filtro na Rotina
type: support-article
updated_at: '2026-03-25T18:22:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7978616627095-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FATA900-DASHBOARD-Exibi%C3%A7%C3%A3o-de-todas-as-moedas-para-Filtro-na-Rotina
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39291755871639) Tempo aproximado para leitura: **00:03 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar na FATA900 Dashboards Filtro de Moedas na Manutenção de Visões, apresenta somente a moeda Real, mesmo no ambiente com outras moedas cadastradas.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - FATA900 - Todas as versões  
  
**Causa**  
Mesmo que existam outras moedas na **SM2**, faz-se necessário o relacionamento contábil, pois a validação da rotina passa a verificar **MOEDA** X **CALENDÁRIO CONTÁBIL**.   
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:   
  
**1**. Abra o sistema módulo **34 - Contabilidade Gerencial.**  
**2**. Pelo menu acesse: **Atualizações** > **Cadastros** **Moedas** **Contábeis** (**CTBA140**) - Crie a moeda.  
**3**. Depois, novamente pelo menu, acesse **Atualizações** > **Moedas** X **Calendários** (**CTBA200**) e faça a referência entre moeda e o calendário contábil ativo para o sistema.   
**4.** Reinicie o **Dashboard** e todos os filtros que compõem moeda serão apresentados.

**Saiba Mais**

[Moeda x Calendário (CTBA200 - SIGACTB)](https://tdn.totvs.com/pages/viewpage.action?pageId=339511932)

[Moedas Contábeis (CTBA140 - SIGACTB)](https://tdn.totvs.com/pages/viewpage.action?pageId=306856715)
