---
article_id: 4419591453079
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: abae1a5bc973e6115cf5095955772c19e06ab767d3cd8f5b31f574960be2b4f3
fetched_at: '2026-06-28T22:40:48.883840+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 ECF - Registro
  0010 Tipo de pessoa Jur. Imune ou isenta
type: support-article
updated_at: '2022-01-19T16:26:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419591453079-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Tipo-de-pessoa-Jur-Imune-ou-isenta
---

**Dúvida**

Como preencher o parâmetro Tipo de pessoa Jur. Imune ou isenta( TIP\_ENT )  para que seja gerado no Registro 0010

Tipo de Pessoa Jurídica Imune ou Isenta:  
01 – Assistência Social  
02 – Educacional  
03 – Sindicato de Trabalhadores  
04 – Associação Civil  
05 – Cultural  
06 – Entidade Fechada de Previdência Complementar  
07 – Filantrópica  
08 – Sindicato  
09 – Recreativa  
10 – Científica  
11 – Associação de Poupança e Empréstimo  
12 – Entidade Aberta de Previdência Complementar (Sem Fins  
Lucrativos)  
13 – Fifa e Entidades Relacionadas  
14 – CIO e Entidades Relacionadas  
15 – Partidos Políticos  
99 – Outras.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419599180567/mceclip0.png)

**Ambiente** Cross Segmento - TOTVS Backoffice  - Microsiga Protheus - Todas as versões  
  
**Solução**

Necessário verificar no manual da receita a regra para preenchimento do parâmetro

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419605262743/mceclip2.png)

Observação: Este campo é obrigatório para 0010.[FORMA\_TRIB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403575196951-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-Tributa%C3%A7%C3%A3o?source=search) igual a “8” (Imune do IRPJ) ou “9” (Isenta do IRPJ).  
  
Caso 0010.TIP\_ENT = “01”, “02”, “03”, “04”, “05”, “07”, “08”, “09”, “10”, “13”, “14” ou “99”, os planos referenciais serão U100A e U150A.  
  
Caso 0010.TIP\_ENT = “11”, os planos referenciais serão U100B e U150B.  
Caso 0010.TIP\_ENT = “12”, os planos referenciais serão U100C e U150C.  
Caso 0010.TIP\_ENT = “06”, os planos referenciais serão U100D e U150D.  
Caso 0010.TIP\_ENT = “15”, os planos referenciais serão U100E e U150E

Esse parâmetro é específico para empresas tributadas pelo Lucro Presumido.

Preenchimento deste parâmetro irá refletir na geração dos blocos [0010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search) , [0020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016512051-MP-SIGACTB-Reg-0020-ECF-Erro-apresentado-no-validador-IND-ALIQ-CSLL?source=search) , [J050 ,J051](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) ,[U100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search), [U150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)

Exemplo :

Observação: Este campo é obrigatório para 0010.[FORMA\_TRIB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403575196951-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-Tributa%C3%A7%C3%A3o?source=search)  igual a “8” (Imune do IRPJ) ou “9” (Isenta do IRPJ).

Caso 0010.TIP\_ENT = “01”, “02”, “03”, “04”, “05”, “07”, “08”, “09”, “10”, “13”, “14” ou “99”, os planos referenciais serão U100A e U150A.  
Caso 0010.TIP\_ENT = “11”, os planos referenciais serão U100B e U150B.  
Caso 0010.TIP\_ENT = “12”, os planos referenciais serão U100C e U150C.  
Caso 0010.TIP\_ENT = “06”, os planos referenciais serão U100D e U150D.  
Caso 0010.TIP\_ENT = “15”, os planos referenciais serão U100E e U150E.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419591485463/mceclip4.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419599235479/mceclip3.png)

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419591200407/mceclip0.png)**Obs.: Em caso de duvidas quanto ao preenchimento dos parâmetros acesse o manual da Receita e ou contate a Receita
