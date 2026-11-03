---
article_id: 33819195543959
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 529bc0be283da2f5ee0db3e922a1fe022f52fcd861d2831005d465171dac20be
fetched_at: '2026-06-28T22:38:55.682610+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105 - Como efetuar
  o rateio para mais de uma linha na solicitação de armazém?
type: support-article
updated_at: '2025-07-30T17:20:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33819195543959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-Como-efetuar-o-rateio-para-mais-de-uma-linha-na-solicita%C3%A7%C3%A3o-de-armaz%C3%A9m
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33819190145687) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Na solicitação ao armazém, tenho a opção de efetuar o rateio entre centros de custos e contas contábeis, porém preciso digitar linha a linha. É possível efetuar o rateio para mais de uma linha na solicitação de armazém?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33 ou Superior.  
  
**Solução**  
Sim, é possível, porém é necessário que todas as linhas já estejam digitadas e que o rateio esteja posicionado na primeira linha. Abaixo segue uma demonstração:  
  
  
Para solucionar essa dúvida, realize os seguintes passos:

1. Após entrar na rotina, digite todas as linhas que tenham o mesmo rateio;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33819190146071)
2. Posicione-se no item “01”, vá ao botão “Outras Ações” -> “Rateio”;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33819190146839)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33819190149399)
3. Após isso, digite as informações do rateio que deseja utilizar e clique em “Salvar”;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33819190150679)
4. O sistema irá perguntar se deseja “Replicar informações para os demais itens do documento?” selecione a Opção “Sim”;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33819190151703)
5. Agora todas as linhas do documento irão receber as mesmas informações para o rateio;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33819195524503)

**Observação**: Este tipo de comportamento só ocorre quando o rateio é efetuado no primeiro item, ou seja, caso esteja posicionado no segundo o sistema não oferecerá a opção de Replicar as informações para as demais linhas.

**IMPORTANTE:** Quando solicitado ao sistema replicar as informações para os demais itens do documento, o sistema irá alterar todos os rateios, sem exceção. Ou seja, caso já tenha efetuado o rateio de outras linhas, essa informação será substituída pela informação digitada na primeira.

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Movimentações*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
