---
article_id: 360033933633
category: eSocial - Gerar XML/ Integração Evento
content_hash: 8a0958e9403d4d3dacce0102a3c466ceefa436dea38debbf731ff6ba1bc9e712
fetched_at: '2026-06-28T22:47:13.194522+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RM - eSocial - O trabalhador devera encontrar-se ativo no período
type: support-article
updated_at: '2025-12-23T13:15:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033933633-RM-eSocial-O-trabalhador-devera-encontrar-se-ativo-no-per%C3%ADodo
---

**Dúvida**  
Como analisar o erro 317 "O trabalhador devera encontrar-se ativo no período" ao transmitir S-1200 de rescisão complementar?

**Ambiente**  
RM - eSocial - Todas as versões  
  
**Solução**  
Este erro ocorre quando é enviado um S-1200 para um funcionário demitido e no XML é gerado a tag **InforPerApur**. Esta tag indica que as informações apresentadas são referentes ao mês de apuração atual e como o funcionário se encontra demitido ocorrerá o erro. Para solucionar este incidente, execute os passos abaixo:

1. Acesse **Rescisão**| **Cancelamento** e cancele a rescisão complementar realizada  
2. Acesse **Rescisão**| **Complementar** e execute a rescisão complementar novamente  
3. Caso a empresa possua tomador de serviço realize a distribuição de SEFIP em **Encargos**| **SEFIP**| **Distribuir Sefip**  
4. Acesse **eSocial | Eventos Periódicos** egere o XML S-1200 novamente  
5. Abra o XML e verifique se foi gerada a tag **InfoPerApur**  
5.1. Caso não tenha gerado a tag **InfoPerApur**realize a transmissão do evento  
5.2. Caso tenha sido gerada, entre em contato com a central de suporte TOTVS

**Importante**  
Para funcionário demitido não é permitido lançamento de verbas manualmente no envelope, tais verbas deverão ser lançadas sempre através da rotina de rescisão complementar associando à um acordo coletivo cadastrado em **eSocial | Acordo Coletivo**. Caso contrário, o XML será gerado incorretamente para o funcionário demitido

**Saiba mais**   
Para mais informações sobre rescisão complementar, acesse:

* [Diferença Processo de Rescisão Complementar - Retificação de Rescisão e Acordo Coletivo](http://tdn.totvs.com/pages/viewpage.action?pageId=419535691)
* [RM - eSocial - Como informar ao eSocial as verbas geradas por dissídio em Rescisões Complementares ou Diferenças Salariais (Acordo Coletivo)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004806532-RM-eSocial-Como-informar-ao-eSocial-as-verbas-geradas-por-diss%C3%ADdio-em-Rescis%C3%B5es-Complementares-ou-Diferen%C3%A7as-Salariais-Acordo-Coletivo-?source=search)
