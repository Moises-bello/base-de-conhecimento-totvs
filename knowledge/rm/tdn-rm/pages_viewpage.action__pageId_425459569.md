---
content_hash: dc3b3942b5e0e59d29fd65f17dc6aad2a0b40eac4da43faff60ac337def1e08a
fetched_at: '2026-06-29T00:09:37.168751+00:00'
page_id: '425459569'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Movimento Solicitação de Armazém
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459569
version: 2
---

**Linha RM x Protheus SigaMNT - Movimento Solicitação de Armazém**

---

O Tipo de movimento tem o objetivo de criar uma Solicitação de Armazém no Backoffice RM através da mensagem Request. Uma Solicitação de Armazém será criada sempre que uma Ordem de Serviço  do Protheus SigaMNt possuir Insumos Previstos e o seu status for alterado para "Liberado" ou utilizada a funcionalidade Liberar.O.s.  
     
 **Passo 1-** Acessar através do Sistema RM : Backoffice / Gestão de Estoque , Compras e Faturamento.

**Passo 2-** Acessar : Aba Ambiente / Configuração / Parâmetros / Gestão de Estoque, Compras e Faturamento.

**Passo 3-** Selecione o movimento Requisição de Materiais e clique em Avançar.

**Passo 4-** Inclua um novo registro preenchendo os campos conforme desejado e salve.  
    
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

**Passo 5-** Selecione o Tipo de Movimento Criado e clique em Parametrizar.

**Passo 6-** Clique em Avançar.

**Passo 7-** Selecionar os parâmetros e preencher os campos com os valores abaixo informados .

|  |  |  |
| --- | --- | --- |
| **Etapa** | **Campo** | **Valor** |
|  |  |  |
| **Mov - Identificação** | Numeração | 1.1.XX |
|  | Edita Numeração | Edita |
|  | Mascara Numero | ######### |
|  | Busca Numero em | Filial |
|  | Edição de Série | Mostra |
|  |  |  |
| **Mov - Datas 1/2** | Data de emissão | Edita |
|  | Data do movimento | Data Emissão |
|  | Data de entrega | Edita |
|  |  |  |
| **Mov - Outros Dados** | Usar cópia de Movimentos por referencia | Selecionado |
|  | Motivo de Referencia | Codigo: 25 - Descrição: Cópia Simples com relacionamento somente de Movimento |
|  | Não calcular movimento ao abrir edição | Selecionado |
|  |  |  |
| **Mov – Valores Financeiros 2/4** | Fórmula Valor Bruto | 1 |
|  | Fórmula Sub-Total | 7 |
|  | Fórmula do valor do documento | 8 |
|  | Edita Moeda | Não edita |
|  |  |  |
| **Mov - Campos Livres 1/2** | Edita Observação | Selecionado |
|  |  |  |
| **Item - Identificação 1/2** | Nº Máximo de itens | 999 |
|  | Codigo do produto | Código Principal |
|  | Tipo dos Itens | Ambos |
|  | Data Entrega | Edita |
|  |  |  |
| **Item - Identificação 2/2** | Permitir item repetido | Selecionado |
|  |  |  |
| **Item - Preços** | Edição de Preços | Mostra |
|  | Aceitar preço zero | Checado |
|  | Nunca Recalcular | Checado |
|  |  |  |
| **Item – Tab – Global** | Centro de Custo | Edita |
|  | Copiar do Movimento | Checado |
|  |  |  |
| **Item - Estoque 2/3** | Local de estoque por item | Selecionado |
|  |  |  |
| **Rateio C. Custo - Departamento** | Tipo de rateio | Valor |
|  | Rateio do Movimento / Usa rateio por Centro de Custo | Usa |
|  | Rateio do Movimento / Usar Rateio por Departamento | Não Usa |
|  | Rateio do Item / Usa rateio por Centro de Custo | Usa |
|  | Rateio do Item / Usar Rateio por Departamento | Não Usa |
|  |  |  |
| **Compra/Venda – Características (Opcional)** | Opção de Faturamento | Com seleção do tipo de movimento |
|  | Movimento Gerado | [Tipo de Movimento de Baixa MNT] |
|  | Pedir confirmação da baixa do Pedido de Venda | Selecionado |

**Passo  8-** Selecione a ultima aba e clique em avançar.

**Passo  9-** Clique em Concluir para finalizar as configurações do parâmetros.

**Passo 10–** Acesse o Módulo de Integração.

**Passo 11–** Acesse : Integração / Mensagens Únicas / Integrações.

**Passo 12–** Selecione a integração e acesse : Anexos / Parâmetros de Integração.

**Passo 13-**  Incluir um novo Parâmetro de Integração e salvar, preenchendo o cadastro conforme desejado e informando ao campo Valor o Código do movimento parametrizado na etapa Mov - Identificação.
