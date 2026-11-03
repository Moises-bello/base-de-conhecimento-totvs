---
article_id: 20836978162839
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: cf581e673cd046b569541ea57c08568d04b699679c7924e68de3325b68f0c9f0
fetched_at: '2026-06-28T22:37:49.290309+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) -SIGAFIN - FINA713 - Nome do
  Boleto Gerado ao efetuar o download pelo Novo Gestor Financeiro
type: support-article
updated_at: '2024-10-08T17:22:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20836978162839-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Nome-do-Boleto-Gerado-ao-efetuar-o-download-pelo-Novo-Gestor-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20836930619543) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como é gerado o nome do Boleto enviado via API - **FINA713 - Boleto Online** ?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20836978124311)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Solução**O nome do boleto é gerado pela função **Seconds()** que retorna um valor que representa o número de segundos, decorridos desde a meia-noite, conforme a hora atual do sistema, para o nome do boleto.   
**-- <https://tdn.totvs.com/pages/releaseview.action?pageId=24347077>**  
  
Caso deseje mudar o nome do Boleto, temos pontos de entrada disponíveis para a ação, segue abaixo   
**-- [NGFBXBOL – Permite o download do boleto em PDF dos boletos personalizados.](https://tdn.totvs.com/pages/releaseview.action?pageId=692920438)**

**Importante**Como é gerado o nome do arquivo quando é gravado no diretório spool/boletos

Segue um exemplo de arquivos gerados no diretório spool

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26920942518423)

Segue como foi gerado o Json do retorno do banco

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26920942521495)**

O arquivo será criado com o nome seguindo o formato abaixo:

**banco + numeroInscricao(cpf) + função Randomize() + função time()**<https://tdn.totvs.com/display/tec/Randomize>  
<https://tdn.totvs.com/display/public/framework/Time>Utilizando o print acima, ficaria **banco + numeroInscricao(cpf) + função Randomize() + função time() HHMMSS  
001+74910037000193+867+10h:47m:28s  
001+74910037000193+677+10h:33m:57s  
  
  
Saiba mais**

[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/viewpage.action?pageId=612548392)

[JOB Transmissão e Envio de E-mail - FINA713](https://tdn.totvs.com/pages/viewpage.action?pageId=619130482)

[Novo Gestor Financeiro - (FINA710 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=611007335)
