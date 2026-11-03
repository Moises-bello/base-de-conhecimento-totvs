---
article_id: 11594542049559
category: SIGAEST - SALDOS
content_hash: 7c7d8c56d956780a187756cf247a39c55e53e43511efe72045c19f34f6c4df4d
fetched_at: '2026-06-28T22:39:14.877746+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Inconsistência de
  saldos gravados | Desbalanceamento entre Tabelas de Estoque
type: support-article
updated_at: '2026-03-26T20:53:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11594542049559-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Inconsist%C3%AAncia-de-saldos-gravados-Desbalanceamento-entre-Tabelas-de-Estoque
---

O artigo aborda divergências entre registros de movimentação e tabelas de saldo no TOTVS Protheus, recomendando a verificação com o relatório MATR282 para identificar inconsistências reais. Destaca a necessidade de mapear o processo que gera o erro para correção, sem solução pronta imediata. Sugere testes em ambiente padrão e atualizado, e orienta acionar o suporte com evidências para análise e possível correção sistêmica.

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16490619764631) Tempo aproximado para leitura: 00:05:00 min**

**Ocorrência**  
Os registros de movimentação do produto e as tabelas de saldo não conferem entre si.

Exemplo SB2 X SB8 X SBF X SD5 etc.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**

Primeiramente é importante conferir se de fato há um cenário de desbalanceamento, propriamente.

Há situações onde apenas não foram parametrizados os relatórios de forma compatível para o cenário, gerando a falsa impressão de haver desbalanceamento.

Recomendamos a extração do relatório MATR282 parametrizado como indicado no link a seguir para identificação de possíveis divergências reais de saldos entre as tabelas: [**SIGAEST - MATR282 - Parametrização para identificar divergência de saldos entre tabelas SB2 X SB8 X SBF**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF?source=search)

Caso demonstre, de fato, divergência de saldo entre as tabelas, verifique se está enquadrado em algum destes cenários:

* [Tratamento correto de desbalanceamento de tabelas de Lote e Endereço em todos os cenários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402491211159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Tratamento-correto-de-desbalanceamento-de-tabelas-de-Lote-e-Endere%C3%A7o-em-todos-os-cen%C3%A1rios?source=search)
* [Dicas de Analise de divergência de Saldo Atual/Posição de produtos com controle de Lote e Endereço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402435493271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Dicas-de-Analise-de-diverg%C3%AAncia-de-Saldo-Atual-Posi%C3%A7%C3%A3o-de-produtos-com-controle-de-Lote-e-Endere%C3%A7o?source=search)
* [Dicas de Analise de divergência de Saldo Atual/Posição de Saldo em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009601821)

Do contrário, atente-se às instruções a seguir.

**Solução**

A identificação de registros inconsistentes já gravados nas tabelas do sistema não permite, isoladamente, uma ação corretiva imediata no Produto Protheus ou através do Suporte Técnico.

Para que seja possível aplicar uma correção sistêmica, é imprescindível o mapeamento da rotina ou do processamento padrão que está originando a divergência. Em suma, precisamos identificar o fluxo operacional que resulta na falha sistêmica para que a correção seja aplicada na origem do cálculo.

Não há atualmente uma "correção pronta" específica para tal situação "processamento X gravar um saldo incorreto na tabela". No cenário comum os saldos demonstrados no sistema resultam de acordo com as diferentes formas de movimentações de entrada e saída padrão do sistema. Para uma possível correção é necessário sinalizar qual processamento estaria resultando em cálculo incorreto.

**Premissas para Análise e Correção:**

