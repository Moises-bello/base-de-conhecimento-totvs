---
article_id: 18950074653079
category: Comércio Exterior - Easy Export Control - Embarque
content_hash: 65e57d56919794d5c526361e641ff07cf8fc439241f0639618da4fd3e335c6d4
fetched_at: '2026-06-28T22:36:56.610450+00:00'
product: protheus
section_id: 1500001549322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Rateio do seguro
  gerando item com valor zerado na transmissão da DUE
type: support-article
updated_at: '2023-11-09T17:49:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18950074653079-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Rateio-do-seguro-gerando-item-com-valor-zerado-na-transmiss%C3%A3o-da-DUE
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18950049566487)*Tempo aproximado para leitura: **00:04:00 min**

**Dúvida**Ao gravar um pedido com 2 itens, sendo um deles com o valor muito maior que o outro, o valor de seguro é rateado de forma errada, deixando um dos itens com o valor zerado.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Export Control* – A partir da versão 12.1.2210.

**Solução**

O processo é montado de acordo com a condição de venda "Preço aberto" ou "Preço fechado"(verificar qual está sendo utilizado na rotina do "Processo de Exportação" marcado como "Preço.Ab."), o *Incoterm* informado no processo, somando as despesas, subtraindo os descontos, o valor é montado de acordo com a sua nota fiscal, sendo que o valor do pedido não pode ser maior que o valor do embarque.  
   
**VMCV** - É o valor da mercadoria na condição de venda, na moeda de negociação. Sugere com a soma do valor da mercadoria adicionando as despesas que compõe a *Incoterm* e formam preço de venda, este irá considerar o *Incoterm* informado.  
   
**VMLE** - É o valor da mercadoria no local de embarque, na moeda de negociação. Na exportação corresponde ao valor **FOB** da mercadoria. Sugere com a soma do valor da mercadoria adicionando as despesas até o ponto de embarque que formam preço de venda.

**Saiba mais**

[Problema na transmissão da DUE - rateio do seguro gerando item com valor zerado](https://tdn.totvs.com/pages/releaseview.action?pageId=606642680)
