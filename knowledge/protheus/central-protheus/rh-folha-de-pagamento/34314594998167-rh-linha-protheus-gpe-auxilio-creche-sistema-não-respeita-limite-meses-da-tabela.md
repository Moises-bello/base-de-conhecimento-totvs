---
article_id: 34314594998167
category: RH - Folha de Pagamento
content_hash: bfea12fc60340bfcc58d377d203d4f09e2e783a26cb43adef8c234c3cd7c45ba
fetched_at: '2026-06-28T22:44:17.062950+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Auxilio Creche - Sistema não respeita limite meses
  da tabela S015
type: support-article
updated_at: '2025-09-03T21:21:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34314594998167-RH-Linha-Protheus-GPE-Auxilio-Creche-Sistema-n%C3%A3o-respeita-limite-meses-da-tabela-S015
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34314571630487) Tempo aproximado para leitura: 00**:05:00 min.**  
  
**Dúvida**  
Sistema esta calculando Auxilio Creche mesmo que o Limite Meses esteja devidamente preenchido na S015  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2210

**Causa**

Este incidente acontece quando a S015 esta devidamente preenchida mas o valor do Auxilio Creche no cadastro de Dependentes (SRB) também esta preenchido (RB\_VLRCRE)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314594985367)

**Solução**

**Para que não ocorra este problema o campo RB\_VLRCRE deve ficar em branco e a tabela S015 preenchida corretamente com o sindicato, para considerar o valor do Auxilio Creche e o Limite Meses corretamente**

**Cadastro S015**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314594986647)**

**Cadastro Dependentes**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34314571633303)**

**Observação:** Ao preencher o campo RB\_VLRCRE (Dependentes), o sistema não faz mais o controle automático (S015) referente ao campo Limite Meses. Para casos que o RB\_VLRCRE esteja preenchido o correto seria também o preenchimento do campo RB\_DTBAIXA para que o sistema entenda que o pagamento não deve mais ser efetuado.
