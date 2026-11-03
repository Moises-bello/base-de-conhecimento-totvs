---
content_hash: 3f90fabab6c19a6d34d4e54356e6aabcca75cdb5bb408c65af3459f14ae58b7b
fetched_at: '2026-06-29T00:08:06.949280+00:00'
page_id: '236597431'
product: rm
source: tdn-rm
title: TTUWVX_DT_Apuracao_Resultados
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUWVX_DT_Apuracao_Resultados
version: 118
---

# APURAÇÃO DE RESULTADOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Gestão Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Apuração de Resultados* | *Apuração de Resultados* | |
| **Cadastros Iniciais:** | *1) Aluno cadastrado e matricula em período letivo e em turmas/disciplinas;*  *2) Fórmula cadastrada para apuração de resultados;*  *3) Consulta SQL para apuração de resultados.* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Chamados Relacionados** | *TUVYVO* |
| **Requisito (ISSUE):** | *N/A* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *Sql Server e Oracle* |
| **Tabelas Utilizadas:** | *SMATRICPL* |
| **Sistema(s) Operacional(is):** | *Windows 7* |

## Descrição

Ajuste no processo de apuração de resultados para que ao alterar o status do resultado na matrícula no período letivo a data do resultado será preenchida automaticamente, ou seja, sempre que executar a fórmula GravaCampoPL ('CODSTATUSRES', <Status do resultado>).

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *(11.82.44)* deste chamado ou *(12.1.12)* do chamado TUVYVO.

## Procedimento para Utilização

Para a rotina Apuração de Resultados:

1. Acessar o Totvs Educacional | Matrícula e Avaliação | Apuração de Resultados;
2. Executar o processo inserindo a(s) fórmula(s) e utilizando as consultas;
3. Após a execução a data do resultado no cadastro da matrícula do aluno será a mesma data da execução do processo.

divs
