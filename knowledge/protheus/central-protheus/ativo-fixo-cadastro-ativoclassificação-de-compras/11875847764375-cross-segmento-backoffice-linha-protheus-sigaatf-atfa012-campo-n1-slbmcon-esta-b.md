---
article_id: 11875847764375
category: Ativo Fixo - Cadastro Ativo/Classificação de Compras
content_hash: 7b45be1efd73c104026756196e0d3a89174e390dd302c2e2f4c22940fe10e268
fetched_at: '2026-06-28T22:41:48.475068+00:00'
product: protheus
section_id: 1500001547662
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus -SIGAATF ATFA012 campo N1_SLBMCON
  esta bloqueado
type: support-article
updated_at: '2024-05-09T14:30:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11875847764375-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-campo-N1-SLBMCON-esta-bloqueado
---

**Dúvida**

Ao incluir o bem (ATFA012)  o campo N1\_SLBMCON esta bloqueado , porem na classificação do bem (ATFA240) este campo é habilitado

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11875541624727)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Ativo Fixo – A partir da versão 12  
  
**Solução**

O campo N1\_SLBMCON só ficará habilitado para os bens ( [N3\_TIPO = 03 componentes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035878114-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-Tipos-de-ativo-campo-N3-TIPO-?source=search)) que possuem código de CIAP atrelado , e para que tenha o código do CIAP atrelado precisa ter sua origem do documento de entrada , devido o reflexo que esse cadastro trará no modulo e entres fiscais  
  
Esse tratamento foi criado em conjunto com o time do modulo fiscal conforme documentação abaixo 

Segundo a legislação 'Ato COTEPE/ICMS nº 09/2008  EFD ICMS / IP' é necessário ter um Bem do tipo 'bem em construção' cadastrado no módulo Ativo Fixo(**SIGAATF)**, este bem gerará um registro na tabela Manutenção Ciap(**SF9).**

A geração do bem final acumulará o saldo dos componentes amarrados a ele, atualizando o registro do bem em construção na tabela de Manutenção Ciap(**SF9).**

[**https://tdn.totvs.com/pages/releaseview.action?pageId=567740807**](https://tdn.totvs.com/pages/releaseview.action?pageId=567740807)
