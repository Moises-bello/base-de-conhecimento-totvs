---
content_hash: 884a6618292479930d916424aad01a5c23e7f022cd23c2613a70e5c3a885a80f
fetched_at: '2026-06-29T00:08:31.654556+00:00'
page_id: '273303476'
product: rm
source: tdn-rm
title: 193030 MSAU-6228 DT Filtrar Padrão de Prescrição por Unidade de Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273303476
version: 99
---

# Filtrar padrão de prescrição por unidade de atendimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Prontuário | Prescrição médica | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | Oracle® e SQL Server® |

## Descrição

Realizado ajuste no PEP para filtrar o padrão de prescrição de acordo com a unidade de atendimento do paciente.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações da versão 12.1.16.001 do aplicativo RM Saúde.

## Procedimento para Utilização

       1.            No TOTVS Gestão Hospitalar, acesse o Menu Cadastros > Cuidados com o paciente > Prescrição médica > Padrões de prescrição;

       2.            Selecione um principio ativo e em seguida na aba padrão de prescrição selecione ou cadastre uma apresentação;

       3.            Na tela de concentração, selecione a aba padrão de prescrição e insira um novo padrão;

       4.            Preencha o campo Diluição e na aba Unidades de Atendimento informe as unidades de atendimento que possuíram acesso ao padrão de prescrição;

OBS: Se não for selecionado nenhuma unidade, o padrão ficará habilitado para todas as unidade de atendimento.

       5.            Em seguida acesse o prontuário de qualquer paciente e cadastre uma nova prescrição;

       6.            Ao buscar o medicamento, o sistema deve apresentar somente os padrões de prescrição habilitados para a unidade de atendimento do paciente.

divs
