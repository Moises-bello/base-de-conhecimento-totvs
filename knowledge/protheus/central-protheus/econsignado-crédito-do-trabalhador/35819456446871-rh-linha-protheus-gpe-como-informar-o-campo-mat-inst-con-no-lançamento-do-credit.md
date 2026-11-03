---
article_id: 35819456446871
category: eConsignado (Crédito do Trabalhador)
content_hash: b737e0f6640f4b497723f5a66faaa71d3badc55df04b336e7a1ce1badb5a731a
fetched_at: '2026-06-28T22:43:07.236075+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Como informar o campo Mat. Inst. Con, no lançamento
  do Credito do Trabalhador eConsignado
type: support-article
updated_at: '2025-10-22T22:24:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35819456446871-RH-Linha-Protheus-GPE-Como-informar-o-campo-Mat-Inst-Con-no-lan%C3%A7amento-do-Credito-do-Trabalhador-eConsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35819463538327) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como informar o campo Mat. Inst. Con, no lançamento do Credito do Trabalhador eConsignado?  
  
**Ambiente**  
TOTVS RH  - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
No lançamento do Credito do Trabalhador eConsignado, na rotina de Valores Futuros (GPEA110) o campo Mat. Inst. Con refere-se a Instituição Financeira que realizou o empréstimo para o funcionário.  Não existe uma consulta padrão para esse campo, com isso aceitará o que for preenchido pelo usuário manualmente ou se realizada a importação do arquivo pela rotina Credito do Trabalhador (GPEM944) será preenchido automaticamente conforme arquivo baixado do portal emprega Brasil.   
  
Esse campo precisa ser preenchido com a mesma instituição financeiras das informações do governo, que consta na tabela 37 para que não seja rejeitado pelo eSocial no momento do envio do evento. [eSocial - Tabelas](https://frontend.esocial.gov.br/adm/Home/Index)  
  
Se a instituição do empréstimo não constar na tabela 37, deve-se entrar em contato com o eSocial.

[RH - Linha Protheus - GPE - eSocial - eConsignado - Como funciona a contratação e regras gerais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30758384672151-RH-Linha-Protheus-GPE-eSocial-eConsignado-Como-funciona-a-contrata%C3%A7%C3%A3o-e-regras-gerais)  
[RH - Linha Protheus - GPE - eSocial - Como gerar valores referente ao eConsignado nos eventos de remuneração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27451839338263-RH-Linha-Protheus-GPE-eSocial-Como-gerar-valores-referente-ao-eConsignado-nos-eventos-de-remunera%C3%A7%C3%A3o)

**Saiba mais:**

[eConsignado - Credito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
