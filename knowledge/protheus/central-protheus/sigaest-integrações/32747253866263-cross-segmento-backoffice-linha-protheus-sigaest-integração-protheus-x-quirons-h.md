---
article_id: 32747253866263
category: SIGAEST - INTEGRAÇÕES
content_hash: 34d143710fdc77d98310531d1fba739ccc3cfb7f9f81419da113a1a93f9eb17b
fetched_at: '2026-06-28T22:38:46.182895+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - INTEGRAÇÃO Protheus
  x Quirons: HELP FWINTERGDEF'
type: support-article
updated_at: '2025-07-15T10:54:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32747253866263-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-INTEGRA%C3%87%C3%83O-Protheus-x-Quirons-HELP-FWINTERGDEF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32747292344983) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao efetuar uma movimentação interna o Protheus retorna o HELP FWINTERGDEF - Movimentação não encontrada durante a integração com o Quirons  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**

Esse help ocorre devido ao Protheus não localizar as devidas amarrações para efetuar a integração.

Para efetuar o tratamento desta mensagem seguem alguns passos abaixo;

**Passo 1:**

Avaliar na tabela XX3, se o registro com campo XX3\_TRANS da linha criada para integração possui alguma informação de falha, por exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32747253814935)

**Passo 2:**   
Verifique se os adapters que estão sendo utilizados durante a integração estão de acordo com a recomendação da documentação abaixo  
<https://tdn.totvs.com/pages/releaseview.action?pageId=653566644#ADAPTER-6>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32747292350103)

**Passo 3:**

Caso a tag a qual gerou a informação de erro no XX3\_TRANS esteja configurada corretamente, mas não esteja em um adapter da documentação oficial efetue um teste sem o adapter em questão

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32747292351511)**

**Passo 4:**  
Verifique também se todos os adapters utilizados estão configurados corretamente, se notar alguma diferença efetue um teste recriando o adapter conforme as configurações documentadas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32747292352407)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32747253821207)

**Observação**:

Caso ainda assim persista, é possível utilizar o Schedule do SCHEDESTMG configurado para que a execução não seja do tipo "sempre ativa", com intervalos de 1min ou mais dependendo de sua necessidade e adapter do STOCKTURNOVER = Assincrono.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32747292353175)

Em paralelo também efetuar a configuração do adapter do STOCKLEVEL = Assincrono, pois o Quirons não enviará nenhum retorno ao Protheus referente a esta integração.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32747292356119)

**Saiba mais:**

<https://tdn.totvs.com/display/public/framework/A+camada+do+EAI>

[Clique aqui e veja mais artigos sobre Integrações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)
