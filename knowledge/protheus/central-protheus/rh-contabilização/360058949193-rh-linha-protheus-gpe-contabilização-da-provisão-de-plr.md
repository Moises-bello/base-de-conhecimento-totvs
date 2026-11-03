---
article_id: 360058949193
category: RH - Contabilização
content_hash: 06b99a7f8dd3bc274fba0216aeba41256d035944fe43473f369327fc87b81717
fetched_at: '2026-06-28T22:43:45.928737+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Contabilização da provisão de PLR
type: support-article
updated_at: '2025-07-29T13:57:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058949193-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-da-provis%C3%A3o-de-PLR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33791339782423)**Tempo aproximado para leitura:**00:01:30 min**

**Dúvida**Contabilização da provisão de PLR.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

Após o cálculo da provisão, durante a contabilização, será gerado na tabela de resumo da folha (SRZ) os movimentos dos funcionários que receberam verbas de lançamento de PLR, assim como as verbas de baixa de PLR pagas.  
  
Os registros serão gerados utilizando a informação “PP” (Provisão PLR) para o campo do tipo da SRZ (RZ\_TIPO).  
   
Os valores negativos de PLR que foram recebidos também serão criados para o ‘desprovisionamento’ do saldo do funcionário, com sua respectiva verba de baixa.  
  
As outras atividades do processo de contabilização, como por exemplo, configuração de lançamento padrão, continuarão a funcionar da forma atual do produto padrão.

**Saiba mais:**

[Ponto de entrada para calculo de provisão PLR](https://tdn.totvs.com/pages/viewpage.action?pageId=286739120)
