---
article_id: 5814892004247
category: Materiais - Compras (SIGACOM)
content_hash: 46ce6db8b4e1671b9a15258cd3b6dc7d379c08494324e08de592bb6b01f0cc3d
fetched_at: '2026-06-28T22:41:07.439881+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao gerar Nota de Devolução
  no Monitor do Colaboração / Importador XML ocorre erro de " type mismatch on + on
  COLVERDEV(COMXCOL.PRW) "
type: support-article
updated_at: '2024-06-12T20:12:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5814892004247-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-gerar-Nota-de-Devolu%C3%A7%C3%A3o-no-Monitor-do-Colabora%C3%A7%C3%A3o-Importador-XML-ocorre-erro-de-type-mismatch-on-on-COLVERDEV-COMXCOL-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24131963640087) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao gerar Nota de Devolução no Monitor do Colaboração / Importador ocorre erro de " type mismatch on + on COLVERDEV(COMXCOL.PRW) "   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**Nas ocorrências já mapeadas deste erro, ao se gerar NF através do monitor do Totvs Colaboração ou Importador XML, esta mensagem pode ocorrer na importação de NFs de Devolução onde os registros da tabela SDT da NF que está sendo importada, estão com os campos ***DT\_NFORI***, ***DT\_SERIORI*** e ***DT\_ITEMORI*** em branco.

Dessa forma, orienta-se avaliar na base de dados do ambiente em questão se os registros da tabela SDT em questão da NF que está sendo importados estão com estes campos em branco, e assim realizar a devida manutenção preenchendo-os com as informações conforme a NF Origem. Esta NF de Origem também deve existir na base de dados em questão.

IMPORTANTE :  Para necessidade de apoio na manutenção da base de dados, orienta-se o contato com um analista especialista junto ao Executivo de Serviço e Negócios Totvs (ESN) que atende ao cliente para solicitação.

É também aconselhado estar com o sistema atualizado conforme o pacote mais atual do Compras contido no link abaixo:

* [Acumulado Compras](https://tdn.totvs.com/pages/releaseview.action?pageId=522011099)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
