---
article_id: 35361266596759
category: Escrita Fiscal - Configurador de Tributos
content_hash: a75a0d0adc481c1ac9a725552df38c596275310502cf617a0e1d847f2a22cd75
fetched_at: '2026-06-28T22:39:18.384418+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS – FISA170 - O código
  das regras de calculo do documento fiscal (F2B_REGRA) grava em quais tabelas?
type: support-article
updated_at: '2025-10-02T21:22:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35361266596759-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-O-c%C3%B3digo-das-regras-de-calculo-do-documento-fiscal-F2B-REGRA-grava-em-quais-tabelas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35361261848855) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
O código das regras de calculo do documento fiscal (F2B\_REGRA) grava em quais tabelas?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**  
O código do F2B\_REGRA não será gravado nas tabelas **SFT,** **SF3 e** **CD2**

Em especial, a tabela CD2 levará o código conforme legado, devido ao ID TOTVS utilizado e às regras de transmissão.

O **código da regra** será gravado apenas nas seguintes tabelas:

* F2B - Campo F2B\_REGRA
* F2D - Campo F2D\_TRIB
* CIN - Campo CIN\_REGRA
* CJ2 - Campo CJ2\_CODIGO

Para mais informações sobre as tabelas disponíveis e suas finalidades, consulte a documentação oficial do TOTVS:

[Principais Rotinas e Tabelas](https://tdn.totvs.com/display/public/PROT/CFGTRIB+-+Configurador+de+Tributos#CFGTRIBConfiguradordeTributos-PrincipaisRotinaseTabelas)

[CFGTRIB - Configurador de Tributos - P12](https://tdn.totvs.com/display/PROT/CFGTRIB+-+Configurador+de+Tributos+-+P12)
