---
article_id: 1500001247822
category: Escrita Fiscal - CIAP
content_hash: 33e45f22d576bfafc11cff2f51fc0b712fc382dbffb09da74369d705170a7558
fetched_at: '2026-06-28T22:39:33.876506+00:00'
product: protheus
section_id: 1500001538561
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como tratar componente
  no CIAP?
type: support-article
updated_at: '2021-07-29T12:54:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001247822-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-tratar-componente-no-CIAP
---

**Dúvida** Como tratar componente no CIAP?  
  
**Ambiente**Protheus - Compras -  A partir da versão 11.80  
  
**Solução**

•Para atender a geração dos registros G125 e 0300 do Sped Fiscal, foi incluída a opção de componentes na Manutenção CIAP (MATA905).  
•A definição do ativo com o tipo Bem ou Componente é realizada através da TES (F4\_COMPONE) ou diretamente pelo campo da SF9 nos casos de inclusão manual e após a inclusão de todos os componentes é criado o ativo principal (Junção) e vinculado ao bem principal o valor de ICMS de todos os bens que estão fazendo parte da composição.,

## **Composição do Bem Principal**

## A “Junção” é realizada através da rotina de manutenção CIAP.

•Componente A – Valor de ICMS = R$ 500,00  
•Componente B – Valor de ICMS = R$ 500,00

## **Criar o “Bem principal”:**

•Posicionar sobre um ativo tipo Componente – Ações relacionadas -> Ativo Principal.

## Após seguir este processo o sistema cria um bem que aguarda os valores de ICMS dos seus componentes.

## **Baixa dos Componentes**

## Baixar os ativos tipo Componente e compor com seus valores o bem principal:

•Em manutenção CIAP, selecionar o ativo tipo componente – Alterar e preencher o campo “C. Bem Principal” com o código do bem criado e salvar o cadastro.  
•  
•Em ações relacionas -> Componentes – Baixa componente.  
•

## Após realizar este procedimento o ativo tipo componente será baixado

## (Legenda Azul) e seu valor de ICMS (F9\_VALICMS) será agregado ao F9\_VALICMS do bem principal.

Obs.: Caso queira se apropriar dos componentes  MV\_APRCMP = T  
  
BOLETIM CIAP  
  
<http://tdn.totvs.com/pages/viewpage.action?pageId=187532625>
