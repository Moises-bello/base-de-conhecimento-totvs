---
article_id: 6351933093527
category: eSocial - Cadastros
content_hash: 91a84c2dbae3537b9e73f6d45d57d740f6eaf1d4e992e89265b76e89149f22fe
fetched_at: '2026-06-28T22:47:14.532130+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Nota Orientativa nº 06/2021 - Ajuste de incidências
  de IRRF conforme Tabela 21
type: support-article
updated_at: '2024-06-26T14:33:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6351933093527-RH-RM-FOP-eSocial-Nota-Orientativa-n%C2%BA-06-2021-Ajuste-de-incid%C3%AAncias-de-IRRF-conforme-Tabela-21
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24446166093079) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como ajustar incidências de IRRF conforme Tabela 21, enviando corretamente a informação na tag **codIncIRRF** do evento S-1010?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões12.1.33.257, 12.1.34.156, 12.1.2205.101 e superiores.  
  
**Solução**Em 26/11/2021 foi disponibilizada a **Nota Orientativa S-1.0. 2021.06**, com informações sobre a vigência dos itens de tabela do eSocial indicando que, após o término do período de vigência, as rubricas dos eventos de Folha (S-1200, S-1210, S-2299, etc.) não serão aceitas caso o S-1010 vigente no governo não contenha **codIncIRRF** da **Tabela 21** do leiaute S-1.0. Ou seja, se foi enviado um S-1010 no leiaute 2.5 com o **codIncIRRF** que não exista no leiaute S-1.0, este S-1010 deverá ser atualizado.

Ainda conforme a Nota Orientativa, o **De/Para** a ser seguido na atualização das incidências das rubricas é o do quadro abaixo, ficando à cargo da empresa definir a incidência específica a ser utilizada:

![](https://tdn.totvs.com/download/attachments/630000929/image2022-5-17_8-58-47.png?version=1&modificationDate=1652788727687&api=v2)

Na documentação abaixo orientamos como **identificar as incidências** dos eventos no RM e como **ajustá-las**:

* [Nota Orientativa nº 06/2021 - Leiaute S-1.0 - Revisão da tabela “21 – Códigos de Incidência Tributária da Rubrica”](https://tdn.totvs.com/pages/releaseview.action?pageId=684996490)

Caso seja necessário o ajuste de alguma incidência, será gerado um gatilho do S-1010 na fila de eventos do eSocial. É importante que seja realizado a edição do gatilho e alterado o campo **Competência** para o mês e ano **igual ou anterior** ao período de apuração que serão enviados os eventos da Folha. Dessa forma, a tag ***iniValid*** irá gerar corretamente o início de validade da incidência.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6426955516439)

**Importante**  
É necessário que os eventos de Folha sejam reenviados após o ajuste do S-1010.  
  
**Saiba Mais**Para mais informações acesse:  
[- S-1010 - Tabela de Rubricas](https://tdn.totvs.com/pages/viewpage.action?pageId=605863561)
