---
content_hash: f18c00e9cd08f754f678a9825746ce03096b5ed9a9339eb8c39056eba2b1ef75
fetched_at: '2026-06-29T00:08:11.249507+00:00'
page_id: '242387925'
product: rm
source: tdn-rm
title: TSJMP0_DT_Parâmetro_Não_Permite_Alta_com_Checagem_de_Medicamentos_Pendente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=242387925
version: 108
---

# Não permitir alta com check de medicamentos pendente

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Saúde |
| **Módulo:** | TOTVS Gestão Hospitalar |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Posto de Enfermagem | Alta | |
| **País(es):** | Brasil |
| **Sistema(s) Operacional(is):** | Windows® |

## Descrição

Criado parâmetro para não permitir cadastrar alta para pacientes com check de medicamentos não finalizados.

## Procedimento para Utilização

1. Acesse **Opções / Parâmetros / Parâmetros Gerais / Unidades de Diagnóstico II** e marque o parâmetro “**Não permite Alta para paciente com medicamentos pendente de checagem da enfermagem**”.
2. Cadastre um registro de internação para qualquer paciente.
3. Acesse o **Prontuário** do paciente e prescreva um medicamento para o paciente.
4. Acesse a movimentação de estoque e processe a requisição gerada pela prescrição.
5. Acesse novamente o **Prontuário** do paciente na aba **Enfermagem / Check de medicamento**.
6. Verifique se os itens prescritos aparecem na tela.
7. Acesse o menu **Cuidados com o paciente / Posto de Enfermagem / Alta, e cadastre a alta do paciente**.
8. Ao o salvar a alta o sistema não permitirá o registro e informará que existe medicamento pendente de check.
9. Acesse novamente o **Prontuário** do paciente na aba **Enfermagem / Check de medicamento**.
10. Finalize todos os checks pendentes.
11. Cadastre novamente a alta.
12. O sistema permitirá a alta quando todos os checks estiveram finalizados.

divs
