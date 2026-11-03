---
article_id: 360051104734
category: RH - Ponto Eletrônico
content_hash: 46f2760fce0a6eb6b4d6fbe8b97e629b2fd9034858a67b8ad2131c0ffecc144f
fetched_at: '2026-06-28T22:44:58.325113+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Intrajornada no SIGAPON X SIGATEC
type: support-article
updated_at: '2022-06-29T08:07:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051104734-RH-Linha-Protheus-PON-Intrajornada-no-SIGAPON-X-SIGATEC
---

**Ocorrência**Quando ocorre integração de marcações do módulo de Gestão de Serviços para o Ponto Eletrônico, o sistema gera uma hora a menos trabalhada.  
  
**Ambiente**RH - Linha Protheus - Ponto Eletrônico - A partir da versão 12.1.17  
  
**Causa**Este incidente ocorre, por conta do campo da Intrajornada no cadastro de Escalas do módulo de Gestão de Serviços, em conjunto com o parâmetro MV\_TECINTR,  
  
O campo da Intrajornada serve para ditar para o Sistema que deve ser abatida 01 hora de descanso do atendente, independente se no cadastro da Escala for informado o intervalo ou não. Este abatimento ocorre de acordo com o período informado no parâmetro MV\_TECINTR.  
  
Exemplo:  
- escala cadastrada das 06h - 12h - 13h - 18h  
- conteúdo do parâmetro MV\_TECINTR - 6 (06 horas neste caso)  
- campo da Intrajornada como SIM no cadastro da escala  
  
O sistema vai considerar 10h trabalhadas, pois entende que deveria ter ocorrido um intervalo depois das 06h e antes 12h, e também do intervalo cadastrado na Escala.  
  
**Solução**Caso não queira dar este tratamento na integração dos módulos, deve deixar o campo da Intrajornada no cadastro da Escala como Não ou então, aumentar a quantidade de horas informada no conteúdo do parâmetro MV\_TECINTR.
