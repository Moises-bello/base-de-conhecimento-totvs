---
article_id: 31988354717847
category: eSocial - Gerar XML/ Integração Evento
content_hash: 4a71ebbd02fa88747d1287142d2635437ffea1283c5652eaa2e8438f4cae7a9e
fetched_at: '2026-06-28T22:47:12.285038+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro de Schema instFinanc na transmissão dos eventos
  S-2299/S-1200 com o Governo
type: support-article
updated_at: '2026-05-26T19:32:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31988354717847-RH-RM-FOP-eSocial-Erro-de-Schema-instFinanc-na-transmiss%C3%A3o-dos-eventos-S-2299-S-1200-com-o-Governo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31988319983383) Tempo aproximado para leitura: **00:04:00 min**  
  
**Ocorrência**  
Ao transmitir S-2299 ao Governo é apresentada a mensagem **Erro de schema: Element '{http://www.esocial.gov.br/schema/evt/evtDeslig/v\_S\_01\_03\_00}instFinanc': [facet 'pattern'] The value '79' is not accepted by the pattern '\d{3}'.**  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro ocorre quando existe desconto de empréstimo relacionado ao Crédito do Trabalhador nos XML's S-1200/S-2299, e foi informado no cadastro do empréstimo, no campo 'Código do banco concedente do empréstimo' um código com 2 dígitos, porém conforme o leiaute do eSocial S-1.3 NT 03/2025, é necessário informar um código com 3 dígitos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988319985047)

Segue o trecho do leiaute demonstrando a obrigatoriedade de 3 dígitos:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31988319988119)

**Solução**  
Para solucionar o erro de schema, realize os seguintes passos:  
  
1. Acesse **Administração de Pessoal | Anexos | Folha de Pagamento | Empréstimos**  
2. Selecione o empréstimo do Crédito do Trabalhador  
3. Ajuste o campo **Código do banco concedente do empréstimo**, informando um código com 3 dígitos  
4. Localize o evento com erro, e regere-o antes de enviar.

**Saiba Mais:**

No link abaixo, você encontrará o link para a Tabela 37 do eSocial onde constam os códigos de Banco de acordo com o Banco Central:  
[Tabelas do eSocial](https://frontend.esocial.gov.br/adm/Home/Index)
