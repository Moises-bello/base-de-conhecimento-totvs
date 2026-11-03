---
article_id: 360052230814
category: RH - FGTS / SEFIP
content_hash: feced48e84625165e989109a3ecb51dd85eab89ed2cdbeccf7bea5d4b2d86bbf
fetched_at: '2026-06-28T22:43:41.437254+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - O que verificar quando é gerado no validador SEFIP
  o erro 130391
type: support-article
updated_at: '2025-08-14T18:28:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052230814-RH-Linha-Protheus-GPE-O-que-verificar-quando-%C3%A9-gerado-no-validador-SEFIP-o-erro-130391
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34187278707991) Tempo aproximado para leitura: 00:01:30 min**  
**Dúvida**O que verificar quando é gerado no validador SEFIP o erro 130391- CÓDIGO DE IDENTIFICAÇÃO DA EMPRESA NA CAIXA INVÁLIDO?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**

Caso opte por informar o código da empresa na Caixa conforme instruções abaixo, o mesmo deverá estar correto pois é validado durante a importação do arquivo sefip.re podendo gerar inconsistência no validador.

1 - A primeira verificação que o sistema realiza para preenchimento do código de identificação da empresa na caixa é pelo parâmetro de geração da SEFIP através da rotina GPEM610.

![](https://tdn.totvs.com/download/attachments/359467009/image2018-5-3_13-13-4.png?version=1&modificationDate=1525364276000&api=v2)

2 - Caso o campo acima esteja em branco o sistema buscará este código da tabela S037 conforme imagem abaixo:

![](https://tdn.totvs.com/download/attachments/359467009/image2018-5-3_13-9-48.png?version=1&modificationDate=1525364276000&api=v2)

3 - Se o campo acima também estiver em branco o sistema não levará nenhum código para o arquivo sefip.re. e também não gerará divergência durante a importação, pois este código é opcional para o envio das informações.

**Saiba mais:**

[RH \_ FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
