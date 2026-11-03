---
article_id: 360059556733
category: MDT - EPI
content_hash: 72754453a3bfb70a802a65e421fbe11fe48a35c77d558c3031b95d45dffc3291
fetched_at: '2026-06-28T22:44:25.495385+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Para que server a rotina Histórico de EPI (MDTA696)
  e como incluir
type: support-article
updated_at: '2025-03-12T18:54:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059556733-RH-Linha-Protheus-MDT-Para-que-server-a-rotina-Hist%C3%B3rico-de-EPI-MDTA696-e-como-incluir
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25627955569175)** Tempo aproximado para leitura:**00:02:00 min****Dúvida**Para que server a rotina Histórico de EPI (Equipamento de Proteção Individual) (MDTA696) e como incluir?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**A rotina **Histórico de EPI** (Equipamento de Proteção Individual) (MDTA696) permite verificar e ajustar as entregas de EPI, que por algum motivo não foram lançadas corretamente em sua data. A rotina possui a mesma interface da rotina de **Funcionários x EPI** (MDTA695), o que facilita a utilização. Esta rotina não realiza **movimentação no estoque** após efetuar a gravação do histórico das entregas de EPI. É possível apenas realizar entregas com data menor do que a data atual.  
  
Por meio do parâmetro **"MV\_NG2U696**" é possível configurar os usuários que terão acesso a rotina de Histórico de EPI's.

1. Para cadastrar acessar rotina primeiro verifique no modulo **Configurador** (SIGACFG) se o usuário que vai acessar a rotina está habilitado, acessando o parâmetro **MV\_NG2U69** através do caminho ambiente > cadastro > parâmetros.  
Exemplo:  
  
![MV_NG2U69.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360097879894)  
  
2. Após esse processo acesse no modulo SIGAMDT (35) o caminho: atualizações > miscelânea > histórico > **Histórico de EPI** (MDTA696). Escolha o trabalhador, e clique em Histórico, para incluir o **EPI**.  
  
![hist._epi.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360097882554)  
 **Observação**  
Caso não seja definido o usuário no parâmetro **MV\_NG2U696** ao acessar a rotina **Histórico de EPI (MDTA696)** será apresentada a tela abaixo.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100148733)  
 **Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
