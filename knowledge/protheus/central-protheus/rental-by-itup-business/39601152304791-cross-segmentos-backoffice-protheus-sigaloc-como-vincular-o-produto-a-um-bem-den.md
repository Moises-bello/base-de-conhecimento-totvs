---
article_id: 39601152304791
category: Rental by ItUp Business
content_hash: 1c3c9b259931eb6a40d86fc26c715404964ba35b5660690117dd85fd8f61015f
fetched_at: '2026-06-28T22:36:20.586807+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Como vincular o produto a
  um bem dentro do projeto na rotina de Orçamento (LOCA001)
type: support-article
updated_at: '2026-04-08T14:50:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39601152304791-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-vincular-o-produto-a-um-bem-dentro-do-projeto-na-rotina-de-Or%C3%A7amento-LOCA001
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39601178240535) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Como realizar o vínculo de um produto a um bem para que este seja apresentado na inclusão de um Orçamento (LOCA001)?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Solução**  
Para que o bem seja exibido corretamente na rotina de **Orçamento** (**LOCA001**), é fundamental que o cadastro do bem no módulo de Manutenção de Ativos esteja configurado com os status e vínculos de estoque adequados.

**Passos**

1. Acesse o módulo **19** **SIGAMNT** **(Manutenção de Ativos)**, vá em Atualizações > Bens > **Status do Bem** **(MNTA710)** e realize a criação do status desejado.
2. Ainda no módulo **19** **SIGAMNT**, acesse Atualizações > Bens > **Bens** **(MNTA080)** e realize o cadastro do ativo.
3. No cadastro do Bem, certifique-se de que os campos abaixo estejam preenchidos corretamente:

* **Status Bem (T9\_STATUS)**: Deve conter o código criado no passo 1.
* **Estoque (T9\_CODESTO)**: Deve estar preenchido para permitir o vínculo com o estoque.

4. Acesse o módulo **94** **SIGALOC (Locação de Equipamentos)**, vá em Atualizações > Cadastros > Cadastros Básicos > **Cadastro de** **Status (****LOCA081)** e crie o status correspondente, realizando obrigatoriamente o vínculo com o código de status utilizado no módulo **19 SIGAMNT**.

**Saiba Mais:** [**Cross Segmentos - Backoffice Protheus - SIGALOC - Como configurar o Status na integração SIGALOC x SIGAMNT**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28089040989591-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Como-configurar-o-Status-na-integra%C3%A7%C3%A3o-SIGALOC-x-SIGAMNT)
