---
article_id: 13922311421719
category: RH - CNAB
content_hash: 73e5155514cfef05bcc737b335bd16cb48fd4b51f2e20d419f7825758f889d2e
fetched_at: '2026-06-28T22:43:39.349154+00:00'
product: protheus
section_id: 360004833653
source: central-protheus
title: RH - Linha Protheus - GPE - Uso da pergunta/filtro Centro de Custos na geração
  do arquivo CNAB com folha rateada
type: support-article
updated_at: '2025-09-19T19:08:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13922311421719-RH-Linha-Protheus-GPE-Uso-da-pergunta-filtro-Centro-de-Custos-na-gera%C3%A7%C3%A3o-do-arquivo-CNAB-com-folha-rateada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32854174581655) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Uso da pergunta/filtro Centro de Custos na geração do arquivo CNAB com folha rateada  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**

A geração da folha de pagamento rateada por centro de custos, realizada conforme documentação abaixo, apresentará os valores de líquidos separados conforme configuração da rotina:  
[RH - Linha Protheus - GPE - Como funciona o procedimento do calculo por rateio no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003370381-RH-Linha-Protheus-GPE-Como-funciona-o-procedimento-do-calculo-por-rateio-no-Protheus)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13922815438871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13922869287959)

Porém a rotina de geração de líquidos não realiza a validação no filtro/pergunta pelo centro de custo do cálculo da folha e sim pelo centro de custos do cadastro do funcionário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13923079238423)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13923269223703)

Observação: A  do filtro á apenas a título de seleção para geração do arquivo. As informações de centro de custos do rateio tanto do cadastro quanto do cálculo da folha não são validadas dentro do arquivo txt  CNAB.

**Saiba Mais:**

[Artigos - CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833653-RH-CNAB)
