---
content_hash: 2c3882f045aad956113ac9e7420502178e37a7e998788169298c91e78e0435d9
fetched_at: '2026-06-29T00:08:09.277672+00:00'
page_id: '239032572'
product: rm
source: tdn-rm
title: TUUQVM_Documentos_Candidato_AreaOfertada_Mesmos_Documentos
type: documentation
url: https://tdn.totvs.com/display/LRM/TUUQVM_Documentos_Candidato_AreaOfertada_Mesmos_Documentos
version: 118
---

# DOCUMENTOS DO CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Documentos do candidato* |
| **Situação/Requisito:** | *Ao atualizar um documento entregue na inscrição do candidato está ocorrendo erro ao salvar operação.* |
| **Solução/Implementação:** | *Foi identificado que o erro era causado pelo fato das duas áreas terem documentos em comum, ao carregar na tela, o sistema carregava os dois registro no binding source, dois documentos iguais porém com a obrigatoriedade diferente, ao tentar salvar o sistema identificava que o registro estava duplicado e não permitia, foi feito o ajuste no evento que carrega o registro na tela, para não ser carregado com duplicidade e permitir a alteração da situação do documento corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
