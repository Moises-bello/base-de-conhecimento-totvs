---
article_id: 1500008982442
category: TAF - eSocial - Rotinas comuns (Processamento, Monitoramento e Diagnóstico)
content_hash: 85a4cdba1009fd9d35cf9379dad99105dfe73a76aad46cc0c29a61d8a9a001db
fetched_at: '2026-06-28T22:45:21.117847+00:00'
product: protheus
section_id: 1500001536781
source: central-protheus
title: MP - TAF - CONFIGURAÇÃO MULTITREAD PROCESSAMENTO TAF
type: support-article
updated_at: '2021-04-30T20:25:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008982442-MP-TAF-CONFIGURA%C3%87%C3%83O-MULTITREAD-PROCESSAMENTO-TAF
---

**Dúvida**  
Como configurar multitread no processamento de integração do TAF?  
  
**Ambiente**  
Cross Segmento - Microsiga Protheus – TAF – A partir da versão 11.80  
  
**Solução**  
Para configurar a integração utilizando multithreads, configure os parâmetros abaixo:

1. Acesse **Configurador** os parâmetros:

**-** **MV\_TAFQTTH**: Define a quantidade de Threads utilizadas na integração TAF;

Exemplo: Caso o parâmetro **MV\_TAFQTTH** for igual a "5" e tenha 100 registros pendentes para o processamento da integração para a filial "01" do grupo de empresa "T1", o sistema divide a quantidade de registros para que as 5 threads configuradas processem 20 registros cada;

Utilizado junto com o parâmetro **MV\_TAFQPRC,** onde define a quantidade máxima de registros a serem consideradas para cada **thread**, caso o número de registros para cada **thread** for maior que a configurada neste **parâmetro**, será considerado a quantidade definida deste;

A divisão de registros para cada **thread** é por filial, ou seja, ao terminar o processamento de integração da filial "01", essas mesmas 5 **threads** serão utilizadas para processar a integração da filial "02", fazendo a mesma divisão de quantidade de registros por **thread;**

**- MV\_TAFQPRC:** Define Qtd de Registros no Processamento **TAFAINTEG**;

Quantidade máxima de registros que será considerada na query na integração **"Transferir registros da TAFST1** para **TAFST2"** e **"**Transferir registros da **TAFST2** para o **TAF";**

Exemplo: 

Se **MV\_TAFQPRC** = 1000, será considerado o processamento de no máximo 1000 registros (da TAFST1 ou **TAFST2** conforme integração executada) por **thread;**

Dividendo utilizado, por evento, no processo de **multiThread** Fiscal, na integração "Transferir registros da **TAFST2** para o **TAF";**

Exemplo:

**MV\_TAFLPRC** = 300;

**MV\_TAFQTTH** = 4;

Quantidade de registros T013 (Notas Fiscais): 2000;

Considerando os valores acima, se a quantidade de registros for maior que a quantidade das **threads**, o sistema irá realizar o rateio da seguinte forma;

1) dividir a quantidade de registros pela quantidade de threads: 2000 registros / 4 **threads** = 500 registros;

2) verificar se a quantidade de registros para cada **thread** é maior que o conteúdo do parâmetro **MV\_TAFLPRC**; 

Se a quantidade for maior que o parâmetro, automaticamente a quantidade de registros será utilizada do parâmetro, ou seja, será enviado 300 registros para cada **thread;**

Valor Default:= 2000;

Exceto para os layouts: "T087", "T088" e  "T010";

**Observação**: caso o parâmetro esteja configurado como 0 ou em branco, nenhum registro será enviado para a thread;

Mais informações no link abaixo:

https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=602829146
