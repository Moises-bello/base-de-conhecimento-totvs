---
article_id: 38099515116439
category: 'Financeiro - Cheques '
content_hash: 43fc083f5bdca7f39632463f38cb8e8bc27c9fd05696280c6aa92d8a09794aa1
fetched_at: '2026-06-28T22:37:38.150755+00:00'
product: protheus
section_id: 35057400818327
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA390 - Como baixar dois ou
  mais títulos a pagar com um único cheque
type: support-article
updated_at: '2026-02-02T16:41:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38099515116439-Cross-Segmentos-Backoffice-Linha-Protheus-FINA390-Como-baixar-dois-ou-mais-t%C3%ADtulos-a-pagar-com-um-%C3%BAnico-cheque
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38099515093399) Tempo aproximado para leitura: **00:04 min**  
  
**Dúvida**  
Como realizar a baixa de múltiplos títulos a pagar utilizando um único cheque no Protheus?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33.  
  
**Solução:**

Para realizar a baixa de vários títulos com um único cheque, o sistema utiliza a rotina "Cheques sobre títulos" (FINA390). Esta funcionalidade permite agrupar diversos títulos em aberto de um mesmo fornecedor, gerando uma única numeração de cheque (um único movimento bancário) para a quitação do montante selecionado.

1. No módulo **Financeiro (SIGAFIN)**, acesse **Atualizações > Contas a Pagar > Cheque Sobre Títulos (FINA390)**.
2. Clique em **Cheque Sobre Títulos** e configure os parâmetros, selecionando os títulos do fornecedor que deseja quitar com o cheque (os títulos devem obrigatoriamente pertencer ao mesmo fornecedor para o agrupamento).  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38099515096471)
3. Certifique-se de que os títulos que deseja baixar estejam dentro do período informado nos parâmetros.
4. Na tela de seleção, o sistema apresentará os títulos em aberto.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38099558186775)
5. Após a seleção, confirme a operação.
6. O sistema gerará a baixa dos títulos selecionados e atribuirá o número do cheque.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/38099558187415)
