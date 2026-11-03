---
content_hash: ed883617d34bfef507e882417279265598d555fee530a288273539bb3868a6c3
fetched_at: '2026-06-29T00:11:50.377309+00:00'
page_id: '840393371'
product: rm
source: tdn-rm
title: Pré Requisitos para Faturamento IAMSPE
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=840393371
version: 15
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Pré Requisitos para faturamento IAMSPE**
3. **Processos que utilizam este convênio**
4. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

O convênio IAMSPE (Instituto de Assistência Médica ao Servidor Público Estadual de São Paulo) teve suas regras de faturamento totalmente migradas do RMSaude.exe (antigo Delphi) para o Gestão Hospitalar (RM.exe) a partir do Release 12.1.2406.

As documentações de Processos e cálculos já se encontram disponibilizadas por assunto (elaboração de conta Honorários, fatura convênio, etc).

Este documento será apenas para indicar os links dos locais onde citam este convênio.

Pré Requisitos para faturamento IAMSPE

## **02. PRÉ REQUISITOS PARA FATURAMENTO IAMSPE**

* **Cadastro do Convênio - IAMSPE - Cadastro> Uso Geral> Convênio**

Atenção para o preenchimento do campo "Padrão de Informação" que deverá estar IAMSPE.

* **Cadastro de Condições Contratuais - IAMSPE**

Atenção para o preenchimento da aba "Eletrônico III", campos "Versão TISS" no RM.exe deverá ser a partir da versão 4.01.00 .

* **Cadastro de Padrão de Faturamento**

Informações sobre os percentuais da equipe médica - consulte o link [Percentual da função da Médica - IPSEMG](https://tdn.totvs.com/pages/viewpage.action?pageId=847872407).

Processos que utilizam este convênio

## **03. PROCESSOS QUE UTILIZAM ESTE CONVÊNIO**

**02.1 Elaboração da conta do paciente**

**Honorários:**  <https://tdn.totvs.com/x/iBA4IQ>

* [Cirurgia Múltipla Pela Mesma Via de Acesso - IAMSPE](https://tdn.totvs.com/pages/viewpage.action?pageId=695606694)
* [Cirurgia Multipla Por Outra via de Acesso - IAMSPE](https://tdn.totvs.com/display/LRM/Cirurgia+Multipla+Por+Outra+via+de+Acesso+-+IAMSPE)
* [Obstetrícia e Neonatologia IAMPSE](https://tdn.totvs.com/pages/viewpage.action?pageId=695606762)
* [Tratamento em Politraumatizados IAMSPE](https://tdn.totvs.com/display/LRM/Tratamento+em+Politraumatizados+IAMSPE)

      Para esses convênios a regra para obter a tabela DTS é a mesma da regra geral. A diferença está na obtenção dos valores.

       Acesse o menu Cadastros | Faturamento | Outros Cadastros | Tabela de procedimentos e serviços. Escolha IAMSPE, em Anexos, selecione a opção "IPSEMG/IAMSPE - Valores".

**Diárias - Cálculos IAMSPE/IPSEMG:** <https://tdn.totvs.com/x/JN7HIw>

**Taxas e Serviços - Cálculos IAMSPE/IPSEMG:** <https://tdn.totvs.com/x/iR8gJ>

**SADT - Cálculos IAMSPE/IPSEMG: <https://tdn.totvs.com/x/Em6-J>**

**02.2 Encerramento da Parcial**

**Lançamento automático de diária:**

**Lançamento de Permanência a maior:**

**02.3 Fatura Convênio : <https://tdn.totvs.com/x/lt6ZJQ>**

**OBS.: Esta documentação sobre a fatura ainda está sendo atualizada até a entrega da release 12.1.2406**

No legado RMSaude.exe o convênio IAMSPE era faturado na versão TISS 2.2.03 e a partir do release 12.1.2406 a versão da TISS deverá ser a partir da 4.01.00.

Tabelas Utilizadas

## **03. TABELAS UTILIZADAS**

SZATENDHONORARIO : campos específicos para este convênio SP, SH, SADT, SPPREST

SZTABPROCIPSEMG :  cadastro de valores do IAMSPE/IPSEMG no Anexo do Cadastro de Tabelas de Procedimentos e Serviços
