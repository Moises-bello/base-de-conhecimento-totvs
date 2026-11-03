---
content_hash: b70a1e291710e8cc1764f8d2deb77b4152e50ed93dafcebf30f7521f5c8e1d08
fetched_at: '2026-06-29T00:06:09.578944+00:00'
page_id: '203755960'
product: rm
source: tdn-rm
title: ER_PCREQ-2600_Sincronizar_com_MS_Project
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-2600_Sincronizar_com_MS_Project
version: 16
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Sincronismo MS Project |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP008 | **IRM1** | PCREQ-2250 |
| **Requisito1** | PCREQ-2600 | **Subtarefa1** | PDR\_CP\_TOP008-142 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Este processo visa permitir que o usuário efetue o sincronismo de um arquivo do Microsoft Project com o projeto aberto no TOTVS Obras e Projetos. 

O processo de sincronismo é responsável por conciliar as informações do MS Project com as do projeto do TOTVS Obras e Projetos, atualizando suas informações, hierarquias, predecessões e recursos, tornando assim as informações das duas fontes de dados compatíveis, considerando possíveis restrições de regra de negócio.

## Definição da Regra de Negócio

O processo de sincronismo deve ser responsável por efetuar a correspondência entre as tarefas do MS Project e do TOTVS Obras e Projetos, identificando ações a serem tomadas para que as informações sejam completamente sincronizadas entre o projeto corrente no TOP e o arquivo do MS Project.

**RN001. Geração de arquivo vinculado**

A integração deve ser parametrizada com o vínculo a arquivo do MS Project, podendo definir o arquivo padrão através dos parâmetros do projeto.

Para que o sincronismo com o MS Project ocorra corretamente é aconselhável que o vínculo seja iniciado em uma das situações listadas abaixo:

          1 - O projeto do TOP com dados cadastrados e um arquivo do MS Project recém criado (sem modificações).   
          2 - Um arquivo do MS Project com dados cadastrados e o projeto do TOP recém criado (sem modificações).  
          3 - Iniciar o sincronismo com as duas fontes de dados (arquivo do MS Project e projeto no TOP) recém criados.

Este vínculo é efetuado através da execução do sincronismo inicial do projeto, assim preenchendo a tabela De-Para e adicionando no arquivo todos os dados referentes à base de dados do TOTVS Obras e Projetos ou vice-versa.

No primeiro sincronismo do arquivo do MS Project será atribuído a ele um identificador único, que será utilizado na composição da tabela De-Para e assim sendo é desaconselhável a duplicação ou cópia deste arquivo, pois os dois serão considerados como sendo um mesmo arquivo para o sincronismo.  
Os parâmetros de sincronismo serão também salvos no arquivo para que na próxima execução os mesmos sejam sugeridos ao usuário.

**RN002. Conciliação de tarefas**

A conciliação entre as tarefas do TOTVS Obras e Projetos e do MS Project será efetuada através de uma tabela de De-Para, que relaciona os registros a partir da chave da tarefa no TOP, chave única do arquivo e UID do registro no MS Project. A tabela será alimentada a cada sincronismo, não sendo necessária nenhuma iteração com a mesma a cada inclusão, alteração ou exclusão no TOP.

Durante a conciliação será identificada a ação original executada e a ação de sincronismo a executar seguindo as seguintes regras:

          1 - Registros existentes na base de dados do TOP, na tabela De-Para e no MS Project  
               **Ação Original:** Registro alterado em uma das extremidades  
               **Ação de Sincronismo:** Sincronizar os dados do registro nas duas extremidades, considerando o sistema parametrizado como mandatário.

          2 - Registros existentes na base de dados do TOP e não pertencem à tabela De-Para  
               **Ação Original:** Registro incluído no TOP  
               **Ação de Sincronismo:** Incluir registro no arquivo do MS Project 

          3 - Registros existentes no arquivo do MS Project e não pertencem à tabela De-Para  
               **Ação Original:** Registro incluído no MS Project  
               **Ação de Sincronismo:** Incluir registro no projeto do TOP 

          4 - Registros existentes na base de dados do TOP e na tabela De-Para, mas não no arquivo do MS Project  
               **Ação Original:** Registro excluído no MS Project   
               **Ação de Sincronismo:** Excluir registro no projeto do TOP 

          5 - Registros existentes no arquivo do MS Project e na tabela De-Para, mas não no TOP  
               **Ação Original:** Registro excluído no TOP  
               **Ação de Sincronismo:** Excluir registro no arquivo do MS Project

 

