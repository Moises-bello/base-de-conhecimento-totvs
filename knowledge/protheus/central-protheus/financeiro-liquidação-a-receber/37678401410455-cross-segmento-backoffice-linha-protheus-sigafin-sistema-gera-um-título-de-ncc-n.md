---
article_id: 37678401410455
category: Financeiro - Liquidação a Receber
content_hash: 2d2c7e078dcb178ce44ac9e45ba8a5f3defd25f170c29dd4ba9c8cfb0f65ac3d
fetched_at: '2026-06-28T22:37:42.270393+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Sistema gera um título
  de NCC na liquidação
type: support-article
updated_at: '2026-01-14T21:05:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37678401410455-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Sistema-gera-um-t%C3%ADtulo-de-NCC-na-liquida%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37678401404183) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Liquidação gerando NCC  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões.  
  
**Causa**  
Por que, ao informar um valor adicional na liquidação, o sistema gera um título de NCC correspondente ao valor excedente?  
  
**Solução**  
Quando os títulos gerados apresentam valor superior ao montante total em processo de liquidação, o sistema gera automaticamente um **título de crédito ao cliente (NCC)** correspondente à diferença apurada.

A **NCC** será criada com as seguintes características:

* **Prefixo:** LIQ
* **Número:** correspondente ao número da liquidação.
* **Tipo:** NCC

Para que os **juros** sejam incorporados ao processo de liquidação, é necessário que estejam previamente informados no **título principal**. Nessa condição, o sistema realizará automaticamente o cálculo das parcelas, considerando os respectivos juros.

Alternativamente, caso seja necessário informar os juros no momento da liquidação, o valor poderá ser preenchido no campo **“Vlr. Adic. Neg.”**. Ao proceder dessa forma e concluir a liquidação, o sistema **não efetuará a geração da NCC**, uma vez que o valor adicional será absorvido diretamente no processo.

**Saiba mais**

[Liquidação Receber - FINA460](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)

[Liquidação Pagar - FINA565](https://tdn.totvs.com/pages/releaseview.action?pageId=312167645)
