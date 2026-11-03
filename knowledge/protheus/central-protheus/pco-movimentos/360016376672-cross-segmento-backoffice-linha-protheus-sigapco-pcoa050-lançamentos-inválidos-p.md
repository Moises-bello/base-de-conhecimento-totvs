---
article_id: 360016376672
category: PCO - Movimentos
content_hash: baae34e9f447389a2832cb3a202b0d473ea43cd97d1fba71facae8ff6337af90
fetched_at: '2026-06-28T22:37:09.471915+00:00'
product: protheus
section_id: 1500001550962
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO -  PCOA050 - Lançamentos
  inválidos por linha
type: support-article
updated_at: '2023-11-21T13:15:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016376672-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA050-Lan%C3%A7amentos-inv%C3%A1lidos-por-linha
---

**Ocorrência**No módulo **Planejamento e Controle Orçamentário** , ao realizar um lançamento em manutenção de lançamentos, é apresentada a mensagem **Lançamentos inválidos.**  
  
**Ambiente**

Protheus - Planejamento e Controle Orçamentário - A partir da versão 11.80

**Causa**

Esse incidente ocorre, pois no cadastro das entidades (custo,item,classe,conta,etc) deve esta como bloqueado/inexistente para lançamentos.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1.1 Acesse o cadastro de **cada entidade envolvida** no lançamento;  
1.2 Verifique os campos referente a **bloqueio ex. ctt\_bloq –centro de custos**;  
1.3 Altere o campo **desbloqueando** o cadastro;  
1.4 Clique em **Salvar**.

2.1 Acesse a rotina de lançamento (PCOA050)   
2.2 Alterar o lançamento   
2.3 Clique em **Salvar**.

Permanecendo inválido (ainda nas rotina de lançamento)

3.1 Pesquisar cada entidade com F3   
3.2 verificar se a mesma esta cadastrada com o código correto   
3.3 Informa o código valido

3.4 Verifique se o lançamento está sendo realizado para uma entidade analítica.  
3.5 Clique em **Salvar**.
