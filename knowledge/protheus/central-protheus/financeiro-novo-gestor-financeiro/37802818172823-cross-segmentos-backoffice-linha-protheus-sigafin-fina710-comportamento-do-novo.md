---
article_id: 37802818172823
category: Financeiro - Novo Gestor Financeiro
content_hash: 44fee446e558f8c2bec05da62ec9a4bd4dc804be2580cebb0ec2a34755ba892c
fetched_at: '2026-06-28T22:37:41.467859+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Comportamento
  do novo gestor financeiro quanto ao número de dias no campo A6_RETENCA
type: support-article
updated_at: '2026-01-20T16:43:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37802818172823-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Comportamento-do-novo-gestor-financeiro-quanto-ao-n%C3%BAmero-de-dias-no-campo-A6-RETENCA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37802792455831) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Qual o comportamento do novo gestor financeiro quanto ao número de dias configurado no campo A6\_RETENCA no cadastro de banco?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Conceito:

O Fluxo de caixa apresenta um gráfico definido como padrão com a exibição Mensal dos últimos 12 meses e o somatório de **Entradas****e****Saídas****.** Clicando sobre as legendas, é possível visualizar somente as entradas ou as saídas.  
  
Para títulos em borderô o fluxo de caixa considera a configuração de "**dias de retenção**" (**A6\_RETENCA**) do banco para exibir o título conforme seu vencimento + dias de retenção bancária.  
   
Importante: No momento de geração do borderô via rotina **FINA060** por exemplo, no F12 na montagem do borderô, a pergunta "Considera Retenção Bancaria ? " precisa estar igual a "SIM".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37802818163863)

**Exemplo de baixa realizada no dia 17/09/2025 e o campo A6\_RETENCA com conteúdo "1" e configurado para considerar a retenção bancária na montagem do borderô.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37802818164503)

**Saiba mais:** [**Movimentações Financeiras - FINA710**](https://tdn.totvs.com/pages/releaseview.action?pageId=622668231)
