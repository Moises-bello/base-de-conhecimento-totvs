---
content_hash: 475f79f39ce399c2ae1188eea2ff7afd0dfecf6c1773ab4950de3fdf04eb160d
fetched_at: '2026-06-29T00:09:21.184944+00:00'
page_id: '422545855'
product: rm
source: tdn-rm
title: Consultar Autorização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545855
version: 8
---

A consulta das informações da NF-e é feita automaticamente pelo TSS ou pelo TOTVS Colaboração. Este processo no RM consiste simplesmente em buscar nestes serviços para o RM o resultado da consulta feita na SEFAZ, executar as devidas atualizações no banco de dados e emitir as devidas mensagens para o usuário.

Com o uso do TSS este processo deve ser disparado manualmente através da seleção dos registros que estão com o status Pendente.

Quando é utilizada a integração com o TOTVS Colaboração 2.0 consulta pode ser agendada através de Jobs.

O processo de Consulta só pode ser executado em registros que estejam com o status Pendente e pode ser executado em mais de um registro de uma só vez.

Quando uma NF-e é consultada se o retorno resultar em uma autorização o registro terá seu status alterado para Autorizada. Neste caso o movimento que gerou a nota será bloqueado para edição.  
A nota ainda poderá ser Rejeitada ou Denegada.

Maiores Informações

Caso a chave de acesso da Nota autorizada na SEFAZ seja diferente da chave de acesso do sistema, o processo irá atualizar a [chave de acesso retornada pelo TSS](https://tdn.totvs.com/pages/viewpage.action?pageId=622496002) e será exibido a seguinte mensagem orientando ao usuário a validação da Nota.

Essa validação é necessária para verificar se as informações que estão no RM estão condizentes com a nota que consta na SEFAZ.

Comportamento disponível a partir das versões abaixo:

- 12.1.31.183  
- 12.1.32.120  
- 12.1.29 ainda não disponível
