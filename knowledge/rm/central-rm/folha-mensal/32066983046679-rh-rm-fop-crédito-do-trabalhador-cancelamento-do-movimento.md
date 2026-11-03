---
article_id: 32066983046679
category: Folha Mensal
content_hash: cf9970f60191a3f0cfd166e7d9ed79b181c1a2df6d4357467eb5a49fbb223c15
fetched_at: '2026-06-28T22:46:58.100406+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: 'RH - RM - FOP - Crédito do Trabalhador: Cancelamento do movimento'
type: support-article
updated_at: '2025-07-04T19:04:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32066983046679-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Cancelamento-do-movimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32066990167959) Tempo aproximado para leitura: **00:02:32min** **Dúvida**Como é realizada a atualização do cadastro do empréstimo Crédito do Trabalhador ao cancelar o movimento da folha?  
  
**Ambiente**

TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

12.1.2406.275  
12.1.2410.225  
12.1.2502.142 e superiores

**Solução**

Em  **Folha mensal | Cancelamento**, existe o parâmetro **Atualiza cadastro de empréstimo.** Ele foi **adequado** para contemplar também os empréstimos **Crédito do Trabalhador**.

Agora, ao cancelar um movimento na folha  marcando a opção **"Atualiza cadastro de empréstimos"**, o sistema também atualiza automaticamente os dados do **Crédito do Trabalhador**, garantindo consistência entre o movimento da folha e o cadastro de empréstimos.

Exemplo do processo:

1. Cadastro inicial do empréstimo:  
   O empréstimo está previamente registrado no sistema.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066983032087)
2. Lançamento na folha:  
   O valor do empréstimo é lançado no movimento do funcionário por meio de um grupo de eventos.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066983032855)
3. Alteração no cadastro de empréstimos:   
   Após o lançamento, o cadastro de empréstimos é atualizado com os novos valores.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066990170647)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066990172823)
4. Cancelamento do movimento com a opção marcada:  
   Ao cancelar o movimento e marcar "Atualiza cadastro de empréstimos", o sistema reverte os valores no cadastro conforme as regras da funcionalidade.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066983034903)
5. Resultado:  
   cadastro de empréstimos é atualizado automaticamente, refletindo o cancelamento do movimento.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066990174231)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/32066983036183)  
   **Importante :**

* Os campos **"Nro de Parcelas Pagas"** e **"Saldo Devedor"** não serão alterados pelo cálculo e não serão alterados pelo cancelamento de movimento também porque esses campos serão atualizados pelo valor informado no arquivo de importação do crédito do trabalhador.
* Os valores que estavam no anexo **Descontos de Empréstimos** retornaram para o **Valor da Parcela**, caso haja informação no campo **"Valor da Insuficiência de Saldo"** então o retorno para o Valor da Parcela será a soma desse campo **"Valor da Insuficiência de Saldo"** com o campo **"Valor"** do mesmo anexo.

**Saiba mais:**

* [RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)
* [FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
* [Crédito do Trabalhador - Linha RM - Medida Provisória Nº 1.292, de 12 de Março de 2025](https://tdn.totvs.com/pages/viewpage.action?pageId=925361639)
