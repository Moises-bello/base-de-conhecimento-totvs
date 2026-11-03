---
article_id: 360018812971
category: PCO - Planilhas
content_hash: 9bbebaf9e2e9cfbe14fe338f9fbdd84d45f7176290d41b460328b9dbc9627d7b
fetched_at: '2026-06-28T22:37:05.393469+00:00'
product: protheus
section_id: 1500001539901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA100 - Integração
  de Planilha em XML para planilha de Orçamentos do módulo PCO.
type: support-article
updated_at: '2023-11-21T13:51:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018812971-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA100-Integra%C3%A7%C3%A3o-de-Planilha-em-XML-para-planilha-de-Or%C3%A7amentos-do-m%C3%B3dulo-PCO
---

**Dúvida**Integração de Planilha em XML para planilha de Orçamentos do módulo PCO.

**Ambiente**Protheus – SIGAPCO – A partir da versão 11.80  
  
   
**Solução**

A integração do Microsoft Excel, em **"Planilha Orçamentária",** permite associar uma célula ou o nome da referência para atualização de um dado.

Geralmente o valor orçado para uma determinada entidade em um período é estabelecido por diversas fórmulas e cálculos. Ao obter o valor desejado com base nos cálculos realizados, nem sempre os dados utilizados para o cálculo precisam ser acompanhados e documentados na ferramenta gestão de orçamentos. Esses dados utilizados para determinar o valor do orçamento são denominados “Memória de Cálculo”.

Pode-se acompanhar a memória de cálculo de uma planilha, fazendo com que os valores da planilha orçamentária sejam lidos através da célula ou pelo nome da referência da integração com a planilha do Microsoft Excel.

Para isto, deve-se incluir a fórmula “PCOSETLINK("<nome da planilha>","<célula ou nome da referência>"). A planilha indicada deve estar cadastrada no Banco de Conhecimento do Protheus.

Procedimentos

Para vincular uma planilha do Microsoft Excel com a planilha orçamentária

No ambiente Planejamento e Controle Orçamentário, opção “Atualizações/Planilhas/Orçamentos”, selecione um orçamento e clique  em **“Alterar”**.

Será apresentada a janela Planilha Orçamentária

Em Ações Relacionadas, selecione “**Documento**” para vincular uma planilha do Microsoft Excel.
