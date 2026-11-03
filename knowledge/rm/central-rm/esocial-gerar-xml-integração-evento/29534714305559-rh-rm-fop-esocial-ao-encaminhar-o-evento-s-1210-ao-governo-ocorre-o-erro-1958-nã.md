---
article_id: 29534714305559
category: eSocial - Gerar XML/ Integração Evento
content_hash: 60deb5e05f2e902011152d1cb1a1233e40135023e66198f80d5efbbe3bec3f07
fetched_at: '2026-06-28T22:47:11.893234+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao encaminhar o evento S-1210 ao Governo ocorre
  o erro 1958: Não e permitido a recepção do evento referente a período de apuração
  maior ou igual a 2025-01-01 em versão anterior a S-1.3'
type: support-article
updated_at: '2025-01-27T18:29:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29534714305559-RH-RM-FOP-eSocial-Ao-encaminhar-o-evento-S-1210-ao-Governo-ocorre-o-erro-1958-N%C3%A3o-e-permitido-a-recep%C3%A7%C3%A3o-do-evento-referente-a-per%C3%ADodo-de-apura%C3%A7%C3%A3o-maior-ou-igual-a-2025-01-01-em-vers%C3%A3o-anterior-a-S-1-3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29534714137623) Tempo aproximado para leitura: **00:01:30 min****Ocorrência**Ao enviar o evento S-1210 para o Governo, ocorre o erro 1958: Não e permitido a recepção do evento referente a período de apuração maior ou igual a 2025-01-01 em versão anterior a S-1.3. Ação sugerida: Envie o evento para a versão S-1.3.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**O erro ocorre pois o Governo determina que o evento S-1210 com período de apuração 01/2025, deve ser encaminhado no Leiaute S-1.3. Conforme [Publicação da Versão S-1.3 dos Leiautes do eSocial e da Nota Técnica nº 04/2024 Revisada](https://www.gov.br/esocial/pt-br/noticias/publicacao-da-versao-s-1-3-dos-leiautes-do-esocial-e-da-nota-tecnica-no-04-2024-revisada)

**Solução**Para solucionar o erro, será preciso:  
1. Acesse Configurações | Parametrizador | eSocial | Configurações Gerais 1/7 e alterar o Leaiute para o S-1.3;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29534714220823)

2. Avance todas as páginas até sua conclusão;  
3. Após salvar o passo anterior, acesse o XML do evento e selecione gerar XML para que o mesmo atenda ao novo Leiaute S-1.3;  
4. E integre o evento com o Governo.

**Saiba mais**

Para maiores informações, acesse:  
[RH - RM - FOP - eSocial - Leiaute S-1.3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26091695488919-RH-RM-FOP-eSocial-Leiaute-S-1-3)
