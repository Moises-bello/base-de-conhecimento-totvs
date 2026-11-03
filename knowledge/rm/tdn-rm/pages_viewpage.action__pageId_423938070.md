---
content_hash: 6e724dade340d9e7580f809611f9a40fdeee835f2958480b2520c9793307b5fa
fetched_at: '2026-06-29T00:09:25.229030+00:00'
page_id: '423938070'
product: rm
source: tdn-rm
title: Manifesto Eletrônico de Documentos Fiscais (MDF-e Client Neogrid)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938070
version: 6
---

O usuário deverá criar um movimento que foi parametrizado para MDF-e do tipo 2.2.xx, após criar o movimento ele deverá entrar em "Vendas | Faturamento | Manifesto Eletrônico Documentos Fiscais - MDF-e", quando na tela do MDF-e, o usuário poderá realizar o seguinte processo:

1. Enviar o MDF-e via Client Neogrid
2. Após o Client Neogrid enviar o XML para a Neogrid, uma cópia deste XML irá para a pasta "SENT"
3. O WebService da Neogrid irá transmitir o XML à SEFAZ
4. Após o retorno da SEFAZ à Neogrid, o cliente irá buscar este XML de retorno e jogar na pasta "IN"
5. O usuário executa o Monitor de [Arquivos TOTVS Colaboração](http://tdn.totvs.com/display/LRM/Monitor+de+Arquivos+XML)que irá ler esse diretório (pasta IN) e enviar o arquivo para o ERP
6. O status do MDF-e mudará de acordo com o XML de retorno da SEFAZ
7. Se autorizado o processo de emissão estará finalizado
8. Se rejeitado o usuário deverá observar atentamente a mensagem e efetuar as devidas correções.

---
