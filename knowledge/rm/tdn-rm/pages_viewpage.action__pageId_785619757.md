---
content_hash: cbc66fc16f9a36a268e3189c5d75fab5b817f1435d7a0a9bce9b30f53f5d0a08
fetched_at: '2026-06-29T00:11:38.875641+00:00'
page_id: '785619757'
product: rm
source: tdn-rm
title: Nota Técnica 2023.001
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=785619757
version: 17
---

#f5f5f5#363636noneNota Técnica 2022.003

## **Conteúdo**

Conteúdo

## **01. Introdução**

A Nota Técnica divulga novos campos e regras de validação da Tributação Monofásica sobre Combustíveis.  
  
**Alterações de Campos:**  
  
1 - Novos campos e alterações de regras existentes abrangendo a nova forma de tributação monofásica sobre combustíveis.

No Grupo LA (Detalhamento Específico de Combustíveis) foram adicionados os campos pBio, indImport, cUFOrig e pOrig para os CSTs 02, 15, 53 e 61. [Mais informações na documentação do grupo](https://tdn.totvs.com/pages/viewpage.action?pageId=419542718#GrupoJ-5).

2 - Novas regras de validação para tributação monofásica sobre combustíveis.  
  
Mais informações na [NT 2023.001](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=B/6oigHgyAw=)

## **02. Regras**

* Ao preencher a natureza de operação no item do movimento o campo CST é carregado com o valor do CST da regra de ICMS, este campo será utilizado no envio da NF-e para preenchimento do grupo de ICMS;
* No cadastro do tributo é imprescindível que exista **apenas um tributo ICMS cadastrado.** Para que seja possível buscar a alíquota por pauta automaticamente é necessário parametrizar um tipo de movimento específico com o campo "**Procurar Alíquota Em**" marcado com a opção: "**Pauta do Produto**". Esta regra também se aplica ao tributo **ICMS ST**.

  Imagem
* Novos grupos foram adicionados no sistema para atender a NT 2023.001: Acessar a aba "Grupo N - ICMS Normal e ST"  [Grupo Tributação do ICMS= 02](https://tdn.totvs.com/pages/viewpage.action?pageId=421387606); [Grupo Tributação do ICMS= 53](https://tdn.totvs.com/pages/viewpage.action?pageId=421387606) e  [Grupo Tributação do ICMS= 61](https://tdn.totvs.com/pages/viewpage.action?pageId=421387606).
* Necessário preencher corretamente a [pauta no anexo do cadastro do produto](https://tdn.totvs.com/display/public/LRM/Pautas+do+Produto) conforme imagens abaixo:

Imagens

## **03. Exemplo de XML**

xmlExemplo tag ICMS02




{...}

0
02
3.0000
0.9400
2.82
]]>Observação

Para geração do grupo (ICMS=61) é expressamente necessário as linhas de ICMS normal e ICMS ST (monofásico) no item do movimento, mesmo que os valores da linha de ICMS sejam zeradas.

Mais informações no documento de [origens das informações para geração da (NF-e)](https://tdn.totvs.com/pages/viewpage.action?pageId=421387606)
