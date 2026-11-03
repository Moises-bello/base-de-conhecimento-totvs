---
article_id: 39419431020823
category: SIGAACD - Automação e Coleta de Dados
content_hash: 8f0425cd21241bbcccada0d17e0d5330a977dd1e7bc28829e38cedf05ec1d71b
fetched_at: '2026-06-28T22:39:13.926503+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD Automação e Coleta
  de Dados - Diferença entre a análise de inventário pelo coletor e pelo monitor (MV_ANAINV)
type: support-article
updated_at: '2026-03-31T15:44:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39419431020823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados-Diferen%C3%A7a-entre-a-an%C3%A1lise-de-invent%C3%A1rio-pelo-coletor-e-pelo-monitor-MV-ANAINV
---

O parâmetro MV\_ANAINV no TOTVS Protheus define a etapa de análise e encerramento da contagem de inventário. Com valor "1", a análise é feita pelo coletor, finalizando automaticamente a contagem. Com outro valor, a análise é feita pelo monitor, exigindo validação e acerto manual via rotina de monitoramento.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39419431011735) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Qual é a finalidade do parâmetro MV\_ANAINV e qual a diferença entre realizar a análise de inventário pelo coletor e pelo monitor?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAACD Automação e Coleta de Dados - Todas as versões

**Solução**

O parâmetro MV\_ANAINV define a etapa de análise e o encerramento da contagem do inventário no sistema. O comportamento varia conforme o conteúdo preenchido no parâmetro.

1. **Análise pelo Coletor (MV\_ANAINV configurado com "1")**

   O sistema exibe o status "Ativado para Coletor". Neste cenário, o inventário é finalizado (indicador visual azul) diretamente pela rotina de Gravação do Lançamento de Inventário (ACDA035 ou via coletor). Assim que a contagem é finalizada pelo operador, o registro sai automaticamente do status "1 - Em andamento" (indicador visual amarelo), aguardando apenas o acerto final.
2. **Análise pelo Monitor (MV\_ANAINV configurado com conteúdo diferente de "1")**

   O sistema entende que a análise está "Ativada para Monitor". Durante o uso da rotina de gravação pelo coletor (ACDA035), o processamento fica pendente. Para concluir o processo, um usuário deve acessar a rotina de Monitoramento do Inventário (ACDA032), clicar no botão "Gera Inventario(SB7)" e, após validar que não existem contagens em andamento, executar o acerto de inventário.

***Saiba Mais:***  
[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)

[*SIGAACD - Como é configurada a integração do SIGAACD?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016476392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-%C3%A9-configurada-a-integra%C3%A7%C3%A3o-do-SIGAACD-)
