---
article_id: 360026887011
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 567c5b1b6c5ab6cb5d7bbda227c74b7380a12dd66a5e5425396f4c50b77f0e26
fetched_at: '2026-06-28T22:39:44.301278+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus  - SIGAEIC - Numeração dos
  titulos gerados a partir do SIGAEIC
type: support-article
updated_at: '2021-08-31T11:55:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026887011-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Numera%C3%A7%C3%A3o-dos-titulos-gerados-a-partir-do-SIGAEIC
---

**Dúvida**

Onde são armazenadas a numeração, referente os títulos do SIGAEIC?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões.

**Solução**

O parâmetro MV\_EICNUMT  controla se a numeração dos títulos deve ser feita pelos campos das tabelas de Comex (1) EWQ, ou (2)numeração sequencial Protheus.

Campos utilizados para sequenciamento:  
Título da Invoice   W9\_NUM          - Nº.Titulo            
Título do Frete      W6\_NUMDUPF   - Nº Título Frete.           
Título do Seguro    W6\_NUMDUPS   - Nº Título Seguro.  
Título de despesas WD\_CTRFIN1    - Nº Título de despesas.

MV\_DUPLDOC  -  O parâmetro pode ser configurado para que o título no financeiro seja o mesmo número informado na Invoice, para isso a 3ª letra deve ser "I", indicando que o número do título e invoice serão os mesmos.   
  
Exemplo:  
MV\_DUPLDOC com conteúdo 'SRI'

Demais posições do parâmetro MV\_DUPLDOC:  
A primeira posição "S" indica se o número dos títulos gerados será o número do Documento WD\_DOCTO caso este esteja preenchido, caso WD\_DOCTO esteja em branco seguira a configuração do parâmetro MV\_EICNUMT.

A Segunda posição  pode ser "R" ou "L", sendo "R":  
Irá gravar o número do titulo pegando o conteúdo do campo W9\_INVOICE da direta para esquerda de acordo com o tamanho do campo E2\_NUM;

Caso "L" irá gravar o número do titulo pegando o conteúdo do campo W9\_INVOICE da esquerda para direita de acordo com o tamanho do campo E2\_NUM;
