---
article_id: 1500005799442
category: TAF - REINF
content_hash: cd04edbb0a41d1762995e9061868d854eb2fd13b98ba0924d1f75119bd5a0d9c
fetched_at: '2026-06-28T22:41:34.633437+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Erro ao acessar no menu
  o Painel Reinf a tela fica em branco
type: support-article
updated_at: '2025-02-14T16:50:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005799442-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Erro-ao-acessar-no-menu-o-Painel-Reinf-a-tela-fica-em-branco
---

**Dúvida**

Ao acessar no menu o Painel Reinf a rotina fica em branco.

![B1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007814161/B1.png)

**Ambiente**

TAF - A partir de 12.1.23

**Solução**

**1 - Validar se a pasta http-root existe no rootpath, se não existir, criar;**

**2 - Validar se o Rest está no ar e com as API’s necessárias compiladas;**

Digitar na url do navegador o endereço e porta do Rest

![B2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007648102/B2.png)

 Verificar se as API’s necessárias estão compiladas no RPO

                 REPORTESOCIALBASECONFER – Serviço dos Relatórios de Conferência do eSocial

                 WSTAF001 – REINF

                 WSTAF002 – Apuração Reinf

                 WSTAF003 -  API Reinf - Funções genéricas

                 WSTAF004 -  Transmissão Reinf

                 WSTAF005 -  Acompanhamento Reinf

**3 - Validar se o HTTP está no ar:**

Na pasta http-root que fica dentro do RootPath, criar um arquivo chamado “teste.csv”;

Na url do servidor digitar: [http://SEUIP:PORTAHTTP/teste.csv](http://seuipportahttp/);

Se o HTTP estiver configurado corretamente, vai ser feito o download do arquivo teste.csv.

**4 - Validar se os artefatos do projeto estão dentro da pasta app-root, que fica dentro da pasta http-root:**

![B3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007648122/B3.png)

**5 - Validar o arquivo index.html da pasta preindex possui 91 linhas:**

![B4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500007814201/B4.png)
