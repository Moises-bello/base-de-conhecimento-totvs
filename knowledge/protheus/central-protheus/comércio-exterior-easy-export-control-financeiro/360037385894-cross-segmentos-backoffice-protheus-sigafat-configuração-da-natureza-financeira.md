---
article_id: 360037385894
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: a3c673bbfe2e6a3f2c8cfb2530eab3adae76f379104dbfb2049b6b1bfd4a1b87
fetched_at: '2026-06-28T22:36:58.159549+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Configuração da Natureza
  Financeira no Pedido de Vendas (MV_1DUPNAT e MV_2DUPNAT)
type: support-article
updated_at: '2026-04-10T20:24:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037385894-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-da-Natureza-Financeira-no-Pedido-de-Vendas-MV-1DUPNAT-e-MV-2DUPNAT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39666045055639) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como configurar o Protheus para sugerir a Natureza Financeira corretamente no Pedido de Vendas?  
  
**Ambiente**  
Cross Segmentos - BackOffice Protheus - SIGAFAT - Todas as versões.  
  
**Solução**

Para a geração de duplicatas no Financeiro, o Protheus exige uma Natureza Financeira. O sistema utiliza parâmetros para definir de onde essa informação deve ser extraída.

**1. Configuração dos Parâmetros**

Acesse o módulo **Configurador (SIGACFG)** e ajuste os parâmetros abaixo de acordo com a regra de negócio da sua empresa:

* **MV\_1DUPNAT**: Define a origem da natureza para Pedidos de Venda padrão.
* **MV\_2DUPNAT**: Define a origem para Pedidos de Devolução ou que utilizam Fornecedor.

**Opções de preenchimento:**

* `SA1->A1_NATUREZ`: Busca do cadastro do **Cliente**.
* `SA2->A2_NATUREZ`: Busca do cadastro do **Fornecedor**.
* `SC5->C5_NATUREZ`: Busca do campo Natureza no **Cabeçalho do Pedido de Vendas.**

**2. Resolução de Mensagens de Erro (Helps)**

Caso o sistema apresente um alerta ao salvar o pedido, verifique a causa abaixo:

| **Help** | **Causa** | **O que fazer?** |
| --- | --- | --- |
| **A410NATVZO** | Parâmetro em branco. | Preencha o `MV_1DUPNAT` com uma das opções acima. |
| **A410NATUSO** | Campo não está como "Usado". | No Configurador, verifique se o campo (A1\_NATUREZ ou C5\_NATUREZ) está marcado como Usado e se o módulo Faturamento está selecionado na aba "Módulos". |
| **A410NATCLI** | Campo vazio no Cadastro. | Se o parâmetro aponta para o Cliente, preencha o campo Natureza no cadastro do Cliente (MATA030). |
| **A410NATPED** | Campo vazio no Pedido. | Se o parâmetro aponta para o Pedido, preencha o campo Natureza no cabeçalho do Pedido (MATA410). |
| **A410NATBLK** | Natureza Bloqueada. | É necessário utilizar uma natureza que esteja ativa. |

**Saiba mais:**

* [FAQ - Mensagens de Natureza no Pedido de Venda](https://tdn.totvs.com/x/h_ruDQ)
* [Natureza (MATA030 - SIGAFAT)](https://tdn.totvs.com/x/oQ8NF)
