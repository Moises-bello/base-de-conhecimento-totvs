---
content_hash: cff3f38fb1f715a62b8735a459acdea84ba9b5c34226a041ea319f6b849f31fd
fetched_at: '2026-06-29T00:09:26.190385+00:00'
page_id: '423938297'
product: rm
source: tdn-rm
title: Exclusão de Ocorrências
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938297
version: 5
---

Processo responsável pela exclusão de ocorrências (, , Transferência Monetária – Parcial e Total) existentes em patrimônios bem como atualização de seus respectivos valores (em moeda e índice).

A Exclusão de Ocorrências não será realizada nas seguintes situações:

* Período de Cálculo diferente da ocorrência: a ocorrência só poderá ser excluída caso sua data esteja dentro do período de cálculo, ou seja, uma baixa (por exemplo) realizada no mês de janeiro de 2011 só poderá ser excluída caso o período de cálculo seja janeiro/2011.
* Ocorrências com data anterior a última realizada: ao excluir uma ocorrência deve-se verificar a existência de ocorrências realizadas posteriormente a mesma. A exclusão deverá ser realizada respeitando a data considerando sempre a última ocorrência.

**Exemplo**

O patrimônio 01.01.001 possui 2 ocorrências, um acréscimo no dia 01/02/2011 e uma baixa parcial no dia 03/04/2011. Nesta situação a ocorrência a ser excluída é a baixa parcial, visto que foi a última realizada no patrimônio. Lembrando que o período de cálculo deverá estar em Abril/2011.

**Realizando o processo de exclusão**

Existem duas maneiras de executar o processo de exclusão de ocorrências: a partir da visão de ocorrências realizadas (Operações Patrimoniais/Consulta de Ocorrências) e também pela visão de patrimônios cadastrados (em Anexos).

Na visão de ocorrências realizadas serão exibidas todas as informações referentes as ocorrências, tais como data, valor, tipo (baixa, acréscimo ou transferência monetária). Ao identificar qual ocorrência será excluída deve-se selecioná-la e escolher a opção "Exclusão de ocorrências" em "Processos".

Para a exclusão da ocorrência a partir da tela de visão de patrimônios cadastrados deve-se selecionar o patrimônio desejado, acessar a aba responsável pelas ocorrências e escolher a opção "Exclusão de ocorrências" em "Processos".

Após a execução, com sucesso, do processo as informações contidas na visão de ocorrências realizadas serão excluídas e os valores (em moeda e índice) do(s) patrimônio(s) envolvido(s) serão atualizados, voltando ao último estado antes da ocorrência. Estes valores poderão ser verificados a partir do cálculo razão (na visão de patrimônios).

**Log**

Após cada execução do processo de exclusão de ocorrências será gerado um log contendo todas as informações referentes ao processo. Também serão exibidas as mensagens referentes as validações caso não sejam respeitadas as regras para realização da exclusão. Estas mensagens trarão quais pontos devem ser verificados e, caso necessário, corrigidos a fim de permitir que o processo seja realizado com sucesso.

Veja Também

* Consulta de Ocorrências
