---
article_id: 360016357812
category: ADVPL - Ponto de Entrada
content_hash: dd7756914a0c0002cb65379a46a76669acf37cec62ac7957d3f6a41e734adca0
fetched_at: '2026-06-28T22:40:11.694429+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Geração de registros
  K200 / K230 / K235 via ponto de entrada SPDFISBLCK
type: support-article
updated_at: '2024-10-21T17:49:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016357812-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Gera%C3%A7%C3%A3o-de-registros-K200-K230-K235-via-ponto-de-entrada-SPDFISBLCK
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27224567485591)**Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como gerar os registros K200 / K230 / K235 via ponto de entrada SPDFISBLCK?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.80  
  
  
**Solução**Para os clientes que possuem a movimentação de produção em sistema de terceiros, o bloco K deve ser gerado pelo ponto de entrada SPDFISBLCK

**K200**

-Quando o tipo de estoque for 1 ou 2 deve existir o registro de referência na **SA1** ou **SA2**

-Quando o tipo de estoque for 1 ou 2 o COD\_PART deve ser definido com a nomenclatura da tabela + código + loja, exemplo "SA100000102" e o tamanho do campo **COD\_PART** no alias deve estar de acordo, exemplo:

```
nTamPar := 3 + TamSX3("A1_COD")[1] + TamSX3("A1_LOJA")[1]  
  
AADD(aCampos,{"COD_PART" ,"C",nTamPar,0}) //Campo 06 do registro K200
```

**K230 e K235**

-O produto deve estar cadastrado na base do **Protheus** para que seja gerado o registro **0200** de referência

-As informações do registro **0200** podem ser manipulada pelo ponto de entrada **SPEDPROD**

Documentação do ponto de entrada SPDFISBLCK: <https://tdn.totvs.com/pages/releaseview.action?pageId=723311922>Documentação do ponto de entrada SPEDPROD: <https://tdn.totvs.com/pages/viewpage.action?pageId=706922410>
