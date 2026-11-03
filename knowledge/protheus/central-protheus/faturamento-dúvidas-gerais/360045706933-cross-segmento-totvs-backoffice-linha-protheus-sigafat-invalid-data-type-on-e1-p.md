---
article_id: 360045706933
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 9573a1e3896c82b96e16939bd289c4049c042ef4c09a238a78e80d1671cf732a
fetched_at: '2026-06-28T22:38:28.588961+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Invalid data
  type on (E1_PREFIXO) '
type: support-article
updated_at: '2023-02-03T18:29:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045706933-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Invalid-data-type-on-E1-PREFIXO
---

**Ocorrência**

No momento do faturamento da nota fiscal de saída, ocorreu o error.log abaixo:

**Invalid data type on (E1\_PREFIXO) in file d:\bamboo-agent-5.7.2\xml-data\build-dir\tp11-tecx17v3r1-tecxwin64\advpl\instrvar.inl at line 535**  
**on MANFS2FIN(MATA461.PRX) 21/01/2020 11:05:25 line : 6593**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

O erro ocorre porque o  campo **E1\_PREFIXO** está com o tipo inválido,  este campo recebe a informação do que estiver contido no parâmetro **MV\_1DUPREF** que deve ser do tipo caractere , abaixo a configuração padrão:  
![](https://totvssuporte.zendesk.com/attachments/token/eTiA7lQTKlEyge5kyTq5sITr6/?name=inline183399101.png)  
  
**Solução**

Ajuste o conteúdo do parâmetro para que o erro deixe de ocorrer.

Caso utilize a série diretamente no parâmetro, informe a série entre aspas duplas, em formato caractere, exemplo **"001"**.
