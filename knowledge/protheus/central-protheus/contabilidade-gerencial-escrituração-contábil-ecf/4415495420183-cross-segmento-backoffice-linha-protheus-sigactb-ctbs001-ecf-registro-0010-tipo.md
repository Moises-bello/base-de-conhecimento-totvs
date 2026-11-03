---
article_id: 4415495420183
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 882ec659099c133c8e3345716846a990712f18377695e7ec1e4a5ee134f39f41
fetched_at: '2026-06-28T22:40:48.879078+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBS001 ECF - Registro
  0010 Tipo de escrituração?  '
type: support-article
updated_at: '2022-01-19T15:14:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415495420183-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-Registro-0010-Tipo-de-escritura%C3%A7%C3%A3o
---

**Dúvida**   
Como preencher o parâmetro Tipo de escrituração (TIP\_ESC\_PRET)  para que seja gerado no Registro 0010

Escrituração:  
  
C – Obrigada a entregar a ECD ou entrega facultativa (haverá recuperação dos dados).  
L – Não obrigada a entregar a ECD/Livro Caixa (Opção do Lucro Presumido - parágrafo único do art. 45 da Lei nº 8.981, de 1995).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419606229783/mceclip0.png)  
  
**Ambiente**   
Cross Segmento - TOTVS Backoffice  - Microsiga Protheus - Todas as versões  
  
**Solução**

Necessário verificar no manual da receita a regra para preenchimento do parâmetro

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415472231063/mceclip2.png)**

**Atenção:**- Este campo deve ser preenchido pelas pessoas jurídicas tributadas pelo lucro presumido e as imunes ou isentas.  
- Caso a pessoa jurídica entregue a ECD facultativamente e não queira recuperar os dados da ECD, deve utilizar a opção “L”.

Esse parâmetro é específico para empresas tributadas pelo Lucro Presumido.

Preenchimento deste parâmetro irá refletir na geração dos blocos [0010](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050634994-MP-SIGACTB-ECF-Reg-0010-COMO-GERAR-OS-REGISTRO?source=search) , [0020](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016512051-MP-SIGACTB-Reg-0020-ECF-Erro-apresentado-no-validador-IND-ALIQ-CSLL?source=search) , [J050 ,J051](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006756771-MP-SIGACTB-ECF-O-que-avaliar-quando-J050-e-J051-n%C3%A3o-%C3%A9-gerado?source=search) , [J100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035548174-MP-SIGACTB-ECF-J100-COMO-GERAR?source=search), K030 ,[K155](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055863753-MP-SIGACTB-ECF-K155-COMO-GERAR?source=search) , [K156](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search) ,L030 ,L200, [L210,](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051194493-MP-SIGACTB-ECF-L210-SEM-CENTRO-DE-CUSTO?source=search) [L300](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054288214-MP-SIGACTB-ECF-L300-COMO-GERAR?source=search), M010 , [M030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053637214-MP-SIGACTB-LALUR-M030-COMO-GERAR?source=search) , [P100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033885453-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECF-P100-COMO-GERAR-?source=search), [P150](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033364654-MP-SIGACTB-ECF-P150-COMO-GERAR-?source=search), [Q100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125451-MP-SIGACTB-ECF-Bloco-Q?source=search), [U100](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search), Y672...

Exemplo :

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415495212055/mceclip3.png)**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415495220247/mceclip4.png)**

O preenchimento do parâmetro influencia em diversos blocos , veja alguns deles (para mais informações verifique no manual da receita)

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415487370391/mceclip6.png)**

**![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4415495327767/mceclip7.png)**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419591200407/mceclip0.png) Obs.: Em caso de duvidas quanto ao preenchimento dos parâmetros acesse o manual da Receita e ou contate a Receita**

**Saiba mais:**

[ERRO PVA -TIP\_ESC\_PRE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006982951-MP-SIGACTB-ECF-ERRO-PVA-TIP-ESC-PRE?source=search)

[Bloco Q](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007125451-MP-SIGACTB-ECF-Bloco-Q?source=search)

[ECF – IMUNE OU ISENTA COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047581974-MP-SIGACTB-ECF-IMUNE-OU-ISENTA-COMO-GERAR?source=search)

[ECF – Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
