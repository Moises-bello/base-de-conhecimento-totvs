---
content_hash: 20244a77c48e0bcf4cf8ed62b8fbaa7d6e7f0f8caecbdea2ff97d7df9268dbef
fetched_at: '2026-06-29T00:08:17.763804+00:00'
page_id: '258278485'
product: rm
source: tdn-rm
title: Exportação e Importação de Relatórios Versionados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=258278485
version: 33
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

# Importação:

---

falseImportaçãoSelecionando relatório para importação

| **Na visão de relatórios do sistema, sele**cione o men**u**  **"Processo | Importar Estrutura de Relatórios”** | Busque o relatório onde estejam salvos ou na pasta “Objetos Gerências”  (Diretório Default da instalação: C:\totvs\CorporeRM\ObjetosGerenciais\Relatórios) |
| --- | --- |
|  |  |

Conferencia de dados na importação:

      Durante o processo de importação existe a possibilidade de comparar se as consultas SQL importadas são iguais ou não as consultas de mesmo código existentes na base.  Com isto, é possível escolher entre as opções “Importar sentença e substituir se existir”, “Não importar (Utilizar a Atual)” ou “Importar com Outro Código”

      Quando já existe um relatório na base de dados que possui o mesmo código do relatório a ser importado, um aviso é exibido informando tal situação. Caso o usuário queira importar o relatório com este código, a opção “Sobrescrever Existente” deverá ser marcada. Com isso o relatório que que existe na base será substituído pelo relatório selecionado na importação:

      No caso de um relatório versionado, além do aviso de existência de um relatório de mesmo nome na base, outro aviso é exibido informando que por ser um relatório versionado o código do mesmo não pode ser alterado. Caso o usuário execute o processo, por se tratar de um relatório versionado, ele será importado substituindo o relatório existente na base de dados mesmo que a opção “Sobrescrever Existente” esteja desmarcada.

Importantefalse

      Relatórios ***versionados não permitem*** que sua estrutura ***seja alterada***!

      Caso exista na base de dados um relatório versionado, que teve seu código alterado manualmente, ao importar o relatório versionado de código original, o relatório existente na base de dados será substituído pelo relatório importado mesmo que a opção “Sobrescrever Existente” esteja desmarcada. Exemplo:

Editando Relatório Versionadofalse

      Para ter acesso a estrutura de edição de um relatório versionado, é necessário que o usuário importe o relatório desejado, exporte-o para um diretório de sua escolhe e importe este relatório anteriormente exportado pois ao fazer isso, o relatório deixa de ser versionado possibilitando então que o usuário altere a estrutura do relatório da maneira que lhe for conveniente. Exemplo:

      Selecionar e exportar o relatório versionado:

      Após, selecionar o processo “Importar Estrutura de Relatórios”

      Selecionar o relatório anteriormente exportado:

      Como o relatório deixa de ser versionado, seu código pode ser alterado durante o processo de importação:

|  |  |
| --- | --- |

      Executar o processo:

false

      Observe que o relatório agora deixa de ser versionado o que possibilita que o usuário altere a estrutura do relatório do modo mais adequado as suas necessidades.

|  |  |
| --- | --- |

# Exportação:

---

      Este processo tem a mesma funcionalidade para relatórios ***versionados***quanto para ***não versionados***. Para acessar a janela de exportação de relatórios, depois de selecionado qualquer produto, acesse o menu "Gestão | Ferramentas de Análise | RM Reports"

falseExportaçãoExportando o relatório

    Marque o relatório e selecione "Processos | Exportar Estrutura de Relatórios”

    Escolha um diretório para salvar o relatório em disco.

|  |  |
| --- | --- |

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.12 ou Superiores

false

**Processo:** Exportação e Importação de Relatórios Versionados

falsefalse

**Status:** Finalizado

false

**Data:** 22/09/2016

false

**Autores:**
