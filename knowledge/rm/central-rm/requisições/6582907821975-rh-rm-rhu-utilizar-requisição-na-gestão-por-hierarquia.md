---
article_id: 6582907821975
category: Requisições
content_hash: dff5ea94426bd89efa82cd9c308718d42c93fc94818f81b016b60ecaa00b00e0
fetched_at: '2026-06-28T22:47:25.344353+00:00'
product: rm
section_id: 1500000861382
source: central-rm
title: RH - RM - RHU - Utilizar requisição na gestão por hierarquia
type: support-article
updated_at: '2026-05-29T21:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6582907821975-RH-RM-RHU-Utilizar-requisi%C3%A7%C3%A3o-na-gest%C3%A3o-por-hierarquia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15864107473943) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**

Como utilizar a requisição na gestão por hierarquia?

**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - 12.1.34 e superiores

**Solução**

Para utilizar a requisição, primeiramente é necessário acessar **Gestão de Pessoas | Configuração | Parametrizador | Gerenciamento de Hierarquia**e marcar o parâmetro da visão conforme necessidade:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40837723975575)

Caso selecione a opção **Usando integração com o Agilis**será utilizado o fluxo customizado ou padrão atual do sistema, de forma que, utilizando o fluxo padrão, será considerada toda a hierarquia até o seu ultimo nível como se fosse o cadastro de chefe e supervisores. Caso o fluxo seja customizado, será necessário validar a fórmula para alterar para os novos parâmetros. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40837706389783)

Quando utilizada a opção, **Não usando integração com o Agilis** será excluído o vínculo entre requisição e o fluxo de aprovação do Agilis e a partir deste momento, todo o processo de aprovação será controlado pelo Gestão de Pessoas. Após marcar esta flag, será necessário acessar Tipos de Requisição, editar as requisições que serão utilizadas e será neste momento apresentada uma visão um pouco diferente à anterior.  

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40837706390167)

As principais mudanças são, os campos de associação do Agilis que não estará mais disponível na visão e a aba **Ações dos níveis de Hierarquia para o Tipo de requisição**. Sobre a visão inicial do cadastro, a mesma é utilizada à nível cadastral, de forma que é informado o tipo de requisição, se ela está ativa, se há um relatório gerencial para a requisição e se há algum e-mail customizado para a requisição em questão.

Sobre a visão de **Ações dos níveis de Hierarquia para o Tipo de requisição**, nesta visão será feita a criação do fluxo a ser seguido pelas requisições, de forma que será identificado quais são os níveis que participaram da aprovação da requisição e quais são as ações que o mesmo pode tomar, por exemplo, todos os meus níveis irão participar do fluxo, mas somente o meu diretor poderá aprovar as requisições, com a alteração será possível realizar esta validação de acordo com o parâmetro marcado na visão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40837706390679)

**Alterações que ocorrem na visão de requisição após a ativação da gestão por hierarquia**

Quando se utiliza a gestão por hierarquia, as pessoas que estiverem em posições hierárquicas de níveis com Múltiplo vinculo não poderão abrir novas requisições que envolvam movimentação e alteração cadastral. Isto acontece, pois, a pessoa não será considerado um gestor e por não haver subordinados vinculados à posição da mesma, não há motivo para que o funcionário consiga solicitar contratação ou alteração de dados, somente o seu gestor poderá realizar esta solicitação.  
  
No campo Hierarquia Requisitante será listada todas as hierarquias associadas a este funcionário e será possível determinar qual a hierarquia que está fazendo a abertura desta requisição.  
  
Sobre a Hierarquia Destino, as hierarquias que serão apresentadas sempre serão as hierarquias inferiores à hierarquia que o requisitante está vinculado.  
  
**Obs:** Este campo apresentará as hierarquias únicas somente quando não houver pessoas vinculadas à esta posição, caso a hierarquia tenha uma pessoa vinculada, não será apresentada a hierarquia na lista de seleção.  
  
As opções de aprovação serão determinadas com base na opção selecionada dentro das ações no tipo de requisição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26792682004247)

**Saiba Mais**

Para maiores informações, acesse:

- [Ativação da Hierarquia Por Posição](https://tdn.totvs.com/pages/releaseview.action?pageId=653572529)
