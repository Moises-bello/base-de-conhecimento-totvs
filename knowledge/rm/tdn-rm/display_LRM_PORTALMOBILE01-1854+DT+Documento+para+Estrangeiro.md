---
content_hash: 81a53723d28bb16b1eb9e79bc5f31464bcd85ce97ad066d8bf3dc19cedca3bac
fetched_at: '2026-06-29T00:08:44.412319+00:00'
page_id: '307851510'
product: rm
source: tdn-rm
title: PORTALMOBILE01-1854 DT Documento para Estrangeiro
type: documentation
url: https://tdn.totvs.com/display/LRM/PORTALMOBILE01-1854+DT+Documento+para+Estrangeiro
version: 97
---

# Documento para Estrangeiro na inscrição do Processo Seletivo

|  |  |
| --- | --- |
| **Linha de Produto:** | TOTVS |
| **Segmento:** | RM |
| **Módulo:** | Educacional |
| **Função:** | Inscrição e Alteração de dados pessoais |
| **Situação/Requisito:** | Ao realizar a inscrição de uma pessoa que seja estrangeiro, e esteja marcado o parâmetro "Obrigar o preenchimento de um dos campos (CPF, Passaporte ou Registro Geral), caso estejam visíveis". Em casos onde, conforme o nome do parâmetro informa, estes campos estejam marcados, deve-se obrigar apenas o preenchimento de um destes campos para um indivíduo estrangeiro. |
| **Solução/Implementação:** | Foi realizada uma implementação onde o sistema identifica se o usuário é estrangeiro ou não, de acordo com o País selecionado no grupo de Endereço do formulário de Inscrição ou Alteração de Dados Pessoais (para manter compatibilidade com o Processo Seletivo do portal antigo), seja diferente do país parametrizado na aba "Parâmetros" > Nacionalidade.  Apenas um dos campos se torna obrigatório o seu preenchimento:  - CPF  - Passaporte  - Registro Geral  Ao realizar o preenchimento de um destes campos, automaticamente os demais deixam de ser obrigatório. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |

divs
