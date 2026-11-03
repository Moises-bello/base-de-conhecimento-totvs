---
article_id: 4403566448279
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 12e52ad8d8a803ad7f848797faa5a3cdbc9170903c82b288414df45b1a779032
fetched_at: '2026-06-28T22:40:47.517519+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 ECF - Registro
  0010 Período de apuração do IRPJ e CSLL?  '
type: support-article
updated_at: '2022-01-19T13:52:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403566448279-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Per%C3%ADodo-de-apura%C3%A7%C3%A3o-do-IRPJ-e-CSLL
---

**Dúvida**

Como preencher o parâmetro Período de apuração do IRPJ e CSLL (FORMA\_APUR) para que seja gerado no Registro 0010,

 K030 ,[K155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055863753-MP-SIGACTB-ECF-K155-COMO-GERAR?source=search),[K156](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) , L030,[L100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054165034-MP-SIGACTB-ECF-L100-COMO-GERAR?source=search),[L300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-MP-SIGACTB-ECF-L300-COMO-GERAR?source=search) ,[M030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637214-MP-SIGACTB-LALUR-M030-COMO-GERAR?source=search),N030

Indicador do Período de Apuração do IRPJ e da CSLL:  
T – Trimestral  
A – Anual

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403556614039/mceclip0.png)

**Ambiente**  
Cross Segmento - TOTVS Backoffice  - Microsiga Protheus - Todas as versões  
  
**Solução**

Necessário verificar no manual da receita a regra para preenchimento do parâmetro

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403558437399/mceclip1.png)

Ao preencher  Período de Apuração FORMA\_APUR = “A”  os registros K030 ,[K155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055863753-MP-SIGACTB-ECF-K155-COMO-GERAR?source=search),[K156](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) , L030,[L100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054165034-MP-SIGACTB-ECF-L100-COMO-GERAR?source=search),[L300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-MP-SIGACTB-ECF-L300-COMO-GERAR?source=search) ,[M030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637214-MP-SIGACTB-LALUR-M030-COMO-GERAR?source=search),N030 serão gerados :   
A00 – Anual  
A01 – Rec. Bruta de janeiro /Balanço suspensão redução até janeiro  
A02 – Rec. Bruta de fevereiro /Balanço suspensão redução até fevereiro  
A03 – Rec. Bruta de março /Balanço suspensão redução até março  
A04 – Rec. Bruta de abril /Balanço suspensão redução até abril  
A05 – Rec. Bruta de maio /Balanço suspensão redução até maio  
A06 – Rec. Bruta de junho /Balanço suspensão redução até junho  
A07 – Rec. Bruta de julho /Balanço suspensão redução até julho  
A08 – Rec. Bruta de agosto /Balanço suspensão redução até agosto  
A09 – Rec. Bruta de setembro /Balanço suspensão redução até setembro  
A10 – Rec. Bruta de outubro/Balanço suspensão redução até outubro  
A11 – Rec. Bruta de novembro /Balanço suspensão redução até novembro  
A12 – Rec. Bruta de dezembro/Balanço suspensão redução até dezembro

Ao preencher  Período de Apuração FORMA\_APUR = “T”    os registros K030 ,K155,K156 ,M030,N030,P030 ,[P100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033885453-MP-SIGACTB-ECF-P100-COMO-GERAR-?source=search),[P150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033364654-MP-SIGACTB-ECF-P150-COMO-GERAR-?source=search)  
  
T01 – 1º Trimestre  
T02 – 2º Trimestre  
T03 – 3º Trimestre  
T04 – 4º Trimestre  
Regra: O período deve estar compreendido entre a data início e data fim da escrituração

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419591200407/mceclip0.png) Obs.: Em caso de duvidas quanto ao preenchimento dos parâmetros acesse o manual da Receita e ou contate a Receita

Veja como [Reg 0010 COMO GERAR OS REGISTRO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search)