**RN003. Conciliação de recursos (insumos)**

A conciliação de insumos do TOTVS Obras e Projetos com os recursos do MS Project será efetuada através de uma tabela de De-Para, que relaciona os registros a partir da chave do insumo no TOP, chave única do arquivo e UID do registro no MS Project. A tabela será alimentada a cada sincronismo, não sendo necessária nenhuma iteração com a mesma a cada inclusão, alteração ou exclusão no TOP.

Durante a conciliação será identificada a ação original executada e a ação de sincronismo a executar seguindo as seguintes regras:

          1 - Registros existentes na base de dados do TOP, na tabela De-Para e no MS Project  
                **Ação Original:** Registro alterado em uma das extremidades  
                **Ação de Sincronismo:** Sincronizar os dados do registro nas duas extremidades, considerando o sistema parametrizado como mandatário.

          2 - Registros existentes na base de dados do TOP e não pertencem à tabela De-Para  
               **Ação Original:** Registro incluído no TOP  
               **Ação de Sincronismo:** Incluir registro no arquivo do MS Project 

          3 - Registros existentes no arquivo do MS Project e não pertencem à tabela De-Para  
               **Ação Original:** Registro incluído no MS Project  
               **Ação de Sincronismo:** Incluir registro no projeto do TOP 

          4 - Registros existentes na base de dados do TOP e na tabela De-Para, mas não no arquivo do MS Project  
               **Ação Original:** Registro excluído no MS Project   
               **Ação de Sincronismo:** Excluir registro no projeto do TOP 

          5 - Registros existentes no arquivo do MS Project e na tabela De-Para, mas não no TOP  
               **Ação Original:** Registro excluído no TOP  
               **Ação de Sincronismo:** Excluir registro no arquivo do MS Project 

**RN004. Conciliação de relacionamento de recursos / composições** 

Visto que o Microsoft Project não possui uma entidade equivalente às composições do TOTVS Obras e Projetos, mantendo somente as informações de relacionamento de recursos e tarefas, será seguido o algoritmo abaixo para conciliação do relacionamento de recursos (insumos ou composições).

**Algoritmo de conciliação** 

* + Número de recursos da tarefa igual a 0?
    - Inserir nulo nos campos de insumo e composição.
  + Número de recursos da tarefa igual a 1?
    - Insumo relacionado à tarefa igual ao recurso relacionados no MS Project?
      * Sim: Nenhuma ação
      * Não: Relacionar insumo na tarefa
  + Número de recursos da tarefa maior que 1?
    - Insumos da composição relacionada à tarefa são iguais aos recursos relacionados no MS Project (insumos e quantidades)?
      * Sim: Nenhuma ação
      * Não: Incluir nova composição

 

**RN005. Conciliação de dependências de tarefas (predecessoras e sucessoras)** 

Para o sincronismo serão consideradas as informações de tarefas predecessoras e sucessoras da fonte de dados conforme parâmetro de fonte de dados mandatária no sincronismo, assim desconsiderando ações efetuadas na outra fonte de dados no intervalo entre o ultimo sincronismo e o corrente.

**RN006. Atualizar o modelo de dados**

 

Durante a conciliação dos registros é utilizada a definição de relação de campos equivalentes entre o TOP e o MS Project listada na tabela abaixo para preencher o modelo de dados utilizado no sincronismo.  
Os campos marcados na tabela em laranjado serão parametrizáveis, permitindo que o usuário possa selecionar se deseja envia-los e para qual campo (de tipo de dado compatível) relacionar. Na tabela abaixo está representado o mapeamento padrão. 

