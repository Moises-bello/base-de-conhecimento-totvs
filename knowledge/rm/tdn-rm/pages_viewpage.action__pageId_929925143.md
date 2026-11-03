---
content_hash: f1bec116eb11ff37c6a26503392d1ed4b2f3fd3284cb447ba85e5b90a8199278
fetched_at: '2026-06-29T00:12:08.195237+00:00'
page_id: '929925143'
product: rm
source: tdn-rm
title: DT - S-1005 - Possibilitar a geração das informações de processo do FAP no
  CNO da obra
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929925143
version: 29
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS - Folha de Pagamento |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1005 - Possibilitar a geração das informações de processo do FAP no CNO da obra |
| País: | Brasil |
| Issue: | [DRHROTRM-11826](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11826 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.262
* 12.1.2410.210
* 12.1.2502.128 e superiores

## **03. SITUAÇÃO/REQUISITO**

Permitir a geração  das informações de processo do FAP no CNO da obra.

## **04. SOLUÇÃO**

Foi implementada a inclusão dos dados do processo do FAP, permitindo que, ao gerar o XML do evento **S-1005**, seja considerado o número do processo do FAP cadastrado nesse anexo, em vez de utilizar os dados da seção centralizadora do CNPJ.

1) No menu Administração de Pessoal | Cliente/Fornecedor | Anexo eSocial, ao marcar os parâmetros **"Tomador de serviço folha"** e **"Obra Própria"**, os campos do FAP serão habilitados. Quando preenchidos, o XML do evento S-1005 considerará essas informações para o preenchimento da tag referente ao processo FAP, conforme tela abaixo:

2) Ao gerar o XML do evento S-1005, o sistema seguirá o seguinte formato:

3) No menu Administração de Pessoal | Cliente/Fornecedor | Anexo CEI do Cliente/Fornecedor, também foram disponibilizados os campos dos processos do FAP, conforme print abaixo:

 

4) Na geração do XML do evento S-1005, o sistema passou a considerar os novos campos, conforme descrito abaixo:

IMPORTANTE:

Quando um tomador possuir múltiplos CEIs, será gerado um gatilho para o tomador e outro para cada **CEI**. O XML do evento S-1005 considerará as informações do FAP registradas no respectivo CEI.

Caso não deseje que o sistema busque os dados do processo do FAP no Cliente/Fornecedor, marque o parâmetro **"Considera Dados da Filial"**. Com essa opção ativada, os dados serão obtidos a partir da filial informada nesse parâmetro.

## **05.** **ASSUNTOS RELACIONADOS**

[Mapeamento S-1005](https://tdn.totvs.com/display/LRM/Evento+S-1005)

[Cliente/Fornecedor - Anexo eSocial](https://tdn.totvs.com/display/LRM/eSocial)

[Cliente/Fornecedor - Anexo CEI do Cliente / Fornecedor](https://tdn.totvs.com/display/LRM/Anexo+eSocial)
