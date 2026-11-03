---
content_hash: 51c3b0447ee0996ce3e2e35ebf859dfa5b8f4e56dfb6cd585352102b53fde4c8
fetched_at: '2026-06-29T00:08:28.206034+00:00'
page_id: '271667268'
product: rm
source: tdn-rm
title: MEDU-2437_DT_Inscricao_Vaga_Estagio
type: documentation
url: https://tdn.totvs.com/display/LRM/MEDU-2437_DT_Inscricao_Vaga_Estagio
version: 110
---

# INSCRIÇÃO NA VAGA DE ESTÁGIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Inscrição na vaga de estágio* |
| **Situação/Requisito:** | Botão de inscrever candidato no portal não está sendo possível vincular uma fórmula visual, pois o botão chama um método customizado do DataServer e não o SaveRecord. |
| **Solução/Implementação:** | Ajuste na chamada do portal para inscrição do aluno, passando a chamar o SaveRecord do DataServer EduVagasCandidatosData para que seja possível vincular formula visual ao "processo". |
| **Conversores e Parâmetros:** | *N/A* |
| **Tickets relacionados:** | *N/A* |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
