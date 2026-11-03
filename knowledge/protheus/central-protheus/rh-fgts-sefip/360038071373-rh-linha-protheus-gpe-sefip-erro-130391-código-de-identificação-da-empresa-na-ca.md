---
article_id: 360038071373
category: RH - FGTS / SEFIP
content_hash: f8bb0fab378acd219b971915ae68231ae9ce93ac50f6b538e088ed487de23066
fetched_at: '2026-06-28T22:43:41.487183+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - SEFIP  Erro 130391  Código de Identificação da
  Empresa na Caixa inválido
type: support-article
updated_at: '2025-08-19T12:16:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038071373-RH-Linha-Protheus-GPE-SEFIP-Erro-130391-C%C3%B3digo-de-Identifica%C3%A7%C3%A3o-da-Empresa-na-Caixa-inv%C3%A1lido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34286259472151) Tempo aproximado para leitura: 00:01:30 min**

**Dúvida**Análise que deve ser realizada quando for apresentada a mensagem no validador SEFIP: "Erro 130391 - Código de identificação da empresa na caixa Inválido.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
**Solução**Caso opte por informar o código da empresa na Caixa conforme instruções abaixo:  
  
O código deverá estar correto, pois, é validado durante a importação do arquivo sefip.re podendo gerar inconsistência no validador.

1. A primeira verificação que o sistema realiza para preenchimento do código de identificação da empresa na caixa é pelo parâmetro de geração da SEFIP através da rotina GPEM610:![](https://tdn.totvs.com/download/attachments/359467009/image2018-5-3_13-13-4.png?version=1&modificationDate=1525364276000&api=v2)

2. Caso o campo acima esteja em branco, o sistema buscará este código da tabela S037 conforme imagem abaixo:![](https://tdn.totvs.com/download/attachments/359467009/image2018-5-3_13-9-48.png?version=1&modificationDate=1525364276000&api=v2)

3. Se o campo acima também estiver em branco o sistema não levará nenhum código para o arquivo sefip.re e também não gerará divergência durante a importação, pois este código é opcional para o envio das informações.

**Saiba mais:**

[RH - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
