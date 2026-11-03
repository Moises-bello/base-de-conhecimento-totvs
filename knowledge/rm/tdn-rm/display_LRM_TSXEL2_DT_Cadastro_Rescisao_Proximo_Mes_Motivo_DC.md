---
content_hash: 476f52face7e6d1982392107f212979a9bdfc811a720f92d114a9650cde48d5f
fetched_at: '2026-06-29T00:06:03.259723+00:00'
page_id: '198952288'
product: rm
source: tdn-rm
title: TSXEL2_DT_Cadastro_Rescisao_Proximo_Mes_Motivo_DC
type: documentation
url: https://tdn.totvs.com/display/LRM/TSXEL2_DT_Cadastro_Rescisao_Proximo_Mes_Motivo_DC
version: 3
---

# LIBERAÇÃO DE COMPETÊNCIA

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Rotina de Liberação de Competência* | *Liberação de Competência* | |
| **Cadastros Iniciais:** | *Realizar o cadastro de rescisão de qualquer tipo para um funcionário qualquer, para o próximo mês.*  *O funcionário pode ter férias marcadas ou não.* |
| **Parâmetro(s):** | *Rescisão para o próximo mês.* |
| **Chamados relacionados** | *TRZNQH* |
| **Banco(s) de Dados:** | *SQL Server, Oracle* |
| **Tabelas utilizadas:** | *PMUDSITUACAO, PMOTDEMISSAO* |
| **Versões/Release:** | *12.1.7* |

## Descrição

Ao executar a rotina de Liberação de Competência do TOTVS Folha de Pagamento, tendo algum funcionário que possua rescisão cadastrada para o próximo mês, o sistema passou a verificar um motivo de mudança de situação que seja compatível com o motivo da demissão para que seja exibido corretamente no Histórico de Situação, ao invés de exibir apenas DC - Desconhecido.

## Procedimento para Utilização

1. No contexto TOTVS Folha de Pagamento, acesse o menu Administração de Pessoal > Funcionários.
2. Será aberta a visão de funcionários. Selecione qualquer funcionário com Situação: Ativo.
3. Clique no ícone de Rescisão ou então acesse o menu Anexos > Movimento > Rescisão.
4. Preencha as informações do cadastro da rescisão com qualquer Tipo de rescisão.
5. Vá para a aba "Rescisão".
6. Na data de demissão/cálculo, preencha com uma data da próxima competência.
7. Preencha os demais campos obrigatórios do cadastro de rescisão.
8. Clique em Salvar.
9. Acesse o menu Folha Mensal > Liberação de competência.
10. Avance o assistente até o final, preenchendo as informações que forem solicitadas.
11. Ao finalizar o processo, o Histórico de Situação será atualizado corretamente com o motivo da rescisão, desde que exista um mesmo motivo cadastrado para a Demissão e para a Mudança de Situação.
