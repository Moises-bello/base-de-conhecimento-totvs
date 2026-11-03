---
article_id: 360000465528
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 4671e64f75b7ae3205c4bfdbd7aaf45e6298da086a45a0fc3b5614380d2e3304
fetched_at: '2026-06-28T22:41:43.198081+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - Cálculo Mensal não
  calcula para todos os bens e preenche o campo N3_FIMDEPR '
type: support-article
updated_at: '2022-07-05T19:41:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000465528-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-C%C3%A1lculo-Mensal-n%C3%A3o-calcula-para-todos-os-bens-e-preenche-o-campo-N3-FIMDEPR
---

**Ocorrência**Ao calcular a depreciação ATFA050, alguns bens não estão sendo depreciados

**Ambiente**  
Protheus – Ativo Fixo – A partir da versão 12.1.17  
  
**Causa**

Esse incidente ocorre, pois o sistema estava acelerando a depreciação preenchendo o campo N3\_FIMDEPR para bens que ainda possuíam saldo a depeciar   
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Deve-se acessar o link abaixo, onde esta disponível o pacote de correção:

**[Pacotes de Atualização - Ativo Fixo](https://tdn.totvs.com/pages/viewpage.action?pageId=382557083)**

2. Aplicar a patch em base de homologação

3.  Analise de base para identificar os bens que foram preenchidos incorretamente e fazer o devido ajuste manualmente limpando o N3\_FIMDEPR para os bens que foram preenchidos erroneamente.

4. Executar a rotina de descalculo mensal(ATFA070)

6. O cálculo ocorrerá somente para os bens com o campo N3\_FIMDEPR em branco

7. Executar o cálculo da depreciação(ATFA050) novamente.

**Obs:** Não é indicado realizar mais de um descalculo de depreciação. Para casos onde será necessário retornar o cálculo anterior ao último realizado sugerimos restaurar o bakup.
