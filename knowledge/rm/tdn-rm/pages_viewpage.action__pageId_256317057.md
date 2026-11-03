---
content_hash: 051fe58f53b90b043bbb631b08823a1318483d0771b8145aaa7b480ca23c2e6d
fetched_at: '2026-06-29T00:08:17.615105+00:00'
page_id: '256317057'
product: rm
source: tdn-rm
title: TVTBJL_DT_Cheques_Emissão_de_Cheques_(sem baixar)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=256317057
version: 117
---

# Cheques - Emissão de Cheques (sem baixar)

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | Gestão Financeira |
| **Função:** | Cheques - Emissão de Cheques (sem baixar) |
| **Situação/Requisito:** | O sistema está com divergência de comportamento da versão 1180 para a versão 12 quando é realizado a emissão  de cheque para vários lançamentos com a opção de um cheque por lançamento. Ao preencher a aba de dados  Adicionais o Banco, agência, conta corrente e forma de pagamento do primeiro cheque, o sistema automaticamente  replicava os dados para os demais cheques. |
| **Solução/Implementação:** | Otimização no processo de recebimento de cheque a receber. Agora selecionando a opção "Replicar Banco,  Agência, Conta Corrente e Forma de Pagamento para todos os cheques" que é exibido ao selecionar um cheque por  lançamento, o sistema faz a cópia dos dados informados do primeiro cheque repassando para os próximos sempre  respeitando os dados default dos próprios lançamentos (Convenio). |
| **Conversores e Parâmetros:** | N/A |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | FIN000156 |

divs
