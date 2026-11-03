---
content_hash: bb1533a9451522cac15b1a9f9e2333075b9231b38bd5341c8ac058cf7b8c703c
fetched_at: '2026-06-29T00:06:13.939399+00:00'
page_id: '208348702'
product: rm
source: tdn-rm
title: TSVI54_DT_ERRO_Processo_Alterar_Status_Opcoes_Candidato_Descricao_Fixa
type: documentation
url: https://tdn.totvs.com/display/LRM/TSVI54_DT_ERRO_Processo_Alterar_Status_Opcoes_Candidato_Descricao_Fixa
version: 1
---

# PROCESSO ALTERAR STATUS DAS OPÇÕES DO CANDIDATO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Processo Seletivo* |
| **Função:** | *Processo Alterar status das opções do candidato* |
| **Situação/Requisito:** | *Foi alterado o nome de um dos cadastros de Status de opção, porem ao executar o processo de alteração de status das opções do candidato no log é exibido o nome original do status e não o nome que foi alterado.* |
| **Solução/Implementação:** | *O processo Alterar status das opções do candidato monta os itens de Status de forma estática, e não recupera as informações mais recentes dos registros de Status das Opções.*  *Foi realizado um ajuste que permite recuperar as informações atuais dos cadastros de Status das Opções.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | *Versão na qual está sendo feita a manutenção deste programa.* |
| **Versão Expedida:** | *Versão em que o programa será oficialmente expedido.* |

divs
