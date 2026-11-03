---
article_id: 4425314855447
category: RH - Lançamentos
content_hash: 6f07abb24b244839d175b2e7f1472e77c24f35cfe3db0b5969b2938891df1a6b
fetched_at: '2026-06-28T22:43:31.355619+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - Pagamento de Acúmulo de Função quando um Funcionário
  substitui outro
type: support-article
updated_at: '2025-07-24T17:13:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4425314855447-RH-Linha-Protheus-GPE-Pagamento-de-Ac%C3%BAmulo-de-Fun%C3%A7%C3%A3o-quando-um-Funcion%C3%A1rio-substitui-outro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26164504577943) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**Pagamento de **Acumulo de Função quando um Funcionário substitui outro**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No Sistema, **não existe um tratamento padrão para o caso**, ou seja, **não há um identificador de cálculo** para o calculo automático de de acumulo de função. Nestes casos, o que deve ser feito é **incluir uma verba em Atualizações - Def. de Cálculo - Verbas**, do tipo **Provento**, **sem id de cálculo**, configurar as incidências de INSS, IRRF, FGTS, e para médias, caso entre para médias.  
  
**Atenção:** Se a verba entrar para **médias,** ela **não pode incorporar o salário**, e se ela **incorporar** **ao salário não pode** ter informação para **médias.**  
  
Após criá-la, **pode efetuar o lançamento em Lançamentos - Por Funcionário mensalmente**, ou **informar numero de parcelas**, desta forma não precisa lançar mensalmente, **caso o valor seja fixo**. Além desta rotina, também pode usar a rotina de **Lançamentos - Valores Fixos informando a data de início de fim do pagamento** ou ainda, em **Valores Futuros,** informando o **período de início do pagamento**

**Saiba Mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
