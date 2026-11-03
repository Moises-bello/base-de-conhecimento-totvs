---
content_hash: 2675433b3617c607acd750d21a72de5e89d646b605e36c7414cf66789b269456
fetched_at: '2026-06-29T00:08:24.813684+00:00'
page_id: '270904934'
product: rm
source: tdn-rm
title: 197233 MCP-1273 ER NF-e Nota Técnica 2016/001 - Unidade Tributável no Comércio
  Exterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270904934
version: 148
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Cadastros > Produtos > Controle Estoque  Cadastros > Mais...> Tabelas Auxiliares > Unidade |
| **Segmento Executor** | Construção & Projetos | | |
| **Chamado** | 197233 | | |
| **País** | Brasil | | |

   

## Objetivo

Esta melhoria tem como objetivo atender à Nota Técnica 2016/001 que adequa a NF-e ao Projeto do Portal Único do Comércio Exterior, padronizando a Tabela de Unidades de Medidas Tributáveis no Comércio Exterior, conforme o código NCM (Nomenclatura Comum do Mercosul) da mercadoria a que se refere, com base nas unidades recomendadas pela Organização Mundial de Aduanas (OMA).  

A Nota Técnica 2016/001 tem como objetivo estabelecer uma Tabela de Unidades de Medidas Tributáveis no Comércio Exterior, publicada na aba “Documentos”, opção “Diversos”, do Portal da NF-e , a qual relaciona, para cada código NCM, a unidade de medida, que deverá ser obrigatoriamente utilizada na emissão de documentos fiscais, para quantificar os produtos a que se refiram, nos campos relativos à Unidade Tributável (uTrib) e Quantidade Tributável (qTrib) da Nota Fiscal Eletrônica – NF-e.

O disposto na NT 2016/001 aplica-se apenas aos contribuintes que operem no Comércio Exterior, relativamente às notas fiscais relacionadas a Operações de Exportação (tpNF=1-Saída e idDest=3) ou nas Operações vinculadas à Exportação (CFOP=1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505).

## Definição da Regra de Negócio

Para atendimento à NT 2016/001, no cadastro de Unidades (**Cadastros | Mais... | Tabelas Auxiliares | Unidade**) foi criado o campo onde será informado o Código da Unidade Tributável (TUND.CODUNDTRIBUTAVEL) correspondente à unidade.

Na tabela de Unidades (TUND) deverão ser observadas as seguintes consistências:

* O Código da Unidade Tributável apenas será habilitado para edição caso o campo Tributável esteja marcado (TUND.TRIBUTAVEL = 1);
* O preenchimento do Código da Unidade Tributável será obrigatório caso o campo Tributável esteja marcado;
* O campo Tributável não poderá ser desmarcado caso a unidade esteja configurada como Unidade Tributável em algum produto (TPRODUTODEF.CODUNDTRIBUTAVEL);
* Ao salvar o registro, caso o campo tributável esteja desmarcado e o código de unidade tributável preenchido será emitida a mensagem "Para a Unidade que não é tributável é necessário limpar o campo Cód. Unidade Tributável".

No cadastro de Produtos, tabela TPRODUTODEF (**Cadastros | Produto**), na aba **Controle Estoque**, dentro do group box **Unidades**, serão criados os campos:

* Unidade Tributável;
* Fator de Conversão Unidade Tributável.

O lookup do campo Unidade Tributável deverá:

* Somente apresentar para seleção as unidades que estejam configuradas como tributável;
* Exibir coluna contendo a unidade tributável das unidades apresentadas.

No momento da gravação do registro do Produto o sistema deve verificar, e somente permitir a Unidade Tributária informada, caso a sua unidade base seja a mesma da Unidade de Controle do produto.

Na geração do arquivo XML das NF-e relacionadas a Operações de Exportação (tpNF=1-Saída e idDest=3) ou nas Operações vinculadas à Exportação (CFOP=1501, 2501, 5501, 5502, 5504, 5505, 6501, 6502, 6504 ou 6505), o sistema irá:

* Identificar o código da Unidade Tributável de cada item da NF-e conforme a seguinte prioridade:
  + Cadastro de Produtos - verificará o preenchimento do campo Código da Unidade Tributável e caso o mesmo esteja preenchido, irá enviar o seu conteúdo para o campo uTrib do XML da NF-e;
  + Cadastro de Unidades - caso o produto não tenha unidade tributável cadastrada, será verificado no cadastro de Unidades o preenchimento do campo Código da Unidade Tributável da unidade utilizada no item de movimento e caso o mesmo esteja preenchido, irá enviar o seu conteúdo para o campo uTrib do XML da NF-e;
  + Unidade Base - caso nem o produto e nem a unidade utilizada no item de movimento possuam unidade tributável informada, o sistema irá verificar a unidade base da unidade do item de movimento, e caso a unidade tributável da mesma esteja preenchida, irá enviar o seu conteúdo para o campo uTrib do XML da NF-e. Se a unidade base não estiver configurada como unidade tributável, será enviado o próprio código da unidade base.
* Identificar o Fator de Conversão a ser utilizado no cálculo da quantidade na unidade tributável conforme a seguinte prioridade:
  + Caso o produto possua Unidade Tributável configurada, o sistema irá verificar se o Fator de Conversão Tributável também foi informado, e em caso positivo, o sistema utilizará o mesmo para o cálculo e gravação da quantidade na unidade tributável (campo qTrib do XML da NF-e);
  + Caso o produto possua Unidade Tributável mas o Fator de Conversão Tributável não esteja informado, o sistema utilizará o Fator de Conversão cadastrado para a Unidade Tributável parametrizada no produto;
  + Caso o produto não possua Unidade Tributável e a unidade utilizada no item de movimento seja tributável, o sistema utilizará o fator de conversão = 1;
  + Caso o produto não possua Unidade Tributável e a unidade utilizada no item de movimento também não seja tributável, o sistema utilizará o fator de conversão = 1.

Importante salientar que, caso no cadastro de Produtos o Fator de Conversão Tributável esteja informado, mas não conste a informação da Unidade Tributável o sistema desconsiderará esse Fator de Conversão e passará a utilizar o fator informado no cadastro da Unidade Tributável na tabela de Unidades.

**Para realizar a implantação da funcionalidade na versão 12.1.14, é necessário executar os scripts EXECSQLTOTVSGESTAODEESTCOMPFATMCP-1273.ZIP e MCP-1573\_1200.ZIP****disponíveis no pacote, já para as versões superiores à 12.1.14 não há necessidade de execução de nenhum script específico.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Unidade | Alteração | Cadastros > Mais > Tabelas Auxiliares > Unidade | Conforme definições constantes deste documento |
| Produto | Alteração | Cadastros > Produto | Conforme definições constantes deste documento |

## Tabelas Utilizadas:

* TUND - Unidade;
* TPRODUTODEF - Definições dos Produtos.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
