---
article_id: 17096949945623
category: eSocial - Gerar XML/ Integração Evento
content_hash: 472c28b152fdab17705b4a51e3db3ef272939433b7c69cc9f60e89cffe3e9df3
fetched_at: '2026-06-28T22:47:12.039611+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Como gerar os eventos S-2231 ou S-2300 para funcionário
  cedido temporariamente para outro órgão
type: support-article
updated_at: '2025-07-02T17:58:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17096949945623-RH-RM-FOP-eSocial-Como-gerar-os-eventos-S-2231-ou-S-2300-para-funcion%C3%A1rio-cedido-temporariamente-para-outro-%C3%B3rg%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17096935051415) Tempo aproximado para leitura: **00****:02:00 min****Dúvida**Como gerar os eventos S-2231 ou S-2300 para funcionário cedido temporariamente para outro órgão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões.  
  
**Solução**

* **Na empresa cedente - Evento S-2231**1. Acesse o menu **RH | Folha de Pagamento | Administração de Pessoal | Funcionários**, identifique o funcionário desejado, acesse **Situação**, realize o cadastro do afastamento e salve;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17117005638423)

2. Após acesse **Históricos | Histórico de afastamentos | eSocial**, o Sistema ira habilitar os dados do trabalhador cedido;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17117134488983)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17117766128791)

3. Ao gerar o XML na fila de eventos, o sistema irá trazer as seguintes *tags* no evento S-2231.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17117267931159)

* **Na empresa cessionária - Evento S-2300**1. Ao admitir o funcionário com o código de categoria eSocial **410-Trabalhador cedido - informação prestada pelo Cessionário** o sistema irá habitar uma nova aba com os dados da Cessão;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17116883094295)

2. Em **Dados da Cessão** preencha os dados da empresa cedente;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17116865456791)

3. Ao gerar o XML na fila de eventos, sistema irá trazer as seguintes tags no evento S-2300.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17116747076887)

**Importante**Para funcionários cedidos a empresa cessionária deverá encaminhar o S-2300 e não o S-2200.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17097899750295)

**Saiba mais**Para saber mais consulte o link abaixo:  
- [S-2231 - Cessão/Exercício em Outro Órgão;](https://tdn.totvs.com.br/display/public/LRM/DT+Trabalhador+Cedido)
