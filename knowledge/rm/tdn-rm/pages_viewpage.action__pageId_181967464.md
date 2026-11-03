---
content_hash: 31c595b8a198f259cce0c855c7c0ce60e71e2c55c0b3f535825dc3a6a31d9b3a
fetched_at: '2026-06-29T00:05:57.789444+00:00'
page_id: '181967464'
product: rm
source: tdn-rm
title: RMFIN00004_Como avaliar seu Evento Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=181967464
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Gestão Financeira – **Versão:** 11.82 |
| **Processo** | : | Como avaliar seu Evento Contábil |
| **Subprocesso** | : | Eventos Contábeis |
| **Data da publicação** | : | 20/01/2015 |

**Introdução**

Este documento apresentará passo a passo como avaliar seu evento contábil quando houver diferenças de débito e crédito ou contabilizações nulas.   
  
  
**Principais Motivos para que o evento não carregue partidas contábeis**

Quando realizamos a parametrização de um evento contábil existem duas principais características que devem ser avaliadas durante a implementação de seu Item de Evento.   
Dentre elas, cito as mais importantes abaixo.

**IMPORTANTE:** Lembrando que para uma partida contábil ser carregada caso o valor do item e a origem da conta estejam retornando valor corretamente.

**1. Valor**

Quando realizamos a inclusão de um evento contábil devemos tomar conta de que o evento contábil pode ter seus valores carregador por fórmulas ou percentuais.

**IMPORTANTE:** Lembrando que ambas as opções necessárias, fórmula ou percentual, deve ser previamente analisada quanto a função que o evento contábil terá para realizar contabilizações.

**1.1 Fórmulas**

As fórmulas serão vinculadas para cada item de evento e podem receber várias funções e expressões sejam necessárias para a regra de negócio de sua empresa.   
Lembrando que as fórmulas podem possuir consultas SQL e até mesmo declaração de variáveis.   
Caso não possua conhecimento sobre o que uma fórmula faz o suporte do RM poderá lhe ajudar com esta dúvida pontual. Exemplo:

**1.2 Percentual**

O Evento Contábil pode possuir itens de evento parametrizados com percentual ao invés de serem parametrizados por fórmulas mais complexas.   
Isto dependerá do nível de complexidade de sua empresa e do cálculo que o deve ser realizado para carregar um valor contábil.

**IMPORTANTE:** Utilizar um valor percentual não significa que o mesmo será carregado em todas as ocasiões. O evento deve ser analisado como um todo.

**2. Conta Contábil**

**2.1 Informar Conta**

Quando utilizar dentro do Item de Evento o Campo Origem da Conta como "Informar Conta" significa que o sistema irá utilizar a conta contábil apontada independente de qualquer outra parametrização.

   
  
  
**2.2 Tabela Default**

Quando utilizar dentro do Item de Evento o Campo Origem da Conta como "Tabela Default" o sistema irá buscar as contas contábeis dentro dos defaults contábeis da tabela informada no campo "Buscar Default em".

 

Como exemplo podemos avaliar um Buscar Default em: **Filial**.   
O item de evento parametrizado para buscar default em Filial irá até o cadastro da Filial nos seus cadastros de Defaults Contábeis.

 

**2.3 Pontos Importantes a serem analisados:**

**2.3.1 "Obter Default de"**

Caso o item de Evento tenha o campo "Obter Default de" como Débito, o sistema irá buscar os dados contábeis das linhas de Débito do Default Contábil da Filial.   
O mesmo acontecerá para o campo "Obter Default de" como Crédito.

**2.3.2 "Classif. Conta"**

Caso o campo Classif. Conta esteja preenchido significa que o sistema irá validar a classificação do Item de Evento com a classificação do item de cadastrado nos defaults contábeis.   
Os dois campos devem possuir o mesmo valor conforme imagem abaixo. Caso diferentes não serão carregadas.

Para maiores informações:

[Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/default.aspx)

**COMUNIDADE** **[R@ Finanças](http://fluig.totvs.com/portal/p/10097/subject/rfinanas-community)**

**Canais** **de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Planejamento e Controle Orçamentário), 4 – (RM Fluxus).
