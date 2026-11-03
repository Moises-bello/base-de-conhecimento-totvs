---
article_id: 360019789851
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 7bddf0d0e8741d6b7e25bc6d0e75ace71ebac0c70934b3833015c465d1316822
fetched_at: '2026-06-28T22:38:41.131042+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Filtro de busca
  no Browser do Pedido de Venda
type: support-article
updated_at: '2023-05-22T15:02:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019789851-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Filtro-de-busca-no-Browser-do-Pedido-de-Venda
---

**Dúvida**

Ao realizar uma busca no browser do Pedido de Venda o sistema filtra os registros conforme os dados informados, porém, ao realizar qualquer ação na rotina (Alterar, Visualizar, Incluir ou Excluir) o filtro é desfeito.

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da versão 12.

**Solução**

Esse  comportamento é o padrão das demais rotinas do Protheus. Essa alteração tornou-se necessária para garantir a integridade dos dados do sistema.

Mas é possível criar um filtro por expressão para obter o mesmo resultado, siga os passos abaixo:

1. Acesse a rotina de **Pedido de Vendas** (**MATA410**) e clique na opção **Filtrar**;

2. Selecione a opção **Criar Filtro**;

3. Informe o Campo e Operador desejado, selecione a opção **Informar dados do filtro durante a execução,** clique em **Adicionar** e confirme a operação;

4. Salve o filtro criado;

5. Ao selecionar o filtro, informar o conteúdo que deseja pesquisar;

6. O filtro ficará aplicado independente da operação realizada pelo usuário. Para retirar o filtro do Browser basta clicar na opção **Remover.**

Para mais detalhes do processo acesse: [**Busca no Browse do Pedido de Venda**](https://tdn.totvs.com/x/z7bSGQ)
