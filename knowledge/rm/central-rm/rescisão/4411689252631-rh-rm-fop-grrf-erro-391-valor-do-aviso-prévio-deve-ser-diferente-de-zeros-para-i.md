---
article_id: 4411689252631
category: Rescisão
content_hash: b7a97ccb60d11bf6437f6aa3d86c7e050c2723d9cf53fabbd90cb95f42fa1816
fetched_at: '2026-06-28T22:46:54.516970+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - GRRF: Erro 391 - Valor do Aviso Prévio deve ser diferente
  de zeros para indicativo de Aviso Prévio igual a 2 - Indenizado'
type: support-article
updated_at: '2025-01-20T21:39:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411689252631-RH-RM-FOP-GRRF-Erro-391-Valor-do-Aviso-Pr%C3%A9vio-deve-ser-diferente-de-zeros-para-indicativo-de-Aviso-Pr%C3%A9vio-igual-a-2-Indenizado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min**  
 **Ocorrência** Ao enviar a GRRF é apresentado o seguinte erro: Inconsistência 391 valor do Aviso Prévio deve ser diferente de zeros para indicativo de Aviso Prévio igual a 2 - Indenizado

![](https://totvssuporte.zendesk.com/attachments/token/63Nrl7G3AMHosNxpdN47Ox3Tm/?name=inline1876399846.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse erro ocorre porque a rescisão original do funcionário teve aviso prévio indenizado. Desta forma, na rescisão complementar deve também existir valor para o evento de aviso prévio indenizado  
  
**S****olução**Para solucionar essa ocorrência, possui duas opções:  
  
**Opção 1**  
1. Verifique no arquivo o > Registro Tipo 40 > posição 239 a 253 se consta o valor do aviso.  
  
![](https://totvssuporte.zendesk.com/attachments/token/BDfke0XPQ1CycNTXKSRGZPHBY/?name=inline603661386.png)  
  
2. Entrar na ficha financeira do funcionário e lançar o **evento de Dif. Aviso Previo com valor R$0,13.**  
2. Cadastrar um**evento de desconto** que irá estornar esses R$0,13 para que não altere nada no TRCT.  
  
**Quando você lançar estes dois eventos, um irá anular o outro, desta forma, não irá alterar no líquido.**  
  
3. Gerar o arquivo novamente e enviar para a GRRF.

**OBS.: Deve-se realizar este procedimento pois a GRRF não aceita o valor do aviso zerado.**  
  
**Opção 2**  
1. Realize alteração manualmente do arquivo.  
  
Linha 3, Posição 239 a 253 e informe **13** correspondendo **R$0,13**.   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6191210741911/mceclip1.png)  
  
2. Gerar o arquivo novamente e enviar para a GRRF.
