---
content_hash: 38555c5e31376dbc13ab5a6d92d4d1f2354551d5ec4d96125137c0eece052057
fetched_at: '2026-06-29T00:06:01.757829+00:00'
page_id: '198939781'
product: rm
source: tdn-rm
title: TRZNQH_DT_Cadastro_Rescisão_Próximo_Mês_Motivo_DC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198939781
version: 2
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
| **Versões/Release:** | *11.82.40* |

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
