---
content_hash: 6a4fb663e7286c61d82aa1fb607fef7b5329c2e80ef417540d05f8484157d88f
fetched_at: '2026-06-29T00:08:09.396147+00:00'
page_id: '239036451'
product: rm
source: tdn-rm
title: TUUJAD_DT_Aviso_Automatico_Ferias_em_dobro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUUJAD_DT_Aviso_Automatico_Ferias_em_dobro
version: 115
---

# AVISO AUTOMÁTICO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Aviso Automático* |
| **Situação/Requisito:** | *Envio de aviso automático em tela para situação de férias em dobro estava causando erro na execução do processo.* |
| **Solução/Implementação:** | *Inclusão de um DISTINCT na query de consulta dos funcionários que devem receber o aviso, pois a consulta estava retornando as chapas em duplicidade, causando a falha na execução do processo* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TUUJAD* |
| **Requisito (ISSUE):** |  |

divs
