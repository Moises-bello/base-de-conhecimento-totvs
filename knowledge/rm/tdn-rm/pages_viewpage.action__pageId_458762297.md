---
content_hash: 99fda9c358104cf40948efc004595efec8464ca9bd5da6ac92ed27ca3d483f6a
fetched_at: '2026-06-29T00:10:13.842157+00:00'
page_id: '458762297'
product: rm
source: tdn-rm
title: Filtro Obrigatório ao Executar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=458762297
version: 11
---

# Índice:

---

.\*ndice:

# Objetivo

---

Esta página tem a finalidade de relatar a forma de uso e funcionalidades do ***Filtro Obrigatório ao Executar***.

# Introdução

---

Existem relatórios que ao serem executados retornam centenas de registros demandando alto processamento e com morosidade na geração do relatório. Muitos desses casos é ocasionado simplesmente porque o usuário esqueceu de informar o filtro durante a geração do relatório. Por isso, disponibilizamos o recurso para informar se o filtro é obrigatório para a geração do relatório. Assim, ao solicitar a geração do relatório o sistema irá bloquear essa execução até que o usuário informe um filtro para a sua geração.

Disponibilidade

*Versão **12.1.24** e superiores* - Recurso nativo

*Versão **12.1.22** e superiores* - Recurso disponível através da execução de scripts específicos na base de dados.

# Utilização

---

Na tela de edição do relatório é necessário marcar a caixa de seleção *"Filtro obrigatório ao executar"*.

Quando o relatório for executado sem filtro o sistema irá notificar o usuário sobre a obrigatoriedade do filtro. A notificação será através de uma caixa de mensagem quando o relatório for executado pelo assistente de geração ou através do log de execução quando gerado através de processos:

Após informar os filtros necessários o relatório seguirá o fluxo normal de geração.

Aplicações

Filtros somente são aplicados para relatórios que possuam pelo menos uma tabela como fonte de dados. Relatórios que possuem apenas fonte de dados SQL não possuem filtros para aplicar esse recurso.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Filtro Obrigatório ao Executar

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
