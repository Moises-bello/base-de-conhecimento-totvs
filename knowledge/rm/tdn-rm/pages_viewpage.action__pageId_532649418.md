---
content_hash: 715479d356960acde5fcf29979fc7199ce34e6642fbd612150989230bb05fa76
fetched_at: '2026-06-29T00:10:36.478269+00:00'
page_id: '532649418'
product: rm
source: tdn-rm
title: Como gerar a tag ideDmDev com prefixo período quando há movimentação para autônomos
  do Totvs Gestão Financeira com categorias diferentes e mesmo CPF?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532649418
version: 7
---

# Objetivo:

---

Quando existe cadastro de autônomos que tem múltiplos vínculos cadastrados e possuem lançamentos no mesmo período de pagamento, surgiu a necessidade de criar o campo prefixo período para diferenciar o período de pagamento a ser enviado para cada autônomo. Abaixo o exemplo de cadastro do campo:

1true1Execução do scriptExecução do script

Para a criação do novo campo será necessária a atualização da base no sistema RM.Atualizador.exe.

true1CadastroCadastro

No exemplo abaixo possui o cadastro de dois autônomos com o mesmos CPF onde um deles possui o cadastro do prefixo:

Código: C09999 e código de categoria: 712

Código: C00312 e código de categoria: 701

Acesse o menu Backoffice | Gestão Financeira | Cadastros | Clientes Fornecedores | Anexos | eSocial

1) Cadastrado o campo Prefixo Período para o cliente/fornecedor código: C00312 e código de categoria: 701

**Observações:**  
O campo pode ser preenchido com números ou letras.

2) Feito o lançamento financeiro para os dois vínculos;

Feito o lançamento na data 28/01/2019 para o cliente/fornecedor com o código: C09999 sem o cadastro de prefixo.

Feito lançamentos nas datas 10/01/2019 e 28/01/2019 para o cliente/fornecedor com o código: C00312 que possui o cadastro de prefixo.

Após o cadastro dessas informações basta gerar o xml no caminho RH / folha de pagamento / eSocial / Gerar XML

Sistema gerou os xml's para os autônomos corretamente.

Conforme cadastro acima para o cliente/fornecedor código: C09999 que não possuía o cadastro de prefixo foi gerado com tag ideDmDev com o número padrão 1.

Conforme cadastro acima para o cliente/fornecedor código: C00312 que possui o cadastro de prefixo com valor "A" foi gerado com tag ideDmDev 1A (número padrão 1 + A) .
