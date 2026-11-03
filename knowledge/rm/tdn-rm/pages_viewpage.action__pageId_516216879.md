---
content_hash: daacd1a32e9eccc094ee3cbf218ea14233200d317f5d90d95846fd04b34b71b6
fetched_at: '2026-06-29T00:10:27.085776+00:00'
page_id: '516216879'
product: rm
source: tdn-rm
title: RM Reports - Aplicar SQL Distinct em Sub-Detalhe.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=516216879
version: 1
---

# Índice

---

# Introdução

---

Opção nas configurações de um sub-detalhe para Aplicar SQL distinc.

# Objetivo

---

Com a opção de aplicar um sql distinct, é possível evitar repetições de dados em uma bando do relatório RM Reports.

# Aplicar SQL Distinct

---

Nas configurações do Sub-Detalhe, é possível marcar a opção para adicionar um distinct na consulta SQL gerada para a geração do relatórios, evitando assim a repetição de dados desnecessários..

**Exemplo das consultas geradas ao gerar um relatório**

**Sem o "Aplica SQL Distinct":**

SELECT PFUNC.CHAPA,PFUNC.NOME,PFUNC.SALARIO,PFUNC.CODCOLIGADA,ABATFUN.DATAREFERENCIA  
AS DATAREFERENCIA\_2053604311  
FROM PFUNC PFUNC (NOLOCK)  
LEFT OUTER JOIN ABATFUN (NOLOCK)  
ON (ABATFUN.CODCOLIGADA = PFUNC.CODCOLIGADA AND ABATFUN.CHAPA = PFUNC.CHAPA )

WHERE ( ((PFUNC.SALARIO = 1000.00  
)) AND (ABATFUN.DATAREFERENCIA IS NOT NULL AND  
(ABATFUN.DATAREFERENCIA < '03/03/2011')  
) ) AND (PFUNC.CODCOLIGADA = 1)

LINHAS RETORNADAS: 12

**Com o "Aplica SQL Distinct":**

SELECT **distinct** PFUNC.CHAPA,PFUNC.NOME,PFUNC.SALARIO,PFUNC.CODCOLIGADA,ABATFUN.DATAREFERENCIA  
AS DATAREFERENCIA\_821172028  
FROM PFUNC PFUNC (NOLOCK) LEFT OUTER JOIN APARFUN (NOLOCK)  
ON (APARFUN.CODCOLIGADA = PFUNC.CODCOLIGADA AND APARFUN.CHAPA = PFUNC.CHAPA )  
LEFT OUTER JOIN ABATFUN (NOLOCK)  
ON (ABATFUN.CODCOLIGADA = APARFUN.CODCOLIGADA AND ABATFUN.CHAPA = APARFUN.CHAPA )

WHERE ( ((PFUNC.SALARIO = 1000.00  
)) AND (ABATFUN.DATAREFERENCIA IS NOT NULL AND  
(ABATFUN.DATAREFERENCIA < '03/03/2011')  
) ) AND (PFUNC.CODCOLIGADA = 1)

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Campos Complementares Globais

falsefalse

**Status:** Finalizado

false

**Data:** 31/10/2018

false

**Autores:**
