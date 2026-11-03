---
article_id: 4407441232023
category: TAF - Escrituração Contábil Fiscal - ECF
content_hash: 9da0f5b38ce59d6bd5e6820f464c84723a94355cad087dcf93c3af908ed18390
fetched_at: '2026-06-28T22:41:31.678861+00:00'
product: protheus
section_id: 4404430589335
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001/TAFA334 - ECF
  Como gerar o Registro X310  '
type: support-article
updated_at: '2024-01-24T11:02:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407441232023-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-TAFA334-ECF-Como-gerar-o-Registro-X310
---

**Dúvida**

ECF Como gerar o Registro X310: Operações com o Exterior – Contratantes das Exportações.

**Ambiente**

Cross Segmento - Backoffice Linha Protheus – Contabilidade – A partir da versão 11.80

**Solução**

Através da rotina MATA010 Produto:

* Origem (B1\_ORIGEM) preenchido .

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407442477079/mceclip0.png)

Aba Outros

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407442606359/mceclip1.png)

**Exemplo** :

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407442638231/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407442717719/mceclip3.png)![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407442734487/mceclip4.png)

**Através da rotina MATA030 Cliente:** 

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407594802967/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407594814999/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407592575639/mceclip2.png)

**Através da rotina MATA020** **Fornecedor:**

* Tipo ( A2\_TIPO ) preenchido com: 'X'

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407439257495/mceclip5.png)

* P. Vinculo ( A2\_VINCULO ) diferente de vazio.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407442851479/mceclip6.png)

* MATA410 Incluir pedido de venda

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407443169303/mceclip7.png)

* Fatura pedido de venda

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407443224087/mceclip8.png)

* Gerar  [Relatório TRANSFER PRICE (MATR933)](https://tdn.totvs.com/pages/releaseview.action?pageId=6076191)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407439917335/mceclip10.png)

**Através da rotina central de escrituração CTBS001** ao gerar a ECF deve seleciona "Sim" para DIPJ

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045096293/mceclip4.png)

* Verifique no **manual da receita** o correto preenchimento dos parâmetros abaixo

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407443860247/mceclip12.png)

![](https://totvssuporte.zendesk.com/attachments/token/YO57WiWrVsS0xn5dAe2JJApaJ/?name=inline-1974789449.png)

![](https://totvssuporte.zendesk.com/attachments/token/09EFSEROUuJmoiyXsmgw0DQwt/?name=inline1010239994.png)​​

![](https://totvssuporte.zendesk.com/attachments/token/CV2kqlj9sd7xcpOqiw6mauRgy/?name=inline-2105789309.png)​

![](https://totvssuporte.zendesk.com/attachments/token/SN5h2anENFrg4zwHGvcW5IJE2/?name=inline-978959472.png)

Veja que o [T097 e o T097AA](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais) foi gerado

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407440655255/mceclip14.png)

**Através do layout do TAF**  verifique se foi gerado corretamente  
  
[Último Layout Disponível](http://tdn.totvs.com/pages/releaseview.action?pageId=498722271)

![mceclip22.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407445288855/mceclip22.png)

Através da APSDU acesse as tabelas TAFST1 e TAFST2  e veja se o bloco T097 e TA097AA foi gerado  
  
  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração  
     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada  
  
   Ex: 

T097|20211231|000000001|01|PRODUTX320|68860,00|84135090|11,00|15|1|1|620,96|36760,00|7930,46|0,0000|0,0000|0,0000|||

|T097AA|CLIENTE X320|249|1900,00|02|

* Verifique o TAFSTATUS = 3

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407440722327/mceclip15.png)

**A rotina TAFA334** do TAF e veja se o bloco X foi gerado 

[**Registro X300 - Operações com o Exterior – Exportações (Entradas de Divisas)**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais)

* Tabelas - CAY (Oper. Exterior - Exportações) / C0A (Nomenclatura Comum Mercosul) / C1J (Unidade de Medida) / CZT (Código CNC) / CZU (Tipo de Moeda) / V6U (Cód. Fonte de Cotação)
* Registro do Layout TOTVS - T097
* Rotina - TAFA334 (Operações com o Exterior - Exportações)

**[Registro X310 - Operações com o Exterior – Contratantes das Exportações](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais)**

* Tabelas - CAZ (Oper. Exterior - Contratantes) / C08 (Países Bco Central/SISCOMEX)
* Registro do Layout TOTVS - T097AA
* Rotina - TAFA334 (Operações com o Exterior - Exportações)

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407440861207/mceclip19.png)

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407445254167/mceclip21.png)

Através da rotina TAFOBRIG gere o arquivo TXT 

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045097553/mceclip10.png)

