---
article_id: 4410323555863
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7a96d65d8d70bbc83e74329438a73372d54e613cf4fbd12a1ebba35bc6e157d8
fetched_at: '2026-06-28T22:42:11.805399+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - MATR972 - InterFunctionCall:
  cannot find function A972CRIATEMP in AppMap on R972IMP(MATR972.PRX)'
type: support-article
updated_at: '2022-08-17T19:40:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410323555863-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MATR972-InterFunctionCall-cannot-find-function-A972CRIATEMP-in-AppMap-on-R972IMP-MATR972-PRX
---

**Dúvida**

Ao acessar a rotina MATR972 é apresentado o erro abaixo:MATR972 - InterFunctionCall: cannot find function A972CRIATEMP in AppMap on R972IMP(MATR972.PRX)

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

O relatório de conferencia da GIA SP (MATR972) se tornou obsoleto, por que a geração da GIA é efetuada pelo modulo TAF.  
  
Para utilização da GIA-SP pelo TAF, basta seguir os procedimentos, conforme documentações:   
  
[MP - FIS - GIA-SP - 1º Passo - Atualização do Ambiente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034675574-MP-FIS-GIA-SP-1%C2%BA-Passo-Atualiza%C3%A7%C3%A3o-do-Ambiente?source=search)  
[MP - FIS - GIA-SP - 2º Passo - Complemento Cadastral](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035192433-MP-FIS-GIA-SP-2%C2%BA-Passo-Complemento-Cadastral?source=search)  
[MP - FIS - GIA-SP - 3º Passo - Wizard de Configuração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034679934-MP-FIS-GIA-SP-3%C2%BA-Passo-Wizard-de-Configura%C3%A7%C3%A3o?source=search)  
[MP - FIS - GIA-SP - 4º Passo - Extrator Fiscal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050629074-MP-FIS-GIA-SP-4%C2%BA-Passo-Extrator-Fiscal)  
[MP - FIS - GIA-SP - 5º Passo - Processamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035197933-MP-FIS-GIA-SP-5%C2%BA-Passo-Processamento?source=search)  
[MP - FIS - GIA-SP - 6º Passo - Gerenciador de Integração](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035198093-MP-FIS-GIA-SP-6%C2%BA-Passo-Gerenciador-de-Integra%C3%A7%C3%A3o?source=search)  
[MP - FIS - GIA-SP - 7º Passo - Obrigações Fiscais](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035203933-MP-FIS-GIA-SP-7%C2%BA-Passo-Obriga%C3%A7%C3%B5es-Fiscais?source=search)  
  
**Procedimento para implementação do relatório da Nova GIA-SP no TAF:**  
[MP - FIS - NOVA GIA SP - Implementação do Relatório da Nova GIA SP, Rotina TAFRGSP.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038990574-MP-FIS-NOVA-GIA-SP-Implementa%C3%A7%C3%A3o-do-Relat%C3%B3rio-da-Nova-GIA-SP-Rotina-TAFRGSP-?source=search)
