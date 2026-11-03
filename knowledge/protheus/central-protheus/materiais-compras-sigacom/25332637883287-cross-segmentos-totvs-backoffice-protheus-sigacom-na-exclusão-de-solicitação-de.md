---
article_id: 25332637883287
category: Materiais - Compras (SIGACOM)
content_hash: 09332852f76ee22869bea525d2516c4cc358d8c01fe91f90416ffe2e3261966b
fetched_at: '2026-06-28T22:41:12.941001+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM  - Na exclusão de Solicitação
  de compras não atualiza o campo Qtd Entrada Prevista. B2_SALPEDI  o que Pode ser?
type: support-article
updated_at: '2024-08-01T12:44:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25332637883287-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Na-exclus%C3%A3o-de-Solicita%C3%A7%C3%A3o-de-compras-n%C3%A3o-atualiza-o-campo-Qtd-Entrada-Prevista-B2-SALPEDI-o-que-Pode-ser
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25332668488599) Tempo aproximado para leitura: **00:03:00min** **Dúvida**  
Na exclusão de Solicitação de compras não atualiza o campo Qtd Entrada Prevista. B2\_SALPEDI o que pode ser?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Causa**

Segue uma das possibilidades do que pode ocasionar essa ocorrência abaixo:

O campo na SC1->C1\_ESTOQUE, está com algum  inicializador por exemplo = “2” e por padrão não tem inicializador.

**Solução**

1.Retirar do Inicializador para o campo C1\_ESTOQUE

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25332668490775)

2.Caso deseje que todos os produtos atualizem a Quantidade prevista independente da verificação do campo F4\_ESTOQUE da Tes,ajuste o parâmetro **MV\_SB1TES** de .T. para .F., dessa forma  todos os produtos irão atualizar previsão de entrada.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
