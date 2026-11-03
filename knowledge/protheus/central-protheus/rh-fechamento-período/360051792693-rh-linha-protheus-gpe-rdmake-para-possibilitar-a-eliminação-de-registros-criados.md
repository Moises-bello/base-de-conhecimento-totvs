---
article_id: 360051792693
category: RH - Fechamento Período
content_hash: 717bd9b616630acded48729642050ce67414a5f91a57c5d50581bc2e4d8bdbca
fetched_at: '2026-06-28T22:43:24.496302+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: RH - Linha Protheus - GPE - Rdmake para possibilitar a eliminação de registros
  criados indevidamente da tabela SRF
type: support-article
updated_at: '2025-04-17T17:57:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051792693-RH-Linha-Protheus-GPE-Rdmake-para-possibilitar-a-elimina%C3%A7%C3%A3o-de-registros-criados-indevidamente-da-tabela-SRF
---

![relogio.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31453771431191) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Rdmake UPDSRFPRE para possibilitar a eliminação de registros criados indevidamente da tabela SRF.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Existia uma **não-conformidade na rotina de Fechamento (GPEM120)** que sob determinadas condições poderia gerar registros na tabela Controle Dias de Direito (SRF) com dados **posteriores ao período ativo da Folha de Pagamento.**

No Exemplo abaixo funcionário teve afastamento por doença com inicio em 12/07/2016 sem data retorno.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31490675402135)

Ao realizar o fechamento do período de 08/2019 sistema cria período aquisitivo de 16/06/2019 a 15/06/2020 com 10 dias proporcionais e situação ativo indevidamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31490675403415)

A rotina de Fechamento já foi corrigida para que não seja gerado nenhum período indevido nas condições citadas acima:  
  
Para que seja possível eliminar os registros que foram gerados indevidamente estamos disponibilizando o RDMAKE **UPDSRFPRE**. Por meio desta rotina o sistema irá verificar todos os registros da tabela Controle dias de Direito (SRF) das Filiais selecionadas e, caso exista registros cuja data inicial (RF\_DATABAS) seja posterior ao inicio do afastamento ele será excluído.  
  
Procedimento para **implantação**

O sistema é atualizado logo após a aplicação do pacote de atualizações *(Patch)* deste chamado e compilação do Rdmake anexo  
  
Procedimento para **configuração**

1.No **Configurador (SIGACFG),**acesse **Ambientes/Cadastro/Menu (CFGX013)**. Informe a nova opção de menu **SIGAGPE**, conforme instruções a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360080554893)

Procedimento para **utilização**

2.No módulo Gestão de Pessoal (SIGAGPE), acesse **Miscelânea / Fechamentos / Atualiza SRF (UPDSRFPRE)**.

O sistema apresenta a rotina UPDSRFPRE - Atualização dos dados da tabela SRF.

![](https://tdn.totvs.com/download/attachments/514429816/image2019-7-23_14-50-50.png?version=1&modificationDate=1567444651653&api=v2)

3.Clique em "Avançar" para que o sistema apresente a tela para seleção das Filiais que serão processadas.

![](https://tdn.totvs.com/download/attachments/514429816/image2019-7-23_14-51-26.png?version=1&modificationDate=1567444651543&api=v2)

4.Clique em **Avançar** para iniciar o processamento.

**Saiba Mais:**

[RDMKE - correção de registros criados indevidamente na tabela SRF](https://tdn.totvs.com/pages/viewpage.action?pageId=514429816)

[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
