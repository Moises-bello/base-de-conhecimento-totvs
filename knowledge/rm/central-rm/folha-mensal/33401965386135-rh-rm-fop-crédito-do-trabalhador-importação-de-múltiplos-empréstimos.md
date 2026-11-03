---
article_id: 33401965386135
category: Folha Mensal
content_hash: ccfa94019c3eee1b71473a1b075db9be492962bd647892894648b14354c7e794
fetched_at: '2026-06-28T22:46:58.039720+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Crédito do Trabalhador - Importação de Múltiplos Empréstimos
type: support-article
updated_at: '2025-10-28T17:49:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33401965386135-RH-RM-FOP-Cr%C3%A9dito-do-Trabalhador-Importa%C3%A7%C3%A3o-de-M%C3%BAltiplos-Empr%C3%A9stimos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33401965348503) Tempo aproximado para leitura: **00:02:31 min**  
  
**Dúvida**  
  
Como realizar a importação de crédito do trabalhador quando o colaborador possui mais de um empréstimo ativo dentro da mesma vigência?  
  
**Ambiente**  
  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir dos patches:

* 12.1.2406.296
* 12.1.2410.267
* 12.1.2502.174
* 12.1.2506.114

**Solução**  
  
Em versões anteriores, o sistema RM não estava preparado para importar múltiplos empréstimos ativos para o mesmo colaborador dentro da mesma vigência, o que gerava erro no processo de importação.

Porém, com a adequação realizada pela equipe de produto, o sistema passou a atender esse cenário, conforme a **Portaria MTE nº 933, de 5 de junho de 2025**, que permite ao trabalhador ter mais de um contrato de empréstimo vigente ao mesmo tempo.

Para solucionar a importação de múltiplos empréstimos ativos para um mesmo colaborador, é necessário cadastrar o evento de Código de Cálculo 480 repetidamente, utilizando a natureza da rubrica eSocial 9253, com códigos distintos, conforme a quantidade de empréstimos dentro da mesma vigência.

**Exemplo:**

**Se um colaborador possui dois empréstimos ativos dentro da mesma vigência:**

1. Cadastrar **dois Códigos de cálculo 480**, cada um com um código de evento distinto. No exemplo abaixo, foi criado um evento com o código 0480 e o outro com o código 1480;

   ![Recording 2025-07-11 at 11.10.23.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33402109164311)
2. Ambos devem utilizar a **Natureza de rubrica eSocial 9253**.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/33401934391447)
3. A importação deve referenciar esses dois códigos de forma separada, representando cada contrato de empréstimo individualmente.

**DICA:** Conforme o manual do governo, atualmente o limite de empréstimos permitidos é **ilimitado**, não havendo uma quantidade máxima definida por funcionário. Como sugestão, recomenda-se criar os eventos conforme a necessidade, utilizando **códigos distintos** (todos com o **Código de Cálculo 480 é Rubrica 9253**), o que facilitará a importação sempre que houver novos contratos.

Seguem abaixo alguns exemplos de importação de empréstimos, sua relação com os códigos cadastrados e o resultado esperado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/33401934392087)

**SAIBA MAIS:**

[DT - Crédito do Trabalhador - Cálculos](https://tdn.totvs.com/pages/releaseview.action?pageId=939246677)

[RH - RM - FOP - Dúvidas frequentes: Crédito do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador)

[FAQ - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=946423249)
