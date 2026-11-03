---
article_id: 360037440994
category: Comércio Exterior - Easy Siscoserv - Importação
content_hash: 3b53641ac4cd09bf2362316e45863059bf81afbca2ba31a14c8b66396384ea5b
fetched_at: '2026-06-28T22:39:39.599125+00:00'
product: protheus
section_id: 1500001538321
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAESS - Gravação do Campo
  EEQ_FINNUM
type: support-article
updated_at: '2022-06-21T19:06:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037440994-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAESS-Grava%C3%A7%C3%A3o-do-Campo-EEQ-FINNUM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual Correta Parametrização para gravar o campo **EEQ\_FINNUM**?  
  
**Ambiente** Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Siscoserv – A partir da versão 11.80  
  
**Solução**Quando o parâmetro **MV\_CAMBFRE** está habilitado **'True'**, o título gerado no módulo Finaceiro, contas a pagar, é baixado pela rotina de câmbio no módulo **Easy Import Control**, logo não será gravado o número do título na tabela **EEQ** pois, ao liquidar o câmbio no Easy Import Control **'SWB'** o sistema baixa o título no contas a pagar **'SE2'** e registra a baixa no **Easy Siscoserv** **'EEQ'.**Quando o parâmetro **MV\_CAMBFRE** está desabilitado **'False'** a baixa do título gerado pelo **Easy Import Control** ocorre pelo módulo Financeiro, e desta forma o número do título gravado na tabela **EEQ 'EEQ\_FINNUM**' serve para o sistema rastrear o câmbio do **Easy Siscoserv** através da integração originada pelo módulo **SIGAFIN**. A gravação do campo **EEQ\_FINNUM** é uma necessidade técnica para este cenário.  
Concluindo, a não gravação da informação com os parâmetros **MV\_CAMBFRE**e **MV\_CAMBSEG** habilitados é um comportamento padrão do produto.
