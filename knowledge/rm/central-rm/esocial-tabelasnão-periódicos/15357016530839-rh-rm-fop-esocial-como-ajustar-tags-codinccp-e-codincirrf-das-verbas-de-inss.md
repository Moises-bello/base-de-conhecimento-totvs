---
article_id: 15357016530839
category: eSocial - Tabelas/Não Periódicos
content_hash: 9eb2c301a98e1e2c4ea78983e38185d15cdaaff858b04da8fb6ce77d910b0fbc
fetched_at: '2026-06-28T22:47:10.555853+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP- eSocial - Como ajustar tags codIncCP e codIncIRRF das verbas
  de INSS
type: support-article
updated_at: '2026-04-07T18:20:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15357016530839-RH-RM-FOP-eSocial-Como-ajustar-tags-codIncCP-e-codIncIRRF-das-verbas-de-INSS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15356982163351) Tempo aproximado para leitura: **00:03:59 min**  
  
**Dúvida**  
Como ajustar os valores das tags <codIncCP> e <codIncIRRF> para os eventos de INSS?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas versões  
  
**Solução**  
Em **2023**, com a inclusão do **Imposto de Renda Retido na Fonte - IRRF** no eSocial, foi necessário realizar uma revisão nos valores de incidência de INSS (*tag***<codIncCP>**) e IRRF (*tag***<codIncIRRF>**)no evento S-1010.  
Essa adequação teve como objetivo evitar qualquer discrepância entre a folha de pagamento e os valores retornados pelo governo.   
A partir dos patches 12.1.2302.240, 12.1.2306.187, 12.1.2310.121 os valores dos códigos de cálculos abaixo serão gerados conforme abaixo:

|  |  |
| --- | --- |
| **CÓDIGO DE CÁCULO** | **CODINCIRRF****VALOR CORRETO** |
| [3 - I.N.S.S.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718215) | **41** |
| [11 - I.N.S.S. de 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718209) | **42** |
| [68 - INSS DE DIFERENÇA SALARIAL](https://tdn.totvs.com/pages/viewpage.action?pageId=452718219) | **41** |
| [82 - I.N.S.S. Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452718205) | **43** |
| [85 - I.N.S.S. calculado pelo usuário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718201) | **41** |
| [92 - Restituição de I.N.S.S.](https://tdn.totvs.com/pages/viewpage.action?pageId=452719626) | **41** |
| [103 - I.N.S.S. 2ª parc. 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452718233) | **42** |
| [108 - INSS DE DIF SALARIAL DE 13º](https://tdn.totvs.com/pages/viewpage.action?pageId=452718958) | **42** |
| [110 - INSS DE DIF SALARIAL DE FÉRIAS](https://tdn.totvs.com/pages/viewpage.action?pageId=452718218) | **43** |
| [131 - I.N.S.S. Férias desc. mês ant.](https://tdn.totvs.com/pages/viewpage.action?pageId=452718225) | **9** |
| [141 - INSS Férias no mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718223) | **43** |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | **42** |
| [159 - INSS de férias outro emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718222) | **9** |
| [171 - INSS 13º Sal descontado p/ previd ref lic maternide](https://tdn.totvs.com/pages/viewpage.action?pageId=452718206) | **42** |
| [185 - INSS DE FÉRIAS PROXIMO MÊS OUTRO EMPREGO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719942) | **9** |
| [193 - INSS DE FÉRIAS MÊS ANTERIOR OUTRO EMPREGO](https://tdn.totvs.com/pages/viewpage.action?pageId=452719896) | **9** |
| [205 - INSS Descontado RRA](https://tdn.totvs.com/pages/viewpage.action?pageId=452718220) | **9** |
| [209 - INSS Descontado RRA Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=452719900) | **9** |
| [213 - INSS Descontado RRA 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=452719681) | **9** |
| [89 - I.N.S.S. com alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718204) | **9** |
| [90 - I.N.S.S. Férias com alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718959) | **9** |
| [91 - I.N.S.S. 13º c/ alíquota normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718212) | **9** |
| [137 - I.N.S.S. Fér. Próx. mês c/ alíq. normal](https://tdn.totvs.com/pages/viewpage.action?pageId=452718228) | **9** |
|  |  |
| **CÓDIGO DE CÁCULO** | **CODINCCP****VALOR CORRETO** |
| [142 - INSS Férias próx. mês (informado)](https://tdn.totvs.com/pages/viewpage.action?pageId=452718227) | **0** |
| [153 - Restituição de I.N.S.S. 13º](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452718762) | **32** |

⚠️ [FAQ - Como ajustar os valores das tags <codIncCP> e <codIncIRRF> para Conferência da DIRF no eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=1037965223)

Para ajustar as incidências, siga os passos abaixo:

1. Acessar o menu **eSocial | Outros processos | Comparativo de Incidências de Rubricas**;  
2. Executar o relatório marcando a opção **Exibir a comparação do campo<codIncCP> e <codIncIRRF>** e comparar somente as *tags* **<codIncCP>** e **<codIncIRRF>**;![](https://centraldeatendimento.totvs.com/hc/article_attachments/15356587048599)

3. Através do menu processos, deverá gerar o gatilho das rubricas que estiverem divergentes selecionando a opção **Gera gatilho de rubricas divergentes entre último XML e base**;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15356593065367)

4. Acessar a fila de eventos, gerar o XML dos eventos ajustados e enviar para o governo.   
  
**Importante**  
Os gatilhos criados serão gerados com o início de validade (*tag***<iniValid>**) igual ao mês e ano da competência atual. Caso desejar ajustar o início de validade da verba, basta alterar o campo **Competência** dentro do gatilho para o mês/ano desejado e, após, gerar o XML.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15356637572759)

Se já houver ocorrido o envio de eventos periódicos e/ou rescisão para a competência informada, é necessário realizar a retificação dos eventos de remuneração após envio do S-1010 para que o governo recalcule as bases.   
  
**Saiba mais**  
Para maiores informações, acesse:

* [S-1010: Adequação da tag <codIncIRRF>](https://tdn.totvs.com/pages/viewpage.action?pageId=770940423)
* [RH - RM - FOP - eSocial - Retificação do evento S-1200](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028334171)
* [RH - RM - FOP- eSocial - Retificação do evento de rescisão/desligamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017501692)
