---
article_id: 360052668693
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 57867eff67b886b24bf4872266c08b3484a5a6d52f2a3c102f8d99ab6d1fe1ba
fetched_at: '2026-06-28T22:45:21.080391+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Totalizador - O Totalizador não é retornado
  para o TAF
type: support-article
updated_at: '2026-06-26T12:14:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052668693-RH-Linha-Protheus-TAF-eSocial-Totalizador-O-Totalizador-n%C3%A3o-%C3%A9-retornado-para-o-TAF
---

**Dúvida**

Ao enviar os eventos para o Governo e gerar o Totalizador, o mesmo não é retornado os valores do RET. Este artigo orienta a gerar o console com aos detalhes do problema do retorno dos valores para o relatório de comparação.

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Totalizador - Todas as versões.

**Solução**

1 - Pare o serviço do TAF;

2 - Acesse o diretório de instalação a pasta **bin/appserver** e delete os arquivos **.log** e **.bak**;

3 - Abra o arquivo **appserver.ini** em qualquer editor de texto e adicione uma linha na seção general com a chave **tafconout=1** conforme o exemplo abaixo:

**[General]**

PowerSchemeShowUpgradeSuggestion=0

InstallPath=C:\Ambiente\Bases-TAF\_e\_TSS\TAFconsolelog=1

Segmento=YddTQHWW=VZF=yhu

Serie===AV

MaxStringSize=50

BUILDKILLUSERS=1

**TAFCONOUT=1**

4 - Salve o arquivo .ini, inicie o serviço do TAF

5 - Acesse a rotina de reavaliar totalizadores

[RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Reavaliar Totalizadores, como utilizar a rotina.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17496282095127)  
  
6. Execute a rotina no período que está com problemas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24236160231831)

6 - Após término do processo, encaminhe o arquivo **conosole.log** atualizado localizado na pasta **bin/appserver**.

\*\*  É recomendado que após o envio do **console.log** o**tafconout** seja desabilitado pois ele impacta na performance do sistema.
