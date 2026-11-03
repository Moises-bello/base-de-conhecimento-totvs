---
content_hash: 78c33250abe282fbc3bcbea1f6b72a75084904226eb85ca724fc14ebfe36d8d7
fetched_at: '2026-06-29T00:11:55.666609+00:00'
page_id: '862608096'
product: rm
source: tdn-rm
title: 1.2 - Histórico das Execuções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862608096
version: 32
---

## O que são?

Responsável por exibir todas as execuções das atividades que fazem parte dos Grupos que você tem acesso. Cada execução representa o resultado de uma atividade processada em um servidor específico dentro de um determinado ambiente. O sistema permite que o usuário visualize todas as execuções realizadas, aplique filtros específicos para encontrar registros de interesse, e acesse detalhes mais aprofundados sobre cada execução.

## Para que servem?

Esta funcionalidade é essencial para monitorar e gerenciar as atividades, fornecendo uma visão clara e centralizada do desempenho das execuções. Ao permitir a filtragem por diversos critérios, como versão, atividade, grupo de usuário, status da execução e servidor, o sistema facilita a identificação de problemas e o acompanhamento do progresso das atividades. Além disso, a possibilidade de acessar os detalhes de cada execução, incluindo logs e informações de erro, é crucial para a análise e resolução de falhas, garantindo a eficácia e a confiabilidade dos testes automatizados. O painel é especialmente útil para gerentes de projetos e desenvolvedores que precisam acompanhar o histórico de execuções e garantir que todas as atividades estejam sendo executadas conforme o esperado

## Exemplo de Uso

Exemplo de UsoVisualização

Inicialmente, será exibida uma tabela contendo o histórico de execuções de todos os projetos executados pelos usuários dos Grupos que você tem acesso.

Para acessar essa tela, basta navegar:**→ Gestão de Execução → Histórico de Execuções**

A tabela apresentará os seguintes campos:

* **Nome da Atividade**: O nome da atividade executada.
* **Status**: O estado atual ou final da atividade, podendo ser:
  + **Sucesso** : A atividade foi concluída com êxito.
  + **Falha** : A atividade não foi concluída com sucesso.
  + **Pendente**: A atividade ainda não iniciou sua execução.
  + **Executando** : A atividade está em processo de execução.
* **Data e Hora da Finalização**: O momento em que a atividade foi concluída.
* **Versão**: A versão da Atividade no momento da execução.
* **Servidor**: O servidor no qual a atividade foi executada.
Filtros

Para uma melhor visualização, é possível filtrar os dados de acordo com as seguintes opções:

Em todos os filtros, é possível selecionar mais de uma opção.

1. Versão

* **Versão**: Filtre pelas diversas versões de suas atividades.

2. Atividades

* **Atividades**: Filtre pelos nomes específicos de suas atividades para encontrar rapidamente um caso particular que você deseja visualizar ou editar.

3. Grupos

* **Grupos**: Filtre pelos grupos que associam à sua atividade.

4. Status

* **Status:** Filtre pelos Status de Execução

5. Servidores

* **Servidores:** Filtre pelas atividades que executaram em um determinado Servidor.

É possível remover todos os filtros aplicados na tabela clicando no ícone de **Limpar Filtros.**

Detalhes dos Logs

Para cada execução de uma atividade, é possível visualizar todos os seus detalhes. Basta clicar no ícone correspondente à execução desejada

Nessa tela, os detalhes de uma execução é dividida em duas sessões:

1. Cabeçalho da Execução

**1) Tipo de Atividade:** Indica o tipo de atividade executada (Projeto de teste, Código C#, Script SQL, etc..).

**2) Versão:** A versão da Atividade no momento da execução.

**3) Servidor:** O servidor no qual a atividade foi executada.

**4) Início da Execução:** O momento em que a execução da atividade foi iniciada.

**5) Fim da Execução:** O momento em que a execução da atividade foi concluída.

**6) Execução:**

* + **Projeto:** O status de um Projeto depende da conclusão de todas as Atividades a ele associadas. Se alguma Atividade apresentar erro, o status geral do Projeto será marcado como **Falha**. Atividades com status **Ignorado** não afetarão o status final do Projeto.
  + **Atividade:** O status de uma Atividade reflete diretamente seu resultado, sendo classificado como: **Sucesso** ou **Falha**.

**7) Testes:**

* + **Definição:** Um teste é uma Atividade que tem como objetivo comparar o Estado esperado com o Estado atual de um elemento após a execução de uma determinada ação. As atividades consideradas como testes são: **Comparação de Arquivos, Comparação de Diretório ou Comparação de Base**.
  + **Regra:** Com isso, existindo testes em seu projeto está informação será carregada de acordo com o status de todos eles. Se todos os testes forem executados sem problemas, o status será registrado como **Sucesso**. Caso algum teste apresente falha e seu status não seja ignorado, o status final será registrado como **Falha**.

**8) Executado por:** Indica qual usuário iniciou a execução dessa atividade.

**9) Atividades Executadas:** Aqui serão listadas todas as atividade executadas.

2. Detalhes do Cabeçalho da Execução

Nos detalhes do cabeçalho da Execução, é possível visualizar os seguintes itens:

1. **Passos:** Lista todos os passos da execução, incluindo o tempo gasto em cada um.
2. **Alertas:** Exibe todas as mensagens de alerta que foram disparadas durante a execução, se houver.
3. **Ambientes:** Detalha o diretório do RM onde a execução foi realizada, bem como os parâmetros definidos como variáveis de ambiente.
4. **Parâmetros:** Indica se a execução foi realizada na Continuous Testing ou na Cobertura Funcional.

5. **Diferenças:** Em atividades de comparação de diretórios ou bancos de dados, esta coluna estará disponível para visualização em casos de erro durante o teste. Ela detalha as comparações realizadas e seus respectivos resultados. Além disso, ao executar a atividade de Comparação de Diretórios, o usuário pode optar por exibir apenas os arquivos que diferem entre os diretórios ou visualizar o estado de todos os arquivos. Essa flexibilidade permite um maior controle na análise e compreensão das diferenças identificadas.

---

# Saiba mais

Os filtros oferecidos na tela não só permitem uma busca rápida por execuções específicas, mas também podem ser combinados para uma filtragem avançada. Por exemplo, você pode filtrar por uma versão em conjunto com um status de execução para localizar rapidamente os testes que falharam após uma atualização.

 Cada execução gera um log detalhado, incluindo mensagens de erro, alertas e outras informações relevantes.

# FAQ

**P: Como posso remover os filtros aplicados?**

R: Para remover os filtros, basta clicar no "X" localizado no final da barra de filtros.

**P: Como posso analisar diferenças em atividades de comparação?**

R: Nas atividades que envolvem comparação de diretórios ou bancos de dados, a tela de detalhes oferece uma coluna de diferenças que permite visualizar os resultados das comparações, destacando erros ou discrepâncias encontradas.

**P: Esta tela exibe todas as execuções ou apenas as mais recentes?**

R: A tela exibe todas as execuções realizadas pelo usuário, permitindo que você navegue e aplique filtros para encontrar execuções específicas.
