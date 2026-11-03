---
article_id: 39270926837399
category: Ativo Fixo - Baixa e Baixa de Adiantamento
content_hash: 1c4ee19521f81cfb2762419d03fbf0eeecab21089e0a6c9467781163c324be2a
fetched_at: '2026-06-28T22:41:55.587118+00:00'
product: protheus
section_id: 1500001535901
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - ATFA036 -
  Como realizar o cancelamento da baixa de um Ativo
type: support-article
updated_at: '2026-03-30T13:03:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39270926837399-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Ativo-Fixo-ATFA036-Como-realizar-o-cancelamento-da-baixa-de-um-Ativo
---

O cancelamento da baixa de um ativo fixo no TOTVS Protheus é feito na rotina ATFA036, revertendo o ativo ao estado anterior. Basta acessar o módulo Ativo Fixo, selecionar o ativo baixado, usar "Outras Ações" para escolher "Cancelar Baixa", confirmar os dados e finalizar. O status do ativo muda para "Ativo Disponível".

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39270926820503) Tempo aproximado para leitura: 00:10 min

**Dúvida**  
Como realizar o cancelamento da baixa de um Ativo

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - A partir da versão 12.

**Solução**  
O cancelamento da baixa de um ativo fixo pode ser realizado diretamente na rotina de baixa de Ativo (ATFA036). Este procedimento reverte a baixa efetuada, retornando o bem ao seu estado anterior.

1. Acesse o módulo de **Ativo Fixo** e abra a rotina de baixa de Ativos (ATFA036).
2. Na listagem principal (browser), localize e selecione o bem que deseja cancelar a baixa. Ele deve estar com o status indicado pela legenda vermelha de **Ativo Baixado**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39270912606103)
3. Na parte superior da tela, clique no botão **Outras Ações**.
4. No menu de opções, posicione o cursor sobre **Cancelar** e clique em **Cancelar Baixa**.
5. O sistema abrirá a tela de cancelamento exibindo os detalhes da baixa anterior, distribuídos nas abas *Dados da Baixa*, *Dados da NF* e *Dados da Transportadora*.
6. Confirme as informações e clique no botão **Confirmar** (ícone de verificação verde no canto superior direito) para executar o cancelamento.
7. Uma notificação será exibida com a mensagem **"Registro alterado com sucesso."**. Clique em **Fechar**.
8. Ao retornar para a tela de listagem, observe que a legenda do respectivo ativo foi alterada para a cor verde, confirmando que o status atualizado do bem é **Ativo Disponível**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39270926826263)

**Saiba mais**  
[ATFA036 - BAIXA DE ATIVO](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018556171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-BAIXA-DE-ATIVO)  
[ATFA036- F12: Visualização de Baixas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014647352-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA036-F12-Visualiza%C3%A7%C3%A3o-de-Baixas)
