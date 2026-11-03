---
article_id: 360021554891
category: SIGAEST - INVENTÁRIO
content_hash: 86c287fc9a895ea899841627138b56b2bddb0e7376f057e71c092a00a25cc8a2
fetched_at: '2026-06-28T22:38:50.280053+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - - MATA271 - Bloqueio
  de produtos para inventário por data informada
type: support-article
updated_at: '2026-02-12T15:44:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021554891-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-informada
---

A rotina permite bloquear e desbloquear movimentações de estoque por data informada ou calculada para evitar alterações durante o inventário. O bloqueio pode ser configurado via parâmetro e realizado na rotina MATA271, selecionando produtos e armazéns. O sistema também possibilita bloquear estoque mantendo liberações contábeis. Parâmetros como MV\_BLQINVA e MV\_VLDTINV controlam o bloqueio automático e duração.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37073439449495) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**

Como bloquear produtos para poder inventariá-los sem que outro usuário faça movimentos nele simultaneamente?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Esta rotina permite ***bloquear*** e ***desbloquear***, em uma data informada ou calculada, as movimentações de estoque dos produtos a serem inventariados. Com o objetivo de assegurar que, durante o processo de inventário, os produtos bloqueados não terão seus saldos alterados.

Conforme configuração dos parâmetros, o bloqueio de inventário pode ser efetuado de duas formas:

• **por data informada** = quando a data é informada manualmente;  
• **por data calculada** = quando a data é calculada automaticamente, com base na data de início do inventário (B2\_DINVENT), quando preenchida, ou database + período de inventário (B1\_PERINV) informado no cadastro de Produtos.

Observe o campo "Data Bloq. de Inventário" (B2\_DTINV) disponível na tabela de dados SB2 (Saldos  
Físico e Financeiro), que será preenchido com a data do bloqueio.

A função que verifica o bloqueio chama-se **BLQINVENT** (ExpC1, ExpC2, ExpD1) e seu retorno será .T. ou .F., dependendo do bloqueio do produto (ExpC1), do local (ExpC2) e da data (ExpD1), em que:  
• ExpD1 é a data opcional, se omitida será considerada a data-base do sistema. Esta função pode ser utilizada em User Function, validações, etc.

**Observações importantes**:

[**MV\_BLQINVA**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38347809526295) quando habilitado, o sistema processa automaticamente o bloqueio de todos os produtos que estiverem configurados para bloqueio automático através do campo **Blq. Invent. (B5\_BLQINVA)** e e a data base do ambiente estiver maior que a data do parâmetro **MV\_DATAINV**.

**MV\_VLDTINV** igual a **0** mantém o produto bloqueado até que seja efetuado o desbloqueio manual, mesmo que em datas posteriores a data informada.

**MV\_VLDTINV** igual a **1**, o bloqueio ocorre apenas na data informada no parâmetro, exemplo no print abaixo o produto fica bloqueado para movimentação na data de 18/12/2020 ou desbloqueado manualmente pela rotina.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101589553)

Para melhor entendimento, segue o passo a passo de um bloqueio e desbloqueio da forma mais "convencional", que é o bloqueio por data informada:

Para efetuar o ***bloqueio*** de um produto **por data informada**:

1. 1. Acessar a rotina MATA271 e parametrizar Quanto ao Produto = **Bloqueio**;
   2. Escolher o(s) Armazém(ns) em que deseja inventariar;
   3. Escolher o(s) produto(s);
   4. As perguntas "Da Data" e "Até Data" devem ficar em branco;
   5. Data do inventário: selecionar 'Data Informada'
   6. Data informada: informar a data que deseja bloquear;
   7. Ao confirmar, o sistema apresentará a tela para selecionar os Armazéns que deseja bloquear, efetuar a seleção e clicar em OK;

Para efetuar o ***desbloqueio*** de um produto **por data informada**:

1. 1. Acessar a rotina MATA271 e parametrizar Quanto ao Produto = **Desbloqueio**;
   2. Escolher o(s) Armazém(ns) que deseja desbloquear;
   3. Escolher o(s) produto(s);
   4. As perguntas "Da Data" e "Até Data" devem ser preenchidas com o período que contemple a data do último inventário (B2\_DINVENT);
   5. Data do inventário selecionar 'Data Informada'
   6. Data informada informar a data que deseja desbloquear;
   7. Ao confirmar, o sistema apresenta a tela para selecionar os Armazéns que deseja desbloquear, efetuar a seleção e clicar em OK;

**Observação importante**:

Caso tenha necessidade de efetuar um novo bloqueio após o processamento do inventário e o produto não seja exibido para bloqueio, revisar o campo B2\_DINVENT qual a data que esta populado e nas perguntas "Da Data" e "Até Data" devem constar esse período para que o registro seja liberado para um novo bloqueio. Exemplo nos prints abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000502561)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000502461)

### Desejo fazer o bloqueio de movimentação do estoque para inventariar mas desejo manter a liberação contábil, o que devo fazer?

Essa rotina permite impedir as movimentações do estoque com produtos inventariados, enquanto as movimentações contábeis (ou seja, movimentações que não tenham a ver com o estoque) não seriam afetadas.  
 

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA271 - Bloqueio automático de movimentações de produtos para inventário (MV\_BLQINVA)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38347809526295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Bloqueio-autom%C3%A1tico-de-movimenta%C3%A7%C3%B5es-de-produtos-para-invent%C3%A1rio-MV-BLQINVA)
