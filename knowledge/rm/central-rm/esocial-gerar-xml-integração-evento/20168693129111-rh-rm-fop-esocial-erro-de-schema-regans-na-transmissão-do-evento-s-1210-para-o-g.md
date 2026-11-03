---
article_id: 20168693129111
category: eSocial - Gerar XML/ Integração Evento
content_hash: aec5f26605989a7b1ea7d2819176a062c9f9fdcf884453153cc9d8b6f22e2ce0
fetched_at: '2026-06-28T22:47:12.918623+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Erro de Schema regANS na transmissão do evento S-1210
  para o Governo (S-1.2)
type: support-article
updated_at: '2026-06-01T17:25:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20168693129111-RH-RM-FOP-eSocial-Erro-de-Schema-regANS-na-transmiss%C3%A3o-do-evento-S-1210-para-o-Governo-S-1-2
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20168693099927) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao integrar o evento S-1210 com o governo retorna o Erro de schema: Element '{[http://www.esocial.gov.br/schema/evt/evtPgtos/v\_S\_01\_02\_00}regANS':](http://www.esocial.gov.br/schema/evt/evtPgtos/v_S_01_02_00%7DregANS':) [facet 'pattern'] The value 'XXXXX-' is not accepted by the pattern '\d{6}'.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168705651223)**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.23 e Superiores.  
  
**Causa**  
O erro ocorre quando o número da ANS não consta válido no Registro na Agência Nacional de Saúde - ANS e com 6 dígitos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168705654679)

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **eSocial | Operadora de Saúde | Cadastro Operadoras de Saúde**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168705660311)

2. Identifique a Operadora de Saúde que foi gerada no XML **S-1210;**

XML S-1210

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168693107351)

Operadora de Saúde

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20168693108887)

3. Verifique se o Registro ANS consta cadastrado corretamente, no exemplo acima, é necessário excluir o item "-" e informar mais um número;

4. Após a correção, regere o XML S-1210.

**Importante:**  
Caso o número da ANS conste cadastrado corretamente e mesmo assim o erro persista, será necessário entrar em contato a Agência Nacional de Saúde Suplementar - ANS para conferir se há alguma atualização no Registro ANS, ou entrar em contato com o governo. Abaixo os canais de comunicação:

* [Núcleos da ANS;](https://www.gov.br/ans/pt-br/canais_atendimento/nossos-enderecos)
* [RH - RM - FOP - eSocial - Contato com o Governo para dúvidas sobre os eventos do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432?source=search).
