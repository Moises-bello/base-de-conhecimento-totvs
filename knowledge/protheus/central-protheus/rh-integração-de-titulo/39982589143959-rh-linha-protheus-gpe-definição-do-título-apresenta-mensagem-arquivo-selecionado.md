---
article_id: 39982589143959
category: RH - Integração de Titulo
content_hash: cbfe98f313d58082191b13f21dd53661a036e2f7d05901a3638cd4438b0decec
fetched_at: '2026-06-28T22:43:37.176158+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Definição do Título apresenta mensagem Arquivo
  selecionado é Invalido, Selecione uma das tabelas Permitidas
type: support-article
updated_at: '2026-04-24T13:43:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39982589143959-RH-Linha-Protheus-GPE-Defini%C3%A7%C3%A3o-do-T%C3%ADtulo-apresenta-mensagem-Arquivo-selecionado-%C3%A9-Invalido-Selecione-uma-das-tabelas-Permitidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39982589128471) Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Ao Incluir uma Definição de Título selecionando a opção "Definido por Usuário", quando incluída uma tabela é apresentada a mensagem  "Arquivo selecionado é Invalido, Selecione uma das tabelas Permitidas"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39982587041431)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Esta mensagem ocorre ao tentar incluir em "Informações para busca das verbas Selecionadas" uma tabela que não foi utilizada no cálculo da folha, como por exemplo a tabela SRK - Movimentos Futuros, que pode sofrer alterações ao processar a folha ou a tabela SRG - Cabeçalho de Rescisões, que não contém informações de Valores.

**Solução**  
As únicas tabelas que poderão ser inseridas nessa seleção são as tabelas **SRC**, **SRD**, **RGB** e **SRR**. Caso seja escolhido outro arquivo será exibida a mensagem acima, impedindo a criação da Definição do Título.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39982587041943)

**Saiba Mais:**

[Manual Integração de Títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=800586210)

[RH - Integração de Títulos](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
