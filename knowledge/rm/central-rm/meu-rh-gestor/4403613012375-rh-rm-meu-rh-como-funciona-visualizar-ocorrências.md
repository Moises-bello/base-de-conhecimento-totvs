---
article_id: 4403613012375
category: Meu RH - Gestor
content_hash: a35fb7ef6743a524322411b077506d36c63fd1c0e220459a711e008747c31b8c
fetched_at: '2026-06-28T22:47:32.408653+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RH - RM - Meu RH - Como funciona Visualizar ocorrências
type: support-article
updated_at: '2026-05-25T16:26:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403613012375-RH-RM-Meu-RH-Como-funciona-Visualizar-ocorr%C3%AAncias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22210327032087)**Tempo aproximado para leitura:**00:03:30 min**  
  
**Dúvida**  
Como gerenciar os atrasos e faltas do time no Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.2310  
  
**Solução**  
Ao acessar Gestor → Minha equipe → Aba Visualizar ocorrências no browser ou no Gestor → Visualizar ocorrências pelo mobile, serão carregados os eventos parametrizados como atrasos, faltas e horas extras dos colaboradores do time do período atual.  
  
Ao selecionar a opção "Visualizar as ocorrências" a partir da do item de menu "Gestor", o gestor poderá ter acesso as ocorrências da sua equipe.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22210727684759)

**Totalizador**

A partir das informações apresentadas em cada ocorrência, o totalizador trará as informações de:

* Quantidade de faltas: Para ocorrências de faltas, será apresentado o número total de faltas somando todas as ocorrências.
* Horas em atraso: Para ocorrências de atraso, será somado todo o seu valor de horas.
* Total de horas extras: Para ocorrências de hora extra e afins, será apresentado um valor total de horas extras das ocorrências.

Dentro da opção da Ocorrência existe o atalho com a possibilidade de solicitarmos abono, enviarmos atestado, pagar ou descontar, compensar, validar ou invalidar a ocorrência para o funcionário selecionado. Para melhor explicação referente ao objetivo de cada ação, no fim da desta página a uma tabela descritiva com o título de Ações das ocorrências.

![image2023-7-19_15-56-13.png](https://tdn.totvs.com/download/attachments/777932141/image2023-7-19_15-56-13.png?version=1&modificationDate=1689792973313&api=v2)

Para cada ação mencionada, há a opção de realizar a mesma em loteamento de funcionários, ou seja, realizar a ação para mais de uma ocorrência. Você consegue selecionar as ocorrências pelo campo de preenchimento ao lado da foto/nome e selecionando a ação necessária.

![](https://tdn.totvs.com/download/attachments/777932141/image2023-7-19_15-59-11.png?version=1&modificationDate=1689793152010&api=v2)![](https://tdn.totvs.com/download/attachments/777932141/image2023-7-19_15-59-34.png?version=1&modificationDate=1689793175700&api=v2)

**Observações**  
Validação e invalidação da ocorrência é para controle visual do gestor para identificação do que já foi tratado, não sendo obrigatória ou interferindo no cálculo.

* Os atrasos serão demonstrados pelo intervalo das ocorrências no dia e não um intervalo único devido a situações de mais de um atraso na mesma data.
* As ocorrências demonstradas são referentes a tabela AOCORRENCIACALCULADA, considerando os tipos de ocorrência: Hora extra normal, hora extra feriado, hora extra compensado, hora extra descanso, faltas e atrasos. Este comportamento é diferente do CorporeRM que hoje demonstra as ocorrências da tabela AJUSTFUN, desta forma será necessário realizar o recálculo do espelho de ponto dos colaboradores após realizar os ajustes das ocorrências, para que estes ajustes sejam refletidos também na tabela AJUSTFUN.
* A ação de validar/desvalidar ocorrências realiza a ação diretamente na tabela AJUSTFUN, como acontece hoje no CorporeRM;
* Ao acessar a tela de 'Visualizar Ocorrências' serão demonstradas ocorrências que estão compreendidas dentro do período de ponto, considerando para esta filtragem o campo 'Data da Jornada' que é correspondente ao campo 'DATAREFERENCIA' da tabela AOCORRENCIACALCULADA;
* As datas de inicio e fim da busca avançada realizam a busca nos campos: 'INICIO' e 'FIM' da tabela: AOCORRENCIACALCULADA;
* As ações das ocorrências e a solicitação de abono verificam o parâmetro: 'Bloqueia acesso aos cadastros do RM Portal', caso ele esteja marcado no grupo de quiosque do gestor, não será possível realizar as ações;
* Liberação a partir da versão: 12.1.2310.

**Saiba mais**  
[Para maiores informações sobre Visualizar ocorrências, clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=777932141)
