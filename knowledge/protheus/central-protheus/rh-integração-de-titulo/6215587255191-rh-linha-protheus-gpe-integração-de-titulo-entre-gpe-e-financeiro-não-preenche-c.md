---
article_id: 6215587255191
category: RH - Integração de Titulo
content_hash: 5731eb082f577313ea52a8dc63f794d905136b0344a0d3bbb7602a795da63132
fetched_at: '2026-06-28T22:43:36.373022+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Integração de titulo entre GPE e Financeiro, não
  preenche campo Histórico no Financeiro
type: support-article
updated_at: '2025-07-18T17:40:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6215587255191-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-de-titulo-entre-GPE-e-Financeiro-n%C3%A3o-preenche-campo-Hist%C3%B3rico-no-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33558043365399) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao realizar a integração de títulos do modulo Gestão de Pessoal com o módulo Financeiro, sistema não preenche o campo Histórico no Financeiro.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
  
**Solução**Essa rotina por padrão, não executa o preenchimento do campo Histórico na integração do título no módulo Financeiro. 

Os campos são opcionais e seu uso será para facilitar a visualização à qual o título integrado se refere, de modo que o sistema não irá preencher os campos automaticamente.  
Para atender a necessidade exposta, foi verificado que existe o ponto de entrada GP670ARR que permite a gravação de outros campos.   
Por exemplo, caso seja necessário que os campos E2\_HIST sejam gravados com o conteúdo do campo RC1\_DESCRI, poderá utilizar o ponto de entrada GP670ARR conforme o *link* disponibilizado em Saiba Mais.

**Saiba Mais**[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEM670](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018319712-RH-Linha-Protheus-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEM670)  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)  
<http://tdn.totvs.com/pages/viewpage.action?pageId=6079137>
