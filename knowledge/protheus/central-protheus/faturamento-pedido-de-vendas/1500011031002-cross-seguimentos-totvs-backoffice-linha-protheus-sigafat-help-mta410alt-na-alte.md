---
article_id: 1500011031002
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 26fe82bcc219a90c62cec52c83ad0d0bae99ad0a23f1c0f29d1f97c7c71bcb07
fetched_at: '2026-06-28T22:38:41.209415+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Seguimentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Help MTA410ALT
  na alteração do Pedido de Vendas
type: support-article
updated_at: '2021-05-17T14:50:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011031002-Cross-Seguimentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Help-MTA410ALT-na-altera%C3%A7%C3%A3o-do-Pedido-de-Vendas
---

**Ocorrência**Ao tentar realizar a alteração de um Pedido de Vendas (MATA410), o sistema apresenta o Help MTA410ALT impedindo a alteração.  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento (SIGAFAT) - Todas as versões.  
  
**Causa**O Help MTA410ALT é apresentado sempre que o Pedido de Vendas (MATA410) for originado do módulo "Easy Export Control" (SIGAEEC), caso o parâmetro **MV\_EEC0023** não esteja habilitado (.T.).

Caso o parâmetro **MV\_EEC0023** esteja habilitado (.T.), o sistema permitirá a alteração do Pedido de Vendas (MATA410), porém serão habilitados para edição apenas os campos não integrados.

**Solução**

* Caso necessite alterar um pedido originado do módulo "Easy Export Control" (SIGAEEC), habilite o parâmetro MV\_EEC0023 (.T.);
* Caso o sistema não permita a edição do campo que deseja alterar, significa que o conteúdo foi recebido do SIGAEEC e não será possível a edição através do pedido de vendas, realize um novo processo ou verifique se é possível alterar a informação pelo SIGAEEC.

Em caso de dúvidas nos processos do módulo "Easy Export Control" (SIGAEEC), entre em contato com a área de Suporte responsável pelo Módulo.
