---
article_id: 360060112553
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 989c2fccc80471ed59df8c3dc9b5c0c80732f9c8db9c6190f16c54d8d5ff0b5f
fetched_at: '2026-06-28T22:37:56.194071+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA200 / FINA473 -
  Formato do Arquivo
type: support-article
updated_at: '2022-07-22T15:37:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060112553-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-FINA473-Formato-do-Arquivo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura:**00:03:00min**

**Ocorrência**No retorno do arquivo bancário, ao efetuar um processamento pela rotina do Protheus: **Atualizações -> Comunicação Bancária ->Retorno de Cobranças**, com um layout válido e configurado corretamente, há problemas na identificação dos campos, como por exemplo "Ocorrência" ou "IDCNAB"(Nosso número)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – FINA200 / FINA473  – A partir da versão 11.80  
  
**Causa**Verifique o formato do arquivo de retorno se está como ***UTF-8***, sendo esse o tipo padrão retornado pelos bancos. Caso o arquivo seja processado por uma empresa Terceira e somente após disponibilizado, poderá estar em um formato diferente.

Exemplo:  
"Unix(LF)".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098693934/mceclip0.png)  
  
**Solução**Abra o arquivo no bloco de notas ou no **Notepad++** e converta o formato do arquivo.  
Segue exemplo abaixo.

**Exemplo:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100912873/mceclip1.png)

Deverá ficar dessa forma:

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098694094/mceclip3.png)

**Importante:**Salve o arquivo no novo formato.
