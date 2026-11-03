---
article_id: 24240402771223
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 7bdd9e7b1d9a05cefdc1debba0274a92600b7eb8982deca15b14338e85c870ba
fetched_at: '2026-06-28T22:42:01.229371+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro E112 no Sped Fiscal?
type: support-article
updated_at: '2024-06-17T20:20:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24240402771223-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-E112-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24240391710871) Tempo aproximado para leitura: **00:02:00 min****Dúvida:**Como gerar o registro **E112** no **Sped Fiscal**?  
  
**Ambiente:**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução:**

**1-** Acesse a **MATA967** - **Processos Referenciados**e cadastre o processo.

**2**- Acesse a **MATA953**, crie uma nova linha de acordo com o código de lançamento que irá utilizar (outros créditos/débitos) onde apresentará o **Lanc = M:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24240391712407)

**3**- No campo "**Processo**" ao lado do "**M**", digite manualmente o código do processo criado (pela rotina **MATA967**) (não utilize à lupa, digite o número) e também o **Tipo** e **número do item**:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24240391713559)

**4-** Gere o **Sped Fiscal**, o registro será apresentado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24240402757527)

Abaixo anexado vídeo para ajuda visual:
