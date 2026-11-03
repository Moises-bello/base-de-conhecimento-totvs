---
article_id: 360060606234
category: Financeiro - Contas a Receber - PIX
content_hash: 8f513b20ba4b661343cf669e5198cd899a739281223c831bb83a4c5336c3ea75
fetched_at: '2026-06-28T22:38:16.512433+00:00'
product: protheus
section_id: 1500001539301
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA890 -  Help F891NOPARBCO
  ao gerar o pix
type: support-article
updated_at: '2024-08-29T14:51:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060606234-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA890-Help-F891NOPARBCO-ao-gerar-o-pix
---

**Ocorrência**Na Rotina Monitor PIX, ao gerar o pix, apresenta o help F891NOPARBCO?  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25994803455255)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - FINA890 - A partir das versões 12.1.25  
  
**Causa**Falta do cadastro do parâmetros Banco para o Pix

**Solução**

Acessar a rotina **"MATA070 - Atualização de Banco"**, posicionar em cima do seu banco, e clicar na opção "Chave PIX"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22056000935319)

E efetuar o cadastro de uma chave pix.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22056011437335)

Acesse a rotina **FINA130** - **Cadastro Parâmetros Bancos,** inclua e

note nos campos ressaltados, pois o **Pix a Receber** possui 750 *bytes* e o **Formato Data** 5

![](https://totvssuporte.zendesk.com/attachments/token/aZOuSSiH6U9lrudgbhl3NXulf/?name=inline-497450373.png)

**Importante:**  
As vezes já existe um parâmetros bancos para outro **Cnab, mas** é necessário outro para **Pix** devido a quantidade de **número de *bytes*** ser 750.

Necessário ajustar o parâmetro **MV\_FINPIX9**conforme a necessidade de utilização da rotina   
(**1 = CNAB, 2 = API**)

**Saiba mais:**

**[How To | SIGAFIN - Configuração e Envio do título em PIX via API #totvs\_backoffice\_linha\_protheus](https://www.youtube.com/watch?v=PTkOhnimUac&ab_channel=TOTVSSolu%C3%A7%C3%B5es)**  
**[How To | SIGAFIN - Job Envio de e-mail dos títulos em situação PIX #totvs\_backoffice\_linha\_protheus](https://www.youtube.com/watch?v=sEZvIRlanCk&ab_channel=TOTVSSolu%C3%A7%C3%B5es)**

**[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - JOB FINPIXMAIL - Envio do QRCODE PIX por E-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23444574168215)**

[**Pagamentos instantâneos - PIX**](https://tdn.totvs.com/pages/releaseview.action?pageId=569478747)
