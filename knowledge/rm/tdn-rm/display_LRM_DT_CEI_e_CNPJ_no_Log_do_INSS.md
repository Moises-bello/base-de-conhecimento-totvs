---
content_hash: c3f922d3fdf2f10cc8ef5536011c26954b6f3ffcb03c0904753de6f788f7b60e
fetched_at: '2026-06-29T00:06:25.041268+00:00'
page_id: '224129631'
product: rm
source: tdn-rm
title: DT_CEI_e_CNPJ_no_Log_do_INSS
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_CEI_e_CNPJ_no_Log_do_INSS
version: 1
---

# CEI E CNPJ NO LOG DO INSS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Guia de INSS | Log | |
| **Versão/Release:** | *12.1.4* |

## Descrição

Esta implementação possibilita gerar o log da Guia INSS com CEI e CNPJ quando marcado a opção “Movimento por tomador” e “Construção Civil (Guia por tomador)”. O objetivo é que cada tomador tenha seus registros devidamente identificados.

## Procedimento para Utilização

Em Folha de Pagamento / Encargos / Guia de INSS marque o flag “Movimento por Tomador” e “Construção Civil”, depois avance.

Na próxima tela, preencha o campo obrigatório “Código do Relatório” e avance as telas abaixo.

Na tela seguinte, marque a coligada e avance, será exibida a tela de execução.

Após a execução do processo ter sido concluída com êxito, marque “Gerar Log de Cálculo”, informe o caminho onde será salvo o arquivo de log e gere a Guia de INSS.

Após isto, localize e visualize o Log gerado. No cabeçalho do mesmo adicione as informações de CEI e CNPJ.
