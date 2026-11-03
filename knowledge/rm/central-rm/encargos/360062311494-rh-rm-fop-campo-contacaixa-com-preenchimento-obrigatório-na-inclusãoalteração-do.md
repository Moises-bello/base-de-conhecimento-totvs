---
article_id: 360062311494
category: Encargos
content_hash: 3d9fad263623a53fba3a867083dc98baa3fa670086c639050640cbe1d6019aa6
fetched_at: '2026-06-28T22:46:53.242143+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Campo 'Conta/Caixa' com preenchimento obrigatório na inclusão/alteração
  do Lançamento
type: support-article
updated_at: '2025-03-12T13:52:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062311494-RH-RM-FOP-Campo-Conta-Caixa-com-preenchimento-obrigat%C3%B3rio-na-inclus%C3%A3o-altera%C3%A7%C3%A3o-do-Lan%C3%A7amento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:02:00 min****Dúvida**Ao tentar executar algum lançamento financeiro, o sistema apresenta um erro com a seguinte mensagem:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6347805562135/mceclip0.png)  
  
**Campo 'Conta/Caixa' com preenchimento obrigatório na inclusão/alteração do Lançamento, entretanto nenhum valor foi inserido.**Como corrigir?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Certifique-se de que será necessário utilizar um usuário com acesso a outro módulo, conforme o passo a passo abaixo:  
  
1. Acesse o módulo de**BackOffice | Gestão Financeira**:  
  
![](/attachments/token/wYffbS1yoBmStjiBcrY1nokYc/?name=inline-752927616.png)  
  
2. Acesse **Ambiente | Parâmetros | TOTVS Gestão Financeira**:  
  
![](/attachments/token/V9oh6kZ2L6GsReY53sLrCN5Ka/?name=inline-1829755749.png)  
  
3. Após a abertura da janela, avance até a **Seleção de Processos** e selecione a opção **02.01.01.01. - Lançamento** e avance:  
  
![](/attachments/token/OewMSf0f41F7lCEtUrTu8b2nZ/?name=inline763960333.png)  
  
4. Na próxima janela selecione a opção**Inclusão** e desmarque a opção **Conta/Caixa obrigatório no lançamento**. Depois, avance até finalizar e salvar:  
  
![](/attachments/token/jBex9MpukFJMYo8mHUSTgEmS3/?name=inline89055647.png)  
  
Ao concluir o processo, você poderá executar a rotina que anteriormente não estava sendo processada em decorrência do erro.
