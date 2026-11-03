---
content_hash: bc429a1313acc581b1b94442d961da4a0ce416091fdc0a6a3b89372c61a42a7a
fetched_at: '2026-06-29T00:09:16.864887+00:00'
page_id: '421385591'
product: rm
source: tdn-rm
title: Verificação Eliminação de Resíduos (quando integrado com o Protheus)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385591
version: 2
---

A Eliminação de resíduos é a forma de liberar as quantidades não atendidas de um pedido. No processo de integração entre o TOP e Protheus serve para ajustar as quantidades atendidas de forma a liberar o usuário do TOP a possibilidade de realizar um novo pedido no limite da quantidade não atendida e de acordo com a necessidade do produto no projeto.  
 Para realizar a verificação de eliminação de resíduos é necessário ter pedidos liberados para o BackOffice Protheus e estes pedidos não devem ser pedidos em sua quantidade total.  
 No BackOffice Protheus no modulo compras (SIGACOM) é possível executar o processo "Eliminação de resíduos" que despreza essa parte que não foi utilizada.  
 Após a execução do processo de eliminação de resíduos no Protheus é que é possível executar no Totvs Obras e Projetos o processo "Verificar Eliminação de Resíduos" que verifica e caso exista retorna a informação para o campo estorno do pedido de material.  
 Este processo não bloqueia o usuário podendo usar outras rotinas do sistema enquanto realiza a verificação.  
 Quando executado pela visão de pedidos o sistema permite a escolha de um ou mais pedidos na verificação da eliminação, sendo que todos os pedidos selecionados serão processados mesmo que já tenham sido processados anteriormente.  
 Este comportamento visa possibilitar a atualização da quantidade estornada quando uma nota fiscal é excluída após o processo de eliminação de resíduos já ter sido executado no Protheus.  
  

 Informações Complementares

[Eliminação de Resíduos - Integração Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=327322113)
