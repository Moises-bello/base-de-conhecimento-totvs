---
article_id: 8278008039063
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: ac3a83f889cf22faf9a14dd61ca0d8e6430d40c5cfd3f55501f2ab37a73288a3
fetched_at: '2026-06-28T22:42:00.875270+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS -   Arq. Magnéticos - O que é considerado
  para gerar o Tipo do Item no 0200 do Sped Fiscal?
type: support-article
updated_at: '2022-08-19T12:11:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8278008039063-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-O-que-%C3%A9-considerado-para-gerar-o-Tipo-do-Item-no-0200-do-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**O que é considerado para gerar o Tipo do Item no **Registro 0200 do Sped Fiscal**?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**O campo **07 - TIPO\_ITEM** do registro **0200** é gerado com base no conteúdo do campo **Tipo - B1\_TIPO.**  Assim, de acordo com a informação cadastrada no campo, o Protheus segue a seguinte tratativa:   
   
ME = 00 Mercadoria para revenda  
MP = 01 Matéria-prima  
EM = 02 Embalagem  
PP = 03 Produto em processo  
PA = 04 Produto acabado  
SP = 05 Subproduto  
PI = 06 Produto intermediário  
MC = 07 Material de uso e consumo  
AI = 08 Ativo Imobilizado  
SV = 09 Serviços  
OI = 10 Outros insumos  
   
Os novos tipos cadastrados são tratados como **99 - Outras.**  
   
Caso haja necessidade de que algum tipo seja considerado de forma  diferente do que foi cadastrado, será necessário considerar o ponto de entrada **SPDFIS001**  
  
<https://tdn.totvs.com/display/public/PROT/SPDFIS001+-+Trata+tipos+de+produtos>
