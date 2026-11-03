---
article_id: 360058422034
category: RH - Férias
content_hash: b344d6b1a204011668b238e2f14ce2270f6c0a0dd3dea77491d1d93c74ed8e3c
fetched_at: '2026-06-28T22:43:59.223643+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: 'RH - Linha Protheus - GPE - Sistema apresenta log de ocorrências no cálculo
  de férias com a mensagem: A configuração dos períodos está incorreta ou não existem
  dados válidos para o período que está sendo calculado.'
type: support-article
updated_at: '2025-07-28T17:09:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058422034-RH-Linha-Protheus-GPE-Sistema-apresenta-log-de-ocorr%C3%AAncias-no-c%C3%A1lculo-de-f%C3%A9rias-com-a-mensagem-A-configura%C3%A7%C3%A3o-dos-per%C3%ADodos-est%C3%A1-incorreta-ou-n%C3%A3o-existem-dados-v%C3%A1lidos-para-o-per%C3%ADodo-que-est%C3%A1-sendo-calculado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Após cálculo de **Férias**, Sistema apresenta *log* de ocorrências com a mensagem: **A configuração dos períodos está incorreta ou não existem dados válidos para o período que está sendo calculado. Verifique se existe período que corresponda a data final de férias**.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O problema ocorre devido existir informações incorretas no cadastro de **Períodos**.   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101055573/mceclip0.png)  
  
Exemplo: No cadastro de **Períodos** foi informada data final do mês com 30 dias, porém o mês possui 31 dias.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101055933/mceclip1.png)  
  
**Solução**Para resolver esta inconsistência, siga os seguintes passos:  
**1.** Acesse o cadastro de **Períodos**  pelo menu **Atualizações > Definições de Cálculo > Períodos**;  
**2.** Selecione o **Processo** que fará a manutenção;  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101056053/mceclip2.png)  
  
**3.** Clique em **Outras Ações** e selecione a opção **Excluir**;  
**4. Clique** em **Fechar** a notificação de exclusão, após ler a mensagem;  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101056173/mceclip3.png)  
  
**5.** Clique em **Confirmar** na tela de exclusão;  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360098843374/mceclip4.png)

**6.** Após exclusão, realize o cadastro do mesmo **Período** com as datas corretas.

**Importante**  
Caso existam outros **roteiros** que tenham sido calculados na mesma competência, será necessário cancelar os cálculos antes da exclusão do período.   
  
**Para Saber Mais**  
[RH - Linha Protheus - GPE - Como excluir um período aberto indevidamente ou com informações incorretas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060741313-RH-Linha-Protheus-GPE-Como-excluir-um-per%C3%ADodo-aberto-indevidamente-?source=search)

[RH - Linha Protheus - GPE - Como visualizar cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057823253-RH-Linha-Protheus-GPE-Como-visualizar-c%C3%A1lculo-de-f%C3%A9rias-?source=search)

[RH - Linha Protheus - GPE - Como cancelar cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050830934-RH-Linha-Protheus-GPE-Como-cancelar-c%C3%A1lculo-de-f%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Como imprimir relatório de memória de cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052314713-RH-Linha-Protheus-GPE-Como-imprimir-relat%C3%B3rio-de-mem%C3%B3ria-de-c%C3%A1lculo-das-f%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Pontos de Entrada da rotina Cálculo de Férias - GPEM030](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053133974-RH-Linha-Protheus-GPE-Pontos-de-Entrada-da-rotina-C%C3%A1lculo-de-F%C3%A9rias-GPEM030?source=search)
