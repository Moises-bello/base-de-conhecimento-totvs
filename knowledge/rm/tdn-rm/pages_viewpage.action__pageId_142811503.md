---
content_hash: 12fc656fd85cc595f69034cdb7371c33c68244f9dcba965c9887a9a487627f85
fetched_at: '2026-06-29T00:05:55.388793+00:00'
page_id: '142811503'
product: rm
source: tdn-rm
title: Utilizando a atividade "Alterar propriedade da coluna"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=142811503
version: 23
---

# Adicionar Registro na Tabela:

---

Permiti que o usuário consiga alterar as propriedades de um campo em qualquer visão do sistema.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **ATIVIDADE** |  | **Propriedades** | **Função** | **Valor** |
| Coluna | Qual a tabela/campo será alterado | Activity=RMSWorkflow, Path=DataSet.Tables["GCOLIGADA"] .Columns["NOMEFANTASIA"] |
| NovoTitulo | Altera o label do campo na visão | True / False |
| PermitirEdicao | Se será possível editar o campo | True / False |
| PermitirNulo | Se o campo permitirá valores nulos | True / False |
| ValorPadrao | Seta um valor padrão quando exibir a visão | - |
| Visível | Se o campo será visível | True / False |
| **GATILHO** | -Após a leitura do DataSet vazio.  -Se necessário utilizar campo complementar, adicione o gatinho "Após a Leitura de Edição" | | | |

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e Superiores

false

**Processo:** Fórmula Visual - Utilizando a atividade "Alterar propriedade da coluna"

falsefalse

**Status:** Finalizado

false

**Data:** 23/04/2014

false

**Autores:**
