---
article_id: 360037421594
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 6cd12852329f5e7bb40b665e7388e472f61ffaa35335f63ab5cc7e28d47d1b0c
fetched_at: '2026-06-28T22:42:02.354819+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - O campo 02 - COD_CCUS do registro 0305 está em branco
type: support-article
updated_at: '2025-02-11T21:21:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037421594-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-O-campo-02-COD-CCUS-do-registro-0305-est%C3%A1-em-branco
---

**Dúvida**Por que o campo 02 - COD\_CCUS do registro 0305 do Sped Fiscal não está sendo preenchido?  
   
 **Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80.  
  
**Solução**O registro 0305 contém as informações sobre a utilização do bem, portanto:  
  
Se o ativo foi incluído através da rotina Documento de Entrada (**MATA103**) e o campo **F9\_ROTINA = MATA103** é necessário verificar se o campo **B1\_CC** está preenchido no cadastro do produto.

Porém, se o ativo foi incluído através da rotina Manutenção CIAP (**MATA905**) e o campo **F9\_ROTINA = MATA905,** então, é necessário criar na tabela SF9 o campo F9\_CC. É neste campo que deverá ser informado o Centro de Custo que deve ser um Centro de Custo válido na tabela CTT (**CTT\_CUSTO**). Neste caso, é preciso também realizar a amarração do campo **F9\_CC** no parâmetro **MV\_F9CC**.

Configuração para criar o campo:  
Campo: F9\_CC  
Tipo: Caracter  
Tamanho: 9  
Decimal: 0  
Formato: @!  
Contexto: Real  
Titulo: C. Custo     
Texto: Informa centro de custo  
Help: Informação do centro de custo para preenchimento do campo 02 COD\_CCUS registro 0305 SPED FISCAL.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049949133/mceclip1.png)
