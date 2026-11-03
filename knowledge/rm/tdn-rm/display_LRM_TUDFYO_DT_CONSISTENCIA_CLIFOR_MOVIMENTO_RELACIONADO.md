---
content_hash: 6a5add749de3f22abe435b373b8230656ca6e36a17409ac1516cac6b6f607ea2
fetched_at: '2026-06-29T00:08:05.540860+00:00'
page_id: '235597434'
product: rm
source: tdn-rm
title: TUDFYO_DT_CONSISTENCIA_CLIFOR_MOVIMENTO_RELACIONADO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUDFYO_DT_CONSISTENCIA_CLIFOR_MOVIMENTO_RELACIONADO
version: 117
---

# ME DO REQUISITO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | [TOTVS Gestão de Estoque, Compras e Faturamento - Legislação](http://tdn.totvs.com/pages/viewpage.action?pageId=235597424) |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MOV.001 | *INCLUSAO DE MOVIMENTO.* | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | *TUDFYO, TVDIZ0* |
| **Requisito (ISSUE):** | MOV000003 - Movimento |
| **País(es):** | *-* |
| **Banco(s) de Dados:** | *-* |
| **Tabelas Utilizadas:** | *TTMVEXT* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Foi criado novo parametro (Parametros do Tipo de Movimento -> Etapa Movimento - Outros Dados -> Não consiste Cli/For) para permitir que o usuário selecione se deseja que o cliente fornecedor seja co0nsistido.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *11.82.44 ou 12.1.12*

## Procedimento para Utilização

1.  Abra os parâmetros do tipo de movimento Etapa Movimento - Outros Dados e marque a opção "Não consiste Cli/For".

2. Crie um movimento de substituição, informando um cli/for diferente do movimento inicial e verifique que o processo será permitido.

divs
