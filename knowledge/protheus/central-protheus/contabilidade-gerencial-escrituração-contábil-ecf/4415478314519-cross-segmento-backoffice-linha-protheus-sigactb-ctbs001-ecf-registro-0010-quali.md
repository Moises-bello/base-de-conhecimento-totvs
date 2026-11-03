---
article_id: 4415478314519
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: fc4d1bdbfce363aea9737760bb79e357468c3e34f2a92504029c8d106f474b2e
fetched_at: '2026-06-28T22:40:48.873615+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 ECF - Registro
  0010 Qualificação da Pessoa Jurídica?  '
type: support-article
updated_at: '2022-01-19T15:09:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415478314519-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Qualifica%C3%A7%C3%A3o-da-Pessoa-Jur%C3%ADdica
---

**Dúvida**

Como preencher o parâmetro Qualificação da Pessoa Jurídica(COD\_QUALIF\_PJ)  para que seja gerado no Registro 0010

Qualificação da Pessoa Jurídica:  
01 – PJ em Geral  
02 – PJ Componente do Sistema Financeiro  
03 – Sociedades Seguradoras, de Capitalização ou Entidade Aberta  
de Previdência Complementar

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415452728343/mceclip0.png)

**Ambiente**   
Cross Segmento - TOTVS Backoffice  - Microsiga Protheus - Todas as versões   
  
**Solução** 

Necessário verificar no manual da receita a regra para preenchimento do parâmetro

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415452754327/mceclip1.png)

Atenção: Não preencher no caso de imunes e isentas (preencher o  
0010.[TIP\_ENT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419591453079-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Tipo-de-pessoa-Jur-Imune-ou-isenta?source=search)).

Preenchimento deste parâmetro irá refletir na geração dos blocos [0010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search) , [0020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016512051-MP-SIGACTB-Reg-0020-ECF-Erro-apresentado-no-validador-IND-ALIQ-CSLL?source=search) , [J050 ,J051](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) , K030 ,[K155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055863753-MP-SIGACTB-ECF-K155-COMO-GERAR?source=search) , [K156](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) ,L030 ,L200, [L210,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051194493-MP-SIGACTB-ECF-L210-SEM-CENTRO-DE-CUSTO?source=search) [L300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-MP-SIGACTB-ECF-L300-COMO-GERAR?source=search), M010 , [M030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637214-MP-SIGACTB-LALUR-M030-COMO-GERAR?source=search) , M312 , M362 , X450 ,[Y570](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409779262487-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-como-gerar-o-registro-Y570?source=search) ..

Exemplo :

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415478088087/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415469853207/mceclip4.png)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415478169367/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415459925783/mceclip7.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419591200407/mceclip0.png) Obs.: Em caso de duvidas quanto ao preenchimento dos parâmetros acesse o manual da Receita e ou contate a Receita

Veja como [Reg 0010 COMO GERAR OS REGISTRO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search)
