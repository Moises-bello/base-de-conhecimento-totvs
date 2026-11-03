---
content_hash: bbbab8f2ad1abba4b1681fe5251f0bd6f41cfaa1b1eb6ea23a3dcccb64806ad6
fetched_at: '2026-06-29T00:11:29.306457+00:00'
page_id: '736174517'
product: rm
source: tdn-rm
title: Roteiro para migrar grade numerada antiga para grade numerada por produto
type: documentation
url: https://tdn.totvs.com/display/LRM/Roteiro+para+migrar+grade+numerada+antiga+para+grade+numerada+por+produto
version: 15
---

## **01. OBJETIVO**

Este roteiro tem como objetivo orientar na migração da Grande Numerada Antiga para a Nova Grade Numerada por Produto.

## **02. ROTEIRO**

**1º - Passo:** Avaliar se a máscara atual do cadastro do produto atenderá os novos produtos controlados por grade. Caso não atenda deverá ser ajustada a mascará.

Regra para parametrizar a máscara:

* Ter pelo menos dois niveis na máscara, sendo que o último nível com pelo menos 4 caracteres somente números (#). Exemplo de máscaras: ##.####, ##.###.#####, LL.#####.

**2º - Passo:** Regerar Saldos e Custos dos produtos controlados por grade.

**3º - Passo:** Gerar a ficha física financeira dos produtos por grade e imprima (recomendado).

**4º - Passo:** Nos parâmetros de Tabelas |  Produtos avance até a Etapa 7 - Grade Numerada. Marque o parâmetro Habilitar Grade Numerada por Produto

Atenção

Ao habilitar a ativação da **Grade Numerada por Produto** ocorrerá a desabilitação automática da **Grade Numerada Convencional** de forma IRREVERSÍVEL. Este procedimento não afetará os produtos associados ao modelo convencional, que permanecerão funcionais sem o controle do estoque por grade convencional, até que sejam totalmente substituídos pelos novos produtos de grade numerada. A visão e o diálogo da 'Grade Numerada Convencional' deixarão de ser visíveis no menu do aplicativo e serão substituídos por uma nova visão e diálogo da 'Grade Numerada por Produto'.

**5º - Passo:** Criar um novo produto base, através do menu Cadastros  | Produto  | Incluir**-** O produto base deverá ser de nível analítico e ter o parâmetro "Base para Grade Numerada" marcado no cadastro do produto. 

**6º - Passo:** Criação da Grade Numerada por Produto, através do menu Tabelas Auxiliares | Grade Numerada por Produto  | Incluir,  para mais informações do cadastro acesse [Grade Numerada por Produto](https://tdn.totvs.com/display/LRM/Grade+Numerada+por+Produto).

**7º - Passo:** Criação dos  produtos de Grade Numerada.  através do menu Tabelas Auxiliares | Grade Numerada por Produto | Processo | Assistente Grade Numerada | Avançar | Criar novos produtos de grade numerada - Informe o Produto Base criado no passo 5º e indique quais produtos devem ser criados para grade numerada. Para cada combinação de Linhas X Colunas da grade numerada corresponde a um produto de grade associado.

IMPORTANTE

* Os novos produtos criados devem ser **revisitados** e **parametrizados** conforme a regra de negócio de cada produto.
* Os estoque dos produtos de grade antigas devem ser **zerados**.
* Os produtos da grade antiga devem ser **inativados**.
* Os novos produtos devem ter os **estoque alimentados**, portanto recomenda- se realizar um inventário de estoque, para mais informações acesse [Inventário de Estoque](https://tdn.totvs.com/pages/viewpage.action?pageId=423937977&draft=true).
Importante

A grade numerada antiga será descontinuada em definitivo a partir da release 12.1.2410, portanto as empresas devem se preparar e realizar a migração para a grade numerada por produto.
