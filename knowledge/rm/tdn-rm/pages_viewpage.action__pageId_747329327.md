---
content_hash: eca55f3c9e51167eafc7fa01c68f3a6d184c656d18715d2b883e6c45cbb24b92
fetched_at: '2026-06-29T00:11:32.749752+00:00'
page_id: '747329327'
product: rm
source: tdn-rm
title: Processo de Exportar/Importar Recurso  Smart View no RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=747329327
version: 7
---

# Objetivo:

---

          O objetivo deste documento é exemplificar as possibilidades existentes na exportação/importação de recursos do Smart View no RM.

# Introdução:

---

          O sistema disponibiliza arquivos gerenciais que auxiliam o usuário na extração de diversas informações. Dentre estes disponibilizamos alguns recursos. Abaixo será exemplificado as possibilidades para importação.

# Definições:

---

          Sabendo que os objetos gerenciais configurados como globais impactam todo o sistema, recursos e seus objetos como Relatórios, Tabelas Dinâmicas e Visões de Dados. Serão importados na coligada corrente, mesmo que o recurso exportado e seus objetos possuíam atribuições de uma coligada global.

# Como Usar:

---

false

# Exportar Recurso Smart View no RM

ExportaçãoSelecionando recurso para importação

| **Na visão de recursos Smart View, sele**cione o men**u**  **"Processos | Exportar Recurso”** | Após a execução do processo, clique em "Salvar Arquivo" e selecione onde deseja salvar o arquivo: |
| --- | --- |
|  |  |

A partir da versão 12.1.2406

Na visão de recursos Smart View, selecione o recurso a ser exportado, em seguida, clique em **Mais ações → Exportar Recurso Smart View**

O Download do recurso será realizado na pasta de destino

false

# Importar Recurso Smart View no RM

ImportaçãoSelecionando recurso para importação

| **Na visão de recursos Smart View, sele**cione o men**u**  **"Processo | Importar Recurso”** | Busque o recurso onde estejam salvos: |
| --- | --- |
|  |  |

Conferencia de dados na importação:

* Durante o processo de importação existe a possibilidade código do recurso, sistema para importação.

* Quando já existe um recurso na base de dados que possui o mesmo código do recurso a ser importado, um aviso é exibido informando tal situação. Caso o usuário queira importar o recurso com este código, a opção “Sobrescrever Existente” deverá ser marcada. Com isso o recurso que que existe na base será substituído pelo recurso selecionado na importação:

* No caso de um recurso exportado que possui a versão inválida, ao final do processo será emitido um aviso o motivo pelo qual o recurso não pode ser importado:

A partir da versão 12.1.2406

Na visão de recursos Smart View, selecione o recurso a ser importado, em seguida, clique em **Processos → Importar Recurso Smart View**

O assistente de importação será exibido na tela, em seguida, selecione o arquivo que deseja importar

Seguindo as etapas existentes, é possível alterar o nome do objeto (caso o mesmo não seja um Objeto padrão totvs) e sua aplicação:

.

Após a conclusão do processo com sucesso, o recurso será importado informando a seguinte mensagem:

Índice

.\*ndice:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.2306

false

**Processo:** Integração com o
