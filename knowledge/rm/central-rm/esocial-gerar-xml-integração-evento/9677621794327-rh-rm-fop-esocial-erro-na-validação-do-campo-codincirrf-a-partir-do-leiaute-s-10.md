---
article_id: 9677621794327
category: eSocial - Gerar XML/ Integração Evento
content_hash: 211bb22b3c0aa3f96e3ae5233ac922c272b5c4188c07832c7e03a278d5f53cd8
fetched_at: '2026-06-28T22:47:12.975242+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na validação do campo ''codIncIRRF'': A partir
  do leiaute S-1.0 a tag codIncIRRF não aceita o valor 00'
type: support-article
updated_at: '2024-06-12T11:47:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9677621794327-RH-RM-FOP-eSocial-Erro-na-valida%C3%A7%C3%A3o-do-campo-codIncIRRF-A-partir-do-leiaute-S-1-0-a-tag-codIncIRRF-n%C3%A3o-aceita-o-valor-00
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24127011792023) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar XML  do evento S-1010 é apresentada a mensagem **Erro na validação do campo 'codIncIRRF': A partir do leiaute S-1.0 a tag codIncIRRF não aceita o valor 00. Favor selecionar um valor válido no campo "Isento de IRRF" no cadastro de eventos.**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9961725520535)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões12.1.33.257, 12.1.34.156, 12.1.2205.101 e superiores.  
  
**Causa**Devido as novas regras do **leiaute S-1.0**  será necessário ajustar as incidências de IRRF com os códigos existentes na **Tabela 21 - Códigos de Incidência Tributária da Rubrica para o IRRF**.  
  
**Solução**Em 26/11/2021 foi disponibilizada a **Nota Orientativa S-1.0. 2021.06**, com informações sobre a vigência dos itens de tabela do eSocial indicando que, após o término do período de vigência, as rubricas dos eventos de Folha (S-1200, S-1210, S-2299, etc.) não serão aceitas caso o S-1010 vigente no governo não contenha **codIncIRRF** da **Tabela 21** do leiaute S-1.0. Ou seja, se foi enviado um S-1010 no leiaute 2.5 com o **codIncIRRF** que não exista no leiaute S-1.0, este S-1010 deverá ser atualizado.

Ainda conforme a Nota Orientativa, o **De/Para** a ser seguido na atualização das incidências das rubricas é o do quadro abaixo, **ficando à cargo da empresa definir a incidência específica a ser utilizada**:

![](https://tdn.totvs.com/download/attachments/630000929/image2022-5-17_8-58-47.png?version=1&modificationDate=1652788727687&api=v2)

Na documentação abaixo orientamos como **identificar as incidências** dos eventos no RM e como **ajustá-las**:

* [Nota Orientativa nº 06/2021 - Leiaute S-1.0 - Revisão da tabela “21 – Códigos de Incidência Tributária da Rubrica”](https://tdn.totvs.com/pages/releaseview.action?pageId=684996490)

**Saiba Mais**Para mais informações acesse: 

* [S-1010 - Tabela de Rubricas](https://tdn.totvs.com/pages/viewpage.action?pageId=605863561)
