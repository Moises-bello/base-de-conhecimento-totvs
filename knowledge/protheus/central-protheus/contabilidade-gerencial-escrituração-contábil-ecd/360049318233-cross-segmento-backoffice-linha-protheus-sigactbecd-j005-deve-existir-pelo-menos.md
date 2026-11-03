---
article_id: 360049318233
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 47fb1fdd48240d4c2391c59c1849acdd5a9a73130f095dfc2304515a6ca005af
fetched_at: '2026-06-28T22:40:44.238286+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus  - SIGACTB/ECD - J005 : Deve existir
  pelo menos um registro J100 (Balanço) e um J150 (DRE) para cada registro J005 (Demonstração
  Contábil) informado.'
type: support-article
updated_at: '2024-02-23T20:13:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049318233-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-J005-Deve-existir-pelo-menos-um-registro-J100-Balan%C3%A7o-e-um-J150-DRE-para-cada-registro-J005-Demonstra%C3%A7%C3%A3o-Cont%C3%A1bil-informado
---

**Ocorrência**

Deve existir pelo menos um registro J100 (Balanço) e um J150 (DRE) para cada registro J005 (Demonstração Contábil) informado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360071982874)

**Ambiente**Microsiga Protheus – Contabilidade Gerencial  – A partir da versão 11.80  
  
**Causa**

* Cenário :Empresa não possui movimento nas contas de receita e despesa no primeiro mês , porem possui movimento na contas de ativo e passivo em todos os meses  com isso pretende gerar o arquivo de 01/01 a 31/12

**Solução**

Situação esta sendo apresentada ,pois não existe J100 e o J150 não foram gerados por completo ,para o primeiro mês  
  
Diante disso caso não possua saldo ou movimento nas conta de ativo, passivo, patrimônio liquido, receita e despesa , o sistema não irá gerar J150 e J100 corretamente.

* A apuração de resultado Receita - Despesa = Patrimônio Liquido (Lucro ou prejuízo)

* O Balanço ([J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023992791-MP-SIGACTB-ECD-J100?source=search)) é composto da contas de ativo , passivo  e Patrimônio Liquido (Lucro ou prejuízo) que possua movimento e ou saldo anterior

* A DRE ([J150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028247351-MP-SIGACTB-ECD-COMO-GERAR-O-REGISTRO-J150-?source=search)) é composta do saldo das conta de receita e Despesa que possuam saldo ou movimento

​O J100 e J150 são registro obrigatórios , com isso será necessário verificar junto a receita para validar seu arquivo em vista que sua empresa não teve nenhuma Receita e Despesa ou Ativo e Passivo neste período

Saiba mais :

[MP - SIGACTB - ECD – Arquivo Fracionado que NÃO seja Situação Especial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047508094-MP-SIGACTB-ECD-Arquivo-Fracionado-que-N%C3%83O-seja-Situa%C3%A7%C3%A3o-Especial-?source=search)
