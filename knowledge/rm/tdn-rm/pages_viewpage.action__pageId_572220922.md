---
content_hash: 026b6466d7519a65da8e308f58a86c5e94ff24d3c0c68d71a85b8a245cef746f
fetched_at: '2026-06-29T00:10:52.388752+00:00'
page_id: '572220922'
product: rm
source: tdn-rm
title: Nota Técnica nº 19/2020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=572220922
version: 6
---

false

**A partir das Versões:**

* 12.1.27.302
* 12.1.28.213
* 12.1.29.138
* ou Superiores

# Objetivo:

---

Esta Nota Técnica tem como objetivo disponibilizar ajustes do Leiaute Versão 2.5

---

Adequamos o sistema para atender a versão do leiaute para Nota Técnica 19/2020.

**Configurações | Parametrizador | eSocial | Configurações Gerais |Configurações Gerais 1/6**

Selecionar a versão correspondente ao leiaute.

**Administração de pessoal | Cadastros Globais | Tabelas****Dinâmicas**

**Observação:**Para a alteração dos campos da tabela dinâmica será necessário executar o script através do sistema RM.Atualizador.exe.

**Tabela NATRUBRICA**

Alterada a descrição das naturezas das rubricas da folha de pagamento abaixo:

**DE:** 1619 - Ajuda Compensatória - MP 936/2020 

**PARA:** 1619 - Ajuda Compensatória - Lei 14.020/2020 (conversão da MP 936/2020)

**DE:** 6119 - Indenização rescisória - MP 936/2020

**PARA:** 6119 - Indenização rescisória - Lei 14.020/2020 (conversão da MP 936/2020)

**Tabela PESNOTAFAS**

Alterada a descrição do motivo de afastamento do eSocial.

**DE:** 37 - Suspensão temporária do contrato de trabalho nos termos da MP 936/2020 

**PARA:** 37 - Suspensão temporária do contrato de trabalho nos termos da Lei 14.020/2020 (conversão da MP 936/2020)

**eSocial | Informações do Empregador**

Na Nota Técnica foi excluída a Classificação Tributária "08- Consórcio Simplificado de Produtores Rurais", porém para que não haja problemas caso o usuário já tenha selecionado esta classificação, apenas ajustamos a descrição acrescentando a palavra "INATIVO" e incluímos validação na geração do XML.

Ao gerar o XML do evento S-1000 com essa classificação Tributária 08- Consórcio Simplificado de Produtores Rurais (INATIVO) marcada, caso esteja com o leiaute - 2.5.00 NT19/2020 selecionado no parametrizador do eSocial, o sistema apresentará erro na geração.
