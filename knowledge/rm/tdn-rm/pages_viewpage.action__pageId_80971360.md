---
content_hash: dd4b94c970e6a5f8672234014bede4e1b09d737da3e87b1e7eb5d4ed03c3e3e9
fetched_at: '2026-06-29T00:11:44.203522+00:00'
page_id: '80971360'
product: rm
source: tdn-rm
title: RPT00004.2 - Importar Relatório pela nova MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=80971360
version: 15
---

# Índice:

---

.\*ndice:

# Objetivo:

---

          O objetivo deste documento é exemplificar as possibilidades existentes na exportação/importação de relatórios.

# Introdução:

---

          O sistema disponibiliza arquivos gerenciais que auxiliam o usuário na extração de diversas informações. Dentre estes disponibilizamos alguns relatórios. Abaixo será exemplificado as possibilidades para importação..

# Definições:

---

          Sabendo que os objetos gerenciais configurados como globais impactam todo o sistema, relatórios e seus objetos como fórmulas, gráficos, consultas SQL entre outros. Serão importados na coligada corrente, mesmo que o relatório exportado e seus objetos possuíam atribuições de uma coligada global.

# Como Usar:

---

falseImportaçãoSelecionando relatório para importação

| **Na visão de relatórios do sistema, sele**cione o men**u**  **"Processo | Importar Estrutura de Relatórios”** | Busque o relatório onde estejam salvos ou na pasta “Objetos Gerências”  (Diretório Default da instalação: C:\totvs\CorporeRM\ObjetosGerenciais\Relatórios) |
| --- | --- |
|  |  |

Conferencia de dados na importação:

      Durante o processo de importação existe a possibilidade de comparar se as consultas SQL importadas são iguais ou não as consultas de mesmo código existentes na base.  Com isto, é possível escolher entre as opções “Importar sentença e substituir se existir”, “Não importar (Utilizar a Atual)” ou “Importar com Outro Código”

      Quando já existe um relatório na base de dados que possui o mesmo código do relatório a ser importado, um aviso é exibido informando tal situação. Caso o usuário queira importar o relatório com este código, a opção “Sobrescrever Existente” deverá ser marcada. Com isso o relatório que que existe na base será substituído pelo relatório selecionado na importação:

      No caso de um relatório versionado, além do aviso de existência de um relatório de mesmo nome na base, outro aviso é exibido informando que por ser um relatório versionado o código do mesmo não pode ser alterado. Caso o usuário execute o processo, por se tratar de um relatório versionado, ele será importado substituindo o relatório existente na base de dados mesmo que a opção “Sobrescrever Existente” esteja desmarcada.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Importar Relatório

falsefalse

**Status:** Em construção

false

**Data:** 03/04/2020

false

**Autores:**
