---
article_id: 360034173454
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 4f8c2830d2500af9821bebd07aa45145b3cf210592cc7ea9d850a3957e1aa298
fetched_at: '2026-06-28T22:40:48.749196+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Y550 Como gerar
type: support-article
updated_at: '2024-07-04T18:30:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034173454-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Y550-Como-gerar
---

**Dúvida**Como gerar o registro **Y550: Vendas a Comercial Exportadora com Fim Específico de Exportação ?**

**Ambiente**  
Microsiga Protheus – Contabilidade – A partir da versão 11.80  
  
**Solução**

Para gerar bloco **Y550: Vendas a Comercial Exportadora com Fim Específico de Exportação****,**deve haver operações de saída com os seguintes códigos fiscais: 5501/5502/6501/6502 com os cadastros de produto e fornecedor com as seguintes configurações:

**Através da rotina MATA010 Produto:** 

* Pos.IPI/NCM (B1\_POSIPI) deve estar diferente de vazio

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044240254)

**Através da rotina MATA030** Cliente **:**

 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046092193)

* P. Vinculo ( **A1\_VINCULO** ) diferente de vazio.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044240974)

**Através da rotina central de escrituração CTBS001** 

Na wizard do ECF no passo 6 a pergunta PJ Efetuou Vendas a Empresa Comercial Exportadora...? Deve estar marcada = Sim  
  
![](https://totvssuporte.zendesk.com/attachments/token/6QP8pUby3bqd50hmyVrYqBcXv/?name=inline-650189267.png)​

Ao gerar a ECF deve seleciona "Sim" para DIPJ

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20819633190039)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045101153)

Através da APSDU acesse as tabelas TAFST1 e TAFST2  e veja se o bloco T106 foi gerado  
  
  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração  
     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada  
  
   Ex: |T106|20181231|00000000000000|11071020|10000,00|

* Verifique o TAFSTATUS = 3

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045102393)

**Através da rotina TAFTICKET** também é possível visualizar o bloco T098

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044242694)

**Através do layout do TAF**  verifique se foi gerado corretamente  
  
[Último Layout Disponível](http://tdn.totvs.com/pages/releaseview.action?pageId=498722271)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045098233)

**A rotina TAFA342** do TAF e veja se o bloco Y foi gerado 

[**Registro Y550 - Vendas a Comercial Exportadora com Fim Específico de Exportação**](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoY-Informa%C3%A7%C3%B5esGerais)

* Tabelas - CGI (Vendas Com. Exp. c/ Fim Espec.) / C0A (Nomenclatura Comum Mercosul) / CGI (Vendas Com. Exp. c/ Fim Espec.)
* Registro do Layout TOTVS - T106
* Rotina - TAFA342 (Vendas Com. Expe. c/ Fim Espec.)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045102613)

Através da rotina TAFOBRIG gere o arquivo TXT 

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20819589954199)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044242854)

Veja se o arquivo gerou o dados corretamente

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045102973)

|Y550|: Identificação do tipo do registro.  
|00000000000000|: CNPJ da empresa comercial exportadora adquirente (CNPJ = 00.000.000/0000-00).  
|11071020|: Código NCM (1107.10.20).  
|100000,00|: Valor da mercadoria vendida (R$ 100.000,00)

Apartir do Leiaute 7 , registro Y550  foi excluido pela receita  

Com isso a pergunta fica inativa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24656976507159)

Vendas a Comercial Exportadora com Fim Específico de Exportação

<http://sped.rfb.gov.br/estatico/2E/B756440254D95A88E90837EF8166BFF4968846/Manual_de_Orienta%c3%a7%c3%a3o_da_ECF_Dezembro_2020.pdf>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24656871193751)

<https://tdn.totvs.com/pages/releaseview.action?pageId=599877579>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24656871197591)

Saiba mais :

[MP - SIGACTB - ECF - X320 - UNIDADE DE MEDIDA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020084511-MP-SIGACTB-ECF-X320-UNIDADE-DE-MEDIDA-?source=search)

[MP - SIGACTB - ECF -Como realizar a geração dos blocos X e Y?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006827952-MP-SIGACTB-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-dos-blocos-X-e-Y-?source=search)

[Relatório Transfer Pricing - Preço de Transferência](http://tdn.totvs.com/pages/releaseview.action?pageId=6076191)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
