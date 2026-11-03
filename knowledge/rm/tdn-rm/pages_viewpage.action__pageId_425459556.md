---
content_hash: 4f09dadbce533cfe027a9a90f49b87c03f4204f13338f8d74a004e182ef4d531
fetched_at: '2026-06-29T00:09:37.033660+00:00'
page_id: '425459556'
product: rm
source: tdn-rm
title: Linha RM x Protheus SigaMNT - Movimento Acréscimo em Estoque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459556
version: 2
---

**Linha** **RM x Protheus SigaMNT - Movimento Acréscimo em Estoque**

---

O Tipo de Movimento de Acréscimo em estoque é responsável por efetuar entrada de produtos em determinados Locais de Estoque da empresa, especificados no movimento gerado.

**1 -**Para incluir um Movimento de Acréscimo em estoque acesse através do Sistema RM : Backoffice / Gestão de Estoque , Compras e Faturamento.  
 **2 -**Acessar : Aba Ambiente / Configuração / Parâmetros / Gestão de Estoque, Compras e Faturamento.  
    
 **3 -**Selecione o movimento Gestão de compras / Recebimento de Materiais  e clique em Avançar.   
    
 **4 -**Inclua um novo registro preenchendo os campos conforme desejado e salve. Os campos de preenchimento obrigatório são :

**Aba identificação**

* Cód. Tipo de Movimento: 1.2.XX
* Nome Tipo de Movimento:

**Aba Campos Obrigatórios**

* Máscara do Número: #########
* Fórmula do Valor Bruto: 000001
* Fórmula do Sub-Total: 000007
* Fórmula do Valor do Documento: 000008

**Aba Séries**

* Incluir uma nova série

**5 -** Selecione o Tipo de Movimento Criado e clique em Parametrizar.   
    
 **6 -**Clique em Avançar.  
    
 **7 -**Selecionar os parâmetros e preencher os campos com os valores abaixo informados .

|  |  |  |
| --- | --- | --- |
| **Etapa** | **Campo** | **Valor** |
|  |  |  |
| **Mov - Identificação** | Numeração | 1.2.XX |
|  | Classificação | Recebimento de Materiais (Gestão de Compras) |
|  | Edita Numeração | Edita |
|  | Mascara Numero | ######### |
|  | Busca Numero em | Filial |
|  | Edição de Série | Mostra |
|  |  |  |
| **Mov - Datas 1/2** | Data de emissão | Edita |
|  | Data do movimento | Data Emissão |
|  | Data de entrega | Não Edita |
|  |  |  |
| **Mov - Outros Dados** | Usar cópia de Movimentos por referencia | Checado |
|  | Motivo de Referencia | Codigo: 25   Descrição: Cópia Simples com relacionamento somente de Movimento |
|  | Não calcular movimento ao abrir edição | Checado |
|  |  |  |
| **Mov – Tab – Global** | Centro de Custo - Obrigatório | Desmarcado |
|  |  |  |
| **Mov - Valor Financeiro (Default, pode ser alterado)** | Fórmula Valor Bruto | 000001 |
|  | Fórmula Sub-Total | 000007 |
|  | Fórmula do valor do documento | 000008 |
|  | Edita Moeda | Não edita |
|  |  |  |
| **Mov - Campos Livres 1/2** | Editar Observação | Checado |
|  |  |  |
| **Item - Identificação 1/2** | Nº Máximo de itens | 999 |
|  | Codigo do produto | Código Principal |
|  | Tipo dos Itens | Ambos |
|  | Data de Entrega | Edita |
|  |  |  |
| **Item - Identificação 2/2** | Permitir item repetido | Checado |
|  |  |  |
| **Item - Preços** | Edição de Preços | Edita |
|  | Editar Preço total | Calcular Preço Total |
|  | Aceitar preço zero | Checado |
|  | Recalcular sempre ao recalcular movimento | Checado |
|  |  |  |
| **Item – Tab – Global** | Centro de Custo | Edita |
|  | Copiar do Movimento | Checado |
|  |  |  |
| **Item – Lote/Grade/Num.** | Aceita Número de Série | Checado |
|  | Editar Grade Numerada | Checado |
|  | Consiste Lote | Checado |
|  |  |  |
| **Item - Estoque 1/3** | Saldo Atual | Aumenta |
|  |  |  |
| **Item - Estoque 2/3** | Saldo Financeiro: Efeito sobre o saldo atual | Aumenta |
|  | Local de estoque por item | Checado |
|  |  |  |
| **Rateio C. Custo (Opcional)** | Tipo de rateio | Valor |
|  | Usa rateio por Centro de Custo do Movimento | Usa |
|  | Usar Rateio por Departamento do Movimento | Não Usa |
|  | Usa rateio por Centro de Custo do Item | Usa |
|  | Usar Rateio por Departamento do Item | Não Usa |
|  |  |  |
| **Manutenção** | Integrado com SigaMNT | Checado |
