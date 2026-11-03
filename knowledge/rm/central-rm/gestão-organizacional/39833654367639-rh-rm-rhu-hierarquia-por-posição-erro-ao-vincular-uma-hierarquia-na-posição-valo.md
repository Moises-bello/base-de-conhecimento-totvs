---
article_id: 39833654367639
category: Gestão organizacional
content_hash: 97584fffb1fbd7726c24d7b3c0c6ffd4014cd3465ee55d96417b24e15e9d9f6c
fetched_at: '2026-06-28T22:47:22.150077+00:00'
product: rm
section_id: 1500000861422
source: central-rm
title: 'RH - RM - RHU - Hierarquia por Posição: Erro ao vincular uma Hierarquia na
  Posição (Valor inválido para o campo "Hierarquia")'
type: support-article
updated_at: '2026-04-17T20:17:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39833654367639-RH-RM-RHU-Hierarquia-por-Posi%C3%A7%C3%A3o-Erro-ao-vincular-uma-Hierarquia-na-Posi%C3%A7%C3%A3o-Valor-inv%C3%A1lido-para-o-campo-Hierarquia
---

Tempo aproximado para leitura: **00:08:00 min**  
  
**Ocorrência**  
Ao vincular uma Hierarquia por meio do anexo de Hierarquias da Posição diretamente no cadastro da Posição a seguinte mensagem de erro é apresentada:

Valor inválido para o campo "Hierarquia".  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - 12.1.34 e superiores  
  
**Causa**  
A mensagem de erro em questão é apresentada pois possivelmente a Hierarquia (Nível Único) que desejam vincular já está sendo ocupada por outra Posição.  
  
**Solução**  
Acesse o cadastro da Hierarquia que deseja vincular na Posição e verifique se a mesma é de Nível Único ou Múltiplo. Caso a Hierarquia seja de Nível Múltiplo o sistema permitirá que ela seja vinculada em mais de uma Posição ao mesmo tempo.

![Hierarquia_Nível.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39833659418391)

Contudo supondo que a Hierarquia seja de Nível Único e já esteja vinculada a uma Posição, o sistema não permitirá que ela seja associada a outra Posição ativa ao mesmo tempo e a mensagem de erro **Valor inválido para o campo "Hierarquia"** será apresentada.

Para isso deverá inativar a Hierarquia na Posição de forma que a mesma possa ser vinculada a Posição desejada.

![Hierarquia_vincular_posicao.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/39833659419287)

**Saiba mais**  
Para maiores informações, acesse:

[RH - RM - RHU - Hierarquia por Posição: Vincular a posição à hierarquia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6572321447575-RH-RM-RHU-Hierarquia-por-Posi%C3%A7%C3%A3o-Vincular-a-posi%C3%A7%C3%A3o-%C3%A0-hierarquia)  
[RH - RM - RHU - Criar Nível de Hierarquia](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6302919055127-RH-RM-RHU-Criar-N%C3%ADvel-de-Hierarquia)
