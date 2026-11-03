---
article_id: 360008935151
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 61e3449dcb115a24757d5ee1afcd200e584e33898c693dbc73fa7fca1b88f14d
fetched_at: '2026-06-28T22:41:48.224076+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 - OBRIGATORIEDADE
  OU NÃO DO CAMPO N1_CHAPA
type: support-article
updated_at: '2022-06-02T18:10:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008935151-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-OBRIGATORIEDADE-OU-N%C3%83O-DO-CAMPO-N1-CHAPA
---

**Dúvida**  
Alterar a o numero da plaqueta, mas o campo esta desabilitado

Na confirmação do cadastro do ativo retorna mensagem de numero de plaqueta obrigatório

Deixar campo como obrigatório

**Ambiente**  
PROTHEUS – Ativo Fixo  – A partir da versão 11.80  
  
  
**Solução**

No acesso a rotina de cadastro do ativo, acionar os parâmetros através da tecla F12 configure a pergunta **Repete chapa?**

Que Indica se o campo Número de Plaqueta (N1\_CHAPA - Utilizado pelas empresas para identificação do bem) pode ou não ser repetido. Informa-lo como **SIM** permitirá a inclusão do bem sem validar o número digitado (caso não exista um controle de numeração de plaquetas nos bens ou por qualquer outro motivo), caso contrario o número informado somente será confirmado se já não estiver incluído.
