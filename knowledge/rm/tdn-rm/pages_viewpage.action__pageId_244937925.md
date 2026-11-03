---
content_hash: 73db5ea7676bf82bd3bcf9ea1015b6b192730a3a7c8d95ba9c642f725ab19681
fetched_at: '2026-06-29T00:08:16.335140+00:00'
page_id: '244937925'
product: rm
source: tdn-rm
title: TVFROW_DT_Vinculo_Procedimento_Cirúrgico_Procedimento_de_Origem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244937925
version: 121
---

# FAlterado na Cirurgia o Vinculo de Procedimento Cirúrgico com o Procedimento de Origem

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Controle de Infecção Hospitalar |
| **Rotina:** | |  | | --- | | **Rotina(s) envolvida(s)** | | Procedimento de Origem | | Paciente - Cirurgia | |
| **Cadastros Iniciais:** | Procedimento Cirúrgico NHSN, Procedimento de Origem |
| **Banco(s) de Dados:** | SQL Server®, Oracle® |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Foi necessário possibilitar o vínculo de um determinado procedimento de origem com outro procedimento cirúrgico em algumas cirurgia sem alterar o cadastro do procedimento de origem alterando assim a tela de vinculo de procedimento com a via de acesso, possibilitando a alteração do procedimento NHSN com o procedimento de origem.

## Procedimento para Utilização

       1.            No **TOTVS Controle de Infecção Hospitalar** (RM Janus), acesse **Paciente / Internação / Cirurgia**.

       2.            Acesse os **Procedimentos da Cirurgia**.

Verifique que não existe mais a tela de procedimento de origem que era aberta com o cadastro, agora existe um "de para" entre os procedimentos NHSN e procedimentos de origem conforme a imagem abaixo.

       3.            Acesse o cadastro do procedimento de origem.

Verifique que foi incluído no cadastro a opção com o vinculo do procedimento NHSN, dessa forma fica independente os vinculos, ao alterar o procedimento NHSN no procedimento de origem não é alterado no cadastro da cirurgia.

divs
