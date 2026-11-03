---
article_id: 360018943272
category: SIGAACD - Automação e Coleta de Dados
content_hash: c61b7b278aa6a4c2599513b92d986fe83acf3c1acc74e8c530b879c04082b15b
fetched_at: '2026-06-28T22:39:10.994500+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - É possível trocar
  de endereço durante o processo de Ordem de Separação
type: support-article
updated_at: '2025-07-28T17:00:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018943272-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-%C3%89-poss%C3%ADvel-trocar-de-endere%C3%A7o-durante-o-processo-de-Ordem-de-Separa%C3%A7%C3%A3o
---

O artigo aborda a impossibilidade de trocar o endereço logístico durante a execução da Ordem de Separação (OS) no módulo ACD do TOTVS Backoffice (Linha Protheus) Estoque/Custos. O parâmetro MV\_SUBNSER permite a substituição do número de série apenas dentro do mesmo endereço logístico, não permitindo a alteração do endereço de origem do item. Mesmo que o parâmetro permita substituições, estas são restritas ao endereço físico previamente definido na OS, garantindo a integridade da estratégia de picking e o controle de estoque, e esse controle não funciona no ACD.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33769765075479) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**  
Usando a Ordem de Separação do **ACD**, é possível fazer a troca de endereço?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Atualmente, no **comportamento padrão do módulo ACD**, **não é permitido realizar a troca de endereço logístico durante a execução da Ordem de Separação (OS)**.

### **Sobre o Parâmetro relacionado: MV\_SUBNSER**

O parâmetro `MV_SUBNSER` regula o comportamento de substituição de **número de série** durante a separação, **mas apenas dentro do mesmo endereço logístico**. Ou seja, **não há flexibilização para alteração do endereço de origem do item**, apenas da **identificação do item (número de série)**, conforme configurado.

**Valores permitidos para o parâmetro** `MV_SUBNSER`

**Indica se permite a troca do número de série no ato da separação do pedido de venda.**

| Valor | Descrição |
| --- | --- |
| 1 | Não permite a substituição do número de série (comportamento padrão). |
| 2 | Permite a substituição do número de série, mas apenas no mesmo endereço. |
| 3 | Pergunta ao usuário, em tempo de execução, se deseja substituir o número de série no mesmo endereço. |

> **Importante:** Mesmo que o parâmetro esteja ajustado para permitir substituição (`2` ou `3`), **o sistema irá restringir a substituição ao mesmo endereço físico previamente definido na OS**.

* A tentativa de informar um número de série que esteja **vinculado a um endereço diferente** do registrado na Ordem de Separação resultará em **bloqueio do sistema**, impedindo a continuidade da operação.
* Esse comportamento é intencional e visa preservar a **integridade da estratégia de picking**, evitando divergências de localização ou ruptura no controle de estoque.

A estrutura atual do ACD visa manter controle rigoroso dos processos de separação, com foco em rastreabilidade e integridade logística. **A substituição do endereço durante a separação** **não é contemplada no padrão**, e o parâmetro `MV_SUBNSER` se restringe apenas ao controle de número de série dentro do **mesmo endereço.**

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
