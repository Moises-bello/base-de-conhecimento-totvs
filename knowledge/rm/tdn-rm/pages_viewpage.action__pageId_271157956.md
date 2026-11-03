---
content_hash: ed35395e44d78fe14f8c523be5520cb0d4784f34d765a83b4ec2c593e5ae5ade
fetched_at: '2026-06-29T00:08:25.827654+00:00'
page_id: '271157956'
product: rm
source: tdn-rm
title: Fórmula Visual - Habilitar Log
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271157956
version: 4
---

# Índice:

---

.\*ndice:

# Objetivo

---

       O objetivo deste documento é mostrar como habilitar o Log de Atividades de Fórmula Visual. O Log será armazenado em um arquivo txt dentro do diretório RM.Net. Na próxima seção será apresentado o passo a passo para a configuração.

# Introdução

---

       Para habilitar o Log de Atividades de Fórmula Visual, adicione a tag <add key="TraceWorkflow" value="true" /> no config do Host, como no exemplo abaixo:

xml











...]]>

       Em seguida, reinicie o serviço do host. Após esta configuração, ao executar qualquer fórmula visual, com sucesso ou não, o Log será gerado. O arquivo de Log será armazenado na pasta Processos\Logs\Workflow existente no diretório RM.Net.

       A identificação do log pode ser realizada pelo nome do arquivo da seguinte forma FvID\_[IDColigada]\_[IDWorkFlow]\_[Data+IDArquivo]. 

Exemplo:

Por default a tag não é utilizada no arquivo do host, ou seja, o comportamento padrão do sistema é **não** gerar arquivos de log para atividades de fórmula visual.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Habilitar Log de Atividades de Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:** 16/01/2017

false

**Autores:**

**Douglas Maxwell de Oliveira**
