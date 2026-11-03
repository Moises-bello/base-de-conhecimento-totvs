---
article_id: 30291826912919
category: eSocial - Gerar XML/ Integração Evento
content_hash: 654acc115eecd047233d28b6beb89fa79957bc7d4fa3f37281c0f47b06e5efcf
fetched_at: '2026-06-28T22:47:12.070223+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como será enviado ao governo os eventos de Valor
  a Deduzir de IRRF Simplificado
type: support-article
updated_at: '2026-03-03T18:09:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30291826912919-RH-RM-FOP-eSocial-Como-ser%C3%A1-enviado-ao-governo-os-eventos-de-Valor-a-Deduzir-de-IRRF-Simplificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30291826886039) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Como será enviado ao governo os eventos de Valor a Deduzir de IRRF Simplificado?  
  
**Ambiente**  
RH - RM - FOP - eSocial - A partir das versões 12.1.2402.255 12.1.2406.200 12.1.2410.130 12.1.2502 e Superiores  
  
**Causa**  
Foi criado novos códigos de cálculo no módulo Folha de pagamento para lançar o valor do desconto simplificado quando o mesmo for utilizado:

* [Código de Cálculo 477 - Valor a Deduzir de IRRF Simplificado Folha](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139184)
* [Código de Cálculo 478 - Valor a Deduzir de IRRF Simplificado Férias](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139208)
* [Código de Cálculo 479 - Valor a Deduzir de IRRF Simplificado 13º Salário](https://tdn.totvs.com.br/pages/viewpage.action?pageId=892139220)

O envio do evento de desconto de IRRF é obrigatório para a totalização do IRRF no evento S-5002, já o evento de dedução de IRRF, atualmente, é facultativo.

* Se a empresa quiser informar os valores indicados para cálculo do IRRF Simplificado, o eSocial criou no grupo **Dedução do rendimento tributável do IRRF** e, exige que a informação seja enviada através de rubrica com o **código de incidência 68 - Desconto Simplificado Mensal** quando o mesmo for utilizado (tabela 21). Este código deve ser utilizado para enviar um evento/verba informando que o colaborador teve o desconto simplificado, com o valor do dedutível utilizado conforme a tabela de valores fixos de finalidade Valor a deduzir no IRRF Simplificado vigente, por período/envelope lançado. Será necessário gerar o XML S-1010 e enviar ao governo;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30291803799063)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30291826887959)

* Caso a empresa não queira enviar ao governo estes eventos, os mesmos poderão ser informados no Parametrizador do eSocial, em **Configurações | Parametrizador | eSocial | Eventos a Desconsiderar**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30291826888855)

**Saiba mais**  
Para mais informações acesse:  
- [Códigos de Cálculo para lançar o valor do IRRF Simplificado em evento de Base para enviar para o S-1200](https://tdn.totvs.com/pages/releaseview.action?pageId=892139445)   
- [Cálculo do IRRF Simplificado](https://tdn.totvs.com/pages/releaseview.action?pageId=761006653#1-1)
