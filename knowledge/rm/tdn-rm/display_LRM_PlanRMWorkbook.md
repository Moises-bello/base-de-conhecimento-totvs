---
content_hash: 5d5e5f0447a58ec9ca8cb963b4ebba99f5a43b3c46fa9046cd9079f4673e5514
fetched_at: '2026-06-29T00:05:58.886222+00:00'
page_id: '189305861'
product: rm
source: tdn-rm
title: PlanRMWorkbook
type: documentation
url: https://tdn.totvs.com/display/LRM/PlanRMWorkbook
version: 10
---

# Pré-requisitos

---

2
complete
Linha RM versão 12.1.5 e posteriores

# Descrição

---

A classe PlanRMFactory disponibiliza métodos estáticos para criação de instâncias de PlanRMWorkbook.

# Membros da classe

---

## Propriedades

|  |  |
| --- | --- |
| APIVersion | Versão da API em que o livro foi criado. |
| CodColigada | Código da coligada (banco de dados). |
| CodSistema | Código do Sistema (banco de dados). |
| Culture | Informações de cultura do livro. |
| FileFormat | Formato de arquivo do livro. |
| FullName | Nome completo do livro (diretório + nome do arquivo). |
| HasLock | Verifica se o livro está travado. |
| IdPlanilha | Identificador do livro (banco de dados). |
| IsProtected | Mostra se o livro está protegido. |
| LoadedFromDatabase | Identifica se o livro foi aberto a partir do banco de dados. |
| Name | Nome do livro (filename). |
| Worksheets | Planilhas do livro. |

## Métodos

|  |  |
| --- | --- |
|  | Força o cálculo das fórmulas de um livro. |
|  | Converte o tipo DateTime para o formato de data / tempo do livro. |
|  | Converte o formato de data / tempo do livro para o tipo DateTime. |
|  | Interrompe os cálculo em segundo plano e adquire uma trava exclusiva sobre o livro. |
|  | Libera a trava adquirida pelo método  e reinicia os cálculos em segundo plano. |
|  | Salva o livro com nome, diretório e formatos definidos pelo usuário. |
|  | Salva o livro no mesmo arquivo em que ela foi aberta. |
|  | Salva u livro no banco de dados. |
|  | Serializa o livro aberto. |
|  | Fecha o livro atual. |
|  | Habilita a proteção do livro com uma senha. |
|  | Desabilita a proteção do livro. |

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)
