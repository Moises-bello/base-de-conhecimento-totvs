---
article_id: 37707378170135
category: Materiais - Compras (SIGACOM)
content_hash: be87c8816fac62a18e6a482fa3d073357da3300bfc18ce300012e1ee0dcf95cc
fetched_at: '2026-06-28T22:41:14.417568+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como adicionar campos
  nos relatórios do Smartview do módulo de compras? Exemplo Relatório Relação de Solicitação
  compras?
type: support-article
updated_at: '2026-05-13T17:09:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37707378170135-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-adicionar-campos-nos-relat%C3%B3rios-do-Smartview-do-m%C3%B3dulo-de-compras-Exemplo-Relat%C3%B3rio-Rela%C3%A7%C3%A3o-de-Solicita%C3%A7%C3%A3o-compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37707378131863) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
  
Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como adicionar campos nos relatórios do Smartview de compras?

**Ambiente**  
  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões

**Solução**  
  
1. No configurador acesse **Ambientes >Smartview> Integração Smartview**

2. Na próxima Tela clique no Botão engrenagem e pesquise por SIGACOM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37707378132503)

3. Selecione o Objeto de Negócio disponível que deseja realizar a adição de campos.No meu Exemplo irei selecionar o Relatório: **Relação de Solicitação de compras ,**clique nos **Três pontinhos(...) >Editar** :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37707394773783)

-Na opção **Tabela** irá carregar todas as Tabelas disponíveis para adição de campos do Objeto de negócio selecionado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37707378134679)

-Para adicionar o campo "Selecione o campo desejado"  , clique em **Adicionar >Confirmar**.No meu teste adicionei o campo **C1\_VUNIT.**![](https://centraldeatendimento.totvs.com/hc/article_attachments/37707394789143)

-Adicionei também os campos **C7\_PRECO** e **C7\_TOTAL** clicando em Adicionar >Confirmar.![](https://centraldeatendimento.totvs.com/hc/article_attachments/37707378144023)

4.Segue Visão de dados do Relatório :**Relação de Solicitação de compras** após adição dos campos acima no configurador do sistema.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37707394790807)

Atenção

* Não é possível adicionar campos MEMO ou virtual.
* Para que o campo apareça na listagem o mesmo precisa estar configurado como "Usado" no SX3

Veja mais detalhes na documentação: [Amarração Protheus x Smart View](https://tdn.totvs.com/pages/releaseview.action?pageId=708098869)

Em caso de dúvidas na customização de relatórios Smartview, orientamos o contato junto ao suporte ao Framework do Protheus

***Saiba Mais:***  
[How To | MP - SIGAEST - Inclusão de Campos no SmartView](https://www.youtube.com/watch?v=HelxcMHLmCA)

[Smart View - Compras](https://tdn.totvs.com/x/x_b0L)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
