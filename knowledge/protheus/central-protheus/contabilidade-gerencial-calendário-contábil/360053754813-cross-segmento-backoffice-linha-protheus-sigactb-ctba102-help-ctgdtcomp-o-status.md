---
article_id: 360053754813
category: Contabilidade Gerencial - Calendário Contábil
content_hash: 33c871ad6dc0dc7c735447a2acd3850cf1e098eb2bda8947899059f5cba32ca7
fetched_at: '2026-06-28T22:41:03.376522+00:00'
product: protheus
section_id: 1500001537301
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 Help: CTGDTCOMP
  : O STATUS DESTE PERÍODO NÃO PERMITE DIGITAÇÃO'
type: support-article
updated_at: '2025-02-14T12:17:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053754813-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Help-CTGDTCOMP-O-STATUS-DESTE-PER%C3%8DODO-N%C3%83O-PERMITE-DIGITA%C3%87%C3%83O
---

**Ocorrência**

Help: CTGDTCOMP

Problema : O Status deste período não permite digitação.

Solução :Verifique o Status do calendário para essa data

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087459914)  
  
**Ambiente**

Microsiga Protheus – Contábil – A partir da versão 11.80  
  
**Solução**

1º Passo veja Status do calendário e amarração a moeda 

* [O intervalo de datas informadas não poderá ser processado.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020540691-MP-SIGACTB-CTBA102-O-intervalo-de-datas-informadas-n%C3%A3o-poder%C3%A1-ser-processado-?source=search)
* [Como abrir período contábil bloqueado/fechado para movimentação?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006722952-MP-SIGACTB-CTBA010-Como-abrir-per%C3%ADodo-cont%C3%A1bil-bloqueado-fechado-para-movimenta%C3%A7%C3%A3o-?source=search)

2º Para o correto funcionamento se faz necessário que as tabelas abaixo estejam devidamente populadas e com o mesmo compartilhamento

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087460534)  
Para mais detalhes verifique : 

<https://tdn.totvs.com/display/public/PROT/CTB0012_Compartilhamento_de_tabelas_SIGACTB>  
[Como alterar o compartilhamento de tabelas após bloqueio realizado a partir da LIB versão 20181015](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026077191-MP-SIGACTB-Como-alterar-o-compartilhamento-de-tabelas-ap%C3%B3s-bloqueio-realizado-a-partir-da-LIB-vers%C3%A3o-20181015?source=search)  
  
  
Caso ocorrência persista solicito que realize :

3 º Passo veja

* Em base teste
* Através da CTBA200 Amarração Moeda X calendário e exclua a amarração da moeda ao calendário

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087460634)

* Através da rotina de cadastro de calendário exclua o cadastro do calendário
* F12 selecione Assistente

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088602073)

* Selecione Incluir

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087462674)

* Selecione avançar

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088602853)

* Informe o período  e selecione avançar

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088604193)

* Selecione

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088604733)

* O sistema irá estruturar o calendário

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087463334)

* clicando em avançar seleciona  "Amarrar Calendário com Moedas"

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087463374)

* Selecione Finalizar

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087463454)

* Selecione avançar

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087463494)

* O sistema  apresenta a opção para selecionar as moedas que serão amarradas

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088604953)

* Confirme a alteração

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087463534)

4º  acesse as tabelas abaixo e veja se o sistema populou corretamente as tabelas com o cadastro

CTE - Moeda X Calendário  
CTG - Calendário Contábil  
CQD - Bloqueio do calendário Contábil  
CTO - Moeda cadastrada
