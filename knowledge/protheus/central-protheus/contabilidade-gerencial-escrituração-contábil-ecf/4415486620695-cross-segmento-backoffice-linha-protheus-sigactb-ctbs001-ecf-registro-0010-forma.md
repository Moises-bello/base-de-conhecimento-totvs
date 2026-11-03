---
article_id: 4415486620695
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 334d5b085bcd5d51e3c078dbb0ef317c8a51eaeb33fa59d53d2428534474632e
fetched_at: '2026-06-28T22:40:48.864751+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 ECF - Registro
  0010 Forma de trib. no Período ?  '
type: support-article
updated_at: '2022-01-19T15:18:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415486620695-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-trib-no-Per%C3%ADodo
---

**Dúvida**

Como preencher o parâmetro Forma de trib. no Período(FORMA\_TRIB\_PER))  para que seja gerado no Registro 0010

Forma de Tributação no Período: Forma de tributação no período  
considerando para cada trimestre no formato XXXX onde X é igual  
a:  
0 – ZERO – Não informado – trimestre não compreendido no  
período de apuração.  
R – Real  
P – Presumido  
A – Arbitrado  
E – Real Estimativa (somente utilizado no caso da observação  
abaixo).

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415479105687/mceclip1.png)  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice - Microsiga Protheus - Todas as versões   
  
**Solução**   
Necessário verificar no manual da receita a regra para preenchimento do parâmetro

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415479102231/mceclip0.png)

E – Real Estimativa (somente utilizado no caso da observação  
abaixo).  
Observação: Caso 0010.[FORMA\_TRIB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403575196951-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-Tributa%C3%A7%C3%A3o?source=search) seja igual “3” (Presumido/Real) ou “4” (Presumido/Real/Arbitrado) e houver opção pelo REFIS (0010.OPT\_REFIS), o período tributado pelo lucro real deve ter somente a forma de apuração trimestral (Caso em que deve ser utilizado “R” em 0010.FORMA\_TRIB\_PER) ou somente a forma de apuração correspondente à anual/estimativa (Caso em que deve ser utilizado “E” em 0010.FORMA\_TRIB\_PER)

Preenchimento deste parâmetro irá refletir na geração dos blocos [0010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search) , [0020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016512051-MP-SIGACTB-Reg-0020-ECF-Erro-apresentado-no-validador-IND-ALIQ-CSLL?source=search) , [J050 ,J051](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) , K030 ,[K155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055863753-MP-SIGACTB-ECF-K155-COMO-GERAR?source=search) , [K156](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) ,L030 ,L200, [L210,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051194493-MP-SIGACTB-ECF-L210-SEM-CENTRO-DE-CUSTO?source=search) [L300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-MP-SIGACTB-ECF-L300-COMO-GERAR?source=search), M010 , [M030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637214-MP-SIGACTB-LALUR-M030-COMO-GERAR?source=search) ,M350 , M312 , M362,  P030, , T030, T120, T150, T170, T181 ..

Exemplo :

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415470998807/mceclip5.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415471037207/mceclip7.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419591200407/mceclip0.png) Obs.: Em caso de duvidas quanto ao preenchimento dos parâmetros acesse o manual da Receita e ou contate a Receita
