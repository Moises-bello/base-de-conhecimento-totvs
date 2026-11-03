---
article_id: 12452375321239
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 00f2dfb95d7edc138009ab18322384f795f10a40bad7d73df51cb71bb76b2532
fetched_at: '2026-06-28T22:42:03.629209+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Sped Fiscal
  - Registo E110 com valor zerado
type: support-article
updated_at: '2023-02-16T14:14:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12452375321239-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Registo-E110-com-valor-zerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao gerar o **Sped Fiscal**, o registro **E110 - Apuração do ICMS Operações Próprias** é gerado com valores zerados, ainda que haja dados na **Apuração do ICMS.****Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está incorreta na *wizard* de geração da **Apuração do ICMS/Sped Fiscal.**  
  
**Solução**

O registro **E110** é gerado com base nos valores da **Apuração do ICMS (Tabela CDH).** Dessa forma, primeiramente é preciso validar se há valores na **Apuração do ICMS.**   
Havendo dados na **CDH**, para que o incidente não ocorra, as seguintes perguntas na *wizard* de geração da **Apuração do ICMS**  devem estar conforme *print* abaixo:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12452137253783)

**Importante**   
Ainda que hajam **subapurações** (**Livro** diferente de \*), após rodar todas as **subapurações** é preciso rodar a Apuração com o **Livro \***.

Na *wizard* de geração do **Sped Fiscal**, a pergunta **Livro** também deve estar preenchida com **asterisco**, conforme *print* abaixo:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12452274197527)

**Importante:**

A filial informada na *wizard* de geração do **Sped Fiscal**, deve ser a mesma informada **Apuração do ICMS**

**Exemplo:**

Filial da **Apuração**:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12452317209879)

Filial no **Sped Fiscal:**

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12452348614935)
