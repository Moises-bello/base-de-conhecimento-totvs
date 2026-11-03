---
content_hash: 06664f0963baddfc11d7d667a3093d68f52fb6d2ac56dc69173e5c58f83040d3
fetched_at: '2026-06-29T00:09:29.839266+00:00'
page_id: '425458306'
product: rm
source: tdn-rm
title: Desalocar candidatos em locais de prova
type: documentation
url: https://tdn.totvs.com/display/LRM/Desalocar+candidatos+em+locais+de+prova
version: 3
---

Este processo será executado após ocorrer o processo "Alocar Candidatos em Locais de Prova". Este processo é utilizado para cancelar estas alocações, ou seja, retirar os candidatos dos locais de prova.   
 Utilizando o processo: Será necessário configurar a etapa e as áreas ofertadas que terão seus candidatos desalocados.

Os candidatos não serão desalocados de todas etapas. O assistente vai permitir que o usuário defina para qual a etapa que ele deseja desalocar. Se o parâmetro "Selecionar candidatos específicos?" estiver marcado, será habilitada uma nova etapa para informação dos candidatos que serão desalocados. Será exibida uma grid com a relação de todos candidatos das áreas ofertadas e etapas selecionadas.

Toda vez que este processo for executado o sistema irá verificar se existem candidatos com lista de presença, ou seja, se o processo "Registrar presença de candidatos" já foi executado. Caso isto seja verdade, a lista de presença de todos os candidatos será excluída. Esta medida evita que inconsistências sejam geradas na base de dados, uma vez que a lista de presença é gerada de acordo com os candidatos alocados.

**Pré-requisitos do processo**:  
 **a)** Ter executado previamente o processo "Alocar Candidatos em Locais de Prova".
