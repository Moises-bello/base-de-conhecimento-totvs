---
content_hash: 3b1eeccb73fced494eed4b4d761bc403e144190995891d9c8334d571c16771f9
fetched_at: '2026-06-29T00:12:03.424909+00:00'
page_id: '908685260'
product: rm
source: tdn-rm
title: Tabela de Preço
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=908685260
version: 99
---

Introdução | Tabela de Preço 

# TOTVS Educacional | Tabela de Preço

A evolução da precificação por crédito: Flexibilidade sem duplicidade de dados acadêmicos.

## 📌 O que é esta funcionalidade?

A **Tabela de Preço**  permite separar as regras de precificação
do contexto acadêmico, possibilitando valores distintos por campus/polo, filial, turma e período letivo
sem a necessidade de duplicar matrizes curriculares no ensino superior.

### Cenário anterior à implementação da Tabela de Preço

Para aplicar valores diferentes, a instituição precisa duplicar matrizes,
disciplinas e vínculos acadêmicos, aumentando riscos operacionais e retrabalho.

### ✅ Novo Cenário

A precificação passa a ser centralizada em tabelas independentes,
mantendo a estrutura acadêmica única e reutilizável.

## 🎯 Quando utilizar esta funcionalidade?

* Instituições com valores diferentes por **campus/polo, filial e turma**
* Ofertas com precificação distinta para **novos ingressantes**
* Necessidade de **reajustes rápidos** por período letivo
* Ambientes que exigem **flexibilidade comercial** sem impacto acadêmico

## 🔄 Visão Geral do Fluxo de Implementação

**1. Parâmetros**

Ativação da funcionalidade nos parâmetros do sistema

**2. Cadastro**

Construção da tabela de preço.

**3. Matrícula**

Associação da tabela de preço no curso/habilitação do aluno.

**4. Cobrança**

Geração dos lançamentos financeiros

### ⚠️ Atenção antes de parametrizar

Esta funcionalidade impacta diretamente a geração de cobranças.
Recomenda-se validar o cenário institucional, público-alvo e regras de hierarquia
antes de avançar para as etapas de configuração.

![Demonstração](https://tdn.totvs.com/download/attachments/425458939/1067036887/White%20Colorful%20Modern%20Diagram%20Graph%20(1).gif)
**Mão na Massa: Tabela de Preço na prática**

### Regras Sistêmicas da Tabela de Preço

| Pilar | Regra de Funcionamento | Benefício Sistêmico |
| --- | --- | --- |
| Público-Alvo | Aplicado inicialmente para cobrança por crédito em Calouros. | Define a precificação na matrícula que acompanhará o aluno até o fim. |
| Hierarquia | Busca 1º a tabela do Campus/Polo, senão usa o Default da Matriz Aplicada. | Permite definir valores distintos para o mesmo curso em campus/polo e Matrizes Aplicadas diferentes. |
| Reajuste | Ação centralizada para aplicar percentuais com Histórico de Ajuste. | Evita o reajuste retroativo indesejado e a necessidade de duplicar matrizes. |
| Otimização | Possibilidade de Importação via CSV. | Reduz o tempo de preenchimento manual de valores por disciplina. |

]]>
