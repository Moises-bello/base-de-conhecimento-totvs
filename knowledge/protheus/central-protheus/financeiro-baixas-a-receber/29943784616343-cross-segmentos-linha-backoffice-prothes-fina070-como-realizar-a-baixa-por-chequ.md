---
article_id: 29943784616343
category: Financeiro - Baixas a Receber
content_hash: 8710b704895c44b93363795c7f0af9139b97f043ea5501813075d8e1712ea196
fetched_at: '2026-06-28T22:37:43.815670+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmentos - Linha BackOffice Prothes - FINA070 - Como realizar a baixa
  por cheque e posteriormente liberar o pagamento
type: support-article
updated_at: '2025-07-30T14:49:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29943784616343-Cross-Segmentos-Linha-BackOffice-Prothes-FINA070-Como-realizar-a-baixa-por-cheque-e-posteriormente-liberar-o-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29943746754967) Tempo aproximado para leitura: **00:08 min** **Dúvida**Qual é o processo para realizar a baixa por cheque e, em seguida, efetuar a liberação do pagamento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – Todas as versões  
  
**Solução**Para incluir o cheque no registro do título, acesse "Outras Ações" e selecione a opção "Cheque".

**![Gravar_2025_02_12_16_48_24_600.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29943784576919)**

Ou no momento da baixa, também pelo botão "Outras Ações" da baixa manual e selecionando a opção "Cheque".

**![Gravar_2025_02_12_16_52_00_804.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29943784577943)**

Antes de finalizar a baixa do título, pressione **F12** para exibir os parâmetros. No campo "Gerar Cheque para Adiantamento", selecione a opção **Sim**.

Com essa configuração, será gerado um movimento na **SE5**, onde o campo **E5\_TIPODOC** será registrado como **BA** (sem movimentação bancária).

Para liberar o cheque e gerar a movimentação bancária, acesse a rotina **Cheques Recebidos (FINA191)**. Em **Outras Ações**, selecione a opção **Compensar**.

Na tela exibida, confirme as informações e confirme a operação.

![Gravar_2025_02_12_17_02_31_847.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/29943784582167)

Após a confirmação, será gerado um movimento com **E5\_TIPODOC = CH**, registrando a movimentação bancária correspondente.

**Importante**

O parâmetro **MV\_SLDBXCL** deve estar configurado como **"C"** para habilitar o campo de compensação na rotina de Cheques Recebidos.
