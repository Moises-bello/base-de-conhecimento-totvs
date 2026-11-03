---
content_hash: fa415f2de92d2815040a6102b85e86e50e89f80db2a4a1901ecb6f591f376184
fetched_at: '2026-06-29T00:09:09.953112+00:00'
page_id: '394218139'
product: rm
source: tdn-rm
title: Integridade RM x TAF
type: documentation
url: https://tdn.totvs.com/display/LRM/Integridade+RM+x+TAF
version: 29
---

6Passo 1Passo 1Passo 1

Acertar Duplicidade dados TAF

| Objetivo: | Limpar os registros no TAF que possuem mais de um TAFKEY. Apaga informações na TAFST2 e TAFXERP. |
| --- | --- |
| **Link Documentação:** | [DSERTAF1-8800 - Rotina para exclusão de itens rejeitados na TAFXERP](http://tdn.totvs.com/pages/viewpage.action?pageId=394211644) |
| **Link Pacotes:** | **<https://suporte.totvs.com/portal/p/10098/download?e=706578>** |
| **Pre-requisitos:** |  |
| **Tela** |  |

Passo 2Passo 2

Atualizar Status Integração TAF

| Objetivo: | Ter atualizado no RM os status dos eventos que foram integrados com o TAF. |
| --- | --- |
| **Link Documentação:** | [Como atualizar o Status de Integração com o TAF?](http://tdn.totvs.com/pages/viewpage.action?pageId=382545297) |
| **Link Pacotes:** | Instalação das versões: 12.1.19.362 ou 12.1.20.358 ou 12.1.21.107 ou acima.  <https://suporte.totvs.com/portal/p/10098/download#company/> |
| **Pre-requisitos:** |  |
|  |  |

Passo 3Passo 3

Executar Relatório Paridade RM x TAF

| Objetivo: | Exibir um relatório com as inconsistências encontradas pelo RM x TAF |
| --- | --- |
| **Link Documentação:** |  |
| **Link Pacotes:** | Instalação das versões: 12.1.19.362 ou 12.1.20.358 ou 12.1.21.107 ou acima.  <https://suporte.totvs.com/portal/p/10098/download#company/> |
| **Pre-requisitos:** | Instalação das versões especificas |
|  |  |

### **O que fazer em caso do processo de Integridade RM x TAF retornar logs com inconsistência?**

A execução deste processo terá como saída 2 logs de validação dos eventos do eSocial que foram integrados com o TAF:

Log 1: Diferença\_Status: apresentará a diferença de status dos eventos eSocial que estão na Fila de Eventos do RM comparados com os eventos que estão no

monitor do TAF.  
Log 2: Não\_Encontrados: apresentará os eventos do eSocial existentes no RM que não foram encontrados no TAF.

**ERRO/AÇÃO:**

a.) São apresentados eventos com status diferentes entre TAF e RM  
 Execute o atualizador de status da Integração. Em seguida, gere novamente o processo de Integridade RM x TAF.  
   
 b.) Nos log Não\_encontrados, são listados eventos.  
 Eventos que existem no RM podem ter sido deletados no TAF, deverá avaliar:  
 Caso o evento seja pertinente e deveria ter sido enviado para o governo, deverá avaliar se deverá recuperar o evento deletado no TAF ou se deve gerar novo evento no RM para enviar ao TAF e ao governo respectivamente.

Passo 4Passo 4

Executar Relatório TAF Integridade - Ratreamento XML's

| Objetivo: | Apoiar na identificação de possíveis divergências de conteúdo nos campos (tag´s) dos xml´s gerados.  O relatório efetua a comparação dos arquivos de xml´s, partindo do arquivo de entrada (integrado ou importado ao TAF) contra o arquivo de saída (gerado para transmissão ao RET), apontando as divergências, bem como o conteúdo dos campos para análise. |
| --- | --- |
| **Link Documentação:** | [TAF109\_Relatório Apoio - Rastreamento de XML](http://tdn.totvs.com/pages/viewpage.action?pageId=394211809) |
| **Link Pacotes:** | **<https://suporte.totvs.com/portal/p/10098/download?e=706578>** |
| **Pre-requisitos:** |  |
| **Tela:** |  |

### **O que fazer em caso do processo de Rastreamento do XML retornar registros diferentes?**

Avaliar se houve alteração manual no TAF dos eventos eSocial originados do RM. Se as alterações estiverem condizentes, deverá avaliar se deve efetua-las também nos   
cadastros de origem do RM para garantir a integridade dos dados.  
 Mas se as edições não forem pertinentes, deverá avaliar se deverá deletar o evento no TAF, regerar o evento no RM e integrar novamente com o TAF.  
 Deverá validar se o relatório deixará de apresentar a diferença do evento em questão.

Passo 5Passo 5

Executar Relatório TAF Valores

| Objetivo: | Apoiar na identificação de possíveis divergências entre os valores de INSS existentes no ERP x TAF x RET, auxiliando também na conferência de valores (segurados, deduções salário família e maternidade) da guia de INSS.  O relatório fará a comparação dos valores de INSS integrados do ERP (S-1200, S-2299 e S-2399) contra os valores existentes nas tabelas do TAF e valores retornados do Governo (S-5001). |
| --- | --- |
| **Link Documentação:** | [TAF108\_Relatório Apoio Conferência Valores INS](http://tdn.totvs.com/pages/viewpage.action?pageId=394211788) |
| **Link Pacotes:** | **<https://suporte.totvs.com/portal/p/10098/download?e=706578>** |
| **Pre-requisitos:** |  |
| **Tela:** |  |

Passo 6Passo 6

Comparativo RM X Retorno do Governo

| Objetivo: | Exibir relatório de apoio que auxiliará na identificação de divergência de valores de INSS. Será um comparativo dos valores de bases de INSS, contidos na folha analítica e retorno do Governo. |
| --- | --- |
| **Link Documentação:** |  |
| **Link Pacotes:** | Instalação das versões: 12.1.19.379 ou 12.1.20.367 ou 12.1.21.112 ou acima.  <https://suporte.totvs.com/portal/p/10098/download#company/> |
| **Pré-Requisitos:** | Instalação das versões específicas. |
|  |  |

### **O que fazer em caso do comparativo de bases retornar diferenças de valores?**

1. **Deverá certificar que todos os passos (1 a 5) anteriores foram executados sem que tenha ocorrido saídas inconsistentes.**
2. **Em caso de haver diferenças entre os valores do governo e dos valores da Folha Analítica, deverá certificar se não existem eventos pendentes de envio no RM para o TAF ou pendentes no TAF para envio ao governo.**  
   Analisar possíveis alterações de incidências de eventos na Folha;  
   Recálculos pendentes;  
   Alterações manuais;  
   Alterações de códigos de naturezas de rubricas do eSocial.
