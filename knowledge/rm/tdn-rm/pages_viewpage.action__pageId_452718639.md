---
content_hash: 18a4903b7e61dd1328b7841cab9166c7ab044f86626907bd4268d9a875614a48
fetched_at: '2026-06-29T00:10:00.935684+00:00'
page_id: '452718639'
product: rm
source: tdn-rm
title: Montagem da Avaliação de Desempenho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718639
version: 2
---

**Montagem da Avaliação de Desempenho**

Processo responsável pela montagem da Avaliação, onde é possível selecionar as pessoas que serão avaliadas, vincular a cada uma um Grupo de Avaliação, determinar qual o tipo de Avaliação (características pessoais/critérios ou provas) e indicar para cada Grupo de Avaliado, seu Tipo de Avaliador, os Avaliadores de cada tipo e os Perfis vinculados.

Montagem da Avaliação **sem** integração com o Totvs Avaliação e Pesquisa (RM Testis)  
1) Executar o processo "Montagem da Avaliação de Desempenho".  
2) Selecione as pessoas que serão avaliadas e vincule a cada uma um Grupo de Avaliação.  
3) Determine qual o tipo da Avaliação de Desempenho: Avaliação por Características Pessoais/Critérios.  
4) Indique para cada Grupo de Avaliado, seus Tipo de Avaliador, os Avaliadores de cada tipo e os Perfis vinculados.  
5) Montagem da Avaliação finalizada.  
6) Executar o processo "Assistente de Lançamento Manual".  
7) Inserir os dados(notas) da avaliação: Avaliado, Tipo de Avaliador, Avaliador, Cód. Perfil e a Resposta a cada questão.  
8) Os lançamentos inseridos podem ser visualizados através do anexo "Mostrar resultado dos participantes".  
9) Após realizar o lançamento de todos os participantes avaliados, executar o processo "Fechar Avaliação de Desempenho".

Montagem da Avaliação **com** integração com o Totvs Avaliação e Pesquisa (RM Testis)

**Observação:**

A prova já deve estar criada no TOTVS Avaliação e Pesquisa, sendo esta do tipo "Conhecimento" com característica pessoal vinculada, período de execução definidos, ativa e com todas as questões vinculadas a ela.

1) Executar o processo "Montagem da Avaliação de Desempenho".

2) Selecione as pessoas que serão avaliadas e vincule a cada uma um Grupo de Avaliação.

3) Determine qual o tipo da Avaliação de Desempenho: Avaliação por Provas do RM Testis.

4) Indique para cada Grupo de Avaliado, os Perfis vinculados.

**Atenção:**

Quando o modelo for prova do Totvs Avaliação e Pesquisa, vinculamos apenas o perfil, pois o Avaliado é considerado também como Avaliador, tendo em vista que ele mesmo executa a prova e o resultado é dado individualmente.Desta forma não existe a necessidade da definição de tipos de avaliadores, quando se define que o modelo será avaliações por provas do Totvs Avaliação e Pesquisa.

5) Montagem da Avaliação finalizada.

6) Executar o processo "Exportar para o RM Avaliação e Pesquisa (RM Testis)".

7) A prova deve ser realizada, utilizando o Executor*. (maiores informações sobre a execução da Prova, consultar o help do produto Totvs Avaliação e Pesquisa)*

8) Executar o processo "Importar resultados do RM Avaliação e Pesquisa (RM Testis)".

9) Os lançamentos inseridos podem ser visualizados no anexo "Mostrar resultado dos participantes".

10) Executar o processo "Fechar Avaliação de Desempenho".
