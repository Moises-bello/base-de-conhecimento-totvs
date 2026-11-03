---
article_id: 21083252298135
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 39b9699855a6c495f2577e58407436f08afafc0309965325fa2e487b778ddf5e
fetched_at: '2026-06-28T22:42:09.157293+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - CONV115/CAT79
  - Erro de validação "MEST 121"
type: support-article
updated_at: '2024-02-07T12:54:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21083252298135-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-CONV115-CAT79-Erro-de-valida%C3%A7%C3%A3o-MEST-121
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21083252256151) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao importar os arquivos magnéticos **CONV115** ou **CAT79**, ocorre o erro de validação:  
*MEST 121-Numero do documento fiscal fora da sequência*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21083235422743)  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Causa**Esse erro ocorre pois alguma nota fiscal não está sendo considerada no arquivo.  
O validador do arquivo não aceita que pule a sequência de numeração, ou seja, todas as NFs devem ser entregues no arquivo por sequência.  
  
**Solução**

**1 - *Identifique a Nota Fiscal que está faltando no arquivo:***

Você pode identificar essa nota fiscal através do log dos erros de validação do arquivo, e verificar a situação que ela se encontra no seu ambiente.

*Exemplo:*  
Perceba que no arquivo mestre tem NFs pulando a sequência:  
da *000014321* pula para *000014323*, ou seja, falta a ***000014322:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21083252262423)

***2 - Verifique se essa NF existe em sua base:***

 - Se existir é necessário avaliar:  
  
O campo **FT\_OBSERV** deste documento precisa conter o texto "CANCELAD" ("CANCELADO" ou "CANCELADA") e o campo **FT\_DTCANC** precisa estar preenchido.  
  
Se o parâmetro **MV\_CANCFOR** estiver igual a **.F.**, o sistema verifica se a data de cancelamento está dentro do período ou não. Quando o cancelamento estiver fora do período, a nota fiscal irá levar a situação como '**N'**.  
  
***Exemplo:*** Emissão do documento 30/12/2023 (**FT\_EMISSAO=20231231**), cancelamento 01/01/2024 (**FT\_DTCANC = 20240101**).

O arquivo de dezembro/2023 será levado com a situação '**N'** se o parâmetro **MV\_CANCFOR = .F.**  
  
Quando o parâmetro **MV\_CANCFOR** estiver igual a **.T.**, o simples fato do documento estar cancelado já será suficiente para gerar o arquivo com a situação = **'S'**.  
  
\*\*Os cancelamentos ocorridos dentro do período serão sempre levados com a situação "S".

===

- Se a NF não existir na base siga a dica abaixo:  
  
Para resolver seu problema no arquivo, **será necessário criar a NF no sistema com a numeração que pulou e CANCELAR sem transmiti-la**, para que o sistema preencha campos **F3\_DTCANC** e **F3\_OBSERV** respectivamente.
