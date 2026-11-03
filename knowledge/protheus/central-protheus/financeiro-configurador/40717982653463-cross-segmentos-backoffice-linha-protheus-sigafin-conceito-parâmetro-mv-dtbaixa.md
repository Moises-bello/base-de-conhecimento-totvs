---
article_id: 40717982653463
category: Financeiro - Configurador
content_hash: e190b2eb2d01fe378caa27400a2c0eccda84b7ba9ac22bff54fcb431519c6c8b
fetched_at: '2026-06-28T22:37:57.592563+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Conceito parâmetro
  MV_DTBAIXA
type: support-article
updated_at: '2026-05-25T13:57:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40717982653463-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Conceito-par%C3%A2metro-MV-DTBAIXA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40717982635671) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Qual o conceito do parâmetro MV\_DTBAIXA?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
O parâmetro MV\_DTBAIXA tem por finalidade fazer a validação da data no momento da baixa de um titulo a pagar, verificando se a data da baixa é menor que a data gravada no momento da inclusão do titulo no campo E2\_EMIS1. Caso queira ajustar este conceito, se faz necessário ajuste do parâmetro, para validar os impactos, recomendamos sempre realizar este tipo de validação em ambiente de testes.

| Nome da variável | MV\_DTBAIXA |
| --- | --- |
| Tipo | Lógico |
| Descrição | Valida a data da baixa no campo E2\_EMIS1 |
| Valor padrão | .F. |

Saiba mais: [Utilização do parâmetro MV\_DTBAIXA](https://tdn.totvs.com/pages/releaseview.action?pageId=638717800)
