---
content_hash: d1b5ee3185c721a718eda35cce7669c80ff10df636aa161894cc38ac65e100b7
fetched_at: '2026-06-29T00:06:18.393544+00:00'
page_id: '215484565'
product: rm
source: tdn-rm
title: TTQSK9_DT_Confirmacao_Inscricao_Altera_Status_Para_Pendente
type: documentation
url: https://tdn.totvs.com/display/LRM/TTQSK9_DT_Confirmacao_Inscricao_Altera_Status_Para_Pendente
version: 1
---

# CONFIRMAR INSCRIÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Confirmar Inscrições* |
| **Situação/Requisito:** | *Quando um candidato possui desconto de 100% no valor da inscrição e sua inscrição já está com status de confirmar, o processo de confirmação de inscrição altera o status deste candidato para Pendente (aguardando pagamento) indevidamente.* |
| **Solução/Implementação:** | *Foi verificado que é gerado um lançamento com o valor 0, pois o valor da inscrição e do desconto são iguais, porém o sistema identifica como se o lançamento estivesse aberto e retorna o status para "Pendente", assim foi feito o ajuste no processo para que identifique quando o candidato tiver 100% de desconto na inscrição o seu status permaneça como Confirmado.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | **N/A** |
| **Requisito (ISSUE):** | **N/A** |
| **Versões/Release:** | **12.1.9** |
| **Versão Corrigida:** | **12.1.8** |
| **Versão Expedida:** | **12.1.9** |

divs
