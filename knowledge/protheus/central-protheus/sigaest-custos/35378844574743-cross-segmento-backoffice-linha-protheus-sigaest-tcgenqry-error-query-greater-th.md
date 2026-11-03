---
article_id: 35378844574743
category: SIGAEST - CUSTOS
content_hash: dd0cb6268935fcb111f60734a9367ae44c0e5da7422f420691269a1bc6befb03
fetched_at: '2026-06-28T22:39:02.356725+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - TCGenQry Error - Query
  greater than
type: support-article
updated_at: '2025-10-03T12:10:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35378844574743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-TCGenQry-Error-Query-greater-than
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35378844566807) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**  
Durante o processamento ou validação de qualquer rotina, é apresentado o seguinte error.log em tela.

THREAD ERROR ([XXXX], TP|SD|HTTP@01|TRUE\_,**XXXXXXXXXXXXXXXXX**)   XX/XX/XXXX   XX:XX:XX  
TCGenQry Error - Query greater than **XXXXX** bytes. on **FUNCAO\_TAL**(**FONTE\_TAL.PRW**) 03/10/2025 09:00:00 line : 1234

Onde a nomenclatura com codigo **XXXX** e **FUNCAO\_TAL** ou **FONTE\_TAL**, podem ser diferentes de acordo seus dados, data e fonte.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**  
Isso ocorre porque esta tentando gerar um erro que compõe uma quantiade de bytes maior a que você parametrizou no seu ambiente.  
  
**Solução**  
Bata configurar a chave **MaxQuerySize** na sessão [GENERAL] com conteudo de 31960.

```
[General]
MaxQuerySize=31960
```

Boletim referencia da area de tecnologia: [MaxQuerySize](https://tdn.totvs.com/x/CAN3Ag)

**Saiba mais**  
[*Configurações gerais no estoque custos*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
