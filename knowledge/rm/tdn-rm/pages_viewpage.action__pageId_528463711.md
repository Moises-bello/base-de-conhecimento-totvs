---
content_hash: 7df7bce39d5aad1b7adecfed3ec0cf19831c1ed1c79cfb171afee5c5d70d9971
fetched_at: '2026-06-29T00:10:32.950598+00:00'
page_id: '528463711'
product: rm
source: tdn-rm
title: 'FISCAL01-11876 DT EFD-Contribuições 2020 - Reg. 1011: 1- Cadastro Trib. Discutido'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=528463711
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Tributo Discutido |
| Ticket: | - |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11876 |

## **02. SITUAÇÃO/REQUISITO**

Criação, nos tributos discutidos, do processo judicial os campos: fórmula de base de cálculo, alíquota e CST.  
Código Defensivo nas versões de mercado.

## **03. SOLUÇÃO**

**Funcionalidade: Cadastro de tributos discutidos**

**Cenário I: Cadastrar um tributo discutido**

Dado que o script de marcação LI.2020.01\_01 está executado na base de dados,

Ao abrir a tela de tributos discutidos (anexo ao processo judicial),

Então devem estar visíveis e serem possíveis de salvar os campos: fórmula de base de cálculo, alíquota e CST.

**Cenário II: Buscar fórmula**

Dado que o script de marcação LI.2020.01\_01 está executado na base de dados,

Ao buscar uma fórmula,

Então, devem ser exibidas somente fórmulas do Fiscal (aplicação D).
