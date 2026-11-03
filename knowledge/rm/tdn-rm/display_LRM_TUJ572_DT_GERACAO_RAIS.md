---
content_hash: 1886c1c90c260549b94be8517aea94e6a709858355ba6b018524f231d069ad76
fetched_at: '2026-06-29T00:06:27.932976+00:00'
page_id: '233739175'
product: rm
source: tdn-rm
title: TUJ572_DT_GERACAO_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TUJ572_DT_GERACAO_RAIS
version: 122
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Ao gerar arquivo RAIS para um funcionário que teve rescisão no ano base, recebeu aviso prévio indenizado dessa demissão, foi reintegrado, excluído o histórico de demissão e demitido no ano posterior ao ano base ocorre erro de validação da RAIS acusando que existe valor de aviso prévio e não existe data de desligamento e nem o tipo de desligamento. |
| **Solução/Implementação:** | Ajuste na rotina RAIS para validar se ano e mês de competência do recebimento do aviso prévio indenizado foi posterior à data de rescisão do funcionário, evitando assim que exista verbas de aviso prévio e não exista data e código de desligamento quando esse funcionário foi reintegrado. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUJ572 TUKAC1 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.11* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
