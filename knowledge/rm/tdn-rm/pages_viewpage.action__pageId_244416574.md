---
content_hash: f58f8f01827581b3b62d06c9169739cfe0ba74e6c3fd92f396177af154faf942
fetched_at: '2026-06-29T00:08:13.321059+00:00'
page_id: '244416574'
product: rm
source: tdn-rm
title: TVEBM3_DT_Criação_Pârametro_Encerrar_Registro_Informações_Cirúrgicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244416574
version: 116
---

# Parâmetro para permitir encerrar o registro de informações cirúrgicas.

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Cuidados com o paciente | Registro de informações cirúrgicas | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |

## Descrição

Criado parâmetro que tem por objetivo obrigar o cadastro de no mínimo um procedimento com cirurgião cadastrado ou Descrição técnica da cirurgia ou folha de sala vinculada, para enviar o registro da cirurgia para faturamento.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.11.115  da biblioteca do RM.

## Procedimento para Utilização

Acesse o menu **Utilitários / Parâmetros / Parâmetros Gerais / Cuidados do paciente**.

Marque o parâmetro “**Obriga preenchimento de pelo menos um procedimento vinculado a um cirurgião ou descrição técnica preenchida ou folha de sala vinculada para encerrar o registro**".

Acesse o menu **Cuidados com paciente / Centro Cirúrgico / Registro de informações cirúrgicas**.

Cadastre um novo registro de informações sem informar um procedimento vinculado a um cirurgião, descrição técnica e sem vincular uma folha de sala.

Ao enviar esse registro para faturamento o sistema apresentará a seguinte mensagem “Não é possível concluir o Registro. Verifique se existe ao menos um Procedimento vinculado com Cirurgião na equipe ou uma Folha de Sala vinculada ou Descrição Técnica preenchida”.

divs