Veja se o arquivo gerou o dados corretamente

![mceclip23.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407445492247/mceclip23.png)

|X300|000000000|01|PRODUT X320|68860,00|84135090|11,00|09|S|PVE|||||||||||620,96|36760,00||7930,46|||||||||

|X300|: Identificação do tipo do registro.  
|000000000|: Número de ordem para identificar a operação.  
|01|: Tipo de importação (01 = Bens).  
|PRODUT X320|: Descrição do bem.  
|68860,00|: Total da operação (R$ 100.000,00).  
|84135090|: Código NCM do bem.  
|11,00|: Quantidade.  
|09|: Unidade de medida .  
|S|: Não é operação sujeita a arbitramento.  
|PVEX|: Método do preço de vendas das exportações (PVEX).  
||: Operações realizadas entre a própria pessoa jurídica e outros clientes não vinculados.  
||: Descrição dos bens, serviços ou direitos  
||: Identificação das partes envolvidas – informar razão social e número de identificação.  
||: Tipo do bem, serviço ou direito (I – Idêntico).  
||: Data utilizada no cálculo do preço parâmetro – somente preencher no caso de PECEX.  
||: Critérios para determinação do preço parâmetro – somente preencher se X300.DAT\_UTIL = “T” ou “O”.  
||: Data da transação – somente preencher no caso de PECEX e X300.DAT\_UTIL = “T”.  
||: Data de embarque – somente preencher no caso de PECEX.  
||: Fonte de cotação – somente preencher no caso de PECEX.  
||: Ajustes do preço parâmetro (N = Não).  
|620,96|: Valor do preço médio ponderado de aquisição nas importações apurado no ano-calendário (R$ 90.000,00).  
|36760,00|: Valor do preço médio ponderado de aquisição nas importações praticado no ano-calendário (R$ 90.000,00).  
||: Quantidade ajustada.  
|7930,46|: Valor do ajuste (R$ 1.000,00).  
||: Valor da cotação – somente preencher no caso de PECEX.  
||: Número da declaração única de exportação – somente preencher no caso de PECEX.  
||: Não há.  
||: Não há.  
||: Não há.  
||: Não há.  
||: Não há.

|X310|CLIENTE X320|249|10000,00|02|

|X310|: Identificação do tipo do registro.  
|CLIENTE X320|: Razão social da pessoa jurídica contratante.  
|249|: País (249 = Estados Unidas da América).  
|10000,00|: Valor da operação (R$ 10.000,00).  
|02|: Condição da pessoa envolvida

**Saiba mais :**

[Relatório MATR933](https://tdn.totvs.com/pages/releaseview.action?pageId=6076191)

[MP - SIGACTB - ECF - X320 - UNIDADE DE MEDIDA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020084511-MP-SIGACTB-ECF-X320-UNIDADE-DE-MEDIDA-?source=search)

[MP - SIGACTB - ECF -Como realizar a geração dos blocos X e Y?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006827952-MP-SIGACTB-ECF-Como-realizar-a-gera%C3%A7%C3%A3o-dos-blocos-X-e-Y-?source=search)

[Relatório Transfer Pricing - Preço de Transferência](http://tdn.totvs.com/pages/releaseview.action?pageId=6076191)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)
