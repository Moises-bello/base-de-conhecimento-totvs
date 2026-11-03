---
article_id: 360021939211
category: ADVPL - Classe e Função
content_hash: 84ffe595a531eb26f76bca296448265be446e9b0798c61a193287341e273556b
fetched_at: '2026-06-28T22:40:16.898994+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Function GetFontPixWidths()
  doesn't available in JOB
type: support-article
updated_at: '2022-05-09T23:43:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021939211-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Function-GetFontPixWidths-doesn-t-available-in-JOB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Problemas ao executar os agendamentos em rotina customizadas via schedule**Function GetFontPixWidths() doesn't available in JOB**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Causa**Esse incidente ocorre, pela utilização da função **GetFontPixWidths()**, pois ela não está disponível para rodar via JOB ou se estiver utilizando **MSGYESNO**  e **MsgBox** (Funções que abrem tela).   
  
**Solução**Para solucionar essa ocorrência em caso de customizações, é necessário criar um tratamento para que não execute essa função. Para esse tratamento podemos utilizar a função **lIsBlind().**Esta função determina se a conexão efetuada com o **Protheus** não possui interface com o usuário.

**Saiba mais**[GetFontPixWidths()](http://tdn.totvs.com/display/tec/GetFontPixWidths)  
[lIsBlind()](http://tdn.totvs.com/pages/releaseview.action?pageId=6814878)
