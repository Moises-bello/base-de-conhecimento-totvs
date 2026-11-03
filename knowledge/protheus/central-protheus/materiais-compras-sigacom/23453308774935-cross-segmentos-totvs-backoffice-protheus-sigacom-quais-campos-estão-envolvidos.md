---
article_id: 23453308774935
category: Materiais - Compras (SIGACOM)
content_hash: 7321e7929962c329921cda521b75bfd446371fbae856c0db4853ac1c6c40fdd7
fetched_at: '2026-06-28T22:41:24.133456+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais campos estão
  envolvidos na Integração Documento de Entrada x Ativo fixo?
type: support-article
updated_at: '2024-07-30T18:27:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23453308774935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-campos-est%C3%A3o-envolvidos-na-Integra%C3%A7%C3%A3o-Documento-de-Entrada-x-Ativo-fixo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23453308749335) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Quais campos Estão envolvidos na integração entre o documento de entrada e ativo fixo?  
  
**Ambiente**Protheus – Compras A partir da versão 12  
  
**Solução**

Na integração com o módulo de Ativo Fixo, a rotina Documento de Entrada gera automaticamente o Bem no ativo. Com isso somente campos obrigatórios nativos possuem tratamento para levarem o dado inserido no campos das tabelas SF1 e SD1 para as tabelas SN1 / SN3. Dessa forma, seguem abaixo quais campos estão envolvidos nessa integração.

N1\_DESCRIC    B1\_DESC

N1\_AQUISIC    D1\_DTDIGIT

N1\_QUANTD   D1\_QUANT

N1\_FORNEC    D1\_FORNECE

N1\_LOJA          D1\_LOJA

N1\_NSERIE      D1\_SERIE

N1\_NFISCAL    D1\_DOC

N1\_LOJA          D1\_LOJA

N1\_NFESPEC   F1\_ESPECIE

N1\_NFITEM     D1\_ITEM

N1\_PRODUTO D1\_COD

N3\_CUSTBEM  D1\_CC

N3\_CCUSTO    D1\_CC

N3\_SUBCCON D1\_ITEMCTA

N3\_CLVLCON  D1\_CLVL

N3\_VORIG      Se o parâmetro MV\_ATFMOED = 3

N1\_CBASE e  N3\_CBASE  = D1\_CBASEAF ( parâmetro MV\_CBASEAF )

Dessa forma, se campos da SN1 ou SN3 que não foram mencionados acima estiverem como obrigatório no configurador, o sistema irá validar e será gerado um help informando isso ao usuário.

***Saiba Mais:***

[Integração Documento de Entrada x Ativo Fixo](https://tdn.totvs.com/pages/releaseview.action?pageId=334335454)

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGACOM - Integração Compras x Ativo Fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412569002647-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Ativo-Fixo-x-Compras)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Mensagem de Campo Não Preenchido no Lançamento de Documento de Entrada x Ativo Fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026375592-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Mensagem-de-Campo-N%C3%A3o-Preenchido-no-Lan%C3%A7amento-de-Documento-de-Entrada-x-Ativo-Fixo)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
