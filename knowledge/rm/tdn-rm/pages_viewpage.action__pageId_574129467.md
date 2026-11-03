---
content_hash: 0471260d1689d2b5048542c5880655e3ab22501ce1b32360db2490e2bcf7619f
fetched_at: '2026-06-29T00:10:53.006370+00:00'
page_id: '574129467'
product: rm
source: tdn-rm
title: Validações TISS - Exames
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574129467
version: 7
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

**Para atendimento Interno / Externo:**

Verifica se o item de debito (SPSADT) tem a definição da tabela na ANS, caso não, retorna a mensagem de erro “Item ‘xxxxxxxx’ não está com a definição da tabela na ANS. Acesse o cadastro de Tabelas de Preços Usadas e faça a correlação com ANS.”

Verifica se o CBO está compatível para a versão do padrão TISS, caso não, retorna a mensagem de erro “Não foi identificado o CBO para versão do padrão TISS. Código: 'xxxxx' Versão: 3.03.03. Altere o CBO no lançamento. ”

**Para atendimento Interno e o padrão especial é “11 – Unidade Belém”**

Verifica se existe guia “Guia de Autorização SADT Interno”, caso não, retorna a mensagem de erro “EXAME ‘xxxxxxxx’ não tem autorização em xx/xx/xx. Informe a Guia/Autorização no atendimento do tipo de "Guia de Autorização SADT Interno" deste EXAME.  Em seguida informe no lançamento. ”

Verifica se o número da guia “Guia de Autorização SADT Interno” está informado na aba de “Diagnose e Terapia”, caso não, retorna a mensagem de erro “EXAME ‘xxxxxxxx’ sem a guia de autorização em xx/xx/xx. Informe a Guia para este EXAME no campo Guia da página Diagnose e Terapia. ”

**02. EXEMPLO DE UTILIZAÇÃO**

**05. TABELAS UTILIZADAS**

* SZATENDSADT
* SZCADGERAL
* SZTABPROCSERV
* SZTABPRECODIF
* SZTABPRECOUSADA
* SZANSCBO
* SZATENDAUTORIZ

]]>
