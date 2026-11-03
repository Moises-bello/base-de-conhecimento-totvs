---
content_hash: 8b8b3a76220900e49ca2f56952952b7519d05b245a7f1642caec9d7f99157880
fetched_at: '2026-06-29T00:12:01.255853+00:00'
page_id: '890544620'
product: rm
source: tdn-rm
title: FISCAL01-22907 - Reinf R-4010 - Campos SCP
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-22907+-+Reinf+R-4010+-+Campos+SCP
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-22907 |

## **02. SITUAÇÃO/REQUISITO**

Gerar as Tags das informações da Filial SCP

## **03. SOLUÇÃO**

Foi realizado ajuste para tratar a regra de exibição das tags referentes a Filiais SCP.

Na EFD-Reinf, os campos relacionados a SCP devem ser preenchidos sempre que ocorrerem pagamentos de 'Lucro e Dividendo' realizados aos sócios.

* **indFciScp**- Indicativo de SCP
* **nrInscFciScp**- Número de inscrição no CNPJ
* **percSCP**- Percentual que o beneficiário possui na SCP

Os lançamentos financeiros e fiscais incluídos na Filial SCP são gerados na rotina EFD-Reinf, e os campos relacionados às informações de SCP (Indicativo de SCP, Número de inscrição no CNPJ e Percentual que o beneficiário possui na SCP) serão gerados nos eventos R-4010, **somente** se a filial for **SCP** e a natureza de rendimento do lançamento for igual a **12001**.

* O percentual SCP será exibido apenas se o CNPJ do sócio cadastrado no parâmetro ECF da filial for o mesmo CNPJ do cli/for do lançamento.
* As tags serão geradas apenas pela matriz e o campo "Filial SCP transmite REINF através da Filial Matriz" deve ser marcado, esse campo está localizado localizado nos Dados Ficais/ Dados Adicionais da Filial.

Disponível à partir da biblioteca 12.1.2310
