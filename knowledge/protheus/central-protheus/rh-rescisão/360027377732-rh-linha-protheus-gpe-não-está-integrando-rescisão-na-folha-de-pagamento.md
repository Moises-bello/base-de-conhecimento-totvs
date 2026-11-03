---
article_id: 360027377732
category: RH - Rescisão
content_hash: 8155d9f97ac06024cfc374f12132efe756e8d8b12a0bb96deb06fb5c75ad2616
fetched_at: '2026-06-28T22:43:52.234030+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Não está integrando rescisão na folha de pagamento
type: support-article
updated_at: '2025-06-26T11:49:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027377732-RH-Linha-Protheus-GPE-N%C3%A3o-est%C3%A1-integrando-rescis%C3%A3o-na-folha-de-pagamento
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33067299464087) Tempo aproximado para leitura: **00:01:30 min***

**Dúvida**Não está integrando rescisão na folha de pagamento  
  
**Ambiente**Protheus – Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Verifique no calculo da rescisão o campo Período;

Acesse o Cadastro de Períodos e verifique se este período corresponde a um período aberto, veja se o campo Ativo está com Sim;

Verifique também se existe data de integração, caso exista, faça o cancelamento desta integração em: Miscelânea -> Calculo -> Integração, selecione o Roteiro RES e cancele;

Faça a Integração do roteiro RES novamente;

Após isso, verifique se os dados estão na RGB em Lançamentos -> Por Funcionário
