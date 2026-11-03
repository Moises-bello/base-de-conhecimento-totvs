---
article_id: 35840546548247
category: Materiais - Compras (SIGACOM)
content_hash: b5f6a89b56b3f2c6c788a00e6e91b5d5d34ee1e1f56ef6fe0141be13cac7e68c
fetched_at: '2026-06-28T22:41:21.757550+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como remover
  itens NÃO COTADOS da cotação
type: support-article
updated_at: '2025-10-23T19:35:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35840546548247-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-remover-itens-N%C3%83O-COTADOS-da-cota%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35840530670615) Tempo aproximado para leitura: **HH:MM:SS min**  
  
**Dúvida**  
Qual procedimento pode ser realizado para remover **Itens Não Cotados** que não serão mais necessários nas Cotações do Novo Fluxo de Compras?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - a partir da Release 12.1.2310  
  
**Solução**  
Na tela de **Editar Cotação**, temos um grupo inicial chamado **Itens da Cotação.**

Ao clicar nesse grupo, a lista é expandida e exibe todos os itens que estão associados na cotação atual, ou seja, exibe os produtos que estão sendo cotados. **Caso entenda que um item não seja mais necessário e deseja excluir** esse item da cotação, temos a opção **Remover**, que fica na frente de cada item constante na cotação.

Ao clicar em remover, o sistema exibe uma modal, informando se deseja realmente excluir o item da cotação, detalhando o item selecionado e informando que ao realizar a remoção, não é possível reverter o processo.

**Atenção**

Caso o item a ser deletado tenha sido agrupado, apesar de ser mostrado separadamente cada item no grupo **Itens da Cotação**, ao excluir qualquer um que esteja no agrupamento, **todos serão deletados**, visto que o sistema grava o agrupamento como **item único na SC8.**

![](https://tdn.totvs.com.br/download/attachments/680260500/editar_itens_cotacao.gif?version=1&modificationDate=1716921471697&api=v2)

Esse procedimento é válido apenas se o item não tiver sido preenchido na proposta da cotação.

***Saiba Mais:***

[Novo Fluxo de Compras: Guia de Referência](https://tdn.totvs.com.br/pages/releaseview.action?pageId=680260500)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
