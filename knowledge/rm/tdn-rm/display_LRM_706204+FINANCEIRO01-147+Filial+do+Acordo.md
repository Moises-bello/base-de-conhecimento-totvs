---
content_hash: 93386c25edfb806cd7b3d087b883c7dc361c12ae84493c963070c0f035fef60b
fetched_at: '2026-06-29T00:08:33.048661+00:00'
page_id: '274005282'
product: rm
source: tdn-rm
title: 706204 FINANCEIRO01-147 Filial do Acordo
type: documentation
url: https://tdn.totvs.com/display/LRM/706204+FINANCEIRO01-147+Filial+do+Acordo
version: 106
---

# FILIAL PARA ACORDO FINANCEIRO DE DIFERENTES LANÇAMENTO

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Totvs Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Geração de Acordo. |
| **Situação/Requisito:** | Tela do processo de geração de acordo trava quando executado para mais de um lançamento e a filial default do template de acordo e do contexto não estão informadas. |
| **Solução/Implementação:** | No processo de carga de dados do acordo a filial é buscada na seguinte ordem: lançamentos (quando igual em todos), default informado no template de acordo ou por último da filial informada no contexto do sistema. Caso não encontre em nenhum desses valores será emitida mensagem de erro e o processo finalizado. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | Informe o(s) chamado(s) relacionado(s). |
| **Requisito:** | FINANCEIRO01-147. |

divs
