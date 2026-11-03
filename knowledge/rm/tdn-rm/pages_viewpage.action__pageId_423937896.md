---
content_hash: 0f66c5a6c577b6b98321ecea604020348fd6afeff728c4cc89db50bd3354f9e9
fetched_at: '2026-06-29T00:09:24.113107+00:00'
page_id: '423937896'
product: rm
source: tdn-rm
title: Não Incluir Movimento Automaticamente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937896
version: 2
---

O procedimento padrão do sistema é incluir o movimento automaticamente durante o recebimento de NF-e. Caso seja necessário alterar este comportamento basta utilizar o parâmetro "Não Incluir Movimento Automaticamente". Neste caso, os XML's serão importados e cadastrados na tabela TNFEENTRADA, no entanto, a inclusão do movimento não será realizada durante a importação.   
Para a parametrização acesse o menu Assistente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.03 - Integrações | 04.03.03 - Fiscal | 04.03.03 - Integrações | 04.03.03.03 - Dados Fiscais | Etapa 05 - Importação/Envio de Arquivo XML.   
 Com o XML cadastrado, o movimento poderá ser incluído no sistema através de 2 processos, são eles:

* **Manual**: [Inclusão de Movimento Através de XML - NF-e](http://tdn.totvs.com/pages/viewpage.action?pageId=423937956)
* **Automática**: Inclusão Automática de Movimento

***Importante!*** Para utilizar a segunda opção "Inclusão Automática de Movimento", o parâmetro [Tipo de Recebimento de NF-e](http://tdn.totvs.com/pages/viewpage.action?pageId=423937880) deve estar devidamente configurado.
