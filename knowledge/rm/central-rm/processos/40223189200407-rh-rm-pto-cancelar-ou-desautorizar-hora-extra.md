---
article_id: 40223189200407
category: Processos
content_hash: e39bcec77797ab79f308dd24fcd84b9c7a7611ad159d0e7ef538f600aa5e9063
fetched_at: '2026-06-28T22:46:38.491593+00:00'
product: rm
section_id: 1500000861622
source: central-rm
title: RH - RM - PTO - Cancelar ou Desautorizar hora extra
type: support-article
updated_at: '2026-05-06T22:00:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40223189200407-RH-RM-PTO-Cancelar-ou-Desautorizar-hora-extra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40223181301015) Tempo aproximado para leitura: **00:01:45 min**  
  
**Ocorrência**  
Ao tentar realizar o processo de Cancelar/Desautorizar Extra Autorizada, o sistema finaliza com ressalvas informando que não foram encontradas extras autorizadas conforme a seleção de funcionários, ou o processo não surte efeito mesmo com extras visíveis no espelho.  
  
**Ambiente**  
RH - RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Causa**  
A mensagem de que não foram encontradas extras para cancelamento ocorre quando não existe o registro correspondente na tabela de extras autorizadas (AEAUTFUN). O processo de **Cancelar Extra Autorizada** aplica-se exclusivamente para funcionários que tiveram a autorização de extras executada por rotinas globais de autorização ou configuradas manualmente de forma individual diretamente no espelho.

Caso o funcionário possua a autorização configurada de forma nativa (ex: 24:00 horas diariamente definido no **Parametrizador do Funcionário** etapa **Extra**), não há um registro de autorização para ser cancelado pela rotina de cancelamento.  
  
**Solução**  
Para desautorizar horas extras em cenários onde a autorização é nativa ou quando o processo de cancelamento padrão não encontrar registros, siga as orientações abaixo:

1. Acesse em **Configurações | Parametrizador | Iniciais | Cálculo** e marque o parâmetro **Extra aprovada sobrepõe as extras parametrizadas para o funcionário**:

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40252489501847)
2. Após, acesse o menu **Processos | Autorização |** verifique as datas e a seleção de funcionários a serem considerados**,** marque o parâmetro **Extra Autorizada | Autorizar Extra** e no campo referente ao número de horas, informe o valor **00:00,** execute o processo**:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40252519219095)

Dessa forma, o sistema gravará uma autorização de 00:00 (zero horas), fazendo com que todas as extras calculadas para a data se tornem não autorizadas, após recalcular o espelho de ponto, será possível verificar no Resumo e também em Anexos | Extra Autorizada que o valor mostrará 00:00:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40252519219863)

**Saiba mais**

[Parâmetros do Cálculo](https://tdn.totvs.com/pages/releaseview.action?pageId=452719522)
