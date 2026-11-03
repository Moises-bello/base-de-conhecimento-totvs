---
article_id: 11617314650519
category: Gestão de Transportes (TMS)
content_hash: 738387b281611ce8bcf711bf5b119adc8da48ed9bbffe023952534901ea5035e
fetched_at: '2026-06-28T22:45:27.524184+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Componente Frete Despachante
type: support-article
updated_at: '2023-01-12T18:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11617314650519-Log%C3%ADstica-Linha-Protheus-TMS-Componente-Frete-Despachante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como funciona o componente **06 - Frete Despachante** no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Este componente 06 - Frete Despachante está relacionado ao campo **DTC\_VALDPC**, que é o valor do documento anterior quando está realizando subcontratação ou redespacho intermediário.

Com o campo DTC\_VALDPC preenchido na entrada de documentos, o Sistema considera o valor do documento original com este componente 06 - Frete Despachante, caso queira cobrar um percentual sobre o valor total do documento anterior.  
  
Para configurar o componente, acesse **Atualizações/ Comercial/ Componentes de Frete -** **TMSA030** e cadastre o componente da seguinte forma:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11617068029975)

Vincule este componente na configuração da tabela de frete que vá utilizar. Para isso, acesse **Atualizações/ Comercial/ Config. Tab. Frete -** **TMSA130** e relacione o componente cadastrado:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11617136663319)

Defina na tabela de frete a regra para calcular o componente, conforme sua necessidade. No exemplo abaixo, está configurado para calcular 20% sobre o valor despachante. Para isso, acesse a rotina **Atualizações/ Comercial/ Tabela de Frete -** **TMSA010**e defina a regra:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11617196086551)

Caso esteja cadastrando uma nova tabela de frete ao invés de alterar uma tabela de frete existente, é importante lembrar que esta nova tabela deve ser relacionada no contrato do cliente em **Atualizações/ Comercial/ Contrato Cliente -** **TECA250.**Com os devidos cadastros efetuados, ao gerar um documento na rotina **TMSA050 - Entrada de Documentos** e preencher o campo **Frete Desp - DTC\_VALDPC**, o Sistema irá calcular o percentual definido na tabela de frete sobre o valor preenchido neste campo. No exemplo, foi preenchido 200 reais, e a tabela de frete está configurada para calcular 20% sobre o valor, então o Sistema irá calcular 40 reais para o componente **06 - Frete Despachante**.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11617268655511)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11617271049239)
