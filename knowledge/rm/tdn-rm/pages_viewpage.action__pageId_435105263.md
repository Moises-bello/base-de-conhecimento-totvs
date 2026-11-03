---
content_hash: f49a7623815d05931151718ef60acb8e99294483eccc20b31e8c7d96aedd5a6f
fetched_at: '2026-06-29T00:09:49.233916+00:00'
page_id: '435105263'
product: rm
source: tdn-rm
title: Utilitários - Conversores - Diagnóstico de Integração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105263
version: 4
---

Foi criado a partir da versão 12.1.21 uma ferramenta de diagnóstico da Integração RM TIN x Protheus para que sejam avaliadas algumas inconsistências que acontecem entre os produtos.   
 Para que a ferramenta seja utilizada, deve-se fazer uma conexão com o banco Protheus, utilizando o usuário e senha do banco, fazendo assim uma string de conexão entre os bancos RM e Protheus. Esta conexão é realizada na própria tela da ferramenta de diagnóstico.  
 Após realizar a conexão o RM irá trazer todos os lançamentos financeiros inconsistentes com a situação citada acima. Dessa forma será possível analisar cada caso de divergência e então serão sugeridas algumas ações para solucionar cada inconsistência da integração.  
 Hoje a ferramenta consegue verificar as seguintes inconsistências:

* Casos em que existem um ou mais títulos baixados no Protheus e o lançamento do TIN correspondente está em aberto ou parcialmente baixado.
* Casos em que existem um ou mais lançamentos baixados no TIN e os títulos no Protheus correspondentes estão em aberto ou parcialmente baixado.
* Casos em que existem um ou mais lançamentos no TIN cujo valor divirja do valor dos títulos correspondentes no Protheus.
* Casos em que existam um ou mais boletos remetidos ao banco no TIN, porém o título correspondente no Protheus não esteja em Borderô.
* Casos em que existam diferentes de-para de baixa no TIN, vinculados a um mesmo de-para do Protheus.

Antes de iniciar a análise, a ferramenta possibilita a criação e utilização de filtros para determinar o escopo das validações. As informações disponibilizadas para configuração dos filtros são:

* Chave de Integração Protheus
* Chave de Integração RM
* Código da Coligada
* Código do Cliente
* Data de Baixa
* Data de Emissão
* Data de Vencimento
* Empreendimento
* Número da Venda

Uma vez finalizada a análise e exibidos os seus resultados, a ferramenta disponibiliza acesso a vários cadastros relacionados aos lançamentos listados em cada inconsistência encontrada. São eles:

* Chave de Integração RM (Link para o cadastro do de-para do lançamento).
* Chave de Integração Protheus.
* Chave RM (Link para o cadastro do lançamento no Protheus incluindo os anexos e processos).
* Tabela RM.
* Contrato (Cadastro da Venda no TIN).
* Ação (Possíveis soluções para solucionar a divergência).
