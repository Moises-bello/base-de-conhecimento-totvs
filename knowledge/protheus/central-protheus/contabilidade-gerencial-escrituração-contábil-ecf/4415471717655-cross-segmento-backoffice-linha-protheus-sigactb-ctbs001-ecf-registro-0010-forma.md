---
article_id: 4415471717655
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 5ceda4a357b9add1f1ed03387597b78e6d5ef751b0c29adda55ead447304bc1f
fetched_at: '2026-06-28T22:40:48.860432+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 ECF - Registro
  0010 Forma de apura. da Estimativa??  '
type: support-article
updated_at: '2022-01-19T15:13:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415471717655-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-apura-da-Estimativa
---

**Dúvida**

Como preencher o parâmetro Forma de apura. da Estimativa?( MES\_BAL\_RED)  para que seja gerado no Registro 0010

Forma de Apuração da Estimativa Mensal: Indicação da forma de  
apuração da estimativa mensal, quando 0010.FORMA\_APUR = “A”, considerando o formato XXXXXXXXXXXX onde X é  referente a um mês e é igual a:  
  
0 – Fora do Período: Fora do período de apuração/ Forma de tributação diferente de “R” ou “E”.  
E – Receita Bruta: Estimativa com base na receita bruta e acréscimos.  
B – Balanço ou Balancete: Estimativa com base no balanço ou balancete de suspensão/redução.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415461194519/mceclip0.png)  
  
**Ambiente** Cross Segmento - TOTVS Backoffice  - Microsiga Protheus - Todas as versões   
  
**Solução**   
Necessário verificar no manual da receita a regra para preenchimento do parâmetro

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415486810647/mceclip1.png)

Os meses correspondentes a trimestres marcados em 0010.[FORMA\_TRIB\_PER](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415486620695-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-trib-no-Per%C3%ADodo-?source=search) como diferente de “R” e “E” devem estar preenchidos com zero “0”.  
Os meses correspondentes a trimestres marcados em 0010.[FORMA\_TRIB\_PER](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415486620695-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Forma-de-trib-no-Per%C3%ADodo-?source=search) iguais a “R” ou “E” devem estar preenchidos com “E” ou “B”.

Preenchimento deste parâmetro irá refletir na geração dos blocos [0010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search) , [0020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016512051-MP-SIGACTB-Reg-0020-ECF-Erro-apresentado-no-validador-IND-ALIQ-CSLL?source=search) , [J050 ,J051](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) , K030 ,[K155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055863753-MP-SIGACTB-ECF-K155-COMO-GERAR?source=search) , [K156](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) ,L030 , L100, L200, [L210,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051194493-MP-SIGACTB-ECF-L210-SEM-CENTRO-DE-CUSTO?source=search) [L300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-MP-SIGACTB-ECF-L300-COMO-GERAR?source=search), [M030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637214-MP-SIGACTB-LALUR-M030-COMO-GERAR?source=search), N030, N600, N610, N615 ..

Exemplo :

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415486958231/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415471881879/mceclip3.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419591200407/mceclip0.png) Obs.: Em caso de duvidas quanto ao preenchimento dos parâmetros acesse o manual da Receita e ou contate a Receita
