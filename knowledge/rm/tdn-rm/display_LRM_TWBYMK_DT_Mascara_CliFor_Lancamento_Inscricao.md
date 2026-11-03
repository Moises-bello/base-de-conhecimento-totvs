---
content_hash: 4072cab44a6531d197799145d685eb7b255890cf140c567da0c7c54a480480f5
fetched_at: '2026-06-29T00:08:20.952690+00:00'
page_id: '268798047'
product: rm
source: tdn-rm
title: TWBYMK_DT_Mascara_CliFor_Lancamento_Inscricao
type: documentation
url: https://tdn.totvs.com/display/LRM/TWBYMK_DT_Mascara_CliFor_Lancamento_Inscricao
version: 115
---

# INSCRIÇÃO DO CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Inscrição do candidato* |
| **Situação/Requisito:** | *Quando o processo está configurado para gerar movimento de lançamento, o sistema retorna um erro de máscara de cliente/fornecedor ao realizar uma inscrição pela aplicação desktop e pelo portal do processo seletivo* |
| **Solução/Implementação:** | *Foi identificado que a situação é causada por uma inconsistência na criação do novo código do cliente/fornecedor, que se tenta criar um que já existe, a próxima tentativa de código é concatenada ao atual, gerando um erro de máscara. Foi feito o ajuste no método e a criação do código do cliente/fornecedor passou a ser feita corretamente, o lançamento criado corretamente e a inscrição é concluída.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | *N/A* |

divs
