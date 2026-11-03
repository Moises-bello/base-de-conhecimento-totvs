---
content_hash: 46a8165489c92c44e5a63620bb4ee83d28a30dc952025f7ebcc26f92fb704681
fetched_at: '2026-06-29T00:09:37.155382+00:00'
page_id: '425459568'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Movimento Apropriação de Custos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459568
version: 5
---

**Linha** **RM x Protheus SigaMNT - Movimento Apropriação de Custos**

---

É necessária a criação de um Tipo de movimento e a parametrização com alguns padrões para que o sistema RM consiga receber os processos de Apropriação de Custos enviados através do Protheus SigaMNT.  
    
 **Passo 1 -**Para criar e parametrizar o movimento acesse através do Sistema RM : Backoffice / Gestão de Estoque , Compras e Faturamento.

**Passo 2 -**Acessar : Aba Ambiente / Configuração / Parâmetros / Gestão de Estoque, Compras e Faturamento.

**Passo 3 -**Selecione o movimento Outras Movimentações e clique em Avançar.

**Passo 4 -**Inclua um novo registro preenchendo os campos conforme desejado e salve. Os campos de preenchimento obrigatório são :

**Aba identificação**

* Cód. Tipo de Movimento: 2.1.XX
* Nome Tipo de Movimento:

**Aba Campos Obrigatórios**

* Máscara do Número: #########
* Fórmula do Valor Bruto: 000001
* Fórmula do Sub-Total: 000007
* Fórmula do Valor do Documento: 000008

**Aba Séries**

* Incluir uma nova série

**Passo 5 -**Selecione o Tipo de Movimento Criado e clique em Parametrizar.

**Passo 6 -**Clique em Avançar.

**Passo 7 -** Selecionar os parâmetros e preencher os campos com os valores abaixo informados .

|  |  |  |
| --- | --- | --- |
| **Etapa** | **Campo** | **Valor** |
|  |  |  |
| **Mov - Identificação** | Numeração | 2.1.XX |
|  | Classificação | Outras Movimentações |
|  | Edita Numeração | Edita |
|  | Mascara Numero | ###### |
|  | Busca Numero em | Filial |
|  | Edição de Série | Mostra |
|  |  |  |
| **Mov - Datas 1/2** | Data de emissão | Edita |
|  | Data do movimento | Data Emissão |
|  |  |  |
| **Mov – Tab – Global** | Centro de Custo / Obrigatório | Desmarcado |
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
|  |  |  |
| **Item - Identificação 2/2** | Permitir item repetido | Selecionado |
|  |  |  |
| **Item - Preços** | Edição de Preços | Edita |
|  | Aceitar preço zero | Selecionado |
|  | Nunca Recalcular | Selecionado |
|  |  |  |
| **Item – Tab – Global** | Centro de Custo | Edita |
|  |  |  |
| **Item - Estoque 2/3** | Local de estoque por item | Selecionado |
|  |  |  |
| **Rateio C. Custo** | Tipo de rateio | Valor |
|  | Usa rateio por Centro de Custo do Movimento | Usa |
|  | Usar Rateio por Departamento do Movimento | Não Usa |
|  | Usa rateio por Centro de Custo do Item | Usa |
|  | Usar Rateio por Departamento do Item | Não Usa |
|  |  |  |
| **Compra/Venda – Características** | Opção de Faturamento | Com seleção do tipo de movimento |
|  | Lançamentos Pedido Faturado Parcialmente | Não Gerar |
|  | Movimento Gerado | [Tipo de Movimento] |
|  | Baixar Pedido de Venda após Geração do Movimento | Baixa Sempre |
|  |  |  |
| **Projeto** | Informa Projeto/Tarefa | Obrigatório por Item de Movimento |
|  | Usa Rateio de Tarefa | Obrigatório |
|  | Gera Apropriação | Selecionado |

**Passo 8 -**Selecione a ultima aba e clique em avançar :

**Passo 9 -**Clique em Concluir para finalizar as configurações do parâmetros.

**Passo 10 -**Acesse o Módulo de Integração.

**Passo 11 -** Acesse : Integração / Mensagens Únicas / Integrações.

**Passo 12 -**Selecione a integração e acesse : Anexos / Parâmetros de Integração.

**Passo 13 -**Incluir um novo Parâmetro de Integração e salvar, preenchendo o cadastro conforme desejado e informando ao campo Valor o Código do movimento parametrizado na etapa Mov - Identificação.
