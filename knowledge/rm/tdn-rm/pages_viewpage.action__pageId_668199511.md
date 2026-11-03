---
content_hash: a569df3d637ea24c70f580f5952540f7028c979639ea7689162ea7cb083a0c56
fetched_at: '2026-06-29T00:11:16.440036+00:00'
page_id: '668199511'
product: rm
source: tdn-rm
title: DT - Cadastro de Eventos - Disponibilizado o valor "92-Exclusiva do Empregador
  13o. Salário"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=668199511
version: 6
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | Disponibilizar o valor "92-13º salário" no lookup de Incidência Exclusiva do Empregador. |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | DRHROTRM-2944 |

## **02. SITUAÇÃO/REQUISITO**

   O cliente possui um processo judicial vinculado ao INSS 13º, onde é necessário suspender a parte patronal (tag <codIncCP92> com extDecisão).

   No sistema quando selecionamos a incidência "INSS 13º" é necessário ter a opção do valor "92-13º salário" no campo Exclusivo Empregador, semelhante como ocorre no campo INSS.

**03. SOLUÇÃO**

   No cadastro de evento ao marcar "INSS 13º" foi disponibilizado no campo "Exclusivo do Empregador" o valor "92-13º Salário", conforme abaixo: 

     

     Assim ao gerar o XML do S-1010, na tag <codIncCP> será levado o valor 92:

     

## **04. DEMAIS INFORMAÇÕES**

Segue abaixo o link do mapeamento do evento S-1010:
