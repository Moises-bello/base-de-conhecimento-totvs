---
article_id: 40723182913047
category: Financeiro - Configurador de Tributos
content_hash: c5fbc7875919c16a14892601386f1b5221089172eb8f7772c1bd4b61076f09b1
fetched_at: '2026-06-28T22:37:45.796848+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - FISA170 - Como
  gerar o imposto IRRF pela data da emissão contábil via Configurador de tributos?
type: support-article
updated_at: '2026-05-25T17:40:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40723182913047-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-IRRF-pela-data-da-emiss%C3%A3o-cont%C3%A1bil-via-Configurador-de-tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40723182893335) Tempo aproximado para leitura: **05:00:00 min**  
  
**Dúvida**  
Como gerar o imposto IRRF pela data da emissão contábil via Configurador de tributos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.2210

**Solução**  
Para gerar o imposto de IRRF no Contas a Pagar utilizando a data de Emissão Contábil, é necessário configurar uma Regra de Vencimento específica e vinculá-la à Regra Financeira.

**Passos**

1. Acesse a rotina Configurador de Tributos (FISA170).
2. Acesse o menu de **Regras Financeiras** e clique em **Regra de Vencimento**.
3. Selecione a opção **Incluir** e preencha os campos correspondentes à regra.
4. No campo "Data base p/ vencto. do imposto (Emissão)", selecione a opção **3- Emissão Contábil**.
5. Salve a configuração e certifique-se de que ela está devidamente vinculada à sua Regra Financeira.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723182894615)

No exemplo a seguir, temos um lançamento de um Documento de Entrada usando uma Regra Fnanceira da rotina **FISA170 -** Configurador de tributos.Observar-se que a data de emissão (contábil) da nota fiscal  é diferente da data de  lançamento do documento.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723182895255)](https://centraldeatendimento.totvs.com/hc/article_attachments/40723182895255)

Após a inclusão da nota fiscal podemos observar no Contas a Pagar (FINA050) que o título de IRRF foi gerado com a data de emissão contábil, conforme lançamento.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/40723204256791)](https://centraldeatendimento.totvs.com/hc/article_attachments/40723204256791)

**Saiba mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)

[Configurador de Tributos - Regras Financeiras](https://tdn.totvs.com.br/display/public/PROT/Configurador+de+Tributos+-+Regras+Financeiras)
