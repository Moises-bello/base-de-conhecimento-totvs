---
article_id: 360020608812
category: ADVPL - Ponto de Entrada
content_hash: dbf3b8fe31532d2910627f43b679896b6501867a86e983b4675f7c04d37de564
fetched_at: '2026-06-28T22:40:11.540745+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - ADVPL - Erro: F090FIL não realiza
  filtragem'
type: support-article
updated_at: '2022-03-23T11:03:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020608812-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Erro-F090FIL-n%C3%A3o-realiza-filtragem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao utilizar o ponto de entrada F090FIL para realizar a filtragem dos dados da rotina FINA090, o mesmo não está acatando a regra.  
  
**Ambiente**Cross Segmento - Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Causa**Em fontes com data superior à 29/08/2017, foi efetuada a alteração da sintaxe xBase para SQL na estrutura dos filtros da rotina FINA090.  
  
**Solução**Utilizar o ponto de entrada **F090QFIL**.  
  
**Saiba mais**  
[F090QFIL - Ponto de entrada para filtrar os registros da Baixa Pagar Automática](https://tdn.totvs.com/pages/releaseview.action?pageId=544199708)
