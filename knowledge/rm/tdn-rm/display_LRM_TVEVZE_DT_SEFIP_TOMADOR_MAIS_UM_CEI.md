---
content_hash: b9d18dce3fc1c169fa4f4cb30a041265566670c456b6c004cf4a15aaa152526d
fetched_at: '2026-06-29T00:08:13.442996+00:00'
page_id: '244422620'
product: rm
source: tdn-rm
title: TVEVZE_DT_SEFIP_TOMADOR_MAIS_UM_CEI
type: documentation
url: https://tdn.totvs.com/display/LRM/TVEVZE_DT_SEFIP_TOMADOR_MAIS_UM_CEI
version: 117
---

# RATEIO DO TOMADOR DE SERVI~ÇÕ

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Gravar o CEI para tomador de Serviço* |
| **Situação/Requisito:** | Quando altera dados de um tomador pelo cadastro de funcionário, e clicando em salvar na tela de rateio do tomador, o sistema atualizava o código do CEI, o que obrigava a redistribuição global de tomador do SEFIP para que a geração do SEFIP não reportasse a mensagem de duplicação de CEI para um mesmo tomador. |
| **Solução/Implementação:** | Ao salvar os dados do rateio por tomador o sistema atualiza o CEI de acordo com o seu identificado na tabela FCFOCEI. Não necessitando processar a Distribuição do SEFIP por tomador*.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TVEVZE* |
| **Requisito (ISSUE):** |  |

divs