* **Validação em Ambiente de Teste:** Realize a simulação do processo habitual utilizando um produto novo, criado exclusivamente para esta análise, assegurando um histórico isento de resquícios de movimentações anteriores.
* **Simulação do Fluxo Operacional:** Reproduza as operações cotidianas (Notas de Entrada, Notas de Venda, Ordens de Produção, Transferências, Baixas de OS, Movimentações de Terceiros, etc.) até identificar em qual etapa a inconsistência de saldo é gerada.
* **Padronização do Ambiente:** O teste deve ocorrer em um ambiente atualizado e estritamente padrão (incluindo dicionários de dados). Isso é necessário para descartar falhas causadas por customizações ou obsolescência de fontes:
  + [Acumulado SIGAEST conforme sua versão](https://tdn.totvs.com/x/2hgdHw)
  + [LIB Atual](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/) -[Logo Guará](https://suporte.totvs.com/portal/p/10098/download?e=989259) | [Harpia](https://suporte.totvs.com/portal/p/10098/download?e=1050526)
  + [Appserver](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFAPP/) - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947528) | [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1031460)
  + Smartclient - [Lobo Guará](https://suporte.totvs.com/portal/p/10098/download#detail/947510) | [Harpia R.33](https://suporte.totvs.com/portal/p/10098/download#detail/1032341)
  + [DBAccess](https://suporte.totvs.com/portal/p/10098/download#000006/368/TFDBA/)
  + [Como desabilitar customizações no ambiente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292)

**Próximos Passos:**

* Assim que o cenário for identificado e o erro sistêmico for passível de reprodução, pedimos que acione o Suporte Protheus Estoque enviando:
  + As evidências detalhadas do processo (prints, logs ou vídeos).
  + A descrição das particularidades do cenário.

**Observação:** Uma vez que a inconsistência seja simulada e confirmada pelo suporte como uma falha do produto, será gerada uma solicitação de correção oficial. A partir disso, a equipe de Desenvolvimento avaliará a viabilidade de ferramentas para o ajuste dos dados históricos já afetados em seu banco de dados.

**Alternativas de Atendimento e Escopo Técnico**  
Caso a inconsistência identificada não tenha origem em uma falha padrão do produto — sendo motivada por customizações, manipulações diretas no banco de dados ou ambientes desatualizados — apresentamos as seguintes diretrizes:

1. **Correção de Registros e Dados (Serviços Tarifados)**

   Se o objetivo for exclusivamente a correção manual dos saldos nas tabelas (ajuste de dados), e não a investigação da rotina sistêmica, o atendimento deve ser direcionado a um canal de serviços, pois o Suporte Padrão **não realiza manipulação de dados em banco**, neste caso orientamos entrar em contato com o ESN responsavel por sua conta.
2. **Consultoria do Suporte (**[**Modalidades de Atendimento**](https://tdn.totvs.com/x/NOJeI)**)**

   Caso o erro seja reproduzido em seu ambiente de teste (atualizado e padrão), mas não seja replicado no ambiente interno da equipe de Suporte, disponibilizamos a modalidade de Consultoria do Suporte.

   **Objetivo:** Analisar o ambiente do cliente para identificar particularidades que impeçam a simulação do erro no ambiente do Suporte Técnico.

   **Pré-requisito:** Esta modalidade foca na rastreabilidade do erro sistêmico e **não se destina à correção manual de tabelas**. Sem a evidência do erro em ambiente padrão e atualizado, as equipes de Suporte e Desenvolvimento ficam impossibilitadas de atuar.

**Complementar / Material de apoio**

* [MATR282 - Parametrização para identificar divergência de saldos entre tabelas SB2 X SB8 X SBF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018463012-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR282-Parametriza%C3%A7%C3%A3o-para-identificar-diverg%C3%AAncia-de-saldos-entre-tabelas-SB2-X-SB8-X-SBF?source=search)
* [Tratamento correto de desbalanceamento de tabelas de Lote e Endereço em todos os cenários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402491211159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Tratamento-correto-de-desbalanceamento-de-tabelas-de-Lote-e-Endere%C3%A7o-em-todos-os-cen%C3%A1rios?source=search)
* [Dicas de Analise de divergência de Saldo Atual/Posição de produtos com controle de Lote e Endereço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402435493271-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Dicas-de-Analise-de-diverg%C3%AAncia-de-Saldo-Atual-Posi%C3%A7%C3%A3o-de-produtos-com-controle-de-Lote-e-Endere%C3%A7o?source=search)
* [Dicas de Analise de divergência de Saldo Atual/Posição de Saldo em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009601821)
* [Dicas de Análise dos Saldos no Relatório MATR460 (P7)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061829673-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Dicas-de-An%C3%A1lise-dos-Saldos-no-Relat%C3%B3rio-MATR460-P7-?source=search)
* [MATR460 (P7) - Saldo físico em Estoque Próprio negativo/divergente. O que fazer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001933381-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-P7-Saldo-f%C3%ADsico-em-Estoque-Pr%C3%B3prio-negativo-divergente-O-que-fazer-?source=search)
* [MATR460 (P7) - Saldo em Estoque De/Em Terceiros negativo/divergente. O que fazer?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002037442)
* [WEBINAR sobre controle de RASTRO e LOCALIZAÇÃO](https://www.youtube.com/watch?v=gnVIMBPaYo4)

**Saiba mais:**

[*Mais artigos sobre Saldos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538801-SIGAEST-SALDOS)
