---
article_id: 1500004085382
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 8b8c074efdf3c58942901330dbc4e344a89480d16cd84300bd16331c81d09071
fetched_at: '2026-06-28T22:38:29.790738+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - É possível gravar o campo
  F2_DTLANC somente quando há dados para contabilizar ?
type: support-article
updated_at: '2025-02-19T10:54:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004085382-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-%C3%89-poss%C3%ADvel-gravar-o-campo-F2-DTLANC-somente-quando-h%C3%A1-dados-para-contabilizar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30084462511383)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**É possível gravar o campo F2\_DTLANC somente quando há dados para contabilizar?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**O campo "Data do Lançamento Contábil (**F2\_DTLANC)"** sempre será atualizado com a data de processamento, mesmo que não seja gerado lançamento contábil na tabela CT2. Esse procedimento é utilizado para evitar reprocessamento indevidos de movimentos já avaliados pela rotina.

Existe a opção de contorno utilizando o ponto de entrada **CTNFSFIL**, segue exemplo de utilização do ponto (o cliente deverá aplicar a regra correta para o seu cenário):

```
User Function CTNFSFIL()

Local cFilAux := ParamIxb[1]
Local lRet := .T.

If "RPS" $ (cFilAux)-F2_ESPECIE
lRet := .F.
EndIf

Return lRet
```

**OBSERVAÇÃO:** O retorno falso não contabiliza.

Se caso não estiver gravando a contabilização, verifique a documentação abaixo:  
**[Cross Segmento - Backoffice Linha Protheus - SIGACTB - MV\_CTBFLAG - Marcação de Flags na Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000600247-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-MV-CTBFLAG-Marca%C3%A7%C3%A3o-de-Flags-na-Contabiliza%C3%A7%C3%A3o)**

**Saiba mais:**

**[Integração Faturamento X SigaCtb (SIGAFAT)](https://tdn.totvs.com/x/W2nXIQ)**
