---
content_hash: 75b640fba3a9332ba441997f7f7f342660f57fe64066bf921aae0285272bc387
fetched_at: '2026-06-29T00:09:55.557692+00:00'
page_id: '447095932'
product: rm
source: tdn-rm
title: 4363196 CONTROLADORIA01-2309 DT Registro I050
type: documentation
url: https://tdn.totvs.com/display/LRM/4363196+CONTROLADORIA01-2309+DT+Registro+I050
version: 4
---

# SPED Contábil - Registro I050

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Contábil |
| **Função:** | SPED Contábil |
| **Situação/Requisito:** | No arquivo gerado pelo SPED Contábil existem contas sem saldo e sem movimentação que estão sendo geradas no registro I050. |
| **Solução/Implementação:** | A geração do SPED contábil foi modificada para que o registro I050 não exiba contas sem movimentação e sem saldo. O cenário descrito acima estava ocorrendo quando a soma do saldo anterior e das movimentações, dos anos "x" e "Y", era zero.  Ex: A conta 1.1.001 possui saldo anterior igual a zero, uma movimentação de 1500 em 2016 e outra de -1500 em 2017. Nesse caso o saldo anterior em 2018 é zero, por isso essa conta não deve compor os registros I050 da ECD. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
