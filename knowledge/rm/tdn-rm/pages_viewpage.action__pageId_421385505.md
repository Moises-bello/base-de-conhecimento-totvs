---
content_hash: 2cde101a964f65c641facbbcdca44be46b84b3d2200ffdc7bfe327e4ee82b64d
fetched_at: '2026-06-29T00:09:16.291655+00:00'
page_id: '421385505'
product: rm
source: tdn-rm
title: Processo de Desativação de Coletores Móveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385505
version: 2
---

---

Para desativar coletores móveis, o usuário deverá selecionar o coletor na visão de cadastro de coletores (Cadastros | Mobilidade | Coletores Móveis) e acessar o menu Processos | Desativar Coletores Móveis.

Para os coletores serem desativados, não poderão existir Folhas Tarefa e/ou Projetos associdos a eles.

Caso exista, o sistema irá exibir a mensagem informativa.

**Exemplo:** "As Folhas Tarefa "A", "B" e "C" e os Projetos "1", "2", "3" estão associadas a coletores "X", "Y", "Z". A execução do processo irá efetuar a desassocição destas Folhas e destes Projetos. Caso existam apontamentos para tais Folhas no coletor, estes serão desconsiderados quando o usuário de coletor tentar importar os dados para o ERP".

* "A", "B" e "C" representam os números e a descrição das Folhas Tarefa associadas a coletores;
* "1", "2" e "3" representam os projetos associados a coletores;
* "X", "Y" e "Z" representam os identificadores dos coletores.

Se o usuário confirmar a execução do processo e desativar os coletores, as Folhas e Projetos associados serão liberados automaticamente para associação a outro coletor. Se não confirmar, o sistema exibirá um aviso ao usuário "Os coletores X, Y e Z permanecem ativos", e cancela o processo.   
 Quando o coletor for desativado, além de excluir o vínculo com as folhas tarefas, será excluído também o vínculo com os projetos vinculados ao mesmo.   
 Caso o parâmetro "Utiliza mais de um projeto por coletor móvel"  disponível nos Parâmetros Gerais esteja desmarcado um mesmo coletor não poderá estar associado e ativo em mais de um projeto simultaneamente.  
 O sistema exibe uma mensagem informativa com os projetos e folhas tarefas associadas caso existam, caso o usuário opte por desassociá-los os mesmos ficarão livres para serem associados a outros coletores.
