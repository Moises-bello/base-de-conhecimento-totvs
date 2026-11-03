---
content_hash: d40d25f8908ee72e8032981c3cb456b363475931391a8bc99e3ab88150573c13
fetched_at: '2026-06-29T00:06:27.504187+00:00'
page_id: '232823948'
product: rm
source: tdn-rm
title: TU0791_DT_Configuração_de_Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232823948
version: 119
---

# **Tela de configuração de relatórios**

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Utilitários | Configuração de Relatórios | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle, SQL |
| **Tabelas Utilizadas:** | SZRELATCONFIG |

## Descrição

Os usuários necessitam gerar alguns relatórios pelo TOTVS Reports, mas exitem pontos no sistema onde os relatórios ainda são gerados pelo RM Gerador. Para atender essa solicitação sem afetar os cliente que utilizam o RM Gerador, foi desenvolvido um recurso onde o usuário pode selecionar o tipo de gerador e o relatório que serão utilizados na geração do relatório.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.10 da biblioteca do RM.

## Procedimento para Utilização

       1.            No **TOTVS Gestão Hospitalar** (RM Saúde), acesse o menu **Utilitários / Utilitários do RM Saúde / Configuração de relatórios**.

       2.            Selecione um relatório e clique em **Editar**.

       3.            Na tela de edição, selecione o tipo de gerador e o relatório que será utilizado na geração.

       4.           Em seguida, acesse a tela onde o relatório é gerado e imprima o relatório.

divs
