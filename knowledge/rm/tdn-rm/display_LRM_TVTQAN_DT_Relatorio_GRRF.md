---
content_hash: 7fee2bc14a9072194483aebf0b5bf7a9cee577415a5593aca590399a762a6f70
fetched_at: '2026-06-29T00:08:18.071723+00:00'
page_id: '261588029'
product: rm
source: tdn-rm
title: TVTQAN_DT_Relatorio_GRRF
type: documentation
url: https://tdn.totvs.com/display/LRM/TVTQAN_DT_Relatorio_GRRF
version: 111
---

# RELATÓRIO GRRF

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Relatório GRRF.* |
| **Função:** | *Campo 40 GRRF.* |
| **Situação/Requisito:** | Ao gerar o arquivo da GRRF para funcionários que possuem rateio de tomadores, e este tomador possui seu CEI informado na tela inicial CNPJ/CPF e não no campo Anexos/Cei do cliente fornecedor, o sistema está levando para o registro 40 inscrição do tomador o valor 1 que indica que este tomador é identificado por CNPJ, porém não é verdade, este tomador é identificado por CEI e precisa ser levado o valor 2 neste campo. |
| **Solução/Implementação:** | Foi ajustado o sistema para quando o usuário preencher o campo CNPJ/CPF do Cliente /Fornecedor  com um CEI válido, o sistema irá levar para o campo identificação do Tomador (Registro 40)  o valor 2 que indica que este tomador é identificado por CEI e não por CNPJ. |
| **Chamados relacionados:** | TVTQAN |

divs
