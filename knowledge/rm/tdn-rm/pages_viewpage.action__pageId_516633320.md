---
content_hash: 05b1cc9e13ae76913b9196d98e7df896102aeab87b63642bbd93d4c9c6b18838
fetched_at: '2026-06-29T00:10:27.697847+00:00'
page_id: '516633320'
product: rm
source: tdn-rm
title: FISCAL01-10894 DT Anexo Benefícios Fiscais do Produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516633320
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Anexo de Benefícios Fiscais |
| Ticket: | FISCAL01-10894 |
| Requisito/Story/Issue (informe o requisito relacionado) : | Anexo de Benefícios Fiscais |

## **02. SITUAÇÃO/REQUISITO**

Criar Anexo no Cadastro do Produto (novo) para que o usuário possa relacionar quais Códigos de Ajustes se aplicam a cada Produto. Para cada Código associado, o usuário deve informar, também, para quais CST's aquele código de aplica. 

Lista de CST's:

CST 00

CST 10

CST 20

CST 30

CST 40

CST 41

CST 50

CST 51

CST 60

CST 70

CST 90

O Código de Ajuste neste Anexo deve ser um lookup para o Cadastro de Ajuste. Inicialmente vamos liberar apenas Códigos do Registro E115 do Sped Fiscal.

## **03. SOLUÇÃO**

**Cenário I: Cadastro dos benefícios fiscais do produto com CST**

Dado que o usuário possui permissão de acesso ao Produto (no Gestão de Estoque),

E marcou os CST's

E Preencheu a lookup de código de ajuste,

Ao cadastrar um benefício fiscal para o produto,

Então, o cadastro deve ser salvo.

**Cenário II: Cadastro dos benefícios fiscais do produto duplicado**

Dado que o usuário possui permissão de acesso ao Produto (no Gestão de Estoque),

E marcou os CST's

E Preencheu a lookup de código de ajuste com um código de ajuste já cadastrado para aquele produto,

Ao cadastrar um benefício fiscal para o produto,

Então, o cadastro deve informar ao usuário que o mesmo está duplicado.

**Obs.:** Não será permitido incluir o mesmo CST para o Produto com Códigos de Ajustes do mesmo Estado
