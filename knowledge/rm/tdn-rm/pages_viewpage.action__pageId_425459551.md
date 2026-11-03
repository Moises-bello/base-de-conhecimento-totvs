---
content_hash: b4a2d8f97141bfbbc8350e0553e90b3bb3e3cb8171eec4f41e90b9947f977c5d
fetched_at: '2026-06-29T00:09:36.981339+00:00'
page_id: '425459551'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Movimento Solicitação de Compra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459551
version: 3
---

**Linha RM x Protheus SigaMNT - Movimento Solicitação de Compra**   
    
 O Tipo de movimento tem o objetivo de criar uma Solicitação de Compra no Backoffice RM através da mensagem Request. Uma Solicitação de Compra será criada sempre que uma Ordem de Serviço do Protheus SigaMNt possuir Insumos Previstos  que não tenham a quantidade informada em estoque e o seu status for alterado para "Liberado", ou utilizada a funcionalidade Liberar.O.s.  
    
 **Passo 1 -** Acessar através do Sistema RM : Backoffice / Gestão de Estoque , Compras e Faturamento.

**Passo 2 -**Acessar : Aba Ambiente / Configuração / Parâmetros / Gestão de Estoque, Compras e Faturamento.

**Passo 3 -**Selecione Gestão de Compras / Solicitação de Compra, e clique em Avançar.

**Passo 4 -** Inclua um novo registro preenchendo os campos conforme desejado e salve.   
    
 **Os campos de preenchimento obrigatório são :**  
    
 **Aba identificação**

* Cód. Tipo de Movimento: 1.1.XX
* Nome Tipo de Movimento:

**Aba Campos Obrigatórios**

* Máscara do Número : #########
* Fórmula do Valor Bruto : 000001
* Fórmula do Sub-Total: 000007
* Fórmula do Valor do Documento : 000008

**Aba Séries**

* Incluir uma nova série

**Passo 5  -**Selecione o Tipo de Movimento Criado e clique em Parametrizar.

**Passo 6  -**Clique em Avançar.

**Passo 7 -**Selecionar os parâmetros e preencher os campos com os valores abaixo informados .

|  |  |  |
| --- | --- | --- |
| **Etapa** | **Campo** | **Valor** |
|  |  |  |
| **Mov - Identificação** | Código | 1.1.XX |
|  | Classificação | Solicitação de Compras (Gestão Compras) |
|  | Edita Numeração | Edita |
|  | Mascara Numero | ###### |
|  | Busca Numero em | Filial |
|  | Edição de Série | Mostra |
|  |  |  |
| **Mov - Datas 1/2** | Data de emissão | Edita |
|  | Data do movimento | Data Emissão |
|  | Data de entrega | Edita |
|  |  |  |
| **Mov - Outros Dados** | Usar cópia de Movimentos por referencia | Selecionado |
|  | Motivo de Referencia | Codigo: 6   Descrição: NF Complementar/ Retificadora |
|  | Não calcular movimento ao abrir edição | Selecionado |
|  |  |  |
| **Mov – Tab – Global** | Edita Centro de Custo - | Edita |
|  | Obrigatório - | Desmarcado |
|  |  |  |
| **Mov - Valor Financeiro 2/4** | Fórmula Valor Bruto | 1 |
|  | Fórmula Sub-Total | 7 |
|  | Fórmula do valor do documento | 8 |
|  | Edita Moeda | Não edita |
|  |  |  |
| **Mov - Campos Livres 1/2** | Editar Observação | Selecionado |
|  |  |  |
| **Item - Identificação 1/2** | Nº Máximo de itens | 999 |
|  | Codigo do produto | Código Principal |
|  | Tipo dos Itens | Ambos |
|  | Data Entrega | Edita |
|  |  |  |
| **Item - Identificação 2/2** | Permitir item repetido | Selecionado |
|  |  |  |
| **Item - Preços** | Edição de Preços | Não Edita |
|  | Aceitar preço zero | Selecionado |
|  | Recalcular Somente quando a condição de pagamento é alterada | Selecionado |
|  |  |  |
| **Item – Tab – Global** | Centro de Custo | Edita |
|  | Copiar do Movimento | Selecionado |
|  |  |  |
| **Item - Estoque 2/3** | Local de estoque por item | Selecionado |
|  |  |  |
| **Rateio C. Custo (Opcional)** | Tipo de rateio | Valor |
|  | Rateio do Movimento / Usa rateio por Centro de Custo | Usa |
|  | Rateio do Movimento / Usar Rateio por Departamento | Não Usa |
|  | Rateio do Item / Usa rateio por Centro de Custo | Usa |
|  | Rateio do Item / Usar Rateio por Departamento | Não Usa |
|  |  |  |
| **Compra/Venda – Características** | Opção de Faturamento | Com seleção do tipo de movimento |
|  | Lançamentos Pedido Faturado Parcialmente | Não Gerar |
|  | Movimento Gerado | [Tipo de Movimento de Ordem de Compra] |
|  | Baixar Pedido de Venda após Geração do Movimento | Baixa Sempre |
|  | Pedir confirmação da baixa do Pedido de Venda | Selecionado |
|  |  |  |
| **Compra/Venda – Outros** | Tipo do Movimento de Compra | Solicitação de Compras |

**Passo  8 -**Selecione a ultima aba e clique em avançar:

**Passo  9 -**Clique em Concluir para finalizar as configurações do parâmetros

**Passo 10 -**Acesse o Módulo de Integração.

**Passo 11 -**Acesse : Integração / Mensagens Únicas / Integrações.

**Passo 12 -**Selecione a integração e acesse : Anexos / Parâmetros de Integração.

**Passo 13 -**Incluir um novo Parâmetro de Integração e salvar, preenchendo o cadastro conforme desejado e informando ao campo Valor o Código do movimento parametrizado na etapa Mov - Identificação.   
    
 **Observações:**

**1** – Para a Integração Linha RM x Protheus SigaMNT é necessário que o valor "Edita " seja selecionado no Combo Box Edita Numeração.   
    
 **2** – O Movimento cadastrado aceitará o valor "Edita" no combo box Edita Numeração, somente se o check box Solicitação de Compra a partir do RM Factor estiver desmarcado, dentro da aba Produção :   
    
 **3** - Se a integração Linha Rm x Protheus SigaMNT estiver ativada, o campo solicitação de compra a partir do RM Factor selecionado dentro da aba Produção e o campo combo box Edita Numeração selecionado com o valor "Edita" dentro da aba Identificação , será exibida uma mensagem ao usuário informando que o Edita numeração não é permitido para integração com o RM Factor.
