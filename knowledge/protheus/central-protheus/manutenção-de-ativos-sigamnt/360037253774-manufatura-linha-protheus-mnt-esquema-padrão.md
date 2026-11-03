---
article_id: 360037253774
category: Manutenção de Ativos (SIGAMNT)
content_hash: 50a757854596a1ad52ce02e9325ae27f14a2458d1c472e328ee17e38cc4b82ad
fetched_at: '2026-06-28T22:42:33.163962+00:00'
product: protheus
section_id: 360012117993
source: central-protheus
title: Manufatura - Linha Protheus - MNT - Esquema Padrão
type: support-article
updated_at: '2021-07-05T19:04:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037253774-Manufatura-Linha-Protheus-MNT-Esquema-Padr%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Para que serve a rotina **Esquema Padrão - MNTA220**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Manutenção de Ativos (SIGAMNT) - Todas as versões  
  
**Solução**A rotina **MNTA220** serve para a montagem da **representação gráfica da estrutura de rodados de um veículo**. O usuário define as característica do gráfico da **família de veículo**. Este gráfico é utilizado sempre que for solicitada a representação dos **bens da Família**.  
  
O programa obriga a **compatibilidade da estrutura padrão** cadastrada através da rotina **Estrutura Padrão - MNTA095** com o gráfico definido. Quando da definição dos componentes do eixo, definir no sentido da direita para a esquerda do eixo.  
  
A rotina possui a opção de definir se deseja ou não, deixar um dos **eixos suspensos através do campo Eixo Susp?,** caso o eixo seja **suspenso**, em qualquer rotina que reporte contador, o usuário pode escolher se os bens com contador dependente do pai terão seus contadores atualizados ou não com o novo reporte de contador. O campo possui duas opções: **1=Sim** e **2=Não**, onde:  
 **1=Sim** - define que o eixo é suspenso e que o usuário pode escolher no momento de informar o contador pai. Exemplo: ao fazer um abastecimento manual. Se ele deseja ou não que o eixo, bens do eixo. sofra com o reporte de contador;  
**2=Não** - define que o eixo não é suspenso e não terá a opção de escolher se os bens do eixo sofrerão ou não no momento de informar o contador pai. Exemplo: ao fazer um abastecimento manual. Todos os bens do eixo sofrerão com o reporte de contador.
