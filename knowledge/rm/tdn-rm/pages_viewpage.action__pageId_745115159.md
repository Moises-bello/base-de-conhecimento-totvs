---
content_hash: d95e320bfbbc7694cd40eb63c68d270ccfe568f6514375ad322e466414f2436b
fetched_at: '2026-06-29T00:11:32.139040+00:00'
page_id: '745115159'
product: rm
source: tdn-rm
title: Emissão de Fatura para Convênios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=745115159
version: 4
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Configurando o Relatório**

Importante

Essa rotina foi migrada para a nova MDI na release 12.1.2205. O relatório padrão não possui mais a opção com espelho, essa opção trazia um quadro com o Resumo geral da Remessa. Caso seja necessário conter essa informação, deverá ser feito uma cópia do relatório padrão e adicionar esse quadro.

## **01. VISÃO GERAL**

Esta rotina é responsável por gerar um relatório da Remessa gerada na rotina de Faturas de Convênios.

## **02. EXEMPLO DE UTILIZAÇÃO**

Na tela **Faturamento para Convênios**, realize o filtro para localizar a remessa que deverá ser impressa. Em seguida marque a remessa na grid e execute o processo "**Emissão de Fatura para Convênios**", aguarde o processamento e o relatório será gerado em tela.

Após o relatório ser gerado, a coluna **Fatura Impressa** será atualizada com a informação "**Sim**"

## **03. CONFIGURANDO O RELATÓRIO**

Siga as etapas abaixo para configurar o relatório no seu ambiente:

1. O relatório padrão para essa rotina é o **SAUREL0057 - Fatura de Serviços Médico-Hospitalares** e o mesmo deve ser importado através do **TOTVS Compartilhamento**.
2. Acessar o parâmetros do sistema, no menu "Ambiente | Parâmetros | Gestão Hospitalar, no item "**Relatórios**"  e informar o relatório acima no campo "**Emissão Fatura para Convênios"**

Observações

Caso o relatório não apareça como opção, reiniciar o RM.Host.
