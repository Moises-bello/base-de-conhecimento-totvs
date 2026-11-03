---
content_hash: 37b5766a8b63cbadae260fb92edf54defab25af65a6fd9e8e62924b3986d5342
fetched_at: '2026-06-29T00:12:15.175467+00:00'
page_id: '971956164'
product: rm
source: tdn-rm
title: DT - eSocial - Leiaute S-1.3 - Nota Orientativa 04/2025
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=971956164
version: 10
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | DT - eSocial - Leiaute S-1.3 - Nota Orientativa 04/2025 |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-14437](https://jiraproducao.totvs.com.br/browse/DRHROTRM-14437) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2502.183
* 12.1.2506.125
* 12.1.2510.281 e superiores

IMPORTANTE:

Para clientes que utilizam o TAF é necessário atualização do pacote conforme descrito no TDN [link](https://tdn.totvs.com/pages/viewpage.action?pageId=969142863).

## **03.****SITUAÇÃO/REQUISITO**

Adequação do produto TOTVS Folha de Pagamento para atender à  [Nota Orientativa 04/2025 do leiaute S-1.3](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-orientativa-s-1-3-04-2025.pdf), com base nas alterações da versão “MOS S-1.3 consolidada até a NO S-1.3 04/2025”, publicada em 10/07/2025.

## **04. SOLUÇÃO**

Adequamos o TOTVS Folha de Pagamento para atender à Nota Orientativa S-1.3 nº 04/2025 do eSocial.

1) Atualizada as descrições da tabela dinâmica do código **PESMOTAFAS**, itens 41 e 42, conforme a **Tabela 18** do eSocial.

2) Criado o item **43** na tabela dinâmica do código **PESMOTAFAS**, com a seguinte descrição:  
*"Licença Maternidade - Prorrogação por 60 dias, Lei 15.156/2025 – Criança com deficiência permanente decorrente de síndrome congênita associada à Zika"*

Para que o XML seja gerado corretamente, é necessário acessar o menu Configurações | Parametrizador | eSocial  e configurar o **De/Para**, informando o seguinte valor:

* **Motivo eSocial:** 43 - Licença Maternidade - Prorrogação por 60 dias Lei 15.166/2025 - Criança com deficiência permanente decorrente de síndrome congênita associa à Zika.

Certifique-se de que o motivo esteja devidamente mapeado no ambiente, garantindo conformidade com o leiaute do eSocial.

Histórico de Afastamento do funcionário:

Geração do XML do evento S-2230:

## **05. DOCUMENTAÇÃO**

[Leiaute S-1.3 e Nota Técnica 01/2024](https://tdn.totvs.com/pages/viewpage.action?pageId=862114556)

[TAF](https://tdn.totvs.com/pages/viewpage.action?pageId=969142863)
