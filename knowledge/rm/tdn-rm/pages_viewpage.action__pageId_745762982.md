---
content_hash: 13da1357eecf8b56302eba6134977ed15e0f7b1f3cc0629d13e9a8cf9eb86444
fetched_at: '2026-06-29T00:11:32.292863+00:00'
page_id: '745762982'
product: rm
source: tdn-rm
title: Nota Técnica 2022.003
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745762982
version: 18
---

#f5f5f5#363636noneNota Técnica 2022.003

## **Conteúdo**

Conteúdo

## **01. Introdução**

A Nota Técnica divulga novos campos e regras de validação da NF-e versão 4.0.  
  
**Alterações de Campos:**  
  
1 - Inclusão do Referenciamento de NF-e por Chave com código numérico zerado (Campo refNFeSig)  
2 - Alteração do número máximo de ocorrências do grupo de Documentos Fiscais Referenciados (tag: NFref) de 500 para 999 ocorrências.  
  
Mais informações na [NT 2022.003](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=/C5jc3RZhNQ=)

## **02. Regras**

* Necessário possuir uma ou mais referências com o campo chave de acesso preenchido;
* A chave de acesso informada na referência deve possuir o código numérico zerado, posição 36 a 43 da chave, segue exemplo na imagem abaixo:

Imagem

Mais informações sobre o Movimento:

## **03. Exemplo de XML**

xmlExemplo tag refNFeSig




{...}
31230215436940000952550010160543651000000008
]]>Observação

Caso a chave de acesso do lançamento referenciado possuir o código numérico zerado a tag: **refNFeSig** será gerada no xml de envio, neste caso o usuário deve certificar-se que a SEFAZ do estado em questão autoriza o envio da nota com esta tag, antes de executar o processo que zera o código numérico da chave de acesso.

Mais informações no documento de [origens das informações para geração da (NF-e)](https://tdn.totvs.com/pages/viewpage.action?pageId=419539277)
