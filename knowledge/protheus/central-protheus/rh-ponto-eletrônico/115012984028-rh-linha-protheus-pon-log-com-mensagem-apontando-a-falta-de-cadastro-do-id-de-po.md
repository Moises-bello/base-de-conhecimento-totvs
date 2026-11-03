---
article_id: 115012984028
category: RH - Ponto Eletrônico
content_hash: eb23f0a0bb2fab9475ed1f09d1aef14bf0bc8c5ce8b17ddb3a3d58f6021cec0e
fetched_at: '2026-06-28T22:44:58.327887+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Log com mensagem apontando a falta de cadastro
  do ID de Ponto 043A
type: support-article
updated_at: '2022-07-19T17:33:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115012984028-RH-Linha-Protheus-PON-Log-com-mensagem-apontando-a-falta-de-cadastro-do-ID-de-Ponto-043A
---

**Ocorrência**Ao processar o Apontamento para os funcionários, o sistema gera o *log* com a mensagem de que **Foram Encontradas Inconsistências nos Eventos. Faltam códigos de Identificadores de Ponto na Tabela 20 do Configurador.** **Número de Identificadores requeridos: 43 / Número de Identificadores Existentes: 42**, conforme imagem abaixo:  
  
![](http://tdn.totvs.com/download/attachments/301178110/image2017-9-28_11-4-47.png?version=1&modificationDate=1506607809000&api=v2 "Linha Microsiga Protheus > PSIGAPON0148 - PONA280: Ao efetuar o cálculo do Apontamento aparece o Log: Número de Identificadores requeridos: 43 / Número de Identificadores Existentes: 42. > image2017-9-28_11-4-47.png")  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Causa**Não existe cadastro de evento vinculado ao ID de Ponto 043A - Suspensão Disciplinar.  
  
**Solução**  
Para correção do problema, basta criar um novo evento e associar o ID de Ponto **043A - Suspensão Disciplinar,** mesmo que o usuário não o utilize.  
  
**Informações complementares**  
Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
