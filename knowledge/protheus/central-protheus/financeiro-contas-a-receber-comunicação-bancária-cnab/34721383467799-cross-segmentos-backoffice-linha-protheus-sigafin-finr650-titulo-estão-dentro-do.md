---
article_id: 34721383467799
category: Financeiro - Contas a Receber - Comunicação Bancária CNAB
content_hash: 1838a79f8f58c69b49264f36b67dfe4af9f1c783bfb7ca91f269e8139879b2e2
fetched_at: '2026-06-28T22:37:48.023576+00:00'
product: protheus
section_id: 26656449081111
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR650 Titulo estão
  dentro do arquivo de retorno de CNAB, porém não apresenta no relatório de retorno
  de CNAB e por consequência não baixa o título.
type: support-article
updated_at: '2025-09-05T12:51:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34721383467799-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR650-Titulo-est%C3%A3o-dentro-do-arquivo-de-retorno-de-CNAB-por%C3%A9m-n%C3%A3o-apresenta-no-relat%C3%B3rio-de-retorno-de-CNAB-e-por-consequ%C3%AAncia-n%C3%A3o-baixa-o-t%C3%ADtulo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34721383452567) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
FINR650 Titulo estão dentro do arquivo de retorno de CNAB, porém não apresenta no relatório de retorno de CNAB e por consequência não baixa o título.  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Amarração entre o cadastro do código da espécie vindo no arquivo de retorno do CNAB com o código espécie do título na tabela 17 do SIGACFG (tabela SX5)

**Exemplo:**

No arquivo de retorno do banco "DDA.RET", temos 8 títulos para realizar a baixa, porém ao emitir o relatório FINR650 - Relatório de retorno CNAB, somente aparece 3 títulos de um total de 8 títulos. Deixando de exibir 4 títulos.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34721367100695)

Podemos observar que cada título possui um segmento G e H

Segue a imagem editado o arquivo de retorno do banco em um bloco de notas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34721367101591)

Avançado a imagem para o lado direito podemos ver a posição da espécie.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34721367104663)

E na posição "**ESPECIE**" (que vai da posição 180 até 181) que significa o tipo do título, temos as posições de cada título conforme baixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34721367103255)

Logo o título 1, a espécie possui o código 01

Logo o título 2, a espécie possui o código 02

Logo o título 3, a espécie possui o código 03

Logo o título 4, a espécie possui o código 04

Logo o título 5, a espécie possui o código 04

Logo o título 6, a espécie possui o código 04

Logo o título 7, a espécie possui o código 04

Logo o título 8, a espécie possui o código 04

Ao consultar a opção espécie do título no **SIGACFG**, podemos observar que o código 04  está amarrado ao tipo do título **AB-**

E por esse motivo esse tipo de título **AB-**  não será demostrado no relatório FINR650 e não será baixado por se tratar de um complemento do título principal.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34721367105303)

Neste caso poderá confirmar junto ao banco se esse código 04 deveria ser um tipo de título AB-,

Caso não seja, poderá ajustar a tabela 17 no configurador SIGACFG manualmente

**Saiba mais:**

[Conciliação DDA (FINA260 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312165346)

Ponto de entrada [FA430PA](https://tdn.totvs.com/pages/releaseview.action?pageId=6071226) também poderá ser utilizado para alteração da espécie dos título no contas a pagar

Exemplo:

#include 'Protheus.ch'  
User Function FA430PA()  
     IF cEspecie $ 'DP |NP |NS '  
           cEspecie:='NF '  
     ENDIF  
Return .T.
