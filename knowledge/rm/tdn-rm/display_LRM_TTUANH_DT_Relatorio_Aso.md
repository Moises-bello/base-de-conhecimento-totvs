---
content_hash: 9784b8de540c6ad597cb3eaea398e20ddcc208c55adb285306794305c8c11beb
fetched_at: '2026-06-29T00:06:22.422410+00:00'
page_id: '223916849'
product: rm
source: tdn-rm
title: TTUANH_DT_Relatorio_Aso
type: documentation
url: https://tdn.totvs.com/display/LRM/TTUANH_DT_Relatorio_Aso
version: 122
---

# RELATÓRIO ASO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Segurança e Saúde Ocupacional* |
| **Função:** | *Relatório ASO* |
| **Situação/Requisito:** | *Ao gerar o ASO o sistema não está levando todos as avaliações de risco para o campo 1 (Riscos Ocupacionais específicos existentes.).* |
| **Solução/Implementação:** | *Ajuste na geração do relatório ASO. Na geração do relatório, o sistema entende que é possível haver interseção de datas entre períodos de alocação externa e a própria lotação do funcionário. Dessa forma, o período da lotação é considerado por completo e pega todos os Riscos daquele período.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTUANH; TTZCOE* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43; 12.1.9* |

divs
