---
content_hash: cb108d2b87837d77728e3891664263717e07590de661f0bd31dc38baa6e9ca56
fetched_at: '2026-06-29T00:10:27.047309+00:00'
page_id: '516207507'
product: rm
source: tdn-rm
title: Utilizando a atividade "Iniciar Transação"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516207507
version: 2
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      A atividade "Importar registros na tabela" tem por função controlar uma transação no banco de dados

**02. EXEMPLO DE UTILIZAÇÃO**

Exemplo abaixo:

* Foi adicionado ao fluxo de trabalho sequencial a atividade "Iniciar Transação" e dentro da mesma foram adicionadas as atividades descritas abaixo:
* Foi adicionado uma atividade de "[Ler Registro](https://tdn.totvs.com/x/lQLvC)" para chamar o Data Server da Tabela Utilizada (GlbPerfilData)
* Em seguida foi utilizada a atividade "[Adicionar Registro na Tabela](https://tdn.totvs.com/x/jAHvC)" para adicionar os dados do registro que vai ser criado e referenciar em qual tabela está sendo criado
* Para finalizar a fórmula foi adicionado a atividade "Salvar Registro" para salvar o registro que stá sendo criado, passando como informação o data server utilizado e referenciando a atividade de "Ler Registro"
