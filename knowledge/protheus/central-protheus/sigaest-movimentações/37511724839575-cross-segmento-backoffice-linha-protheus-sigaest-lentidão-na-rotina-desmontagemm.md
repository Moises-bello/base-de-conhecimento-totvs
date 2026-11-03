---
article_id: 37511724839575
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 219291287b28c985854ce5a837d257ff549ac1eb80dd83d71cc800462d5fb82c
fetched_at: '2026-06-28T22:38:55.632934+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Lentidão na rotina
  Desmontagem(MATA242).
type: support-article
updated_at: '2026-01-07T20:04:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37511724839575-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Lentid%C3%A3o-na-rotina-Desmontagem-MATA242
---

A lentidão na rotina Desmontagem (MATA242) no TOTVS Protheus pode ocorrer devido a filtros para usuários com acesso a uma filial.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37511715143959) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**

Ao processar a rotina **Desmontagem (MATA242)** ocorre lentidão e/ou travamento na execução. **O que fazer para melhorar a performance ou impedir que a mesma conclua o processamento?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
A lentidão na rotina MATA242 pode estar relacionada ao fato de que usuários com acesso a apenas uma filial estão enfrentando demoras maiores na abertura da funcionalidade, possivelmente devido ao sistema realizar filtros dos dados a serem exibidos. Para abordar a questão de lentidão, recomenda-se:

**▸**Validar se o ambiente está atualizado com as últimas versões dos módulos e artefatos.

    Para atualizar estes artefatos, [clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596);

**▸** Aguardar o tempo médio de carregamento que era feito anteriormente.

**▸** Reiniciar os serviços do ambiente ou da máquina em questão, pois pode ser um problema relacionado à infraestrutura.

**▸**Encaminhar [**LogProfiler**](https://tdn.totvs.com/display/public/framework/LogProfiler+-+Como+executar)**e**[**Trace**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/MP%20-%20FIS%20-%20Como%20Gerar%20o%20Log%20DbTrace%20Para%20Monitorar%20Baixa%20Performance?)**do processamento da rotina MATA242.**

**▸**Recomendamos fortemente seguir [**estas dicas (clique aqui)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515552-MP-FRAME-Lentid%C3%A3o-no-Protheus-12) para ter um ganho de performance no processamento.

**▸**Atualização de DBAcess e esquecimento da atualização do dbapi.dll da sua pasta para ser atualizado na pasta do AppServer (detalhes em: [MP - FRAME - Arquivo dbapi.dll do DBAccess no AppServer)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028710652-MP-FRAME-Arquivo-dbapi-dll-do-DBAccess-no-AppServer?source=search);

**Caso, mesmo com as orientações acima não houver ganho de Performance, acione a Equipe de Suporte do módulo de Estoque/Custos encaminhando:**

**▸ Informações sobre tempo médio padrão do processamento e tempo médio atual;**

**▸** [**LogProfiler**](https://tdn.totvs.com/display/public/framework/LogProfiler+-+Como+executar)**e**[**Trace**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/MP%20-%20FIS%20-%20Como%20Gerar%20o%20Log%20DbTrace%20Para%20Monitorar%20Baixa%20Performance?)**do processamento da rotina MATA242.**

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
