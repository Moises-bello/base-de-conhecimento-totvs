---
article_id: 360021321072
category: SIGAEST - INVENTÁRIO
content_hash: a7a358aa3bd2ef9351a7f733aefeb3107d68ffc6b275b544f26713a8df2409b7
fetched_at: '2026-06-28T22:38:50.316949+00:00'
product: protheus
section_id: 1500001538961
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA271 - Bloqueio
  de produtos para inventário por data calculada
type: support-article
updated_at: '2026-06-23T19:30:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021321072-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Bloqueio-de-produtos-para-invent%C3%A1rio-por-data-calculada
---

A rotina de bloqueio/desbloqueio no Protheus visa garantir a integridade dos saldos durante inventário, bloqueando movimentações por data informada manualmente ou data calculada automaticamente com base no início do inventário ou período registrado. A função BLQINVENT verifica o bloqueio, retornando verdadeiro ou falso, e o parâmetro MV\_BLQINVA automatiza o processo para produtos com bloqueio ativo. Procedimentos práticos são realizados via rotina MATA271.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37030302115991) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**

Como funciona o bloqueio/desbloqueio de produtos para inventário por Data Calculada no *Protheus*?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Esta rotina tem como finalidade primordial **bloquear e desbloquear** as movimentações de estoque de produtos em uma data específica (informada ou calculada).

O bloqueio de movimentações visa **assegurar a integridade dos saldos físicos e financeiros** dos itens durante o processo de inventário, impedindo qualquer alteração de saldo nos produtos que estão sendo inventariados.

### 

### **Mecanismos de Bloqueio**

O bloqueio de inventário pode ser configurado de duas maneiras, conforme parametrização:

| **Modalidade** | **Descrição** | **Base de Cálculo** |
| --- | --- | --- |
| **Por Data Informada** | A data do bloqueio é definida e inserida **manualmente** pelo usuário no momento da execução da rotina. | Data informada no parâmetro de execução. |
| **Por Data Calculada** | A data do bloqueio é determinada **automaticamente** pelo sistema. | Baseada na Data do último Inventário (`B2_DINVENT`) ou na Data Base mais o Período de Inventário (`B1_PERINV`) registrado no Cadastro de Produtos. |

O registro da data de bloqueio é armazenado no campo **"Data Inicial Bloq. de Inventário" (**`B2_DTINV`**)**, disponível na tabela **SB2 - Saldos Físico e Financeiro**.

### 

### **Validação de Bloqueio (Função** `BLQINVENT`**)**

O *framework* do sistema utiliza a função `BLQINVENT (ExpC1, ExpC2, ExpD1)` para verificar se uma movimentação está bloqueada:

| **Parâmetro** | **Tipo** | **Descrição** |
| --- | --- | --- |
| `ExpC1` | Caractere | Código do Produto a ser verificado. |
| `ExpC2` | Caractere | Código do Local/Armazém a ser verificado. |
| `ExpD1` | Data (Opcional) | Data da movimentação a ser verificada. Se omitida, a *database* será considerada. |

* **Retorno:** A função retorna **.T.** (Verdadeiro - Bloqueado) ou **.F.** (Falso - Desbloqueado).
* **Utilização:** Esta função está disponível para uso em *User Functions*, validações e demais customizações.

> **❗ Observação de Parâmetro Global:**
>
> Quando o parâmetro [**MV\_BLQINVA**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38347809526295) estiver habilitado, e a data base do ambiente estiver maior que a data do parâmetro **MV\_DATAINV,** o sistema Protheus processa o bloqueio automaticamente para todos os produtos.

## **Procedimentos de Teste (MATA271)**

Abaixo estão os passos para a execução prática da rotina de bloqueio e desbloqueio:

### **Bloqueio de Produto por Data Calculada**

1. **Acesso:** Acesse a rotina **MATA271**.
2. **Parâmetro Inicial:** Preencha o campo **"Quanto ao Produto"** com a opção `Bloqueio`.
3. **Seleção:** Selecione o(s) Armazém(ns) e o(s) Produto(s) que serão alvo do inventário.
4. **Período:** Preencha as perguntas de **"Data de/até"** com o período que deve ser considerado para o bloqueio.
5. **Data do Inventário:** Selecione a opção `Data Calculada`.
6. **Data Informada:** Deixe o campo `Data Informada` em branco.
7. **Confirmação:** Ao confirmar, selecione os Armazéns na tela apresentada e clique em `OK`.

### **Desbloqueio de Produto por Data Informada**

1. **Acesso:** Acesse a rotina **MATA271**.
2. **Parâmetro Inicial:** Preencha o campo **"Quanto ao Produto"** com a opção `Desbloqueio`.
3. **Seleção:** Selecione o(s) Armazém(ns) e o(s) Produto(s) que serão desbloqueados.
4. **Período:** Preencha as perguntas de **"Data de/até"** com o período que **contemple a data do último inventário (**`B2_DINVENT`**)**.
5. **Data do Inventário:** Selecione a opção `Data Informada`.
6. **Data Informada:** Deixe o campo `Data Informada` em branco.
7. **Confirmação:** Ao confirmar, selecione os Armazéns na tela apresentada e clique em `OK`.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Inventário no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538961-SIGAEST-INVENT%C3%81RIO)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA271 - Bloqueio automático de movimentações de produtos para inventário (MV\_BLQINVA)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/38347809526295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA271-Bloqueio-autom%C3%A1tico-de-movimenta%C3%A7%C3%B5es-de-produtos-para-invent%C3%A1rio-MV-BLQINVA)
