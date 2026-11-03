---
content_hash: a503976ad5f0a4430c094e482c47ca91675a61aaada9e487c2d009a35f103c89
fetched_at: '2026-06-29T00:06:26.527929+00:00'
page_id: '225951037'
product: rm
source: tdn-rm
title: TUFVDQ_DT_GERACAO_RAIS_PREFIXO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUFVDQ_DT_GERACAO_RAIS_PREFIXO
version: 122
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | *Erro ao validar arquivo RAIS. prefixo somente com um dígito* |
| **Solução/Implementação:** | Ajuste na rotina RAIS retirar máscara de campos CNPJ e CEI (SEÇÃO) concatenados com prefixo rais, evitando buscar prefixo errado quando não possuir máscaras nesse campo. Agora esses campos são manipulados sempre sem máscara para tratamento de prefixo. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUFVDQ TUHOA6 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.10 11.82.42* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
