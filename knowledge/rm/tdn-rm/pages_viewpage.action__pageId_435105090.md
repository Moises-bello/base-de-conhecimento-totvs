---
content_hash: 1748b7302c99e1f048285b08cc39d434246ecbe96ac1ae599a5714fd48f6fa06
fetched_at: '2026-06-29T00:09:47.860995+00:00'
page_id: '435105090'
product: rm
source: tdn-rm
title: Contrato de Locação - Dados Gerais - Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105090
version: 5
---

Através desse cadastro é possível vincular um imóvel a um contrato de Locação. Será permitido ao sistema  adicionar apenas Imóveis que estejam com o status "Disponível para Locação".

* Imóvel com % de Propriedade da Administradora menor que 100% ou com o checkBox Imóvel de Propriedade da Administradora de Imóvel? desmarcado:
  + Só será adicionado ao contrato de Locação se houver um Contrato de Administração efetivado para mesmo. Caso não possua Contrato de Administração associado o status do imóvel é Disponível para a Administração.
* Imóvel com % de Propriedade da Administradora igual a 100%:
  + O imóvel pode ser incluído em um Contrato de Locação, sem estar vinculado a um contrato de Administração e o seu status é "Disponível para Locação.

**Informações Tributárias**

**Percentual de Participação no Contrato**: Adicionada a possibilidade de informar o percentual de participação do imóvel no contrato. Essa informação será utilizada na geração dos movimentos dos contratos de administração para a emissão de nota fiscal, considerando o percentual definido para cada imóvel. Em outras palavras, permitirá gerar um movimento por imóvel, com o valor proporcional ao percentual informado.

**Pré-Condições:**

* Ter incluído um imóvel  com o status "Disponível para Locação".

**Adicionando um imóvel a um Contrato de Locação**

1. Clique em Incluir Imóvel no Contrato de Locação;
2. Informe um código do imóvel que atenda a pré-condição 1;
3. O campo Valor do Item do Contrato será preenchido automaticamente com o valor informado em Valor de Locação do contrato do imóvel;
4. Informe o percentual de participação do imóvel no contrato;
5. Clique em Ok.

**Alterar os dados do Imóvel do Contrato**

* Permite que  o campo Valor do Item do Contrato seja alterado em um contrato com o status "Em Elaboração".
* O campo de percentual de participação no contrato, pode ser alterado independente do status do contrato.

**Excluir Imóvel do Contrato de Locação**

* Permite excluir o imóvel de um Contrato de Locação com o status "Em Elaboração".

Informações Complementares

---
