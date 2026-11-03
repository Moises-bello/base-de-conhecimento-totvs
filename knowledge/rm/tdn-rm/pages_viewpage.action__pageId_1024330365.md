---
content_hash: cfe12b9c0e5c3ea8518e450189f70180425da6d25c1d707806dae36fce6eae30
fetched_at: '2026-06-29T00:05:48.190197+00:00'
page_id: '1024330365'
product: rm
source: tdn-rm
title: DT - S-1010 - Adequação da tag <codIncIRRF> para Assistência Médica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1024330365
version: 17
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1010 - Adequação da tag <codIncIRRF> para Assistência Médica |
| País: | Brasil |
| Issue: | [DRHROTRM-15575](https://jiraproducao.totvs.com.br/browse/DRHROTRM-15575) |

## **02. LIBERAÇÃO**

  Lembrando que, será a partir dos patches:

* 12.1.2502.254
* 12.1.2506.211
* 12.1.2510.139 e superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar a geração da tag codIncIRRF para a verba de Assistência Médica (código de cálculo 14), de forma a atender o item **[14.6 das Perguntas Frequentes do eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes-producao-empresas-e-ambiente-de-testes)**.

A partir desse ajuste, deverá ser gerado o código **“67 – Plano privado coletivo de assistência à saúde”**,mesmo quando a verba não for dedutível de IRRF, substituindo o código atualmente utilizado **“9 – Verba transitada pela folha de pagamento de natureza diversa de rendimento ou retenção/isenção/dedução de IR”**.

## **04. SOLUÇÃO**

Implementada a tratativa no evento S-1010, para que o produto passe a gerar o código de incidência de IRRF (tag <codIncIRRF>) para a verba com **código de cálculo 14 – Assistência Médica**, independentemente de a verba ser ou não dedutível de IRRF.

Para que o evento **S-1010 de Assistência Médica** reflita essa alteração, é necessário seguir os passos abaixo:

1) Gerar o gatilho do evento S-1010

* **Gatilho Manual:** Acessar o menu eSocial | Fila de Eventos e clicar em incluir. Lembrando que, o gatilho criado será gerado com o início de validade (*tag*<iniValid>) igual ao mês e ano da competência atual. Caso desejar ajustar o início de validade da verba, basta alterar o campo "Competência" dentro do gatilho para o mês/ano desejado e, após, gerar o XML.

* **Gatilho pelo processo para vários eventos** - Acesse o [link](https://tdn.totvs.com/pages/viewpage.action?pageId=770941181) para ver passo a passo.

2) Gerar o XML do evento S-1010. A tag codIncIRRF será preenchida com o valor 67 conforme exemplo abaixo:

ATENÇÃO:

O envio do XML com a alteração do código de incidência de IRRF é necessário somente quando a verba de código de cálculo 14 – Assistência Médica não estiver incidindo em IRRF.

Quando há incidência de IRRF, o sistema já gera automaticamente o código 67, não sendo necessária nenhuma ação adicional.

## **05. DEMAIS INFORMAÇÕES**
