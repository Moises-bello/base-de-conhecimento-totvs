---
article_id: 35446019140119
category: Financeiro - Configurador de Tributos
content_hash: 5fcff6f6125c54d860f437e8fcbbdebcf94d39c256f3347b400ecaf89fb7913b
fetched_at: '2026-06-28T22:37:45.920697+00:00'
product: protheus
section_id: 30946086151959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Como gerar
  os impostos no financeiro através do documento de entrada?
type: support-article
updated_at: '2025-11-10T13:15:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35446019140119-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-os-impostos-no-financeiro-atrav%C3%A9s-do-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35446019110935) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como gerar os impostos no financeiro através do documento de entrada?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir da release 12.1.2210.  
  
**Solução**  
Quando a Nota Fiscal é emitida por meio do documento de entrada, deve ser gerada a respectiva **regra fiscal** responsável pelo cálculo dos tributos no documento. No entanto, para que os impostos sejam integrados ao módulo financeiro, é necessário que exista uma **regra financeira** devidamente cadastrada e **vinculada à regra fiscal** correspondente.

Após o cadastro da regra financeira correspondente ao imposto, deve-se acessar o caminho: **Regra Fiscal → Regra de Cálculo do Documento Fiscal → Regra de Cálculo do Documento Fiscal.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35446024924439)

Localize a regra fiscal, clique em **Alterar** e realize o vínculo com a respectiva **Regra Financeira**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35446019112727)

Para definir a regra financeira do imposto por meio do **Configurador de Tributos (FISA170)**, é necessário que os cadastros de **Fornecedor e Natureza** estejam previamente criados.

Ressalta-se que os cadastros de **fornecedor** e **natureza** não devem conter parametrizações de impostos, uma vez que toda a configuração é realizada exclusivamente nas **Regras Financeiras**, conforme ilustrado no exemplo a seguir:

No**cadastro de** **natureza,** criado sem parametrização de impostos, vincule a **regra financeira** em **"Tipo de retenção x natureza",**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35446019117975)

No **cadastro do fornecedor**, criado sem configuração de impostos, vincule a **regra financeira** em **Outras Ações → Tipos de Retenções**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35446019119895)

Vincule o código da **Regra Financeira**conforme exemplo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35446024926487)

**Saiba mais**

[Financeiro - Configurador de Tributos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/30946086151959-Financeiro-Configurador-de-Tributos)

[Como gerar o imposto Pis, Cofins e Csll com a regra financeira para o pagar?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32402759656855-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Como-gerar-o-imposto-Pis-Cofins-e-Csll-com-a-regra-financeira-para-o-pagar)
