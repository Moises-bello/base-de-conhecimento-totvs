---
content_hash: f0e1585a2e356c243e920a1f2ac293415afc8a5516929520b588bd97dfc89531
fetched_at: '2026-06-29T00:11:50.383222+00:00'
page_id: '840393393'
product: rm
source: tdn-rm
title: Pré Requisitos para Faturamento IPSEMG
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=840393393
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Pré Requisitos para faturamento IPSEMG**
3. **Processos que utilizam este convênio**
4. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

O convênio IPSEMG (Instituto de Previdência dos Servidores do Estado de Minas Gerais)) teve suas regras de faturamento totalmente migradas do RMSaude.exe (antigo Delphi) para o Gestão Hospitalar (RM.exe) a partir do Release 12.1.2406.

As documentações de Processos e cálculos já se encontram disponibilizadas por assunto (elaboração de conta Honorários, fatura convênio, etc).

Este documento será apenas para indicar os links dos locais onde citam este convênio.

Pré Requisitos para faturamento IPSEMG

## **02. PRÉ REQUISITOS PARA FATURAMENTO IPSEMG**

* **Cadastro do Convênio - IPSEMG - Cadastros> Uso Geral> Convênio.**

Atenção para o preenchimento do campo "Padrão de Informação" que deverá estar IPSEMG.

* **Cadastro de Condições Contratuais - IPSEMG**

Atenção para o preenchimento da aba "Eletrônico III", campos "Versão TISS" no RM.exe deverá ser  usada entre as versões 3.00.00 até 3.03.03.

* **Cadastro de Padrão de Faturamento**

Informações sobre os percentuais da equipe médica - consulte o link [Percentual da função da Médica - IPSEMG](https://tdn.totvs.com/pages/viewpage.action?pageId=847872407).

Processos que utilizam este convênio

## **02. PROCESSOS QUE UTILIZAM ESTE CONVÊNIO**

**02.1 Elaboração da conta do paciente**

**Honorários:**  <https://tdn.totvs.com/x/iBA4IQ>

* [Procedimentos múltiplos e sequenciais - IPSEMG](https://tdn.totvs.com/pages/viewpage.action?pageId=847872594)

      Para esses convênios a regra para obter a tabela DTS é a mesma da regra geral. A diferença está na obtenção dos valores.

       Acesse o menu Cadastros | Faturamento | Outros Cadastros | Tabela de procedimentos e serviços. Escolha IAMSPE, em Anexos, selecione a opção "IPSEMG/IAMSPE - Valores".

**Diárias - Cálculos IAMSPE/IPSEMG:** <https://tdn.totvs.com/x/JN7HIw>

**Taxas e Serviços - Cálculos IAMSPE/IPSEMG:** <https://tdn.totvs.com/x/iR8gJ>

**SADT - Cálculos IAMSPE/IPSEMG: <https://tdn.totvs.com/x/Em6-J>**

**02.2 Encerramento da Parcial**

**Lançamento automático de diária:**

**Lançamento de Permanência a maior:**

**02.3 Fatura Convênio : <https://tdn.totvs.com/x/lt6ZJQ>**

**OBS.: Esta documentação sobre a fatura ainda está sendo atualizada até a entrega da release 12.1.2406**

 No legado RMSaude.exe o convênio IPSEMG era faturado na versão TISS 2.2.03 e a partir do release 12.1.2406 a versão da TISS deverá ser entre as versões 3.00.00 até 3.03.03.

Tabelas Utilizadas

## **03. TABELAS UTILIZADAS**

SZATENDHONORARIO : campos específicos para este convênio SP, SH, SADT, SPPREST

SZTABPROCIPSEMG :  cadastro de valores do IAMSPE/IPSEMG no Anexo do Cadastro de Tabelas de Procedimentos e Serviços

Coloque o link das tabelas relacionadas
