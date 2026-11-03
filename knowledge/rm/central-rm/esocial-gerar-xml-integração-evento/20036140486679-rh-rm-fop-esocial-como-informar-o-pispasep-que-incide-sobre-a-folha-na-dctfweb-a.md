---
article_id: 20036140486679
category: eSocial - Gerar XML/ Integração Evento
content_hash: c31539ca48a0a3fca0e14f587beaff1a1e8407e8055b6866bef57d1c3e0afbbb
fetched_at: '2026-06-28T22:47:12.057446+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como informar o PIS/PASEP que incide sobre a folha
  na DCTFWEB através do S-1000
type: support-article
updated_at: '2026-04-17T18:08:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20036140486679-RH-RM-FOP-eSocial-Como-informar-o-PIS-PASEP-que-incide-sobre-a-folha-na-DCTFWEB-atrav%C3%A9s-do-S-1000
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20036111515927) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como informar o PIS/PASEP que incide sobre a folha na DCTFWEB através do S-1000?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.34.232, 12.1.2205.175, 12.1.2209.117 e Superiores.

**Solução**

Para informar PIS/PASEP na DCTFWeb é necessário enviar o Indicador de tributação sobre a folha de pagamento - PIS e COFINS como Sim, conforme validação do MOS.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20036140456087)**

O Indicador de tributação sobre a folha de pagamento - PIS e COFINS é gerado através do S-1000, sendo o valor válido **S**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20036111520919)

Para que o S-1000 seja gerado com a informação, realize os seguintes passos:  
1. Acesse **eSocial - Informações do Empregador - Informações Complementares**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20036111530263)

2. Acesse o gatilho do XML S-1000 na fila de **Eventos Não Periódicos** e ajuste a competência desejada para validade do evento;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20036111541015)

3. Gere o XML, confira se a tag gerou como **S;**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20036140467735)**

4. Integre o evento com o Governo.

• **Suspensão da exigibilidade do PIS/Pasep**

Conforme [notícia publicada pelo Governo](https://www.gov.br/esocial/pt-br/noticias/calculo-do-pis-pasep-sobre-a-folha-de-salarios-e-implementado-no-esocial-e-na-dctfweb), caso o contribuinte seja detentor de decisão judicial que suspenda a exigibilidade do PIS/Pasep, as **informações da suspensão** (processos e valores) **deverão ser prestadas diretamente na DCTFWeb**, pois o eSocial não trata a suspensão destes tributos.

**Importante**

Para que o governo acate a informação do PIS/PASEP no S-1000 é necessário o envio da informação no leiaute S-1.2.

Essa informação só conta em produção à partir do dia 22/01/2023.

O vencimento da DARF de PIS/PASEP sobre Folha de pagamento, até o momento não houve alteração. Sendo assim, continua para todo dia 25.

Cabe às empresas revisarem seu cadastro, não foi disponibilizado nenhuma modificação necessária no produto para atender a entrega da obrigação.

**Saiba mais**  
Para mais informações, acesse:   
- [Alterações S-1000-S-1.1](https://tdn.totvs.com/pages/releaseview.action?pageId=702813784)  
- [eSocial - PIS sobre a Folha de Pagamento](https://tdn.totvs.com/display/public/ConSeg/eSocial+-+PIS+sobre+a+Folha+de+Pagamento)  
- [RH - RM - FOP - eSocial - Como será considerado o salário maternidade no calculo do PIS?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22313707082775-RH-RM-FOP-eSocial-Como-ser%C3%A1-considerado-o-sal%C3%A1rio-maternidade-no-calculo-do-PIS)
