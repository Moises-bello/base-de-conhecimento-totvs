---
content_hash: a922148ce83cc705ad4c4709e09a451a071ca6528c597fdbfa1058a9c52f75f0
fetched_at: '2026-06-29T00:11:33.912139+00:00'
page_id: '761526266'
product: rm
source: tdn-rm
title: Utilizando a atividade "eSocial - Consulta Qualificação Cadastral"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=761526266
version: 8
---

false🔔 ATENÇÃO:

Com a implantação do FGTS Digital e a validação dos dados do trabalhador sendo realizada unicamente com base no CPF, a Consulta de Qualificação Cadastral Online (individual) foi **desativada** e **não está mais disponível** no portal do eSocial.

Diante disso, o **menu de Qualificação Cadastral** foi **removido da Folha de Pagamento** a partir dos patches:

* 12.1.2410.287
* 12.1.2502.190
* 12.1.2506.130 e superiores

📌 Para mais informações, acesse: [eSocial- Qualificação Cadastral Desativada](https://tdn.totvs.com/pages/releaseview.action?pageId=975770468)

# Índice:

---

.\*ndice:

# Objetivo:

---

Este documento tem por objetivo especificar a atividade “eSocial - Consulta Qualificação Cadastral” disponível na Fórmula Visual.

# Especificação:

---

É uma atividade que permite consultar dados do sistema público eSocial, serviço disponibilizado pelo [TOTVS API Services - TAS](https://tdn.totvs.com/pages/viewpage.action?pageId=647704528). 

          **Pré requisito**: Ter o TOTVS API Services [configurado](https://tdn.totvs.com/pages/viewpage.action?pageId=660564412) nos parâmetros globais do sistema.

| **N°** | **Nome do Parâmetro** | **Descrição do Parâmetro** | **Obrigatoriedade** |
| --- | --- | --- | --- |
| 1 | CNPJ | CNPJ a ser consultado | **OBRIGATÓRIO** |
| 2 | Data de Nascimento | Data no formato DD/MM/YYYY | **OBRIGATÓRIO** |
| 3 | NIS | Número de Identificação Social (NIS) | **OBRIGATÓRIO** |
| 4 | Nome Completo | Nome completo | **OBRIGATÓRIO** |

# Acessando o resultado da consulta:

---

Podemos acessar o resultado da consulta através de uma atividade de [expressão](https://tdn.totvs.com/pages/viewpage.action?pageId=161350726), por exemplo:

Adicionando uma atividade [d](https://tdn.totvs.com/pages/viewpage.action?pageId=149881138)e [Log](https://tdn.totvs.com/pages/viewpage.action?pageId=149881483) podemos testar a consulta e visualizar o resultado:

Salvando e executando a Fórmula Visual podemos ver o retorno do campo especificado.

O fluxo da Fórmula Visual para teste seria semelhante a este:

falsefalse

**Produto:** Framework

false

**Versão:** A partir da 12.1.2306

false

**Processo:** Utilizando atividade "eSocial - Consulta Qualificação Cadastral" via Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:**