**RN007. Conciliação de alteração hierárquica e impasses**

Seguindo a premissa do sistema mandatário, a hierarquia de tarefas será espelhada conforme dados extraídos da fonte de dados selecionada como mandatária.

Caso a inclusão de tarefas ou a alteração de hierarquia gere impasses, onde a tarefa é marcada como filha de uma etapa excluída ou marcada para exclusão, a mesma também será marcada para exclusão nas duas fontes de dados.

**RN008. Cálculo da curva ABC**

O sincronismo se baseia em dados calculados da curva ABC para a integração dos recursos (insumos e composições), sendo necessário realizar o cálculo do projeto através da opção existente no próprio processo.

---

**Importante:**

* **Caso hajam erros ao efetuar o download do arquivo sincronizado é importante que o usuário verifique o log de execução para identificar o status o sincronismo, pois esta etapa do processo não compartilha da mesma transação.**
  + Caso haja erro no download do arquivo o mesmo ficará desatualizado, devendo identificar se o mesmo poderá ser utilizado novamente em futuros sincronismos ou um novo arquivo deve ser gerado.
  + Exemplo: Caso o sincronismo seja efetuado corretamente mas o arquivo não seja retornado, o mesmo não será atualizado com o ID de execução utilizado para armazenar o relacionamento De-Para de registros. Ou seja, caso este arquivo seja sincronizado novamente os registros existentes no mesmo serão duplicados no TOP (o mesmo ocorre com registros existentes no TOP). Neste caso o aconselhado é que seja gerado um novo arquivo a partir do processo de sincronismo com o campo "Criar novo arquivo" marcado.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Sincronismo TOP X MS Project] | [Criação] | [Planejamento -> Integração com MS Project -> Sincronizar com o MS Project (Novo)] | - |
|  |  |  |  |

---

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

## 

---

## Regras de Integridade

* **Versão do Microsoft Project**  
  Compatível com a política de manutenção da Microsoft, esta nova funcionalidade será homologada a partir da versão 2007 do MS Project, não mantendo compatibilidade com versões anteriores

* **Manutenção do arquivo do MS Project**  
  O arquivo do Project deve ser gerado e sincronizado sempre utilizando esta rotina, conforme “RN001. Geração de arquivo vinculado”, pois as demais rotinas de integração com o MS Project não alimentarão a tabela De-Para conforme necessário.

* **Tipo de duração das tarefas**  
  Visando compatibilizar com o funcionamento do TOP o arquivo do MS Project será tratado sempre como “duração fixa”.

* **Tipo das tarefas sem recursos**  
  Tarefas integradas que não possuírem recursos serão marcadas como “Valor cotado” no TOP.

* **Parâmetros gerais e de projeto não utilizados no processo de sincronismo**

  Parâmetros de Projeto: Os parâmetros “Versão do Project” e “Criar recursos que não existirem na base de dados” são desconsiderados pelo novo processo de sincronismo.

  Parâmetros gerais: A visão de parametrização de equivalência de campos em sincronismo com MS Project apresenta mais campos do que os sincronizados no novo processo, sendo estes desconsiderados e não necessitando parametriza-los.
* **Equivalência de Campos**

  A parametrização de equivalência de campos é obtida a partir dos parâmetros gerais somente no primeiro sincronismo do arquivo, visto que a mesma é armazenada no arquivo (e obtida dele) para os próximos sincronismos e a disposição das colunas não será alterada.

* **Recalculo de EDT**  
  Caso existam códigos de tarefa repetidos em alguma das fontes de dados o mesmo será recalculado, considerando o primeiro na ordem de leitura como o válido e os próximos terão o seu último número recalculado.
