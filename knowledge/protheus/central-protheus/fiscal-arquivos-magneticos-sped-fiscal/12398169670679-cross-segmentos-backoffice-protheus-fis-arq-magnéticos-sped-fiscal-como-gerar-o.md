---
article_id: 12398169670679
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 24e75d8ec6292f358fa5fca012ef178d743e4cc96683251c750acd0754563f90
fetched_at: '2026-06-28T22:42:01.209601+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro C500 para NF3E (modelo 66)?
type: support-article
updated_at: '2023-02-14T13:48:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12398169670679-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-C500-para-NF3E-modelo-66
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar o registro **C500** com o **modelo 66** - **NF3E - NOTA FISCAL DE ENERGIA ELÉTRICA ELETRÔNICA?**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**Escriture um documento fiscal, utilizando a espécie **NF3e**, conforme *print* abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/DsGscciZ7MBObVCUFlOaY3nZe/?name=image.png)  
  
Ao informar a espécie e apresentar erro de **espécie não existente**, é preciso acessar o **Configurador** para criação da **espécie**.  
  
A **espécie** pode ser criada seguindo o processo do *print* abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/OuGu4TgDjgZWgiD4ylUCZxlPN/?name=image.png)  
  
1. Acesse módulo **Configurador**: **Ambiente -> Cadastro -> Tabela**  
  
2. Localize **Tabela 42** acesse, posicione na última linha, desce com a seta e inclua o registro, conforme caminho no *print* abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/f1xGYFDo56DNp1cp7CgkWHyeY/?name=image.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/w0yTIjHGNaipBxrq8f642vtWO/?name=image.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/ANLXNqiXqZum0Mm0hx9TE71JC/?name=image.png)  
  
  
Após realizar este processo, escriture a nota fiscal e gere o **Sped Fiscal** com cálculo de **Livro** na **TES**, assim o registro **C500** será apresentado.  
  
![](https://totvssuporte.zendesk.com/attachments/token/bF6ch9MPP1UoG6kZbbH2sACby/?name=image.png)
