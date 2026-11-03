---
content_hash: ea1f2604db53e0b5bb3a2dd0916ec8ccaa96df85896e8770a59bee0d3da1acad
fetched_at: '2026-06-29T00:08:07.118175+00:00'
page_id: '236604455'
product: rm
source: tdn-rm
title: ER_Gestao_Hierarquia_Impactos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Gestao_Hierarquia_Impactos
version: 8
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | Gestão Organizacional |
| **Segmento Executor** | RM | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

## Objetivo

O objetivo deste projeto é definir um novo modelo de hierarquia a ser utilizado pelos sistemas de Recursos Humanos da Linha RM.  
O modelo tem como base a hierarquia de seções, porém permite maior flexibilidade para os clientes e melhor usabilidade para os usuários.  
A definição de chefes/subordinados utilizada pelos sistemas de RH passa a respeitar o modelo de posições.

## Definição da Regra de Negócio

**História:** RHUAGIL-116 Listagem de auxiliares no Portal

**Como:** Chefe de uma posição

**Eu Preciso:** Uma lista de auxiliares ativos para as posições que ocupo.

**Para conseguir:** visualizar e tomar ações relacionadas a auxiliares.

 

**Critérios de aceitação:**

* Deve haver uma lista dos auxiliares ativos para as posições que o chefe ocupa. Por meio da lista deve ser possível editar os registros de auxiliares.

**Tela:**

**História:** RHUAGIL-117Definição de auxiliar no Portal

**Como:** Chefe de uma posição

**Eu Preciso:** Ter a possibilidade de definir e editar auxiliares (funcionário ou externo), que poderão atuar como chefes auxiliares de minhas posições. Posso escolher para quais posições desejo atribuir o auxiliar e para qual período.

**Para conseguir:** delegar tarefas para auxiliares executarem na minha ausência ou simplesmente me auxiliando em minhas tarefas.

**Critérios de aceitação:**

* A partir da lista dos auxiliares ativos para as posições que o chefe ocupa, deve ser possível editar os registros de auxiliares.
* É possível editar o período de substituição. Alterando a Data Final o chefe pode finalizar a atuação do auxiliar.
* Na tela de inclusão deve haver uma lista das posições que o chefe ocupa, e onde podem ser selecionadas as posições que o participante indicado deve ser incluído como auxiliar. Pelo menos uma posição deve ser marcada para salvar o registro. Se tiver só uma posição, esta já deve vir marcada.
* Deve ser possível escolher um funcionário ou um externo. Só subordinados estarão disponíveis para serem escolhidos.
* É obrigatório informar o período. Data inicial deve ser menor ou igual a data final.
* O sistema gera um registro de auxiliar para cada posição marcada na tela. Nos registros gerados, além das informações exibidas na tela, o sistema grava o usuário responsável e o momento em que o auxiliar foi definido.

**Tela:**

**História:** RHUAGIL-170  Gerar cópia de Gestões por Posição

**Como:** Analista de RH

 **Eu preciso:** ter um assistente que permita criar cópias de uma Gestão por Posições e seu conteúdo. Criando uma cópia de gestão, posso iniciar um planejamento ou revisão da nova gestão sem impactar a gestão oficial. Em outro momento, se necessário, a nova gestão poderá tornar-se a gestão ativa.

 **Para conseguir:** Planejar uma Gestão por Posições antes de colocá-la em prática.

 **Critérios de aceitação:**

* O processo só pode ser acionado se uma única gestão estiver selecionada na visão de gestões.

* O usuário deverá informar o nome da nova gestão que será gerada. Além disso, O assistente deverá dar as seguintes opções ao usuário:
* Cópia de times: deve ser escolhida uma opção.
  + Copiar todos os times da gestão (marcado por padrão);
  + Copiar apenas os times que possuem participantes;
  + Nenhum.
* Cópia de posições: se a primeira opção for marcada, as duas seguintes estarão disponíveis.
  + Copiar as posições da gestão (marcado por padrão);
  + Copiar os líderes da posição (só pode ser marcado se a opção anterior estiver marcada) (marcado por padrão);
    - Copiar somente os líderes vigentes (habilitado somente se o usuário selecionar a opção de cópia dos líderes, se estiver marcado os líderes não vigentes não serão copiados para a nova Gestão a ser criada);
  + Copiar os vínculos de times com posições (só pode ser marcado se alguma cópia de times foi marcada e se o item “Copiar as posições da gestão” foi marcado) (marcado por padrão).
* O padrão de opções para abertura da tela é o que está definido no protótipo anexado.
* A execução do processo irá criar uma nova Gestão e copiará, além das informações básicas, os itens escolhidos entre as opções acima expostas.
* Não deve ser copiado o histórico de ativações da gestão.

**Tela:**

**História:** RHUAGIL-311 Processo de exclusão de gestão de hierarquia

**Como:** analista de RH

**Eu preciso:** excluir uma gestão de hierarquia não ativa independente se a mesma possui posições, times, lideres e etc vinculadas a ela.

**Para conseguir:** remover completamente e rapidamente uma gestão não utilizada.

**Critério de aceitação:**

* Garantir que todos os registros vinculados a gestão foram removidos.
* Garantir que a gestão foi removida.
* Não permitir que o processo seja executado se a gestão estiver ativa.
* Exibir numa etapa do processo a quantidade de times, posições lógicas, posições físicas e líderes existentes na gestão.

**Tela:**

**História:** RHUAGIL-314  Gestão de hierarquia multi-coligada

**Como:** analista de RH

**Eu preciso:** definir gestões de hierarquia que se relacionam entre as coligadas existentes.

**Para conseguir:** gerir a hierarquia de toda a empresa.

**Critérios de aceitação:**

* No cadastro de líder deve ser possível cadastrar líderes de qualquer coligada. Para isso deve ser incluído um lkp para a escolha da coligada antes dos lkps de funcionário e externo. Na inclusão, por padrão este lkp será carregado com a coligada corrente.
  + Todas as validações do cadastro de líder devem olhar para o campo codcoligadalider.

**Impactos em funcionalidades**

As seguintes funcionalidades dos produtos de RH foram adaptadas para, de acordo com a parametrização, utilizar a regra de hierarquia correta para a coligada:

* Processo de criação de atendente no RM Agilis
* Análise Salarial
* Inclusão de Metas no Portal
* Avaliação de Desempenho por Competências
* Organograma
* Envio de e-mail para Gestor no Mapa de Conhecimento e Análise de Potencial
* Visão de Subordinados
* Fluxo padrão de requisições
* Requisições – Winforms
* Requisições – Portal
* Cadastro de Anotação Pessoal - Winforms
* Aprovação de Batidas
* Saldo de Banco de Horas
* Aprovação de Batidas em Grupo
* Aprovar Abonos
* Encerrar liderança de um funcionário ao demitir o funcionário
* Gestão de Ferias
* Anexo de Funcionários Lotados na Seção
* Rotinas de chefia do Agilis (CRM)

 Em todos os pontos citados acima, o sistema irá validar se deve exibir chefe/subordinado de acordo com a regra de hierarquia por posições ou por seções, de acordo com a parametrização.

O comportamento interno dos itens não foi alterado.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
