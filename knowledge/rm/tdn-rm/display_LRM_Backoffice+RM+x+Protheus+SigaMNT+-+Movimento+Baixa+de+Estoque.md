---
content_hash: 8a352b6fba7dfd49a06f5e711b693937d377fde77e0d511dd6642202ce58a056
fetched_at: '2026-06-29T00:09:50.829747+00:00'
page_id: '436275085'
product: rm
source: tdn-rm
title: Backoffice RM x Protheus SigaMNT - Movimento Baixa de Estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/Backoffice+RM+x+Protheus+SigaMNT+-+Movimento+Baixa+de+Estoque
version: 6
---

**Backoffice RM x Protheus SigaMNT - Movimento Baixa de Estoque**

---

É necessária a criação de um Tipo de movimento e a parametrização com alguns padrões para que o sistema RM consiga receber os processos de Baixa de Estoque, enviados através do Protheus SigaMNT.

**Passo 1 -** Para criar e parametrizar o movimento acesse através do Sistema RM : Backoffice / Gestão de Estoque , Compras e Faturamento.

**Passo 2 -** Acessar . Aba Ambiente / Configuração / Parâmetros / Gestão de Estoque, Compras e Faturamento.

**Passo 3 -** Selecione Gestão de Estoque / Baixa de Estoque, e clique em Avançar.

**Passo 4 -** Inclua um novo registro preenchendo os campos conforme desejado e salve.

Os campos de **preenchimento obrigatório são :**

**Aba identificação**

* Cód. Tipo de Movimento. 1.2.XX
* Nome Tipo de Movimento.

**Aba Campos Obrigatórios**

* Máscara do Número: #########
* Fórmula do Valor Bruto: 000001
* Fórmula do Sub-Total: 000007
* Fórmula do Valor do Documento: 000008

**Aba Séries**

* Incluir uma nova série

**Passo 5 -**Selecione o Tipo de Movimento incluí e clique em Parametrizar.  
 **Passo 6 -**Clique em Avançar.  
 **Passo 7 -**Selecionar os parâmetros e preencher os campos com os valores abaixo informados .

|  |  |  |
| --- | --- | --- |
| **Etapa** | **Campo** | **Valor** |
| **Mov - Identificação** | Numeração | 1.2.XX |
|  |  |  |
|  | Classificação | Baixa de Estoque (Gestão de Estoque) |
|  | Edita Numeração | Edita |
|  | Mascara Numero | ######### |
|  | Busca Numero em | Filial |
|  | Edição de Série | Mostra |
|  |  |  |
| **Mov - Datas 1/2** | Data de emissão | Edita |
|  | Data do movimento | Data Emissão |
|  | Data de entrega | Não Edita |
|  |  |  |
| **Mov - Outros Dados** | Usar cópia de Movimentos por referencia | Selecionado |
|  | Motivo de Referencia | Código: 25 - Descrição: Cópia Simples com relacionamento somente de Movimento |
|  | Não calcular movimento ao abrir edição | Selecionado |
|  |  |  |
| **Mov – Tab – Global** | Centro de Custo / Obrigatório | Desmarcado |
|  | Edita Centro de Custo | Edita |
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
|  | Data de Entrega | Edita |
|  |  |  |
| **Item - Identificação 2/2** | Permitir item repetido | Selecionado |
|  |  |  |
| **Item - Preços** | Edição de Preços | Edita |
|  | Editar Preço total | Calcular Preço Total |
|  | Aceitar preço zero | Selecionado |
|  | Recalcular sempre ao recalcular movimento | Selecionado |
|  |  |  |
| **Item – Tab – Global** | Centro de Custo | Edita |
|  | Copiar do Movimento | Selecionado |
|  |  |  |
| **Item – Lote/Grade/Num.** | Aceita Número de Série | Selecionado |
|  | Editar Grade Numerada | Selecionado |
|  | Consiste Lote | Selecionado |
|  |  |  |
| **Item - Estoque 1/3** | Saldo Atual | Diminui |
|  |  |  |
| **Item - Estoque 2/3** | Saldo Financeiro / Efeito sobre o saldo atual | Diminui |
|  | Local de estoque por item | Selecionado |
|  |  |  |
| **Rateio C. Custo** | Tipo de rateio | Valor |
|  | Rateio do Movimento / Usa rateio por Centro de Custo | Usa |
|  | Rateio do Movimento /Usar Rateio por Departamento | Não Usa |
|  | Rateio do Item / Usa rateio por Centro de Custo | Usa |
|  | Rateio do Item / Usar Rateio por Departamento | Não Usa |

**Passo 8 -**Clique em Concluir para finalizar as configurações do parâmetros

**Passo 9 -**Acesse o Módulo de Integração.  
    
 **Passo 10 -**Acesse . Integração / Mensagens Únicas / Integrações.  
    
 **Passo 11 -**Selecione a integração e acesse . Anexos / Parâmetros de Integração.  
    
 **Passo 12 -**Incluir um novo Parâmetro de Integração e salvar, preenchendo o cadastro conforme desejado e informando ao campo Valor o Código do movimento parametrizado na etapa Mov - Identificação .
