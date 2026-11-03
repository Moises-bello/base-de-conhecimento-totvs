---
content_hash: d779ada221892586f2f4115ae1da372633d8dd4722b89753624135d76b94659f
fetched_at: '2026-06-29T00:08:09.025668+00:00'
page_id: '239020141'
product: rm
source: tdn-rm
title: TUXLL7_DT_Nivel_Ensino_Filial
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXLL7_DT_Nivel_Ensino_Filial
version: 113
---

# NÍVEL DE ENSINO - FILIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Nível de Ensino - Filial* |
| **Situação/Requisito:** | *Em Gestão fiscal >> Cadastros >> Filiais >> Anexos >> Dados educacionais >> Anexos >> Níveis de ensino por filial, foi identificado a seguinte situação: Após criar uma nova filial e tentar associá-la a um nível de ensino, o sistema exibe a seguinte mensagem de erro e não permite salvar, ocorrendo chave duplicada.* |
| **Solução/Implementação:** | *Ajuste na propagação para todos os contextos de uma mesma coligada quando se altera o parâmetro de arrendondamento de carga horária, créditos acadêmicos e créditos financeiros.* |
| **Conversores e Parâmetros:** | *Configurações | Parâmetros | Secretaria | Geral 4/5 | Trunca e Arredonda*  *Configurações | Parâmetros | Tesouraria | Geral 2/2 | Trunca e Arredonda* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs

Configurações | Parâmetros | Secretaria | Geral 4/5 |
