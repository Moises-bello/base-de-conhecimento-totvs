---
article_id: 360034453954
category: Materiais - Compras (SIGACOM)
content_hash: 23c1af19e95ae986022250976d9896bc983f581a6162651af222ec67e94f8da9
fetched_at: '2026-06-28T22:41:24.384652+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Restringir Quantidade
  da Autorização de Entrega maior que Contrato de Parceria  - MV_CONTQTD
type: support-article
updated_at: '2024-12-09T18:30:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034453954-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Restringir-Quantidade-da-Autoriza%C3%A7%C3%A3o-de-Entrega-maior-que-Contrato-de-Parceria-MV-CONTQTD
---

**Dúvida**

Restringir Quantidade da Autorização de Entrega maior que Contrato de Parceria - MV\_CONTQTD  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras – A partir da versão 11.80  
  
**Solução**

Por padrão, ao registrar uma quantidade no contrato de parceria e informar uma quantidade maior na autorização de entrega, o sistema permite, pois não considera um saldo efetivo. Para garantir que a autorização de entrega siga o contrato de parceria, é necessário configurar o parâmetro **MV\_CONTQTD**.  
Esse parâmetro tem as seguintes funções:

1. **Restringe a quantidade na autorização de entrega (AE) = 1 :** para que não ultrapasse a quantidade original do contrato de parceria vinculado.
2. **Desativa a restrição = 2 (DEFAULT) :** Permite que a quantidade na AE seja maior que a do contrato de parceria.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021728632/mceclip0.png)

Ao habilitar a opção para realizar a restrição, a seguinte mensagem é exibida ao vincular ou copiar a autorização de entrega de um contrato de parceria : **A quantidade deste item não pode exceder a quantidade do Contrato Parceria.**

**![Copia-Contrato-Encerrado-.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28393582010519)**

***Saiba Mais :***

[MV\_CONTQTD - Restringe a quantidade do item na autorização de entrega](https://tdn.totvs.com/pages/releaseview.action?pageId=6085236)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
