---
article_id: 32988817534359
category: SIGAEST - RELATORIOS
content_hash: 54600c316ee534fa20ec25f372194a09ed77ef2bed99607ae55212e0d91e2584
fetched_at: '2026-06-28T22:39:06.207874+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 – Significado
  das Informações CLI, FOR, CC, PJ, OP e OS nas Movimentações
type: support-article
updated_at: '2025-06-23T14:57:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32988817534359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Significado-das-Informa%C3%A7%C3%B5es-CLI-FOR-CC-PJ-OP-e-OS-nas-Movimenta%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32988817515927) Tempo aproximado para leitura: 00:01:00 **min**

**Dúvida:**  
 Quais são os significados das informações CLI, FOR, CC, PJ, OP e OS no relatório MATR900?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Este artigo tem como objetivo esclarecer o significado e a aplicação prática dos campos **Cli**, **For**, **CC**, **PJ**, **OP** e **OS** exibidos na rotina **MATR900**. Esses campos representam entidades envolvidas nas movimentações e possuem implicações diretas em diversas rotinas do sistema Protheus.

### **Informações Detalhadas:**

#### **CLI: Cliente envolvido no movimento**

* **Formato:** C + Código do Cliente
* **Descrição:** Indica o cliente vinculado à movimentação.
* **Aplicação:** Utilizado, por exemplo, em **notas de pedido de venda** ou **beneficiamento** pelas rotina **MATA410 (Pedido de Venda) ou MATA103 (documento de entrada),** que utilizam o código do cliente.

#### **FOR: Fornecedor envolvido no movimento**

* **Formato:** F + Código do Fornecedor
* **Descrição:** Representa o fornecedor que participa da movimentação.
* **Aplicação:** Também pode estar presente em **Documento de entrada (MATA103)** **notas de devolução** ou **beneficiamento**, via **MATA410**.

#### **CC: Centro de Custo**

* **Formato:** CC + Código do Centro de Custo
* **Descrição:** Refere-se ao centro de custo envolvido na movimentação.
* **Aplicação:**
  + Pode gerar **movimentações internas** através da rotina **MATA241**.
  + Permite gerar **solicitações ao armazém** via rotina **MATA105**, informando o centro de custo relacionado.

#### **PJ: Projeto (SIGAPMS)**

* **Formato:** PJ + Código do Projeto
* **Descrição:** Identifica o projeto do módulo **SIGAPMS** vinculado à movimentação.
* **Aplicação:**
  + Pode ser usado para **gerar solicitações ao armazém** vinculadas ao projeto.
  + Notas de entrada também podem ser relacionadas ao mesmo projeto.

#### **OP: Ordem de Produção (SIGAPCP)**

* **Formato:** OP + Número da Ordem de Produção
* **Descrição:** Refere-se à ordem de produção criada no módulo **SIGAPCP**.
* **Aplicação:** Permite geração de ordem de produção via rotina **MATA650**.

#### **OS: Ordem de Serviço (SIGAMNT)**

* **Formato:** OS + Número da Ordem de Serviço
* **Descrição:** Representa a ordem de serviço vinculada à movimentação, do módulo **SIGAMNT**.
* **Aplicação:** Identifica que o movimento está associado a uma ordem de serviço em execução.

### **Conclusão:**

Cada um dos campos descritos tem papel específico e impacto direto nas movimentações registradas na rotina MATR900. Compreender o significado e a funcionalidade de cada sigla permite maior controle e rastreabilidade dos processos logísticos, produtivos e financeiros dentro do Protheus.

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Relatórios no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
