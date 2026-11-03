---
content_hash: 3f9efdc395b6abb16bccc94759200faa877f9561997a4d5812975f3e8fb36cea
fetched_at: '2026-06-29T00:08:35.347018+00:00'
page_id: '279174861'
product: rm
source: tdn-rm
title: 952544 CONTROLADORIA01-236 DT Imprimir Natureza Conta Saldo Zero
type: documentation
url: https://tdn.totvs.com/display/LRM/952544+CONTROLADORIA01-236+DT+Imprimir+Natureza+Conta+Saldo+Zero
version: 107
---

# Imprimir a natureza das contas com saldo zero

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Contábil |
| **Função:** | SPED Contábil |
| **Situação/Requisito:** | Ao gerar a ECD, no REGISTRO J100, uma conta credora que teve o saldo final igual a zero está saindo com o Indicador da situação do saldo final como devedor. |
| **Solução/Implementação:** | Ao gerar a ECD os registros I155, I157, I355 e J100 deverão imprimir a natureza da conta quando o saldo for zero. Vale ressaltar que os registros J210 e J215 trabalham com códigos de aglutinação e fatos contábeis, por isso se o saldo for zero, não é possível utilizar uma conta para recuperar a situação do saldo (C - Credor ou D - Devedor). Também é importante frisar que o registro J100 não irá recuperar a natureza da conta, com saldo zerado, dos itens gerados a partir da DRE antiga do Saldus. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados**: | N/A |
| **Requisito (informe o requisito relacionado):** | N/A |

divs
