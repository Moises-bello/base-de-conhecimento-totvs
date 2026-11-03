---
article_id: 360018567332
category: PCO - Cadastros
content_hash: fd3b9acf732dcb81c6f46ed120d9c5f7544cb4fe0e1ec54b9c1bdd62106df1a9
fetched_at: '2026-06-28T22:37:12.923120+00:00'
product: protheus
section_id: 1500001550802
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO -Qual e o compartilhamento
  recomendável das tabelas do módulo SIGAPCO?
type: support-article
updated_at: '2023-11-24T12:58:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Qual-e-o-compartilhamento-recomend%C3%A1vel-das-tabelas-do-m%C3%B3dulo-SIGAPCO
---

**Dúvida**Qual e o compartilhamento recomendável das tabelas do módulo SIGAPCO

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
  
**Solução**

Conforme a necessidade de cada cliente não é recomendado modificar a situação de compartilhamento padrão das tabelas utilizadas no módulo Planejamento e Controle Orçamentário (SIGAPCO).

Caso seja necessário sua alteração é altamente recomendado a alocação de um analista Totvs ou um analista capacitado para que essa alteração seja efetuada e de forma a melhor atender cada estrutura.

Podemos considerar divisão das tabelas em dois grupos: **Cadastros** e **Movimentos/Saldos**, sendo assim as configurações possíveis são:

**CADASTROS         MOVIMENTOS/SALDOS**

Exclusivos               Exclusivos

Compartilhados     Exclusivos

Compartilhados     Compartilhados

**Importante**

As Tabelas Relativas ao Cubo Gerencial AL1, AL2, AL3 e AL4 devem possui o mesmo nível de compartilhamento das tabelas de Movimentos e Saldos ou seja deverá possui o mesmo compartilhamento da tabelas AKD e AKT.
