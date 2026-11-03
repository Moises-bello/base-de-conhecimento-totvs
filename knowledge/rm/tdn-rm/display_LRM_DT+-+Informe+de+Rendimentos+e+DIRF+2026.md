---
content_hash: 28efeac4b38796598105635f0f3d8cf94d3146a240ad92ab5dc07c867bba5b27
fetched_at: '2026-06-29T00:05:48.860649+00:00'
page_id: '1032150946'
product: rm
source: tdn-rm
title: DT - Informe de Rendimentos e DIRF 2026
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+Informe+de+Rendimentos+e+DIRF+2026
version: 4
---

## **01. DADOS GERAIS**

| Produto: | TOTVS - Folha de Pagamento |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Informe de Rendimentos e DIRF 2026 |
| País: | Brasil |
| Ticket: |  |
| Issue: | [DRHROTRM-16019](https://jiraproducao.totvs.com.br/browse/DRHROTRM-16019 "View this issue") |

## **02. VERSÕES**

A partir dos patches:

* + 12.1.2502.266
  + 12.1.2506.228
  + 12.1.2510.157 e superiores

## **03. SITUAÇÃO/REQUISITO**

Devido à substituição da DIRF pelo eSocial, implementamos ajustes estratégicos no sistema para garantir a conformidade com as novas diretrizes e otimizar a rotina operacional.

## **04. SOLUÇÃO**

Melhorias implementadas:

**1 - Mensagem Informativa**

Exibição de mensagem informativa no início do processo de **DIRF / Informe de Rendimentos**, conforme demonstrado abaixo:

**2 - Mensagem de Alerta**

Apresentação de alerta ao selecionar as opções **“DIRF Conferência”** ou **“DIRF em Arquivo”** quando informado **ano-base superior a 2024**, orientando o usuário sobre a mudança de obrigatoriedade, conforme demonstrado abaixo:

**3 - Desativação de parâmetros no Informe de Rendimentos (ano-base > 2024)**

Quando o ano informado for superior a 2024, os seguintes parâmetros permanecerão desabilitados, uma vez que não se aplicam após o encerramento da DIRF:

* Usa filtro de seleção ao gerar DIRF em Arquivo
* Utiliza descrição da seção selecionada na DIRF em Arquivo

**4 - Habilitação de parâmetros para o Informe de Rendimentos no Portal**

Considerando que o **Informe de Rendimentos do Portal** depende das informações armazenadas na tabela **PDIRF**, será necessário habilitar os seguintes parâmetros:

* Deletar Ano de Referência
* Atualizar dados Informe de Rendimentos – RM Portal

**5. Inclusão de banner na Fila de Eventos**

Foi incluído um **banner informativo no menu** eSocial | Fila de Eventos, com o objetivo de alertar e orientar os usuários sobre as mudanças relacionadas à substituição da DIRF pelo eSocial, reforçando as novas diretrizes aplicáveis ao processo.

## **05.****ASSUNTOS RELACIONADOS**
