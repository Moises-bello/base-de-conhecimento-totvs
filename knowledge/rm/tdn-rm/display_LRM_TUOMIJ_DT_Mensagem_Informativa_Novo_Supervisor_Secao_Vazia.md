---
content_hash: cddbbe79390190e42e092f081209fdf5c77b146c7f1bcd7e91f0b3def6902be7
fetched_at: '2026-06-29T00:08:11.402325+00:00'
page_id: '242391963'
product: rm
source: tdn-rm
title: TUOMIJ_DT_Mensagem_Informativa_Novo_Supervisor_Secao_Vazia
type: documentation
url: https://tdn.totvs.com/display/LRM/TUOMIJ_DT_Mensagem_Informativa_Novo_Supervisor_Secao_Vazia
version: 114
---

# Novo Supervisor

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Novo Supervisor* |
| **Situação/Requisito:** | *Ao tentar incluir um novo supervisor em uma seção sem funcionários ativos, o sistema permitia abrir a tela, porém, o lookup de escolha da chapa que seria cadastrada como supervisor não retornava nenhum registro, e nenhuma mensagem era exibida para evidenciar que não existiam funcionários para serem escolhidos na seção.* |
| **Solução/Implementação:** | *Ao clicar no botão "Novo Supervisor" é feita uma verificação se a seção escolhida possui funcionários e caso não encontre, é exibida uma mensagem para o usuário alertando sobre a situação.* |
| **Chamados relacionados:** | *TUOMIJ, TVDRC3* |

divs
