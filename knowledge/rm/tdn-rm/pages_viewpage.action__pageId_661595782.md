---
content_hash: fe7f9794a8af8337b27856f5b587d8aa3e95c2b1bfe5d6ccc87d8e5d03856722
fetched_at: '2026-06-29T00:11:13.532608+00:00'
page_id: '661595782'
product: rm
source: tdn-rm
title: Parâmetros - Qualificação de Fornecedores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=661595782
version: 1
---

**Controle de Qualidade do Fornecedor:**

* Utiliza por Fornecedor: ao utilizar essa opção o controle de qualificação será realizado somente para o fornecedor, independente do produto/serviço que o mesmo fornece.
* Utiliza por Produto/Fornecedor: escolhendo essa opção o controle de qualificação será feito para cada produto/serviço, ou seja, será exigido que o produto/serviço seja comprado com um fornecedor qualificado.
* Utiliza Ambos: será feito controle de qualidade por Fornecedor e por Produto/Fornecedor.

**Fórmula para Cálculo da Qualificação por Fornecedor:** o sistema irá executar essa fórmula caso o Controle de Qualidade do Fornecedor esteja definido como "Utiliza por Fornecedor" ou "Utiliza Ambos". O resultado da fórmula deve retornar um valor entre 0 e 100, esse valor será comparado com o valor do parâmetro "Pontuação Mínima para Qualificação". O resultado da fórmula sendo menor que a pontuação mínima, o Fornecedor será considerado não qualificado, caso o resultado seja maior ou igual a pontuação mínima, o Fornecedor será definido como qualificado.

**Fórmula para Cálculo da Qualificação por Produto/Fornecedor:** o sistema irá executar essa fórmula quando o Controle de Qualidade do Fornecedor for igual a "Utiliza por Produto/Fornecedor" ou "Utiliza Ambos".  
O resultado da fórmula deve retornar um valor entre 0 e 100, esse valor será comparado com o valor do parâmetro "Pontuação Mínima para Qualificação". O resultado da fórmula sendo menor que a pontuação mínima, o Produto/Fornecedor será considerado não qualificado, caso o resultado seja maior ou igual a pontuação mínima, o Produto/Fornecedor será definido como qualificado.

**Pontuação Mínima para Qualificação:** o valor informado nesse campo será comparado com o resultado da(s) fórmula(s) de Qualificação informada(s), para que o Fornecedor ou Produto/Fornecedor seja considerado como "Qualificado" a pontuação mínima deve ser menor ou igual ao resultado da fórmula.  
Deve ser informado um valor entre 0 e 100.
