---
content_hash: 7189ffdb99bc1702396c4b829f1d6eaea60279f41eeacc2a7637bafe0d98aec0
fetched_at: '2026-06-29T00:09:24.840750+00:00'
page_id: '423938038'
product: rm
source: tdn-rm
title: Apontamento via Código de Barras por Estrutura
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938038
version: 2
---

Ao fazer a leitura do código de barras para apontamento de estrutura será disponibilizada a tela com as informações referente ao item que está sendo apontado, onde deverá ser informada a quantidade apontada da estrutura e opcionalmente a quantidade perdida.   
 É disponibilizado no sistema  um relatório padrão de etiquetas de código de barras, caso seja de interesse, pode-se personalizar relatórios específicos conforme o layout abaixo:  
    
 **Layout Código de Barras para Apontamento por Estrutura:**  
  
 ID!OP-0001/11!001.01!BASE!-1  
Onde:  
 **ID**: Identificador padrão de início de código de barras  
 **!:** Separador padrão  
 **OP-0001/11**: Código da Ordem de Produção  
 **001.01**: Código da Estrutura a ser apontada  
 **BASE:** Modelo da Estrutura  
 **-1:** Operador padrão para apontamento via Código de Barras por Estrutura  
***Observação*:**  Os campos Ordem de Produção, Código da Estrutura e Modelo da Estrutura podem ser verificados via consulta SQL na tabela KAPTOCODBARRAETIQUETAS, que é preenchida ao realizar o processo de geração de etiquetas.

Informações Adicionais

* [Como Fazer - Apontamento via Código de Barras por Estrutura](http://tdn.totvs.com.br/pages/viewpage.action?pageId=42043445)
* [Como Fazer – Apontamento múltiplo por estrutura](http://tdn.totvs.com.br/pages/viewpage.action?pageId=42043445)
