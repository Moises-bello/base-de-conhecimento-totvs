---
article_id: 360042818154
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 5b5c8c5e7823bd91256b9f2e4d547677a1724e26c9dee8a2d63fd5710ebc9e9a
fetched_at: '2026-06-28T22:42:02.329662+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Sped Fiscal
  - Erro de validação no registro G125 e G140.
type: support-article
updated_at: '2025-02-11T21:20:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042818154-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Sped-Fiscal-Erro-de-valida%C3%A7%C3%A3o-no-registro-G125-e-G140
---

**Ocorrência**Ao gerar o arquivo do Sped Fiscal ocorre o erro de validação no registro G125 e G140:

![](https://jiraproducao.totvs.com.br/secure/attachment/714761/714761_image-2020-02-05-13-58-45-650.png)

**Ambiente**

Microsiga Protheus – Livros fiscais– A partir da versão 11.80  
  
**Causa**

Quando é realizada a geração do bloco G no Sped Fiscal onde os bens são incluídos **diretamente** através da rotina Manutenção CIAP(**MATA905**) em que o parâmetro **MV\_F9SKPNF = .T.** ocorre erro de validação no registro G125 e G140.

Este problema ocorre pois o campo **F9\_VALICMP** não está habilitado para preenchimento no momento da inclusão do bem, onde os valores do campo **6 - VL\_ICMS\_OP\_APLICADO** do registro **G140** são pegos através deste campo.

Obs.: Quando o bem é incluído através do documento de entrada, o campo F9\_VALICMP é preenchido automaticamente.

**Solução:**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Aplique o pacote atualizado:

<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>

2. Executar o compatibilizador UPDDISTR com o dicionário, encontrado no link acima.

3. O campo ICMS próprio (F9\_VALICMP) será habilitado para preenchimento.

4. Efetue o preenchimento do campo ICMS próprio (F9\_VALICMP) com o valor do ICMS

Mais informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=533755531>
