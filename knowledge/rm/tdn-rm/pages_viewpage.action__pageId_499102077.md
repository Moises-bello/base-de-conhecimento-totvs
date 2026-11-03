---
content_hash: 7df6a63be26417a4b340eccad1d79d1bd5eafab9e0f09bfde0f09b4155f8e377
fetched_at: '2026-06-29T00:10:22.772119+00:00'
page_id: '499102077'
product: rm
source: tdn-rm
title: Ocultar Filtros no Relatório
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499102077
version: 12
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Esta página tem por objetivo demonstrar como fixar e ocultar valores das cláusulas dos filtros de relatório durante sua execução.

# Introdução:

---

       Esta configuração atende aos usuários quanto a necessidade de se ocultar filtros de um determinado relatório, preservando suas clausulas e valores no momento de geração.

false.Criando o filtro

       Para exemplo, utilizaremos um relatório que fará uso da tabela de funcionários (PFUNC). Durante a criação do filtro inserimos três cláusulas para exemplificar cada uma das possíveis situações existentes.

       A cláusula “Chapa do Funcionário = 00001” demonstrará um filtro completamente aberto para o usuário. Durante a execução do relatório esse filtro será exibido. Um usuário que executar esse relatório, **PODERÁ** ver e **ALTERAR** a expressão e valor do filtro.

       A cláusula “Chapa do Funcionário = 00002” demonstra um filtro que é fixo. Durante a execução do relatório esse filtro será exibido. O usuário **PODERÁ** ver a expressão e valor do filtro, mas **NÃO PODERÁ** alterá-las.

       A cláusula “Chapa do Funcionário = 00003” demonstra um filtro que é fixo e oculto. Durante a execução do relatório esse filtro não será exibido. O usuário que executar esse relatório **NÃO VISUALIZARÁ**sua expressão e valor.

false

  *Ao salvar o filtro do relatório é possível perceber que o filtro oculto não é exibido.*

Comportamento do filtro ao executar o relatório

       Ao abrir o assistente de execução do relatório e avançar para a tela de filtro, serão visíveis apenas as cláusulas que não estão marcadas como “Ocultas”

       Ao entrar na edição do filtro, o sistema exibirá apenas as duas primeiras cláusulas e manterá a terceira oculta.

       Ao tentar modificar o filtro o sistema permitirá alteração apenas da primeira cláusula. A segunda não será possível pois tratar-se de um filtro fixo e a terceira cláusula não será exibida.

---

---

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Ocultar filtros

falsefalse

**Status:** Finalizado

false

**Data:** 04/07/2019

false

**Autores:**
