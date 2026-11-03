---
content_hash: cec3608258e1f472b0b8cca863a90b35ff0bc1e8538baafb6ae063433dbe6868
fetched_at: '2026-06-29T00:10:52.967300+00:00'
page_id: '573205113'
product: rm
source: tdn-rm
title: Validações TISS - Diárias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=573205113
version: 2
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Para cada item de diária em um atendimento, as seguintes validações são feitas:

* Procura a tabela ANS usada. Se não for encontrada, um erro é retornado com a mensagem 'Item XXXX não está com a definição da tabela na ANS. Acesse o cadastro de Tabelas de Preços Usadas e faça a correlação com ANS.'
* Caso a encontre a tabela usada, verifica se a tabela não está inativa. Se sim, retorna a mensagem de erro "Item XXXX Tabela {XX} (INATIVA). Acesse o cadastro de Tabelas de Preços Usadas e faça a correlação com ANS.

## **02. EXEMPLO DE UTILIZAÇÃO**

Item sem definição da Tabela ANS:

Tabela inativa:

## **05. TABELAS UTILIZADAS**

* SZPARCIALATEND
* SZATENDIMENTO
* SZATENDDIARIAS
* SZATENDAUTORIZ

]]>
