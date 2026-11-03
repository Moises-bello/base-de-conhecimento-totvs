---
article_id: 360018469372
category: PCO - Cubos
content_hash: 823d961af21394279a5d44c66c537b8528b176a0deb0b85cec816224d7d37aec
fetched_at: '2026-06-28T22:37:11.550260+00:00'
product: protheus
section_id: 1500001550862
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - Quais os tipos de atualização
  do cubo.
type: support-article
updated_at: '2023-11-21T13:03:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018469372-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Quais-os-tipos-de-atualiza%C3%A7%C3%A3o-do-cubo
---

**Dúvida**Quais os tipos de atualização do cubo?

**Ambiente**Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

Existem 3 formas de processar os saldos do Cubo Orçamentário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19209783226903)

**1º** ON-LINE: Ao executar um processo que movimente a tabela AKD o saldo do cubo será atualizado;

**2º** VIA JOB: Ao executar a rotina de reprocessamento o sistema irá travar a tabela AKD para gravação, os valores movimentados durante o reprocessamento serão gravados na tabela ALA (como um espelho da AKD) e conforme o período definido no parâmetro: MV\_PCOJOB1 o sistema irá copiar os dados gravados na ALA para a tabela AKD, todo movimento já copiado será controlado pelo campo ALA\_STATUS (para evitar duplicidade).

**3°** OFF-LINE: Ao executar um processo de integração que movimente a tabela AKD de movimentos a tabela AKT não será atualizada no mesmo momento, sendo necessário realizar o reprocessamento de saldos, para que os saldos fiquem atualizados de forma correta.

**Obs**: Quando Optada por este modo, não será possível utilizar bloqueio.

Para efetuar a carga do cubo o usuário precisa obrigatoriamente executar o reprocessamento do cubo.

Saiba Mais:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGAPCO: PCOA193 Exemplo de como configurar um Cubo Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018810031-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAPCO-PCOA193-Exemplo-de-como-configurar-um-Cubo-Gerencial?source=search)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Configuração do Cubo Gerencial Simples - Utilização PCO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4584114767895-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Configura%C3%A7%C3%A3o-do-Cubo-Gerencial-Simples-Utiliza%C3%A7%C3%A3o-PCO-?source=search)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - CheckList para utilização do modulo Planejamento de Custos Orçamentários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038998854-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-CheckList-para-utiliza%C3%A7%C3%A3o-do-modulo-Planejamento-de-Custos-Or%C3%A7ament%C3%A1rios?source=search)

[Cross Segmentos - Backoffice Linha Protheus - SIGAPCO - PCOA300 - Reprocessamento dos Saldos, Cubos Gerenciais.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028088012-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAPCO-PCOA300-Reprocessamento-dos-Saldos-Cubos-Gerenciais-?source=search)
