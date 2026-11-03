---
article_id: 360020420231
category: Materiais - Compras (SIGACOM)
content_hash: 6a691a3b764d3c99681c8ea5a81870ae8fe72469339ec2722205d86759ec5694
fetched_at: '2026-06-28T22:41:08.881589+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Frete do Pedido de
  Compra não atualiza quando deleta o item da Pré-Nota ou Documento de Entrada
type: support-article
updated_at: '2024-12-06T18:34:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020420231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Frete-do-Pedido-de-Compra-n%C3%A3o-atualiza-quando-deleta-o-item-da-Pr%C3%A9-Nota-ou-Documento-de-Entrada
---

**Dúvida**

Ao vincular um Pedido de compra com vários itens e valor de frete na Pré-Nota (MATA140) ou Documento de Entrada (MATA103), se deletado um dos itens o sistema não está atualizando o valor do frete.

![1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360016211912)

**Ambiente**Protheus – Compras – A partir da versão 12  
  
  
**Solução**

A ocorrência pode estar relacionada ao TES vinculada no Pedido de Compras ou no Produto que não calcula ICMS.

O sistema também considera o parâmetro MV\_VALDESP para rateio conforme documentação:

[Como o sistema realiza o rateio das Despesas Acessórias (Frete/Seguro/Despesa)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037627993-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-o-sistema-realiza-o-rateio-das-Despesas-Acess%C3%B3rias-Frete-Seguro-Despesa-no-Documento-de-Sa%C3%ADda)

Ou seja, se a TES estiver configurada com o campo F4\_ICM=NÃO e o parâmetro constar como MV\_VALDESP=.F. será gerado conteúdo no campo D1\_VALFRE com o valor do frete e se deletado atualizará o campo com valor total;  
  
Caso o campo F4\_ICM=NÃO e o parâmetro configurado como MV\_VALDESP=.T., o sistema faz o rateio apenas para os itens com TES que calculam ICMS, nesse caso o item não preenche o valor no D1\_VALFRE e por isso não atualiza no total, visto que estará zerado.

***Saiba Mais:***

[MP - SIGACOM - Pontos de Entrada - Compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000169747-MP-SIGACOM-Pontos-de-Entrada-Compras?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
