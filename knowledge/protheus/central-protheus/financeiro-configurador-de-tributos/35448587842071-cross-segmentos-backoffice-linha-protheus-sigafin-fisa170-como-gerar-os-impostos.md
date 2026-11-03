---
article_id: 35448587842071
category: Financeiro - Configurador de Tributos
content_hash: 482bb0818dabaf2047818fd566497d423da517cbe4d3992970c86c5b7a03f286
fetched_at: '2026-06-28T22:37:45.925718+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar
  os impostos no financeiro através do documento de saída
type: support-article
updated_at: '2025-10-06T20:53:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35448587842071-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-os-impostos-no-financeiro-atrav%C3%A9s-do-documento-de-sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35448587797271) Tempo aproximado para leitura: **00:08 min**  
  
**Dúvida**  
Como gerar os impostos no financeiro através do documento de saída?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.2210  
  
**Solução**  
Quando a Nota Fiscal é emitida por meio do pedido de venda, deve ser gerada a respectiva **regra fiscal** responsável pelo cálculo dos tributos no pedido. No entanto, para que os impostos sejam integrados ao módulo financeiro, é necessário que exista uma **regra financeira** devidamente cadastrada e **vinculada à regra fiscal** correspondente.

Após o cadastro da regra financeira correspondente ao imposto, deve-se acessar o caminho: **Regra Fiscal → Regra de Cálculo do Documento Fiscal → Regra de Cálculo do Documento Fiscal.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448603002903)

Localize a regra fiscal, clique em **Alterar** e realize o vínculo com a respectiva **Regra Financeira**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448603007767)

Para definir a regra financeira do imposto por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Cliente e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **cliente** e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448603013015)

No **cadastro do Cliente**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448603014167)

Vincule o código da **Regra Financeira**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35448603016727)

**Saiba mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)
