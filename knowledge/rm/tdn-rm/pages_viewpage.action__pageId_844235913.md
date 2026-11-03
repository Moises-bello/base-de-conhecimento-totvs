---
content_hash: 2e161c1eaf91dd72b993a46a46ad0533163b6e9503a6392c554ba627f2c8fee7
fetched_at: '2026-06-29T00:11:50.627092+00:00'
page_id: '844235913'
product: rm
source: tdn-rm
title: DT - Log de Integração RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844235913
version: 25
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Log de Integração RM |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-6568](https://jiraproducao.totvs.com.br/browse/DRHROTRM-6568) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2310.231
* 12.1.2402.176
* 12.1.2406.108 e superiores

## **03. SITUAÇÃO/REQUISITO**

Implementar uma tela onde o usuário possa selecionar os processos (TAF ou Middleware) e o sistema gere um log detalhado do processo de integração, analisando os retornos. Os processos incluídos são:

* Conexão do TAF
* Integração com o TAF
* Atualizar Status

## **04. SOLUÇÃO**

A nova tela "Log de Integração" foi criada, desenvolvida em PO UI, e oferece recursos avançados para a identificação e detalhamento de erros nas integrações. Nesta primeira entrega, focamos nos processos do eSocial, analisando as integrações TAF e Middleware.

Esta implementação representa um avanço significativo para nossos clientes e equipes de atendimento. Ao facilitar a identificação precisa de problemas, ela reduzirá os custos associados à análise de incidentes, aumentando a eficiência e a assertividade ao direcionar as questões para os times responsáveis. Além disso, proporcionará uma redução significativa no tempo e no esforço dedicados à análise de problemas por parte das equipes de desenvolvimento (Folha e TAF).

Acesse o processo em Configurações | Log de Integração

Após a ativação, escolha a integração, o processo e o tipo de registro para mapear. Em seguida, vá para o processo desejado e realize-o.

**PONTOS IMPORTANTES:**

* Os registros serão apresentados na tela em ordem decrescente, com base no campo "Data/Hora".
* Haverá uma opção para excluir linhas.
* O sistema manterá apenas 500 linhas; após esse limite, as linhas mais antigas serão removidas automaticamente para evitar a sobrecarga do banco de dados.
* No ícone é possível definir os campos que serão apresentados em tela.
* Na opção "Exportar" será possível exportar por .CSV ou .Json.
* No ícone  é possível ocultar o menu para uma melhor visualização.

## **05. DEMAIS INFORMAÇÕES**
