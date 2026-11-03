---
content_hash: ea689e4afc37d34407477a880696d0de109c71348b933bcdd4cf813b4a2e360b
fetched_at: '2026-06-29T00:08:40.852145+00:00'
page_id: '286511075'
product: rm
source: tdn-rm
title: 1178259 DEDUINTEGRACOES-178 DT Processo de criação de parcela com "N" cotas
  para a mesma parcela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286511075
version: 104
---

# Criar Parcela

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Processo de Criação de Parcela |
| **Situação/Requisito:** | Ao tentar criar parcelas usando o processo criar parcelas no menu assistente da aba financeiro do módulo educacional, o processo estava criando as parcelas incorretamente .  Exemplo:  Tenho dois serviços para incluir no contato.  1 em 4 cotas (serviço 71) no valor 455,00 e mais 12 parcelas(serviço 1) no valor de 1.820,00.  TESTES REALIZADOS: Ao informar ao sistema para criar 1 parcela em 4 cotas deveria ser criado:  Parcela 1 - Cota 1 Parcela 1 - Cota 2 Parcela 1 - Cota 3 Parcela 1 - Cota 4  Está criando:  Parcela 1 - Cota 1 Parcela 2 - Cota 2 Parcela 3 - Cota 3 Parcela 4 - Cota 4 |
| **Solução/Implementação:** | Melhoria no processo de criação de parcela para que seja executado corretamente quando optamos em gerar “N” cotas para uma parcela. |
| **Conversores e Parâmetros:** |  |
| **Tickets relacionados:** |  |
| **Requisito:** |  |

divs
