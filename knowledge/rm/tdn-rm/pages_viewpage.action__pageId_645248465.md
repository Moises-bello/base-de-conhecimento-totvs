---
content_hash: 7cfcb2914d26bbfdbc62e4daa70fa47eff1555fc8d12ccea9afb025e3a7474d8
fetched_at: '2026-06-29T00:11:11.056279+00:00'
page_id: '645248465'
product: rm
source: tdn-rm
title: S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário Início
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=645248465
version: 17
---

false

**A partir das Versões:**

* 12.1.33.259
* 12.1.34.158
* 12.1.2205.103
* e Superiores

# Objetivo:

---

Apresentar as alterações realizadas no evento S-2300 para atender ao leiaute do eSocial, versão S-1.0, para o grupo 4.

---

13-1S-2300 - XMLS-2300 - XML

Foram necessárias algumas alterações na geração do XML para atender os clientes do grupo 4, sendo elas:

1) Implementado o grupo infoMandElet (O (se codCateg = [304]) N (nos demais casos)). Mais informações Aba Mandato Eletivo

2) Implementada a validaçãonos campos (tpInsc, nrInsc, dtAdmOrig, matricOrig, tpRegTrab) do grupo infoDirigenteSindical para considerar as categorias 301 a 313.

3-2Mandato EletivoMandato Eletivo

Acessar o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários | Registro

1) Preencher com as informações necessárias para geração do grupo <infoMandElet> do leiaute:

**ATENÇÃO:**

Esta aba somente ficará visível quando o funcionário possuir a categoria 304.

2) Após o preenchimento dos dados, o XML será gerado com as informações do grupo <infoMandElet>:

3-3Carga InicialCarga Inicial

Acessar o menu RH | Folha de Pagamento | eSocial | Gerar Gatilhos Eventos Iniciais

Deverá selecionar a "2a. Fase" e selecionar o evento "S-2300".

**ATENÇÃO:**

Para gerar o gatilho com status carga inicial o sistema irá verificar se a data de admissão do funcionário é anterior a data dos "Não Periódicos" ou caso o campo "Economia Mista" esteja marcado o sistema irá considerar a data do campo "Não Periódicos" da economia mista, existem no Parametrizador.
