---
content_hash: 03b399e5738f7107bc2af9ff80385b2f58165f039fd7e8ba86116c0910ddd58e
fetched_at: '2026-06-29T00:11:54.826270+00:00'
page_id: '85819448'
product: rm
source: tdn-rm
title: Mashups - Erro 417
type: documentation
url: https://tdn.totvs.com/display/LRM/Mashups+-+Erro+417
version: 9
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é trazer a solução para o Erro 417 - Exception Failed.

# Solução:

---

       Quando tenta-se utilizar o mashups e é apresentado a mensagem de erro abaixo, deve-se realizar algumas configurações que serão apresentadas neste documento.

**Procedimentos:**

       Além de liberar no Firewall o aplicativo, deve-se aplicar a seguinte Tag no .config do aplicativo usado (arquivo XML que contém informações de configuração do aplicativo RM que está sendo utilizado).

       Exemplo: se estiver utilizando o Fluxus deve-se alterar o RMFluxus.exe.config. Caso esteja utilizando o Nucleus deve-se editar o RMNucleus.exe.config, e assim por diante. Cada aplicativo possui um arquivo de configuração (.exe.config) no mesmo diretório em que encontra-se o executável do aplicativo.

xml



]]>

**Abaixo segue exemplo de arquivo que apresenta o erro (essa informação está no documento somente como exemplo para exemplificar a diferença do arquivo de configuração mais abaixo, que contém a solução da situação)**

xml















]]>

**Abaixo segue um arquivo de exemplo que não apresenta o erro, ou seja, que está com a alteração:**

xml




















]]>Observação

*É importante entender que a configuração deve ser feita no arquivo de configuração do aplicativo que está sendo utilizado.*

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX

false

**Processo:** Erro 417 - Exception Failed

falsefalse

**Status:** Finalizado

false

**Data:** 04/08/2016

false

**Autores:**
