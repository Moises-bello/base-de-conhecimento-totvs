---
content_hash: c93a42822d25a02cf5bee20075466c0782a8a4ce66fdcbb50b4d0b760d1e4773
fetched_at: '2026-06-29T00:05:47.726611+00:00'
page_id: '1015576361'
product: rm
source: tdn-rm
title: DT - Smart UI - Visão duplicada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1015576361
version: 7
---

## **01. DADOS GERAIS**

| Produto: | RM |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Função: | Smart UI - Visão duplicada |
| País: | Brasil |
| Issue: | [DRHROTRM-15601](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15601) |

## **02. VERSÕES**

12.1.2506 e superiores.

## **03. SITUAÇÃO/REQUISITO**

Atualmente devido a **transição e coexistência** da tela do Histórico Salarial e a nova tela em Smart UI, foi identificado o comportamento onde o menu de anexos associado ao registro do colaborador está sendo renderizado em duplicidade.

## **04. SOLUÇÃO**

Após a avaliação do cenário, confirmamos que a duplicação do menu será corrigida através do procedimento abaixo.

**1 - Acesso ao Sistema:** Inicie o sistema (`RM.exe`).

**2 - Menu Serviços Globais:** Selecione o menu **Serviços Globais**.

**3 - Aba Serviços:** Acesse a aba **Serviços**.

**4 - Ações Anexas:** Clique na opção **Actions Anexas**.

**5 - Filtro:** Filtre pela *Action* Principal: `FopFuncAction`.

**6 - Exclusão:** **Exclua** a *Action* Anexo com o nome: `FopActionHistoricoSalarialWinForm`.

**7 - Reinicialização:** Efetue **Logout** e **Login** no sistema.

Após a conclusão do procedimento, acesse o **Cadastro de Funcionários** e **valide** se os anexos do Histórico Salarial estão aparecendo corretamente (sem duplicidade).

false🔔 ATENÇÃO:

Este processo é executado diretamente na **base de dados**. Portanto, **não é necessária a execução** nas estações dos usuários.

## **05. DOCUMENTAÇÃO**
