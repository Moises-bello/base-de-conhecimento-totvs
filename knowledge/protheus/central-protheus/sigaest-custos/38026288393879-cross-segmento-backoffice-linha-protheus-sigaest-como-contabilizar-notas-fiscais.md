---
article_id: 38026288393879
category: SIGAEST - CUSTOS
content_hash: 4f4fe3324d002c5956833d8c7a609eaf24fda570285d101c2aacc731369009be
fetched_at: '2026-06-28T22:39:00.269096+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Como contabilizar
  notas fiscais de entrada com o campo D1_OP preenchido que geram o movimento RE5
type: support-article
updated_at: '2026-01-30T19:58:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38026288393879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-contabilizar-notas-fiscais-de-entrada-com-o-campo-D1-OP-preenchido-que-geram-o-movimento-RE5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38026288364823) Tempo aproximado para leitura: 00**:02:00 min**  
  
**Dúvida**  
Como contabilizar notas fiscais de entrada que possuem o campo **D1\_OP** preenchido e que geram o movimento **RE5** no módulo de Estoque?

**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Para que a nota fiscal de entrada seja corretamente contabilizada juntamente com o movimento de estoque **RE5**, é necessário cadastrar os lançamentos padronizados e executar a rotina de custos conforme os passos abaixo.

#### **Passo 1 – Cadastrar o lançamento padronizado 681**

* Acesse o menu:  
  **Atualizações → Cadastros → Contábil → Lançamentos Padronizados**
* Clique em **Incluir** e cadastre o lançamento **681**.
* Na aba **Valores**, informe a seguinte regra:

   SD1->D1\_CUSTO

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38026301340567)

#### **Passo 2 – Cadastrar o lançamento padronizado 666**

* Na mesma rotina de **Lançamentos Padronizados**, clique em **Incluir**.
* Cadastre o lançamento **666**.
* Na aba **Valores**, informe a seguinte regra:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38026301343383)

#### **Passo 3 – Validar os movimentos na base de dados**

Certifique-se de que os movimentos relacionados à nota fiscal e ao estoque (SD1 e SD3) foram corretamente gravados na base de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38026301347735)

#### **Passo 4 – Executar a rotina de custos**

1. Execute a rotina **Custo Médio / Acompanha Custos**.
2. No parâmetro **Gerar Lançamento Contábil**, selecione **SIM**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38026301348759)

#### **Passo 5 – Conferir a contabilização**

Após a execução da rotina, os **lançamentos contábeis** referentes à nota fiscal de entrada e ao movimento **RE5** serão gerados automaticamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38044208449559)

**Saiba mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Contabilizar as Movimentações no Estoque Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-Contabilizar-as-Movimenta%C3%A7%C3%B5es-no-Estoque-Custos)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-)

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
