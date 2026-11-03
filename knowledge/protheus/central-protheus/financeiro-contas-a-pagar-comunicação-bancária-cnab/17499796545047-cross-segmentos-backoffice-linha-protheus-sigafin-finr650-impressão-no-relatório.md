---
article_id: 17499796545047
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 814acb14ea771d7011896da00f454dec65bc981d42fb570a032cb38a12090b68
fetched_at: '2026-06-28T22:37:56.380701+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR650 - Impressão
  no relatório trazendo informações distorcidas
type: support-article
updated_at: '2023-09-13T20:22:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17499796545047-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR650-Impress%C3%A3o-no-relat%C3%B3rio-trazendo-informa%C3%A7%C3%B5es-distorcidas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17499805352343) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar a impressão do relatório de retorno CNAB - FINR650 - a impressão no relatório está trazendo informações distorcidas

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/17499672913303)**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois está sendo utilizado um arquivo fora do Formato Windows UTF-8 em ambiente Windows

Exemplo abaixo, arquivo Unix(LF)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17507028112407)  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

Copiar o conteúdo do arquivo  
Criar um novo arquivo no formato Windows UTF-8 (Bloco de Notas ou Notepad++)

Salvar o arquivo e imprimir novamente o relatório  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17499695185559)  
  
**Saiba mais**

#### [Relatório de Retorno CNAB (FINR650 - SIGAFIN)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=312162708)
