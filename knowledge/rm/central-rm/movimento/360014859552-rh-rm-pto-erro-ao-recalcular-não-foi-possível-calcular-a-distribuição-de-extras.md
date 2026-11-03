---
article_id: 360014859552
category: Movimento
content_hash: b5137f715aadae044ab0ab69267370fad10dd96701415468ce9d888b8343a766
fetched_at: '2026-06-28T22:46:36.082014+00:00'
product: rm
section_id: 1500000861602
source: central-rm
title: 'RH - RM - PTO - Erro ao recalcular: "Não foi possível calcular a distribuição
  de extras por período devido ao banco de horas está configurado como Diário!"'
type: support-article
updated_at: '2025-01-31T17:27:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014859552-RH-RM-PTO-Erro-ao-recalcular-N%C3%A3o-foi-poss%C3%ADvel-calcular-a-distribui%C3%A7%C3%A3o-de-extras-por-per%C3%ADodo-devido-ao-banco-de-horas-est%C3%A1-configurado-como-Di%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16814857351959) Tempo aproximado para leitura: 00:01:00 min**

**Ocorrência**No módulo **Automação de Ponto**, ao **recalcular** o funcionário, é apresentada mensagem 'Não foi possível calcular a distribuição de extras por período devido ao banco de horas está configurado como Diário!'  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Causa**   
Esse incidente ocorre, pois, a parametrização de **distribuição de extras** no parametrizador do funcionário está como **Período**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. No módulo de **Automação de Ponto acesse** o menu **Configurações | Parametrizador**. Selecione o processo Funcionários e avance. Selecione o funcionário desejado e clique no botão parametrizar e avance.  
   ![parametrizar_funcionario.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29658943924631)
2. Avance até a etapa a **Distribuição de Extras** e altere a distribuição de todos os tipos de extra para diário. Avance as demais etapas até concluir:  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29658932319511)
3. Outra de forma de acessar o parametrizador e através da visão do espelho de ponto do funcionário. Acesse a visão do espelho de Ponto e clique na opção Processos | Parametrizar Funcionário, e avance até a etapa **Distribuição de Extras.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29658932321175)**
4. Após as parametrizações, poderá executar o processo de **recálculo** normalmente.

**Saiba mais:**Para realizar a alteração de forma global acesse o artigo abaixo:  
[RH - RM - PTO - Alteração global de parâmetros dos funcionários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019945111)  
[Distribuição de Extras](https://tdn.totvs.com/pages/releaseview.action?pageId=452719119)
