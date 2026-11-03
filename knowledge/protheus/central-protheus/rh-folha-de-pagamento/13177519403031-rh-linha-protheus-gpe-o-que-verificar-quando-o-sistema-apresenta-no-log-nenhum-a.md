---
article_id: 13177519403031
category: RH - Folha de Pagamento
content_hash: 5a3625e35ef9e2b9d25ad2762a1d6a4f4bc948645072b5b124a43afb1fc3bb75
fetched_at: '2026-06-28T22:44:16.083575+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: 'RH - Linha Protheus - GPE - O que verificar quando o sistema apresenta no
  log: Nenhum agente de grid disponível no momento.'
type: support-article
updated_at: '2024-09-09T19:19:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13177519403031-RH-Linha-Protheus-GPE-O-que-verificar-quando-o-sistema-apresenta-no-log-Nenhum-agente-de-grid-dispon%C3%ADvel-no-momento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26236716924823) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**O que verificar quando o sistema apresenta no log: Nenhum agente de grid disponível no momento.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Causa**Esse incidente ocorre por alguma parametrização indevida ou por falta de atualização das rotinas do GPE.

1 - Configuração no appserver.ini (framework);

2 - Atualização das rotinas do GPE (Responsabilidade do módulo);  
3 - Configuração dos parâmetros (Configuração do módulo);  
4 - Processamento da rotina (realizado pelo módulo);  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

1. Parametrização do appserver.ini (framework) ; <https://tdn.totvs.com/display/public/framework/GridServer+-+Como+configurar>

Definição das pastas: Appserver e Slave 1;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13176803411223)

Definição do arquivo.ini do SERVER:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13175631554327)

Definição do arquivo.ini do SLAVE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13175707288215)

2. Certifique-se de que o ambiente está devidamente atualizado com o último pacote de expedição contínua e a lib disponíveis no portal do cliente:;

<https://suporte.totvs.com/portal/p/10098/download#000006/P2210/P2210AP/>

<https://suporte.totvs.com/portal/p/10098/download#000006/368/TFLIB/>

3. Verifique a definição dos parâmetros pertinentes ao módulo RH:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402890654999>

**MV\_GRID** - Indica se utilizará GRID no Cálculo da Folha **MV\_GPEGRID** - Caso MV\_GRID ativado, habilita rotinas p/ Grid: 1=Provisão, 2=Cálculo Folha/13o., em branco=Todas as opções **MV\_REGGRID** - Indica o numero de registros a serem processados por *Thread* no calculo com GRID  
**MV\_MINGRID** - Desliga o GRID automaticamente se o numero de funcionários a ser processado for menor que o numero definido neste parâmetro

A demonstração foi realizada com as seguintes definições:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13175933450903)

4. No processamento da rotina, suba o appserver do GridServer e do SlaveServer;

Analise se no appserver é apresentada a conexão conforme imagem abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13176139321751)

Após essa verificação já é possível rodar o cálculo da folha de pagamento através da rotina GPEM020:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13176176814999)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13176214836887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13176219655191)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13176433375895)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13176344620695)

Cálculo realizado com sucesso!

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
