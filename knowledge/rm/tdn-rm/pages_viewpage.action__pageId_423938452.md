---
content_hash: 1239a7a15c6897736b03422e34a0dfad8b5b91bf9c9bb1bb53c157c640fee7e5
fetched_at: '2026-06-29T00:09:27.191386+00:00'
page_id: '423938452'
product: rm
source: tdn-rm
title: Importação de arquivo texto com dados contábeis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938452
version: 4
---

A importação de dados contábeis no Totvs – Gestão Contábil consiste em incluir, de forma automática, na base de dados determinadas informações, dispostas ordenadamente em um arquivo texto.

Para realizar a importação de dados contábeis através de arquivo texto, utilizaremos um recurso do TOTVS Business Conector, que tem como um dos objetivos, prover a integração de dados entre diferentes sistemas.

A importação de dados contábeis pode ser utilizada para facilitar a implantação do sistema, povoando de forma dinâmica a base de dados, utilizando as regras dos próprios cadastros. Pode ser utilizada também na migração do RM Cont para o Totvs – Gestão Contábil e na integração de informações entre vários produtos.

No TOTVS Business Conector existe uma ferramenta chamada  que pode ser parametrizada de forma a armazenar os dados das conexões entre sistemas de origem e destino. É possível então que se criem Conceitos personalizados com dados específicos para cada integração.

No Totvs – Gestão Contábil já se encontram cadastrados alguns Conceitos com dados pré-definidos, para serem utilizados na importação de dados contábeis para alguns cadastros. Cada um destes Conceitos já está parametrizado com os devidos layouts que informam, entre outros dados, o nome, o tamanho, o tipo de cada dado a ser utilizado na importação para os respectivos cadastros. Estes Conceitos que já estão disponíveis **não** poderão ser alterados e, caso seja necessário utilizar um Conceito com outro layout, este deverá ser criado por você.

**Observações**

* Cada Conceito utiliza layouts individuais compostos por informações dos dados contidos em cada cadastro, tais como nome dos campos, tamanho e tipo de dados.
* Os arquivos textos utilizados para a importação devem obrigatoriamente ter a mesma estrutura definida no respectivo layout.
* Para estes Conceitos que já se encontram disponíveis, os layouts foram criados sem a utilização de delimitadores de campos que, neste caso, utilizará a largura fixa de cada campo. Sendo assim, no arquivo texto utilizado para importação, a posição definida para cada campo deve ser respeitada assim como o seu tamanho e, caso não exista nenhuma informação para determinado campo, a posição deste deve ser preenchida por espaços, equivalentes ao seu tamanho. Caso você ignore o espaço reservado para estes campos o sistema não fará a importação.

Os Conceitos que já se encontram disponíveis podem ser utilizados para a importação de dados contábeis para os seguintes cadastros. Clique em cada um para visualizar os respectivos layouts.



Existem também Conceitos que já se encontram disponíveis e que poderão ser utilizados na conversão do RM Cont para o Totvs – Gestão Contábil, onde no RM Cont deve-se proceder com a exportação dos dados contábeis e no Totvs – Gestão Contábil, com a importação destes dados. Os Conceitos já estão devidamente parametrizados para converter os dados exportados do RM Cont para o padrão atual.
