---
article_id: 33631903216151
category: Materiais - Compras (SIGACOM)
content_hash: e46a5560f9a5a605b571cf5e9b967fe4381e350e6487ba4c63f09575742ce028
fetched_at: '2026-06-28T22:41:25.414042+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - variable does not exist
  CNATUREZA on VAZIO
type: support-article
updated_at: '2025-07-22T13:39:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33631903216151-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-variable-does-not-exist-CNATUREZA-on-VAZIO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33631903202839) Tempo aproximado para leitura: 00**:02:00 min**  
  
**Ocorrência**  
Ao selecionar a natureza na rotina documento de entrada (MATA103) ocorre o error log abaixo

[TOTVS build: 7.00.240223P-20250326] Called from {|| IF(LMT103NAT,IF(EXECBLOCK("MT103NAT", .F. , .F. ,CNATUREZA),NFEVLDREF("NF\_NATUREZA",CNATUREZA), .F. ),VAZIO(CNATUREZA) .OR. (EXISTCPO("SED",CNATUREZA) .AND. A103VALNAT(CNATUREZA) .AND. NFEVLDREF("NF\_NATUREZA",CNATUREZA) .AND. (LCHANGENAT:= .T. )))}(MATA103X.PRX) 09/06/2025 15:01:46 line : 1591  
  
**Ambiente**  
Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Causa**  
Um dos principais motivos para que ocorra este incidente é a parametrização incorreta do parâmetro MV\_2DUPNAT.  
  
**Solução**  
  
Para solucionar essa ocorrência, realize o preenchimento do parâmetro MV\_2DUPNAT conforme o exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33631903203223)

Caso persista o erro solicitamos que realizem o teste com todos os pontos de entradas desabilitado através do catalogo de personalização de acordo com a documentação: [Como ativar e desativar customizações no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021114292--Cross-Segmentos-Linha-Protheus-Como-ativar-e-desativar-customiza%C3%A7%C3%B5es-no-Protheus)  
  
  
***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
