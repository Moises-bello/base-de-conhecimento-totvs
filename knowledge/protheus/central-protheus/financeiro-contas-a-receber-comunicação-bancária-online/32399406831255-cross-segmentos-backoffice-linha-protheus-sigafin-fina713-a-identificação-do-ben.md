---
article_id: 32399406831255
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 2b13dd09cee8bb2b8ec464c254e98b965eda5d38fc07e2d1f8faaf78e6f7731e
fetched_at: '2026-06-28T22:37:49.296463+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN -  FINA713 - A identificação
  do beneficiário deve conter somente números
type: support-article
updated_at: '2025-05-27T16:56:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32399406831255-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-A-identifica%C3%A7%C3%A3o-do-benefici%C3%A1rio-deve-conter-somente-n%C3%BAmeros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32399378182807) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**O que validar quando ocorre a mensagem "A identificação do beneficiário deve conter somente números"?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - a partir do release 12.1.33  
  
  
**Solução**Essa mensagem ocorre por conta de algum campo preenchido incorretamente no conjunto **agencia/conta/dac** invalido na rotina **FINA130**.  
  
Esse retorno é do Banco, que esta informando que a conta ou **DAC** está incorreta, nesse caso valide em sua rotina **FINA130** **"Parâmetros de bancos"** na aba **"Outros"** como estão os campos do print a seguir, pois pode ser que algum desses campos estejam informando dados incorretos ou conta sem digito.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32399406802967)

**OBS:** O cadastro do banco não deve ser selecionado pela consulta **F3 "Lupa"** do campo **Bco. Oficial**, se faz necessário ajustar manualmente nos campos marcados no print acima com os dados corretos.
