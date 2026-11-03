---
content_hash: 0039d2699a4b140ecddf8e6b1f3f1cd64baab762f31a37f12610c7724009346b
fetched_at: '2026-06-29T00:08:06.207795+00:00'
page_id: '236588904'
product: rm
source: tdn-rm
title: ER_Mapa_de_Conhecimento_por_Nivel_de_Carreira
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Mapa_de_Conhecimento_por_Nivel_de_Carreira
version: 7
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | Acompanhamento RHU |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** |  | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | (x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

**Definição de Mapa de Conhecimento por requisito de acesso:**

* Utilizando tabelas salariais e seus níveis podemos definir o mapa de conhecimento por requisitos de acesso que detalha o que a empresa deseja ou exige de seus funcionários.
* No cadastro, o vínculo de Nível de Carreira serve para que o usuário possa selecionar a função, seção, tabela salarial e um nível.
* Função, Tabela e Nível têm preenchimento obrigatório;

**Definição de Mapa de Conhecimento por competência:**

* Utilizando tabelas salariais e seus níveis podemos definir o mapa de conhecimento por competências que detalha o que a empresa deseja ou exige de seus funcionários.
* No cadastro, o vínculo de Nível de Carreira serve para que o usuário possa selecionar a função, seção, tabela salarial e um nível.
* Função, Tabela e Nível têm preenchimento obrigatório;

Competências e requisitos são definidos por função ou por lotação a partir de níveis da tabela salarial em complemento a função ou a função de uma lotação.  
Essas funções são desdobradas em todos os locais que utilizam o mapeamento de competências como AD, PDI, painel de aprendizagem, etc.

Será disponibilizada uma opção para visualizar pessoas sem mapeamento de conhecimento, tanto por requisito quanto por competências.

Um menu exibe todas as pessoas que não possuem mapeamento de competência e de requisitos de acesso associado. Também é possível filtrar por nome, função e seção.

**Impactos AD:**

* Um parâmetro permite selecionar se o usuário deseja considerar mapeamentos por tabelas e nível na configuração. O sistema ajusta a montagem para tal objetivo e avalia se todos os outros anexos e processos estão adaptados a este modelo

Impactos Tabela Salarial:

* Não é permitido excluir níveis de tabelas que estão definidas no Mapa de Conhecimento. O sistema irá alertar caso isso aconteça.

## 

## Definição da Regra de Negócio

## Definição de Mapa de Conhecimento por competência

Como Analista de RH, eu preciso definir mapa de conhecimento por competências utilizando tabelas salariais e seus níveis para poder detalhar ainda mais o que a empresa deseja ou exige em termos de competências de seus funcionários pelo seu nível de carreira.

**Critérios:**

* No cadastro de definição de Mapa de Conhecimento por competência, criar o tipo de vinculo "Nível de Carreira", onde o usuário poderá selecionar função, seção, tabela salarial e um nível.
  + Função, Tabela e Nível têm preenchimento obrigatório. Seção é opcional.
  + Ao escolher função, o lookup de seções deve mostrar apenas seções de lotações existentes. Ao escolher seção, o lookup de funções deve mostrar apenas funções de lotações existentes (conforme comportamento do tipo de vínculo Lotação).
  + Após selecionar a função, se houver alguma tabela salarial associada, deve carregá-la automaticamente;
  + Só será possível informar um nível da tabela selecionada;
  + Será permitido informar tabelas não vinculadas a função selecionada, isso permite que o usuário já planeje suas competências antes de aplicar a tabela salarial
  + Só será permitido selecionar um nível da tabela salarial selecionada anteriormente
* O grid "Definições do Vinculo" presente na edição deverá considerar este novo tipo de vínculo.

## Definição de Mapa de Conhecimento por requisito de acesso

Como Analista de RH, eu preciso definir mapa de conhecimento por requisitos de acesso utilizando tabelas salariais e seus níveis para poder detalhar ainda mais o que a empresa deseja ou exige em termos de requisitos de acesso de seus funcionários pelo seu nível de carreira.

**Critérios:**

* No cadastro de definição de Mapa de Conhecimento por requisito de acesso, criar o tipo de vinculo "Nível de Carreira", onde o usuário poderá selecionar função, seção, tabela salarial e um nível.
  + Função, Tabela e Nível têm preenchimento obrigatório. Seção é opcional.
  + Ao escolher função, o lookup de seções deve mostrar apenas seções de lotações existentes. Ao escolher seção, o lookup de funções deve mostrar apenas funções de lotações existentes (conforme comportamento do tipo de vínculo Lotação).
  + Após selecionar a função, se houver alguma tabela salarial associada, deve carregá-la automaticamente;
  + Só será possível informar um nível da tabela selecionada;
  + Será permitido informar tabelas não vinculadas a função selecionada, isso permite que o usuário já planeje suas competências antes de aplicar a tabela salarial
  + Só será permitido selecionar um nível da tabela salarial selecionada anteriormente
* O grid "Definições do Vinculo" presente na edição deverá considerar este novo tipo de vínculo.

  Funcionários sem definição por req. Acesso

## Mapa de Conhecimento por Nível Carreira - Impactos AD

Como Analista de RH, eu preciso configurar uma AD que considere definições de mapa com níveis, para poder aplicar a AD conforme mapeamento de competências por nível.

**Critérios:**

* Necessário ter um novo parâmetro no processo de configuração da AD que me permita selecionar se desejo considerar mapeamentos por tabela e nível na configuração.
* Ao considerar tabela e nível, ajustar a montagem para tal objetivo
* Avaliar se todos os outros anexos e processos estarão adaptados a este novo modelo

## Unificação da leitura de Mapa de Conhecimento

Como Analista de RH, eu preciso que todos os locais do sistema que leiam Mapa de Conhecimento considerem o novo tipo de definição por tabela e nível para poder utilizar as funcionalidades sem impactos neste novo tipo de definição.

**Critérios:**

* Todo local que precisar ler definições de Mapa de Conhecimento por competência devem estar centralizados em um único módulo.
* Todo local que precisar ler definições de Mapa de Conhecimento por requisito devem estar centralizados em um único módulo.
* As seguintes funcionalidades precisam funcionar para o novo tipo de definição
  + Geração do PDI por Mapa de Conhecimento
  + Radar de competências do funcionário WIN
  + Radar de competências do funcionário WEB (merecimento de aumento)
  + Análise de potencial
  + Painel de aprendizagem
  + Mapa de conhecimento por Competência e por Requisito de Acesso
  + LNTD

## Impactos Tabela Salarial

Como Analista de RH, eu preciso ter ciência dos impactos nas alterações de tabelas, níveis e em suas vinculações para poder saber quando minhas alterações afetarem definições de Mapa de Conhecimento me ajudando na tomada de decisões.

**Critérios:**

* Não permitir excluir níveis de tabelas que estão definidas no Mapa de Conhecimento
* Alertar ao desativar níveis de tabela que estejam definidas no Mapa de Conhecimento. Atualmente é possível fazer pelo processo "Gerar Tabela Salarial"
* Alertar ao remover o vínculo de uma tabela/nível de uma função/lotação que tenha definição de Mapa de Conhecimento (Processo de vinculação de tabela salarial)

## Visualizar pessoas sem mapeamento

**Como** Analista de RH, eu preciso visualizar todas as pessoas que estão sem mapeamento de conhecimento, tanto de competências quanto de requisitos para poder avaliar e configurar mapeamentos se necessário

**Critérios:**

* Será criado um novo item de menu para exibir todas a pessoas que não possuem nenhum mapeamento de competência associado
* Será criado um novo item de menu para exibir todas a pessoas que não possuem nenhum mapeamento de requisitos de acesso associado.
* Deverá se possível filtrar por nome, função e seção.

## Remover menu de Mapa de Competências da MDI

Como Analista de RH, eu **não preciso** mais visualizar o menu de Mapa de Competências caso não existam itens cadastrados para poder ter uma visão simplificada de tarefas que impactam no meu trabalho.

**Critérios:**

* Caso não existam itens de mapa de competências cadastrados, não deve exibir o menu na MDI.
* Alterar o comportamento do assistente de conversão de mapa de competências para o mapa de conhecimento para que ao final, delete os mapas de competências convertido por completo

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
