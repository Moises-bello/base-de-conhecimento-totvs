---
content_hash: 78d276c199ba1442ff21b9104154c27fde32be26c85913c1f7a348badc2d1218
fetched_at: '2026-06-29T00:08:24.868929+00:00'
page_id: '270907799'
product: rm
source: tdn-rm
title: MRH-4080_DT_Erro_Nome_Funcao_Passivo_Trabalhista
type: documentation
url: https://tdn.totvs.com/display/LRM/MRH-4080_DT_Erro_Nome_Funcao_Passivo_Trabalhista
version: 110
---

# ERRO COM O TAMANHO DO NOME DA FUNÇÃO NO PASSIVO TRABALHISTA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Passivo Trabalhista* |
| **Situação/Requisito:** | *Na geração do Passivo Trabalhista está apresentando o erro: “String or binary data would be truncated. ---> System.Exception: String or binary data would be truncated", quando o nome da Função possui mais de 40 caracteres.* |
| **Solução/Implementação:** | *Na tabela PFUNCAO permite nome com até 100 caracteres, mas na PSIMULADEMISSAO o campo com o nome da função está com somente 40 posições.*  *Ajustar na gravação dos dados na tabela do Passivo Trabalhista, para limitar o nome da função em 40 caracteres.* |
| **Chamados relacionados:** | MRH-4080 |
| **Requisito (ISSUE):** | MRH-4080 |

divs
