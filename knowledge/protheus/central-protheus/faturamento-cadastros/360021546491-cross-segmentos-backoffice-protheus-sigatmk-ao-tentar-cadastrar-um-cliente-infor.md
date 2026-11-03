---
article_id: 360021546491
category: Faturamento - Cadastros
content_hash: f68063bec064db1450620119a19380dc581e377f4921f831e8ee68788073a1ba
fetched_at: '2026-06-28T22:38:35.490000+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Ao tentar cadastrar um cliente,
  informo o CNPJ e apresenta o Help TMKVEENT o que fazer?
type: support-article
updated_at: '2024-04-25T12:38:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021546491-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Ao-tentar-cadastrar-um-cliente-informo-o-CNPJ-e-apresenta-o-Help-TMKVEENT-o-que-fazer
---

**Dúvida**Ao tentar cadastrar um cliente, informo o CNPJ e apresenta o Help **TMKVEENT** o que fazer?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**Pelo comportamento do sistema, o help **TMKVEENT**somente é apresentado quando o parâmetro **MV\_TMKVCGC**esta habilitado **.T.**  
  
O sistema verifica o cadastro de **Suspect** ,**Propesct** e **Clientes**.   
Verifique se o parâmetro **MV\_TMKVCGC**está habilitado, desabilite-o e refaça seu processo.  
  
Ele faz uma validação de CNPJ/CPF por entidade, basicamente ele confronta o CNPJ informado com os registros incluídos nas tabelas a que listo abaixo, caso encontrado ele retorna falso, informando que já existe entidade cadastrada com aquele CNPJ.  
  
Tabelas que o sistema confronta:

* **SA1**
* **SUS**
* **ACH**

**Avalie também, formas de importação de  informações de cliente relacionadas ao seu  CNPJ:**

**[MP - FRAME - Configuração do Mashups](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025045012-MP-FRAME-Configura%C3%A7%C3%A3o-do-Mashups)**

**[Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-Cadastro-de-Clientes-MATA030-x-CAROL-Integração-via-API-](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009140342-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-Cadastro-de-Clientes-MATA030-x-CAROL-Integra%C3%A7%C3%A3o-via-API-)**
