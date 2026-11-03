---
content_hash: 0bdd6d0719876434a8185a3b883a721ab3d546e991395d08ec34e6b9b55cd816
fetched_at: '2026-06-29T00:06:19.656046+00:00'
page_id: '220891035'
product: rm
source: tdn-rm
title: TTSFGM_DT_Registro_ANS_Não_Preenchido
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=220891035
version: 1
---

# DIRF/Informe de Rendimentos

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *DIRF/Informe de Rendimentos* |
| **Situação/Requisito:** | Ao gerar a DIRF quando na tela de operadora de assistência saúde o campo do registro ANS da operadora não é preenchido, o sistema informa ao final da execução o seguinte erro:     System.Data.StrongTypingException |
| **Solução/Implementação:** | *Alterado para validar o preenchimento do registro ans quando salvar os dados da operadora.* |
| **Chamados relacionados:** | *TTSFGM* |
| **Versões/Release:** | *11.82.43* |

divs
