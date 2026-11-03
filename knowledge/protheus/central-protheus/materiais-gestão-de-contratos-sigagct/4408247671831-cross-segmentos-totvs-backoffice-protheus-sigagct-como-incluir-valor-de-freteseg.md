---
article_id: 4408247671831
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 3b8d365360ed0b83ba1a8c000de2c130d2753753fd641a0e4394c75a40c16935
fetched_at: '2026-06-28T22:37:21.564261+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como Incluir Valor
  de Frete/Seguros/Despesas no Contrato/Medição?
type: support-article
updated_at: '2025-11-18T17:06:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408247671831-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-Incluir-Valor-de-Frete-Seguros-Despesas-no-Contrato-Medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36418145428247) Tempo aproximado para leitura:  **00:03:00min**  
  
**Dúvida**

É possível incluir um valor Valor de Frete/Seguros/Despesas no Contrato/Medição?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

**Exemplo de preenchimento do campos Valor do frete/Despesas/Seguros no Contrato:**

Para se informar o **Valor do Frete/Despesas/Seguros** na Inclusão do contrato preencha os campos abaixo na linha do item do Contrato, para que possa carregar automaticamente para a planilha do contrato.

Frete (**CNB\_FRETE**), Despesa (**CNB\_DESPES**), Seguro (**CNB\_SEGURO**)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36418160354967)

No exemplo acima inclui um contrato com 3 parcelas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36418145436311)

**Exemplo de Inclusão de Medição para a primeira parcela.**

Após preencher os campos no contrato e incluir a medição automaticamente será preenchido os campos abaixo:

**Obs:** O sistema faz o rateio nos Valores informados no contrato pela quantidade de parcelas do contrato na realização da medição. Abaixo Segue exemplo dos valores rateados na medição.

Despesa (CNE\_DESPES), Seguro (CNE\_SEGURO) e Frete(CNE\_FRETE)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36418145437847)

**Exemplo de Inclusão de Pedido no Encerramento de Medição:**

Ao gerar um Pedido o sistema preencherá os campos de Frete/Seguro/despesas do pedido no encerramento da Medição, nos campos FreteDespesa/Seguro conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36418160360087)

***Saiba Mais:***

[GCT0166\_Frete, seguro e despesa no contrato](https://tdn.totvs.com.br/display/public/PROT/GCT0166_Frete%2C+seguro+e+despesa+no+contrato)

[GCT0167\_Medição com frete](https://tdn.totvs.com.br/pages/releaseview.action?pageId=969135070)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
