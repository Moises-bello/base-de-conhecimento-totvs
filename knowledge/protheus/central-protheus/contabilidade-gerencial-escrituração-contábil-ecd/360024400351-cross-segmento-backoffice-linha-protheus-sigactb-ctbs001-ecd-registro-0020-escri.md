---
article_id: 360024400351
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 65b6f1bbb82abb0ca5473b780f434feebf757a8e06644ada8b5099a69e311450
fetched_at: '2026-06-28T22:40:44.597949+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 :ECD Registro
  0020: Escrituração Contábil Descentralizada'
type: support-article
updated_at: '2021-12-03T15:03:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024400351-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Registro-0020-Escritura%C3%A7%C3%A3o-Cont%C3%A1bil-Descentralizada
---

**Dúvida**

Como o registro 0020 é gerado no arquivo da ECD ?  
  
**Ambiente**  
Microsiga Protheus  – Contabilidade – A partir da versão 11.80  
  
  
**Solução**

 O sistema gera o registro com base nos dados abaixo

Acesse :Configurador + ambiente + empresas + filial -> Alterar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022399412/mceclip0.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022393311/mceclip2.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022393371/mceclip3.png)

Através da rotina de escrituração informe os campos abaixo para geração do registro

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022400012/mceclip4.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022400032/mceclip5.png)

Será gerado layout abaixo conforme manual da receita

0020|0|10117506800017|SP|123456|3434401|654321|11111111|

Campo 01 – Tipo de Registro: 0020  
Campo 02 – Indicador de Descentralização: 0(escrituração da filial – como indica que é a escrituração  
da filial, os campos 03 a 08 serão dados referentes a matriz)  
Campo 03 – CNPJ: 10117506800017 (Corresponde a 10.117.506/0008-17)  
Campo 04 – UF: SP  
Campo 05 – Inscrição Estadual: 123456  
Campo 06 – Código do Município: 3434401  
Campo 07 – Inscrição Municipal: 654321  
Campo 08 – NIRE: 11111111

 Veja mais : [MP - SIGACTB :ECD ERRO REGISTRO 0020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024401471-MP-SIGACTB-ECD-ERRO-REGISTRO-0020?source=search)

Veja como o sistema gerar [Descentralizada e Centralizada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125892-MP-SIGACTB-ECF-e-ECD-Centraliza%C3%A7%C3%A3o?source=search)
