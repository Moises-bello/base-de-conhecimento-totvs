---
content_hash: 7f30ee02679898d6433b4a4a17d8ff412a2d77672a5c5a44388c1d8d9931e651
fetched_at: '2026-06-29T00:10:22.103811+00:00'
page_id: '496398332'
product: rm
source: tdn-rm
title: Habilitando a atualização da última data de acesso para serviços REST e SOAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496398332
version: 2
---

## 

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

No sistema RM, quando o usuário loga via MDI, WebServices ou APIs, até a versão 12.1.24, a data de último acesso é atualiza na tabela GUSUARIO - campos DATAULTIMOACESSO e DATAULTIMOACESSOVALIDO.

Por padrão, a partir do patch 12.1.24.125 e versão 12.1.25, a data de último acesso será atualiza **apenas** por login feito via **MDI**. Quando o acesso for via **WebServices ou APIs**, a tabela GUSUARIO **não** será atualizada.

ImportanteO intuito dessa alteração é ganho de performance, visto que a cada requisição os campos GUSUARIO.DATAULTIMOACESSO e GUSUARIO.DATAULTIMOACESSOVALIDO eram atualizados. 

Caso seja necessário, por alguma regra de negócio da empresa, atualizar a data de último acesso para serviços REST e SOAP, basta adicionar a tag  <add key="UPDATEDATAULTIMOACESSO" value="true" />  
no arquivo de configuração do host.

## **02. EXEMPLO DE UTILIZAÇÃO**

Para habilitar a atualização da data de último acesso na tabela GUSUARIO: <add key="UPDATEDATAULTIMOACESSO" value="true" /> (Comportamento padrão até o patch 12.1.24.124)

Para desabilitar a atualização: <add key="UPDATEDATAULTIMOACESSO" value="false" /> (Comportamento padrão a partir do patch 12.1.24.125)
