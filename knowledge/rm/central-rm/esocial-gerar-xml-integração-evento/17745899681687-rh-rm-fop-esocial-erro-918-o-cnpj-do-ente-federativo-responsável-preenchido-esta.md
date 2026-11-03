---
article_id: 17745899681687
category: eSocial - Gerar XML/ Integração Evento
content_hash: ba87cd6176a58ea4879bad6b1d0ad546aa5667739ed404737ee4260c92ad6d8a
fetched_at: '2026-06-28T22:47:12.170815+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 918 - O CNPJ do Ente Federativo Responsável
  preenchido esta divergente do CNPJ cadastrado no Sistema CNPJ da RFB. '
type: support-article
updated_at: '2024-06-05T12:03:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17745899681687-RH-RM-FOP-eSocial-Erro-918-O-CNPJ-do-Ente-Federativo-Respons%C3%A1vel-preenchido-esta-divergente-do-CNPJ-cadastrado-no-Sistema-CNPJ-da-RFB
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17745892944023) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**Ao transmitir o evento S-1000ao governo é retornado o erro **918**:**Grupo O CNPJ do Ente Federativo Responsável preenchido esta divergente do CNPJ cadastrado no Sistema CNPJ da RFB. Ação Sugerida: Corrija a informação ou compareça a unidade local da RFB para regularizar a situação****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial -  Todas as versões  
  
**Causa**Este erro ocorre para o evento S-1000 **Informações do Empregador/Contribuinte/Órgão Público** quando a empresa tem a Natureza Jurídica de órgão público e o campo CNPJ do Ente Federativo está com o CNPJ inválido, diferente de um CNPJ válido cadastrado na Receita Federal.  
  
**Solução**Informar corretamente o CNPJ do Ente Federativo no cadastro do empregador, de acordo com o cadastro da RFB - Receita Federal do Brasil e seguindo as normas de validação disponíveis no leiaute do eSocial.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17745873666711)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17741551919255)

**Importante**Nos casos em que o CNPJ estiver informado corretamente, mas houver rejeição do evento, indicamos acionar o atendimento do governo para esclarecimentos, no link abaixo:

[RH - RM - FOP - eSocial - Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432?source=search)
