---
content_hash: 36b5fff108f688b9e3582abd27f723068510beefb33023b0e2e6cf4aed19ab95
fetched_at: '2026-06-29T00:08:13.995777+00:00'
page_id: '244436437'
product: rm
source: tdn-rm
title: TUSWGZ_DT_GRRF_PROCESSO_COM_SUCESSO_MAS_NAO_GERA_ARQUIVO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUSWGZ_DT_GRRF_PROCESSO_COM_SUCESSO_MAS_NAO_GERA_ARQUIVO
version: 111
---

# GRRF

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos.* |
| **Módulo:** | *RM.* |
| **Função:** | *Mensagem de conclusão do Processo.* |
| **Situação/Requisito:** | Ao emitir a GRRF em que não a Dados a Serem emitidos devido a não existir valores para o Total de Recolhimento, o processa informava que foi concluído com sucesso porém por não existir dados a recolher não gerava o arquivo. |
| **Solução/Implementação:** | O processo de geração da GRRF não irá informar que foi concluído com sucesso quando não houver valores para o total a recolher. Neste caso será informado que o processo terminou com ressalvas e no log de debug e aviso será mostrado a mensagem: Não há Total a Recolher para Emissão da GRRF   *.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUSWGZ |
| **Requisito (ISSUE):** |  |

divs
