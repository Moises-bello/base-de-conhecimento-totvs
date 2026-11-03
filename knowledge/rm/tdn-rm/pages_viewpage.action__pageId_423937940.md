---
content_hash: 15d8d180d0179ce4f794e8e3336788d8c9c0c810a0ab39bb9f89276ddff40cd2
fetched_at: '2026-06-29T00:09:24.508364+00:00'
page_id: '423937940'
product: rm
source: tdn-rm
title: Parametrização do Tipo de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937940
version: 3
---

Para utilizar o processo de comparação de tributos entre o XML e o tipo de movimento, deve-se parametrizar um tipo de movimento de entrada (1.2.xx).   
O usuário deverá selecionar a etapa "Importação/Envio de Arquivo XML", onde possui um campo com nome "Operação com arquivo XML" e as respectivas opções de "Recebimento" e "Envio".   
A parametrização dos tributos está localizada na etapa "Fis - Tributação - Item" no campo "Busca Valores Imp. XML".   
Este campo foi criado para que ao criar um movimento através de um arquivo XML importado na base, o sistema verifique se há tributos para serem comparados de acordo com a parametrização do tipo de movimento e os tributos do XML e o mesmo só será habilitado caso na etapa "Importação/Envio de Arquivo XML" a opção "Operação com arquivo XML" esteja selecionada com um dos valores: "Recebimento de NF-e, NFS-e ou CT-e".   
Sendo assim, temos as seguintes opções disponíveis:

* **Tipo de Movimento - Não comparar com XML**: esta opção deve ser selecionada caso o usuário deseje que todas as informações do tributo sejam calculadas/buscadas pelo sistema, sem a necessidade de comparação com os valores advindos do arquivo XML.
* **Tipo de Movimento - Comparar com XML**: Esta opção deve ser selecionada caso o usuário deseje que todas as informações do tributo sejam calculadas/buscadas pelo sistema, mas elas devem ser comparadas com as informações advindas do .XML. No momento de salvar o movimento, o sistema deverá exibir a diferença dos valores encontrados e recebidos do .XML, caso exista.
* **XML**: Esta opção deverá ser selecionada caso o usuário deseje que os valores do tributo sejam aqueles recebidos do arquivo XML da nota, sem a necessidade de comparação com o tipo de movimento.

Essas opções são desconsideradas na importação de XML de NFSe, neste caso são desconsiderados os tributos do XML e considerados os cálculos feitos pelo sistema.
