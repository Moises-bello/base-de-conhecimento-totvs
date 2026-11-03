---
article_id: 360018638652
category: ADVPL - Classe e Função
content_hash: 5ec6f67d11502768f7c269c5806a87ce2c0908b14a369ac9ca78630fc43f36fe
fetched_at: '2026-06-28T22:40:16.689264+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: variable
  does not exist oself'
type: support-article
updated_at: '2022-02-07T14:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018638652-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-variable-does-not-exist-oself
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Ao inserir uma coluna diretamente pelo navegador da rotina e tentar imprimir o Browse(botão "Imprimir Browse") é gerado o erro:

```
variable does not exist OSELF on {|o| U_FUNCAO_CLIENTE(oSelf:oBrowse)} (APLIB090.PRW)
```

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus – ADVPL – A partir da versão 12.1.17  
  
**Causa**Este erro ocorre pela formatação incorreta da coluna criada pela browser. **Solução**Criar a coluna conforme exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360072824953/mceclip0.png)  
**Observação:** A função dentro do campo Dados não possui parâmetros sendo assim não é necessário a utilização dos parênteses ().

**Saiba mais**  
[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - ADVPL - Excluir dados do profile (manutenção de profile)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018587832)
