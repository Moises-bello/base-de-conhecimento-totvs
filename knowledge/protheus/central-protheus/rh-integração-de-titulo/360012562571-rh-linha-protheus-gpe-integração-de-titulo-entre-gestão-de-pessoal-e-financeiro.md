---
article_id: 360012562571
category: RH - Integração de Titulo
content_hash: 2060c013aa287c4ad26a30d0cc4c8f2ace799f512b38641a878c067a5a8b8f76
fetched_at: '2026-06-28T22:43:36.369648+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Integração de titulo entre Gestão de Pessoal e
  Financeiro, não preenche campo centro de custo
type: support-article
updated_at: '2025-10-21T14:52:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012562571-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-de-titulo-entre-Gest%C3%A3o-de-Pessoal-e-Financeiro-n%C3%A3o-preenche-campo-centro-de-custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33641740068887)Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Ao realizar a integração de títulos do modulo Gestão de Pessoal com o módulo Financeiro, sistema não preenche o campo centro de custo no Financeiro.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Essa rotina realmente não leva o preenchimento do campo centro de custos, na integração do título no módulo Financeiro. A indicação por centro de custo no RH é apenas a titulo de definição.  
Os campos são opcionais e seu uso é para contabilização conforme regra de negócio do usuário, ou seja, o sistema não irá preencher os campos automaticamente.  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada GP670ARR que permite a gravação de outros campos.   
Por exemplo, caso seja necessário que os campos E2\_CCC e E2\_CCD sejam gravados com o conteúdo do campo RC1\_CC, poderá utilizar o ponto de entrada. Verifique o *link* disponibilizado em Saiba Mais.  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
<http://tdn.totvs.com/pages/viewpage.action?pageId=6079137>
