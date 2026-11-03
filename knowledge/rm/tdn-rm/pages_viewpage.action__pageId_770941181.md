---
content_hash: c050a700f1154c3d305716e76d5ef2fe1f27eed1e5b754e5dde19886fe7e40c0
fetched_at: '2026-06-29T00:11:36.009026+00:00'
page_id: '770941181'
product: rm
source: tdn-rm
title: S-1010 - Como ajustar os valores das tags <codIncCP> e <codIncIRRF>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=770941181
version: 17
---

false

**A partir das Versões:**

* 12.1.2209.235
* 12.1.2302.158
* 12.1.2306.103

# Objetivo:

---

O objetivo deste documento é fornecer informações sobre como corrigir as tags <codIncCP> e <codIncIRRF> no evento S-1010, caso haja alguma divergência entre a base de dados e o último XML.

---

**PASSO 1**

Acessar o menu eSocial | Outros processos | Comparativo de Incidências de Rubricas

**PASSO 2**

Executar o relatório marcando a opção "Exibir a comparação do campo<codIncCP> e <codIncIRRF>" e comparar somente as tags <codIncCP> e <codIncIRRF>, conforme demonstrado abaixo:

**PASSO 3**

Através do menu processos, deverá gerar o gatilho das rubricas que estiverem divergentes.

**PASSO 4**

Acessar a fila de eventos e gerar o XML dos eventos ajustados e enviar para o governo.

Observações

Os gatilhos criados serão gerados com o início de validade (*tag* <iniValid>) igual ao mês e ano da competência atual. Caso desejar ajustar o início de validade da verba, basta alterar o campo "Competência" dentro do gatilho para o mês/ano desejado e, após, gerar o XML.

Se já houver ocorrido o envio de eventos periódicos e/ou rescisão para a competência informada, é necessário realizar a retificação dos eventos de remuneração após envio do S-1010 para que o governo recalcule as bases.

*Documento de Referência: [DT - S-1010: Adequação da tag <codIncIRRF>](https://tdn.totvs.com/pages/viewpage.action?pageId=770940423) e*
