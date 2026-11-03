---
content_hash: c9db777cd9b1b49d39be91679d8ac9d1d9abe4a3fcd174fbd9adbc895c120d4d
fetched_at: '2026-06-29T00:09:24.470614+00:00'
page_id: '423937922'
product: rm
source: tdn-rm
title: Solicitação de Ordem de Compra (Controle de Produção)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937922
version: 7
---

A geração de solicitação de Ordem de Compra de materiais no TOTVS Planejamento e Controle da Produção pode ser realizada das seguintes maneiras:

* Na promoção da Ordem de Produção do Status de "Criada" para "Aguardando Recursos", onde, caso exista a necessidade de compra de materiais, o sistema irá emitir a seguinte mensagem:

***Deseja Gerar Solicitação de Compra no TOTVS Gestão de Estoque, Compras e Faturamento?***  
Ao confirmar, a tela de solicitação de compra será aberta com as necessidades de materiais para Ordem de Produção. É possível editar cada item e alterar a quantidade "A Solicitar" para mais e para menos.  
Através do ícone correspondente na visão de Ordem de Produção.  
***Observações***: Não é permitido gerar solicitação de compra para ordem de produção com o status 'Criada', 'Concluída' ou 'Cancelada'. Para que o movimento de solicitação de compra seja gerado é preciso que o mesmo esteja configurado através do

"Assistente de Implantação de Processos", acessado pelo menu Opções | Parâmetros | RM Nucleus, processo "04.06 – Gestão de Compras", selecionar o código de tipo de movimento desejado, clicar no ícone "Parametrizar", em "Compra/Venda – Outros Dados" se no campo "Tipo do Movimento de Compra" estiver a opção "Solicitação de Compras" marcada.  
***Atenção!***Na solicitação de compra o sistema irá considerar para a quantidade de material a solicitar a necessidade da ordem menos as quantidades em estoque no TOTVS Gestão de Estoques, Compras e Faturamento, estoque intermediário, estoque empenhado e a quantidade já solicitada não faturada.

Para material controlado por grade o sistema irá considerar o saldo de estoque por grade na solicitação de compra.   
Na promoção de várias ordens de produção, a tela de "Solicitação de Compra" irá listar as necessidades de compra agrupada para as ordens selecionadas.  
Se uma atividade for cancelada após a geração da solicitação de compras, a solicitação deverá ser excluída e regerada, sendo que o material da atividade cancelada não irá aparecer na lista desta solicitação. Caso a atividade seja reativada a solicitação de compra deverá ser excluída e o material da atividade cancelada irá aparecer na lista da solicitação.   
Em parâmetros da produção, pasta "Gerais", há opção para escolha do modo que será a geração de movimento de solicitação de compras através da funcionalidade "Gera Solicitação de compra para todas as Ordens" disponível na visão de ordens de produção, que, ao selecionar várias ordens de produção, poderá ser:

1. Gera Movimento único de Solicitação de Compras
2. Gera Movimento de Solicitação de Compras por OP

---
