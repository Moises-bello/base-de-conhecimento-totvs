---
article_id: 360019401272
category: ADVPL - Ponto de Entrada
content_hash: f09bace2e77c16deae11e4f8be3cab554af602eb9358620911470f4e36ea9c89
fetched_at: '2026-06-28T22:40:12.921347+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Visualizar duplicata
  associada no documento de entrada quando o tipo é diferente de NF
type: support-article
updated_at: '2021-12-30T18:10:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019401272-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Visualizar-duplicata-associada-no-documento-de-entrada-quando-o-tipo-%C3%A9-diferente-de-NF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como visualizar uma duplicata associada no documento de entrada quando o tipo é diferente de NF?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**A rotina **MATA103** realiza a busca do título com base na variável pública **[MVNOTAFIS](http://tdn.totvs.com/pages/viewpage.action?pageId=184781323)**. Como no padrão o tipo de um título gerado por essa rotina nunca seria diferente de NF, a consulta que preenche o folder do financeiro assume essa condição para buscar o título associado, a consulta avalia SE2.E2\_TIPO = MVNOTAFIS. Este comportamento não pode ser alterado por ponto de entrada, porém como a **[MVNOTAFIS](http://tdn.totvs.com/pages/viewpage.action?pageId=184781323)**se trata de uma variável pública, é possível manipulá-la conforme necessidade através de um ponto de entrada antes da abertura do documento, o **[MT103NFE](http://tdn.totvs.com/display/public/PROT/MT103NFE)** por exemplo.

A seguir um exemplo isolado de como seria essa implementação, no caso do campo E2\_TIPO ser gravado sempre com o mesmo conteúdo do F1\_ESPECIE na geração do documento;

```
#Include 'Protheus.ch'  
  
User Function MT103NFE()  
If !INCLUI  
  MVNOTAFIS := Padr(SF1->F1_ESPECIE,TamSX3("E2_TIPO")[1])  
EndIf  
  
Return
```

**Atenção**: Ao sair da rotina, torna-se imprescindível o retorno da variável para seu conteúdo inicial, neste cenário, por exemplo, pode ser utilizado o ponto de entrada **[MT103FIM](http://tdn.totvs.com/pages/viewpage.action?pageId=6085406)**para essa finalidade.
