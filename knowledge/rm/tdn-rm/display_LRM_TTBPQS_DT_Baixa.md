---
content_hash: 8c2eca90d178ebcd2e3adeabc8fdd5950656ecd0d2c4b470c6e396b48475d528
fetched_at: '2026-06-29T00:06:29.383587+00:00'
page_id: '234607901'
product: rm
source: tdn-rm
title: TTBPQS_DT_Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/TTBPQS_DT_Baixa
version: 119
---

Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Baixa |
| **Situação/Requisito:** | Nos testes dos chamados (TT8341 e THIKQN), a situação abaixo só respeita a tag na “Emissão/Recebimento via cheque, no processo de baixa com meio de pagamento cheque, se a tag estiver “sem permissão” de acesso, o sistema não desabilita o campo de “Imprimir Cheque”.  A validação foi feita na Emissão / Recebimento de Cheque pela Visão Geral de Lançamentos, o ajuste deve ser feito também na Baixa quando usado o Meio de Pagamento igual a Cheque.  O checkbox 'Imprimir Cheque' do processo de Emissão/Recebimento de Cheques (acionado através da visão de lançamentos) passa a respeitar o status da tag de segurança [02.01.01.46]. Quando a tag estiver desabilitada, o respectivo campo também ficará desabilitado, impedindo o acionamento da impressão. |
| **Solução/Implementação:** | Otimização na permissão de perfil para informar se será possível o usuário imprimir cheque durante o processo de baixa de lançamentos, onde este seja por meio de pagamento Cheque. |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000040 |

divs
