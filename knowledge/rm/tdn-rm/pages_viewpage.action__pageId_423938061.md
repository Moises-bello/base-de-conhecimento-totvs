---
content_hash: f0e0c8c8e0823bfc28bf988908ca6cf213f143c03d30d6a01cd75416874c76ce
fetched_at: '2026-06-29T00:09:25.207084+00:00'
page_id: '423938061'
product: rm
source: tdn-rm
title: Manifesto Eletrônico de Documentos Fiscais  (MDF-e TSS)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938061
version: 16
---

O usuário deverá criar um movimento que foi parametrizado para MDF-e do tipo 2.2.xx, após criar o movimento ele deverá entrar em "Vendas | Faturamento | Manifesto Eletrônico Documentos Fiscais - MDF-e", quando na tela do MDF-e, o usuário poderá realizar o seguinte processo:

1. Enviar o MDFE à SEFAZ via TSS
2. A SEFAZ irá validar o XML enviado e preparar um novo XML
3. O TSS irá buscar automaticamente esse XML de retorno e enviar para o banco de dados
4. O usuário através do ERP irá efetuar a consulta deste documento através do Processo Consultar Autorização
5. O XML que estava no banco de dados do TSS agora irá aparecer no banco de dados do ERP e atualizar o sistema
6. O status estará de acordo com o XML de retorno da SEFAZ
7. Se autorizado o processo de emissão finalizou
8. Se rejeitado o usuário deverá observar atentamente a mensagem e efetuar as devidas correções.

---
