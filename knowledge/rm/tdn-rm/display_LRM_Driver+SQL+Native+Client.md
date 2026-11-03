---
content_hash: c71606efd79ff9faf907ae71cf7ccede9c48d5db985f74cf9fe7623ec9f83164
fetched_at: '2026-06-29T00:09:52.897021+00:00'
page_id: '439698315'
product: rm
source: tdn-rm
title: Driver SQL Native Client
type: documentation
url: https://tdn.totvs.com/display/LRM/Driver+SQL+Native+Client
version: 36
---

# Índice:

---

.\*ndice:

# Objetivo

---

          O objetivo deste documento é demonstrar como realizar a instalação do driver SQL Native Client para o correto funcionamento do Gerador de Relatórios Delphi (RMGerador.dll).

# Introdução

---

          Devido a migração do tipo DateTime para o tipo DateTime2 em novas colunas criadas nas tabelas do RM, foi necessária uma alteração no Gerador de Relatórios Delphi. O acesso a banco de dados, que antes se conectava através do driver OleDB passou a se conectar com o driver SQL Native Client.

          A partir das versões 12.1.19.4, 12.1.20.3, 12.1.21.2 e 12.1.22.1 ou superiores será necessário a instalação do novo driver caso o mesmo não esteja instalado. As versões citadas podem ser visualizadas através da DLL RMGerador.dll.

          Caso o driver não esteja instalado, ao tentar acessar a Visão Delphi no Menu Gestão da MDI .NET uma mensagem será mostrada ao usuário informando sobre a necessidade da instalação do novo driver.

# Instalação

---

falseFonte de Dados11° Passo

          Baixe o arquivo “sqlncli.msi” através do site da Microsoft conforme link: [Download Instalador - SQL Native Client](https://www.microsoft.com/en-us/download/details.aspx?id=50402).

          Execute o instalador e aceite os termos:

22° Passo

          Em SQL Server Native Client SDK, marque a opção “Will be installed on local hard drive”:

33° Passo

          Após marcar a opção “Will be installed on local hard drive” clique em Next:

44° Passo

          Em seguida clique em install:

55° Passo

          Após ser instalado,  a tela de conclusão será apresentada, clique em Finish:

---

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.19 ou superiores

false

**Processo:** Gerador de Relatórios

falsefalse

**Status:** Em andamento

false

**Data:**

false

**Autores:**
