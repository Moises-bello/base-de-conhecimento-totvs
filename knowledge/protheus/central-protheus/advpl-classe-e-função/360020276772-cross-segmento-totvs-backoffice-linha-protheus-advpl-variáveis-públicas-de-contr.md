---
article_id: 360020276772
category: ADVPL - Classe e Função
content_hash: e1cc090ba1329c78c175b8bd4e97cb96b3dfc1b5f72e9467a57b68c47d64ea71
fetched_at: '2026-06-28T22:40:18.224456+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Variáveis públicas
  de controle da  aba Informações Adicionais - Documento de Entrada(MATA103)
type: support-article
updated_at: '2022-01-06T19:26:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020276772-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Vari%C3%A1veis-p%C3%BAblicas-de-controle-da-aba-Informa%C3%A7%C3%B5es-Adicionais-Documento-de-Entrada-MATA103
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min*** **Dúvida**Tornar campos F1\_UFORITR, F1\_UFDESTR, F1\_MUORITR e F1\_MUDESTR obrigatórios, através do PE MT100TOK. Quais seriam as variáveis à serem utilizadas para estes campos?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 12.1.17  
  
**Solução**A variável que controla os dados dos campos informados na aba **Informações Adicionais** é a **aInfAdic**. Esta variável, que é do tipo **Array** e possui escopo **Private**, pode ser utilizada em pontos de entrada de validação da nota, em cada posição(13 posições na versão atual) conterá um dado informado na aba **Informações Adicionais.**
