---
content_hash: 453e8d462f52ec2f052e57cc59aa8e8ab93ffcd6dce40d63a0474681d4879e04
fetched_at: '2026-06-29T00:06:27.312707+00:00'
page_id: '232819297'
product: rm
source: tdn-rm
title: TUHHKA_DT_Remetente_Recibo_Movimentacao_Email_Nao_Respeita_Parametro
type: documentation
url: https://tdn.totvs.com/display/LRM/TUHHKA_DT_Remetente_Recibo_Movimentacao_Email_Nao_Respeita_Parametro
version: 121
---

# CRIAÇÃO DE USUÁRIOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Usuários - criação* |
| **Situação/Requisito:** | *Ao criar um novo usuário o campo "Código do usuário" é iniciado preenchido com o usuário que está logado. Foi identificado que a geração do esquema de dados estava setando valores padrões e preenchendo ao iniciar a tela, sendo que esta leitura do esquema a foi implementanda para tratar o problema de tipos de dados ao usar o dataserver via webservice.* |
| **Solução/Implementação:** | *Para ajuste foi removido a leitura do esquema na leitura de dados e inserida uma validação no momento de salvar os dados para que verifique e busque o esquema de dados e  verificar se os tipos das colunas estão corretos, assim sendo corrigindo o problema dos tipos pelo webservice e não exibindo mais código do usuário como usuário logado ao criar um novo usuário.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TUJEHY* |
| **Requisito (ISSUE):** | *N/A* |
| **Versões/Release:** | *11.82.43*  *12.1.10* |
| **Versão Corrigida:** | *11.82.43*  *12.1.10* |
| **Versão Expedida:** | *11.82.43*  *12.1.10* |

divs
