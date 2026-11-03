---
article_id: 360062030274
category: Anuais
content_hash: 3787e8e469f1d67a7cc08ec1bed0c8f84f3d967959a1a0751fdb6cc0193a3cba
fetched_at: '2026-06-28T22:46:51.191507+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF/Informe de Rendimentos: Geração da DIRF por matriz'
type: support-article
updated_at: '2025-03-13T10:07:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062030274-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Gera%C3%A7%C3%A3o-da-DIRF-por-matriz
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:25 min****Dúvida**Como realizo a geração da DIRF por matriz, e não por filial?  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
 **Solução**Para que seja realizada a geração da DIRF por matriz, é necessário informar a Quebra de Seção na parametrização inicial como **Quebra da Empresa**. Da mesma forma, nos parâmetros específicos da coligada, informar a quebra como **Quebra da Empresa**. Feito isso, o arquivo deve ser gerado com o CNPJ da Matriz:

![](/attachments/token/MO8gksbNvfwpvXl9LzXoOQNRh/?name=inline253997517.png)

![](/attachments/token/xWEoCotk5fHbL6KZCq6i87Nj2/?name=inline-817358308.png)​

Caso a alternativa anterior não funcione apenas com a **Quebra de Seção**, utilize o flag **Forçar seção centralizadora**. Este flag será utilizada **apenas para empresas que não possuem uma seção centralizadora de coligada**.

![](/attachments/token/ueG7rXDFCEgVELJIRNZSAyFoH/?name=inline380775557.png)

**Saiba mais**[Parametrização DIRF/Informe de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=208345510)  
[Emissão DIRF/Informe de Rendimentos](https://tdn.totvs.com/pages/releaseview.action?pageId=208347682)
