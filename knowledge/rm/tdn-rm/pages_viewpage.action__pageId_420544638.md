---
content_hash: 06dff0afe7a275565981d3fc3065b8125433c74c635cf3e3a227e9908591bd70
fetched_at: '2026-06-29T00:09:13.436329+00:00'
page_id: '420544638'
product: rm
source: tdn-rm
title: Como obter o XML de Parâmetros de Jobs
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=420544638
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

        O XML de parâmetros de jobs é o XML que o RM utilizou para executar um determinado processo, seja ele via sistema ou via WebService.

**Por exemplo:** Quando o usuário executa o processo de cópia de permissões de um usuário (GlbCopyPermisUsrProc) via MDI, é disponibilizado o XML desse processo.   
Esse XML pode ser reaproveitado quando se desejar executar esse mesmo processo via WebService (wsProcess), sendo necessário ajustar apenas os parâmetros do XML.

        A visualização do XML também é válida para conferência do processo e dos parâmetros de execução.

**Veja mais sobre**

ATENÇÃO

É possível recuperar apenas o XML da última utilização do Job quando executado via WebService.   
Os XMLs de Jobs executados na MDI poderão ser consultados normalmente.

**02. EXEMPLO DE UTILIZAÇÃO**

### **VISUALIZAÇÃO DO XML DE PARÂMETROS DE JOBS**

       Na MDI, existem 2 formas de consultar o XML de parâmetros de Jobs.

**1ª Opção:** Diretamente da tela de Gerenciamento de Jobs, localize o JOB que deseja consultar o XML e clique em:  
       Anexos > XML de Parâmetros de Jobs - Última utilização - (WebServices). Esse acesso a tela está disponibilizado **a partir da versão 12.1.23**.

       Será aberta uma tela com o XML do Job selecionado:

       **2ª Opção:**No menu Executar, pesquise por "XML de Parâmetros de Jobs".

       Será aberta uma tela com os Parâmetros de Job disponíveis. Para visualizar o XML é preciso localizar o ID do Job e abrir o registro desejado.

       Veja mais sobre a .

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** XML de Parâmetros de Jobs

falsefalse

**Status:** Finalizado

false

**Data:** 08/10/2018

false

**Autores:**
