---
article_id: 21797380856343
category: Meu RH - Gestor
content_hash: a9ed6593a3056168b01378a8a40ff3524f9c5dced59d95caadeb348a430492d6
fetched_at: '2026-06-28T22:47:32.342039+00:00'
product: rm
section_id: 1500000861742
source: central-rm
title: RM - RH - Meu RH - Como alterar a atitude das ocorrências de ponto
type: support-article
updated_at: '2026-03-28T20:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21797380856343-RM-RH-Meu-RH-Como-alterar-a-atitude-das-ocorr%C3%AAncias-de-ponto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21797349845399) Tempo aproximado para leitura: **00:05:40 min**  
  
**Dúvida**  
Como realizar a alteração da atitude das ocorrências de ponto no Meu RH para compensar, pagar ou descontar.

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir da versão 12.1.2310  
  
**Solução**  
Ao acessar no Meu RH o menu **Gestor** > **Minha equipe** > Aba **Visualizar ocorrências**, serão carregados os eventos parametrizados como atrasos, faltas e horas extras dos colaboradores do time do período atual.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21797349850775)

Dentro da opção da ocorrência existem atalhos que possibilitam **solicitar abono, enviar atestado, pagar ou descontar, compensar, validar ou invalidar** a ocorrência para o funcionário selecionado.

![image2023-7-19_15-56-13.png](https://tdn.totvs.com/download/attachments/777932141/image2023-7-19_15-56-13.png?version=1&modificationDate=1689792973313&api=v2)

**Observação**: O gestor não conseguirá inserir um texto no campo "**justificativa**"  no processo de alteração de atitude. A inclusão da justificativa é feita pelo próprio subordinado, através da rotina [Ocorrência](https://tdn.totvs.com/pages/viewpage.action?pageId=883056768) disponível no menu Ponto.

É possível realizar também a alteração em lote, basta marcar as ocorrências desejadas no campo esquerdo da foto/nome do colaborador, em seguida, selecione a ação necessária.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21797349853335)

Pela opção **Busca Avançada**, é possível filtrar os resultados utilizando as opções de Data Início/fim, Nome e Ocorrência. Para ocorrências há três opções: Falta, Atraso ou Hora extra.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21797380831255)

**Importante**:

* A validação e desvalidação da ocorrência é para controle visual do gestor para identificação do que já foi tratado, não sendo obrigatória ou interferindo no cálculo;
* A ação de validar/desvalidar ocorrências realiza a ação diretamente na tabela **AJUSTFUN**, como acontece hoje no CorporeRM;
* Ao acessar a tela de '**Visualizar Ocorrências**' serão demonstradas ocorrências que estão compreendidas dentro do período de ponto, considerando para esta filtragem o campo 'Data da Jornada' que é correspondente ao campo 'DATAREFERENCIA' da tabela **AOCORRENCIACALCULADA**;
* Os atrasos serão demonstrados pelo intervalo das ocorrências no dia e não um intervalo único devido a situações de mais de um atraso na mesma data;
* As ocorrências demonstradas são referentes a tabela **AOCORRENCIACALCULADA**, considerando os tipos de ocorrência: Hora extra normal, hora extra feriado, hora extra compensado, hora extra descanso, faltas e atrasos. Este comportamento é diferente do CorporeRM que hoje demonstra as ocorrências da tabela **AJUSTFUN**, desta forma será necessário realizar o recálculo do espelho de ponto dos colaboradores após realizar os ajustes das ocorrências, para que estes ajustes sejam refletidos também na tabela **AJUSTFUN**;
* As datas de inicio e fim da busca avançada realizam a busca nos campos: 'INICIO' e 'FIM' da tabela: **AOCORRENCIACALCULADA**;
* As ações das ocorrências e a solicitação de abono verificam o parâmetro: 'Bloqueia acesso aos cadastros do RM Portal', caso ele esteja marcado no grupo de quiosque do gestor, não será possível realizar as ações.

**Saiba Mais**  
[**TDN - Visualizar ocorrências**](https://tdn.totvs.com/pages/viewpage.action?pageId=777932141)
