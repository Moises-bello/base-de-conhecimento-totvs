---
content_hash: 0d60671c8a3ea15e756027f44dd53149f2f357c6d672439547cbb32243aa9c72
fetched_at: '2026-06-29T00:09:37.119833+00:00'
page_id: '425459562'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Movimento Ordem de Manutenção
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459562
version: 5
---

**Linha** **RM x Protheus SigaMNT - Movimento Ordem de Manutenção**

---

O tipo de movimento Ordem de Manutenção tem o objetivo de criar uma Ordem de Manutenção no Backoffice RM. Após a abertuda de uma Ordem de serviço no Protheus SigaMNt, e o seu status alterado para "Liberado", automáticamente será criado um Movimento de Ordem de Manutenção no Backoffice RM.  
    
 **Passo 1 -** Acessar através do Sistema RM : Backoffice / Gestão de Estoque , Compras e Faturamento.

**Passo 2 -** Acessar : Aba Ambiente / Configuração / Parâmetros / Gestão de Estoque, Compras e Faturamento.

**Passo 3 -** Selecione Outras Movimentações, e clique em Avançar.

**Passo 4 -** Inclua um novo registro preenchendo os campos conforme desejado e salve. Os campos de preenchimento obrigatório são :  
    
 **Aba identificação**

* Cód. Tipo de Movimento: 2.1.XX
* Nome Tipo de Movimento:

**Aba Campos Obrigatórios**

* Máscara do Número : #########
* Fórmula do Valor Bruto : 000001
* Fórmula do Sub-Total: 000007
* Fórmula do Valor do Documento : 000008

**Aba Séries**

* Incluir uma nova série

**Passo 5 -** Selecione o Tipo de Movimento Criado e clique em Parametrizar.   
 **Passo 6 -** Clique em Avançar.   
 **Passo 7 -** Selecionar os parâmetros e preencher os campos com os valores abaixo informados .

| Etapa | **Campo** | **Valor** |
| --- | --- | --- |

| **Mov - Identificação** | Código | 2.1.XX |
| --- | --- | --- |
|  | Classificação | Outras Movimentações |
|  | Edita Numeração | Edita |
|  | Mascara Numero | *#########* |
|  | Busca Numero em | Filial |
|  | Edição de Série | Mostra |
|  | Série | OS |

| **Mov - Datas 1/2** | Data de emissão | Edita |
| --- | --- | --- |
|  | Data do movimento | Data Emissão |
|  | Data de Entrega | Não Edita |

| **Mov – Tab Global** | Centro de Custo / Edita Centro de Custo | ``` Edita ``` |
| --- | --- | --- |

| Mov - Outros Dados | Não calcular movimento ao abrir edição | Selecionado |
| --- | --- | --- |

| **Mov - Valor Financeiro 2/4** | Fórmula Valor Bruto | 1 |
| --- | --- | --- |
|  | Fórmula Sub-Total | 7 |
|  | Fórmula do valor do documento | 8 |
|  | Edita Moeda | Não edita |

| **Mov - Campos Livres 1/2** | Editar Observação | Selecionado |
| --- | --- | --- |

| **Item - Identificação 1/2** | Nº Máximo de itens | 999 |
| --- | --- | --- |
|  | Codigo do produto | Código Principal |
|  | Tipo dos Itens | Ambos |
|  | Data de Entrega | Edita |

| **Item - Identificação 2/2** | Permitir item repetido | Selecionado |
| --- | --- | --- |

| **Item – Preços 1/2** | Edição de Preços | Edita |
| --- | --- | --- |
|  | Aceitar preço zero | Selecionado |
|  | Nunca Recalcular | Selecionado |

| **Item – Tab – Global** | Centro de Custo | Edita |
| --- | --- | --- |
|  | Copiar do Movimento | Selecionado |

| **Item - Estoque 2/3** | Local de estoque por item | Selecionado |
| --- | --- | --- |

| **Rateio C. Custo** | Rateio do Movimento / Usa rateio por Centro de Custo | Não Usa |
| --- | --- | --- |
|  | Rateio do Movimento / Usar Rateio por Departamento | Não Usa |

| **Compra/Venda – Características** | Gera Movimento de Venda | Selecionado |
| --- | --- | --- |
|  | Opção de Faturamento | Com seleção do tipo de movimento |
|  | Pedir Confirmação da Baixa do Pedido de Compra | Selecionado |

**Passo 8 -** Clique em Concluir para finalizar as configurações do parâmetros.

**Passo 9 –** Acesse o Módulo de Integração.

**Passo 10 –** Acesse : Integração / Mensagens Únicas / Integrações.

**Passo 11 –** Selecione a integração e acesse : Anexos / Parâmetros de Integração.

**Passo 12 –** Incluir um novo Parâmetro de Integração e salvar, preenchendo o cadastro conforme desejado e informando ao campo Valor o Código do movimento parametrizado na etapa Mov - Identificação.

---
