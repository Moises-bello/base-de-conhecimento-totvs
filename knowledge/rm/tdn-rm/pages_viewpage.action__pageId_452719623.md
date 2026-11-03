---
content_hash: cd6e3d6d1865bd0714b33b85f4fa70559a306ed955f8f68807c087d16361cf2e
fetched_at: '2026-06-29T00:10:09.303373+00:00'
page_id: '452719623'
product: rm
source: tdn-rm
title: Inicializar Gestão por Quadrantes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719623
version: 2
---

**Inicializar Gestão por Quadrantes**

Quando no cadastro da Gestão por Quadrantes está marcado o campo "Utiliza participantes de Avaliações de Desempenho", este processo tem como objetivo verificar a nota potencial e resultado da avaliação de desempenho de cada avaliado e o colocará no respectivo quadrante de acordo com estas pontuações em relação as definições dos quadrantes.

Quando no cadastro da Gestão por Quadrantes está desmarcado o campo "Utiliza participantes de Avaliações de Desempenho", como não há nenhuma avaliação de desempenho associada à gestão, será aberta uma tela de gerência de configuração de participantes.

Nesta tela, poderão ser feitas as operações de adição/exclusão de avaliadores e avaliados, antes da execução do processo. Ao terminar a seleção o sistema fará normalmente as consistências que foram explicitadas acima e ao inicializar todos os participantes serão destinados ao quadrante padrão obrigatoriamente.

O processo Configurar Participantes é um recurso baseado no "Processo Modularizado de Montagem de Participantes", que fornece uma infraestrutura para criação e manipulação de estruturas hierárquicas de avaliadores e seus avaliados.

Após a inicialização da gestão o status da gestão passa de "Não iniciada" para "Iniciada".

**Atenção:**

Para saber mais informações sobre as funcionalidades disponibilizadas para as telas que utilizam a montagem modularizada, o help "Processo Modularizado de Montagem de Participantes" deve ser consultado.  
   
**Observações:**

- Caso não tenha sido definido nenhum quadrante padrão para a Gestão Por Quadrantes e  a gestão seja baseada em uma Avaliação de Desempenho, participantes que não tiverem pontuação ou que tiverem uma pontuação que não se enquadre em nenhum dos quadrantes definidos, estes serão desconsiderados de todo o processo.

- Durante a execução do processo serão realizadas as seguintes verificações:

Verificar se o somatório do percentual da curva de todos os quadrantes associados à gestão é igual a 100;

Verificar se os intervalos de pontuação de todos os quadrantes associados à gestão não entram em conflito;

Verificar se as ordenações de todos os quadrantes não estão em conflito;

Caso seja definido que a gestão é orientada por potencial e resultado, é verificado se os 4 tipos de quadrantes foram definidos corretamente. Caso não sejam cumpridas todas as consistências, a Gestão Por Quadrantes não será inicializada e disponibilizada para uso no Totvs Portal.
