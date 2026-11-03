---
article_id: 8218160531863
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 8b3511cc24509b8bc7a6b0309e8acb32696e82b60a142175cbc430035bb39043
fetched_at: '2026-06-28T22:42:00.929592+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Como gerar
  o registro C197 do Sped Fiscal para o código de ajuste SP90090104 - Destaque do
  IPI sem direito à crédito?  '
type: support-article
updated_at: '2022-08-16T19:49:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8218160531863-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-C197-do-Sped-Fiscal-para-o-c%C3%B3digo-de-ajuste-SP90090104-Destaque-do-IPI-sem-direito-%C3%A0-cr%C3%A9dito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o registro **C197** com código de ajuste **SP90090104** para atender o **Cenário 02 do Manual da CAT66/2018 - Saída com destaque de IPI sem direito à crédito para o adquirente** - **Contribuinte B**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
**Solução**

O código de ajuste **SP90090104** é utilizado no projeto de Eliminação da **GIA**. O projeto refere-se à dispensa da obrigação, pelo contribuinte paulista, de entregar mensalmente a **GIA**, tendo em vista que a **SEFAZ-SP** gerará automaticamente uma **GIA** virtual a partir da **EFD ICMS/IPI.**  
Para isso, foi necessário abrir a possibilidade para que sejam declarados, na **EFD ICMS/IPI** os valores das colunas **Outras;** **Isentas/Não Tributadas e** **ICMS-ST na condição de substituído** através do registro **C197**.  
Dessa forma, nas  operações em que o **ICMS** é integralmente tributado e não existe valor referente às colunas **Outras, Isentas/Não Tributadas** o contribuinte não precisaria enviar registro **C197** com o código **SP90090104**.  
No entanto, nos casos em que  o contribuinte não pode tomar **crédito de IPI** e na **EFD ICMS IPI** o valor do **IPI** não pode ser destacado em  campo próprio no registro **C190**, há uma exceção, visto que, caso o contribuinte não envie o registro **C197** relativo ao código **SP90090104**, uma fórmula será aplicada para calcular o valor da coluna **Outros ICMS** na **GIA**, baseada no registro **C190**, e essa fórmula, incorretamente, resultará em um valor de para a coluna de **Outras.**Para contornar essa situação, o **Manual da CAT66**  indica o envio do registro **C197** com valores zerados para que o valor de **Outros/Isentas** da operação seja zero, porém com **alíquota de maior que zero**, conforme exemplo no **Manual da CAT66**.

*Print:*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8217896444055/mceclip0.png)Para gerar o registro **C197** dessa forma no  **Protheus**, é preciso configurar um **Código de Reflexo** com a regra abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8218045195415/mceclip1.png)

Com esta configuração será gerado um lançamento da tabela **CDA** e a Rotina **SPEDFISCAL** está preparada para buscar **Valor Maior Zero** ou **Alíquota maior que Zero** e **Base igual a Zero**.  
  
Após, siga o processo indicado no link abaixo:  
  
Como gerar os Registros **C190, C195 e C197**?  
[https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010170492-REGISTRO-C190-C195-e-C197](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010170492-REGISTRO-C190-C195-e-C197&sa=D&source=hangouts&ust=1597845127969000&usg=AFQjCNHHy5QwIAzYP_CmdWeaPMuBZ_z-Zw)

Informações dos **códigos de reflexo** conforme **Portaria CAT66**  
<https://tdn.totvs.com/display/public/PROT/FIS0024_Portaria_CAT66_SP>
