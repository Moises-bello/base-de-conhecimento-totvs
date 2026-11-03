---
article_id: 1500002350522
category: NFe - Nota Fiscal Eletrônica
content_hash: 8d77b6acb6751f29de234ec753f683db9afed6559ee5a30b3ef4ea57f66ea671
fetched_at: '2026-06-28T22:40:01.775068+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como incluir LOGO
  para impressão do DANFE? (SmartERP)'
type: support-article
updated_at: '2021-10-11T17:15:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002350522--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-incluir-LOGO-para-impress%C3%A3o-do-DANFE-SmartERP
---

**Dúvida**Como deverá ser incluída a imagem do logo **para as impressões do DANFE** apresentarem o logo desejado **em ambientes Smart ERP**?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**Os logos **devem ser inclusos na pasta SYSTEM** dos diretórios do Protheus.  
O formato e dimensão recomendado para o arquivo é: BMP e tamanho 95X95.  
O parâmetro MV\_LOGOD deverá estar configurado de acordo com a necessidade:  
  
**MV\_LOGOD = S** *(Configuração que permite utilizar uma imagem separada para o logotipo da DANFE)*

A imagem deve possuir a nomenclatura com base na regra abaixo:  
DANFE + Código da Empresa + Código da Filial + .bmp  
Exemplo: DANFE0101.bmp  
Caso seja utilizada apenas uma imagem para todas as filiais  
DANFE + Código da Empresa +.bmp  
  
**MV\_LOGOD = N** *(Imagem padrão)*

A imagem deve possuir a nomenclatura com base na regra abaixo:  
lgrl + Código da Empresa + Código da Filial + .bmp  
Exemplo: lgrl0101.bmp  
Caso seja utilizada apenas uma imagem para todas as filiais:  
lgrl + Código da Empresa +.bmp  
  
Após ter a imagem dentro dos padrões citados e parâmetro configurado, deverá acessar os diretórios do ambiente via SFTP (cadastrado e informado no portal [T-Cloud](https://tcloud.totvs.com.br/)).  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101037434/mceclip2.png)  
  
Nesse exemplo foi utilizado o FileZilla para acesso as credencias obtidas.  
Note que as imagens estão dentro da pasta **protheus\_data/system:**  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101038214/mceclip3.png)
