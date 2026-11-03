---
article_id: 360028088012
category: PCO - Reprocessamentos
content_hash: d80636f6e14f5845dcd5041a371cb7a16850225881e4da8ef28b16352aea2ab4
fetched_at: '2026-06-28T22:37:07.014890+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA300 - Reprocessamento
  dos Saldos, Cubos Gerenciais.
type: support-article
updated_at: '2023-11-24T18:59:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028088012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA300-Reprocessamento-dos-Saldos-Cubos-Gerenciais
---

**Dúvida**

Como reprocessar o saldo dos movimentos no módulo PCO.  
  
**Ambiente**Protheus – Planejamento e Controle Orçamentário – A partir da versão 12  
  
**Solução**

O Objetivo da rotina é recalcular os saldos do dia a dia, até a data base do sistema conforme parâmetros.

O controle de saldos é feito pela tabela de saldos diários (AKT). No reprocessamento, o campo da AKT que informa onde a chave analítica é gravada, é o (AKT\_ANALIT).

A chave é gravada conforme a configuração do CUBO

Solicitamos cautela com o procedimento de recalculo, pois, dependendo do volume de movimentos este processamento poderá demorar muitas horas, então verificar previamente a viabilidade.

Com a instalação do pacote 13 de procedure (p12\_13.zsps), a rotina tem ganho de performance.

Execute a rotina de forma gradativa, por exemplo, reprocessar somente 5 dias, depois 10, 15, 30 dias, depois partir para 2 meses e assim por diante.

Para executar a rotina acessar:

SIGAPCO em Miscelânea/Reprocessamento/Cubos Gerenciais (PCOA300)

Defina os parâmetros conforme necessidade e execute.

**Importante** - *Possíveis erros podem ocorrer devido à inconsistência no cadastro do CUBO**, em caso de erro ao executar a rotina, criar um novo CUBO para teste, inclua um pequeno range nas entidades do CUBO e reprocessar pontualmente por tipo de saldo**,* *se o resultado for positivo reveja a configuração do CUBO em que ocorre o erro, permanecendo o erro entrar em contato o SUPORTE PROTHEUS através de um dos canais de atendimento.*
