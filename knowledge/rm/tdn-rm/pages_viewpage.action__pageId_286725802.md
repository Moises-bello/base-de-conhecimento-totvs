---
content_hash: 65f17512d210421b5d135ebce224c8a4fd843f14b9a49808edbab08468983035
fetched_at: '2026-06-29T00:08:41.407161+00:00'
page_id: '286725802'
product: rm
source: tdn-rm
title: 1095697 MSAU-12279 DT Permitir a Finalização do Atendimento pelo Painel de
  Classificação de Risco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286725802
version: 103
---

# Permitir a Finalização do Atendimento pelo Painel de Classificação de Risco com Perfil de Enfermagem

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Atendimento | Painel de Classificação de Risco | |
| **Banco(s) de Dados:** | Oracle®, SQL Server® |

## Descrição

Melhoria realizada para permitir que usuários com perfil de enfermagem, possa finalizar o atendimento pelo painel de classificação de risco.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.16.157 da biblioteca do RM.

## Procedimento para Utilização

     Verificar se o perfil do usuário está parametrizado como perfil de enfermagem nos parâmetros gerais.

         

  Acessar o painel de classificação de risco pelo menu Atendimento ---> Pronto Atendimento / Ambulatório ---> Painel de Classificação de Risco.

  O botão **Finaliza Atend.**deve estar habilitado na aba **Paciente em Observação,**permitindo a finalização do atendimento em andamento.

divs