* **Relacionamento de recursos em Obras e Etapas**  
  O MS Project possui comportamento diferente do TOTVS Obras e Projetos, permitindo relacionar recursos em tarefas do tipo *Sumary* (Etapas ou Obras do TOP).   
  Ao efetuar o sincronismo considerando o MS Project como mandatário a informação de recursos (insumos/composições) em Obras ou Etapas será enviada ao TOP mas o mesmo as desconsiderará, conforme sua própria regra de negócio, inserindo valor vazio nos respectivos campos, podendo assim tornar as duas fontes de dados com informações diferentes mas sem gerar nenhum impacto funcional.

## 

---

## Anexos

* **Conciliação automática – Exemplos**  
    
  Segue abaixo situações que exemplificam o funcionamento da conciliação automática em diversas situações e parametrizações.  
    
  **1. Tarefas existentes MS Project e não relacionadas a tarefa do TOP**  
    
  Esta simulação visa apresentar as ações tomadas em caso de exclusão de registros no TOTVS Obras e Projetos e em casos de inclusão de registros no MS Project.  
  Para as simulações de tarefas existentes no MS Project e não relacionadas a tarefa do TOP será utilizado como linha base as informações expostas na tabela abaixo.

             

* + **Simulação**  
    Após o primeiro sincronismo foram efetuadas a exclusão das tarefas com IdTrf iguais a 2, 3 e 4 no TOP e incluídas as tarefas com ID iguais a 1006 a 1010 no MS Project, resultando nas seguintes informações expostas abaixo:

                           

* + **Ações efetuadas**  
    Tabela de ações efetuadas nos dois sistemas no intervalo entre o ultimo sincronismo e o sincronismo corrente.

* + **Ações de sincronismo**  
    Tabela com ações a serem tomadas para efetuar o correto sincronismo dos dados.

* + **Resultado**  
    Tabela representativa dos dados no TOP e no MS Project após o sincronismo.**2. Tarefas existentes TOP e não relacionadas a tarefa do MS Project**
* Esta simulação visa apresentar as ações tomadas em caso de exclusão de registros no MS Project e em casos de inclusão de registros no TOTVS Obras e Projetos.
* Para as simulações de tarefas existentes no TOP e não relacionadas a tarefa do MS Project será utilizado como linha base as informações expostas na tabela abaixo.

 

* + **Simulação**  
    Após o primeiro sincronismo foi efetuada a inclusão das tarefas com IdTrf de 7 a 10 no TOP e excluídas as tarefas com ID iguais a 1002 e 1003 no MS Project, resultando nas seguintes informações expostas abaixo:
  + **Ações efetuadas**   
    Tabela de ações efetuadas nos dois sistemas no intervalo entre o ultimo sincronismo e o sincronismo corrente.

                           

* + **Ações de sincronismo**   
    Tabela com ações a serem tomadas para efetuar o correto sincronismo dos dados.

 

* + **Resultado**  
    Tabela representativa dos dados no TOP e no MS Project após o sincronismo.
* **3. Alteração hierárquica com inclusões e alterações simultâneas**
* Esta simulação visa apresentar as ações tomadas em caso de inclusão de registros e de alteração de hierarquia.
* Para a simulação das operações listadas será utilizado como linha base as informações expostas na tabela abaixo.

* + **Simulação**  

    Nesta simulação foram efetuadas as seguintes operações:

     
    - Exclusão da tarefa de IdTrf 3 no MS Project
    - Alteração hierárquica da tarefa de IdTrf 4 no MS Project – Passou a ser filha da nova tarefa criada (listada no item 5)
    - Inclusão da nova tarefa de ID 1006 no MS Project
    - Inclusão da nova tarefa de IdTrf 7 no TOP, após a exportação do MS Project.
    - Inclusão da nova tarefa de ID 1007 no MS ProjectApós a execução das operações listadas acima os dois sistemas resultaram nas seguintes informações expostas abaixo:

* + **Ações efetuadas**  
    Tabela de ações efetuadas nos dois sistemas no intervalo entre o ultimo sincronismo e o sincronismo corrente.
  + **Ações de sincronismo**

    Tabela com ações a serem tomadas para efetuar o correto sincronismo dos dados.
  + **Resultado**

    Tabela representativa dos dados no TOP e no MS Project após o sincronismo.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
