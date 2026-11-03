---
article_id: 360018106252
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 09b5859070762a2d0abc9593b5718f2c135e1799841133c0d063d9ccc9f46be6
fetched_at: '2026-06-28T22:37:56.189830+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA200 - No Retorno
  de Cobrança não baixa os títulos devido a configuração da despesa de cobrança '
type: support-article
updated_at: '2023-06-29T23:27:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018106252-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-No-Retorno-de-Cobran%C3%A7a-n%C3%A3o-baixa-os-t%C3%ADtulos-devido-a-configura%C3%A7%C3%A3o-da-despesa-de-cobran%C3%A7a
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00min**

**Ocorrência**No módulo **Financeiro**ao processar o **Retorno de Cobrança (FINA200)** os títulos não são baixados.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA200 - A partir da versão 11.80  
  
**Causa**Quando apresenta está inconsistência, deve emitir o **Relatório de Retorno Cnab (FINR650)** informando nos parâmetros deste relatório os mesmos arquivos na rotina **Retorno de Cobrança (FINA200**).  
Este relatório apresenta as informações que constam no arquivo de retorno. Através da coluna: **Consistência,** é possível identificar a causa de não baixar os títulos. No exemplo abaixo, o motivo de não baixar os títulos no **Retorno de cobrança** é devido o arquivo envolver a **Despesa de Cobrança**, e na coluna: **Consistência** apresenta: **Valor Rec Menor**:

Segue ilustração abaixo:  
![valorrecmenor.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360013658012/valorrecmenor.PNG)

Neste exemplo, devido no arquivo de retorno está calculando no Valor Recebido a Despesa de Cobrança, é apresentado a Consistência: **VLR REC MENOR**, devido o Valor Recebido ser menor que o saldo do título. Neste caso, o título não será baixado.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o Módulo **Financeiro>****Atualizações>Cadastros>Parâmetros Bancos**;  
2. Selecione o banco correspondente ao retorno Cnab;  
3. Ajuste o campo: **Desp Princ**=Não para: Sim

**Saiba mais**[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CNAB - Como gerar despesa bancária no retorno do CNAB](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016697191--MP-SIGAFIN-CNAB-Como-gerar-despesa-banc%C3%A1ria-no-retorno-do-CNAB-)

[Retorno CNAB Contas a Receber](https://www.youtube.com/watch?v=Df4QunyJ8G0)  
  
[Retorno CNAB Contas a Pagar](https://www.youtube.com/watch?v=F0ZmxzyIdlc)
