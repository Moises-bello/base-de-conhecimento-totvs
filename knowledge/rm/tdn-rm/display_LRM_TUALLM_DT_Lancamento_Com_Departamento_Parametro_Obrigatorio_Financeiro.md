---
content_hash: 686c53bbe0429930f01300169cc16c5a5e7643f4615ef99fa608047ef21ea893
fetched_at: '2026-06-29T00:06:28.852778+00:00'
page_id: '233763317'
product: rm
source: tdn-rm
title: TUALLM_DT_Lancamento_Com_Departamento_Parametro_Obrigatorio_Financeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUALLM_DT_Lancamento_Com_Departamento_Parametro_Obrigatorio_Financeiro
version: 121
---

# GERAÇÃO DE LANÇAMENTOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Geração de lançamentos de devolução* |
| **Situação/Requisito:** | *As informações de centro de custo e departamento no cadastro da unidade bibliotecária, só estavam sendo enviadas para o financeiro no momento de gerar um lançamento quando estes eram definidos como obrigatórios do lado financeiro.* |
| **Solução/Implementação:** | *Foi feito o ajuste no sistema para que sempre que as informações de centro de custo e departamento no cadastro da unidade estiverem preenchidas o sistema irá enviar para o lançamento independente da obrigatoriedade, caso estes sejam obrigatórios no financeiro e não forem preenchidos no Biblios, o sistema irá continuar alertando como antes e impedindo a movimentação.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TULZGN* |
| **Requisito (ISSUE):** | *N/A* |

divs
