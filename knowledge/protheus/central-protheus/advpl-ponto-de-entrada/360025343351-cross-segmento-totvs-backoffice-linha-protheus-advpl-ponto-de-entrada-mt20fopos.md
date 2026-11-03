---
article_id: 360025343351
category: ADVPL - Ponto de Entrada
content_hash: 28ed7ea3efc241f4d946333c5ee5a9714acbb1ac882206cf0123edb883c6fe18
fetched_at: '2026-06-28T22:40:12.667699+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de Entrada
  MT20FOPOS
type: support-article
updated_at: '2022-11-08T20:05:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025343351-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-Entrada-MT20FOPOS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Porque após confirmar a alteração do fornecedor não está lendo o ponto de entrada?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Como a Rotina está em MVC é necessário Utilizar e utilizar o momento após a gravação utilizando o método GetOperation() caso tenha necessidade de Retornar qual a função que o usuário utiliza   
Exemplo:  Incluir = 3, Alterar = 4 e Excluir = 5.

```
ElseIf cIdPonto == 'MODELCOMMITTTS'  
ApMsgInfo('Chamada apos a gravação total do modelo e dentro da transação.')  
ElseIf cIdPonto == 'MODELCOMMITNTTS'  
ApMsgInfo('Chamada apos a gravação total do modelo e fora da transação.')  
ElseIf cIdPonto == 'FORMCOMMITTTSPRE'  
ApMsgInfo('Chamada apos a gravação da tabela do formulário.')  
ElseIf cIdPonto == 'FORMCOMMITTTSPOS'  
ApMsgInfo('Chamada apos a gravação da tabela do formulário.')
```

**Saiba Mais**[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada MVC para as rotinas MATA010, MATA020 e MATA030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016405952)  
[PONTO DE ENTRADA PADRÃO DO MVC](http://tdn.totvs.com/pages/releaseview.action?pageId=208345968)  
[Cross Segmento - Backoffice Linha Protheus - ADVPL - Como validar se uma rotina está em MVC](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016345572)
