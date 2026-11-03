---
content_hash: 57d6e900443537942ce5ebd6c521503ed8b081cb3a06db40a5bf5f9359202fc8
fetched_at: '2026-06-29T00:06:16.270991+00:00'
page_id: '212894708'
product: rm
source: tdn-rm
title: TTDDW8_DT_MANAD
type: documentation
url: https://tdn.totvs.com/display/LRM/TTDDW8_DT_MANAD
version: 1
---

# MANAD

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *MANAD* |
| **Situação/Requisito:** | *Ao gerar o arquivo do MANAD quando o funcionário possui verbas de férias que são dedutíveis de IRRF de férias (somente), o sistema está levando para o MANAD no campo 10 do registro k300 a verba como 3 – não é base de cálculo, fazendo assim com que o evento não entre para a base de IRRF (bloco k200) e ao validar o arquivo no programa do SVA é apresentado erro informando que o valor da base do registro k250 está diferente do K300.* |
| **Solução/Implementação:** | *Quando se tratar de um evento que tenha incidência de "Dedutível de IRRF de Férias", o sistema deve preencher o campo 10 do registro K300 com o valor 1 - base de cálculo salário mensal no momento da geração do arquivo MANAD.* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTDDW8* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.42* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
