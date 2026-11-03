---
article_id: 360019237571
category: RH - Férias
content_hash: 39771f7b5eb6cc014c6bbaff8589a0290264eceb02f26c1717897bffe8b2bee0
fetched_at: '2026-06-28T22:43:58.090132+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como configurar para buscar as maiores médias de
  comissão de um determinado período
type: support-article
updated_at: '2025-09-02T18:36:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019237571-RH-Linha-Protheus-GPE-Como-configurar-para-buscar-as-maiores-m%C3%A9dias-de-comiss%C3%A3o-de-um-determinado-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18585573306775) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como configurar o sistema para buscar as maiores médias de comissão de um determinado período?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O Mnemônico P\_COMISSA ou Parâmetro MV\_COMISSA define a **quantidade de meses** que será considerado para a **apuração das maiores médias de comissões** para funcionários comissionados.  
  
Com a conversão dos parâmetros (SX6) referentes a médias em mnemônicos (carregará o conteúdo padrão dos mnemônico com uma fórmula para validar conteúdo do parâmetro).  
Caso seja necessária alteração, poderá modificar diretamente o mnemônico e o parâmetro será inutilizado.

**> Para alterar o Mnemônico** Acesse: Gestão de Pessoal (**SIGAGPE**) / Atualizações / Definições de Cálculo / Mnemônicos (GPEA300) / Localize o mnemônico **P\_COMISSA** através do Filtro da rotina, clique em Alterar e informe no campo "Conteúdo" quantidade de meses que será considerada para buscar as maiores médias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18585560249751)

**> Caso opte por alterar o Parâmetro**, deixe o mnemônico P\_COMISSA com o conteúdo SUPERGETMV("MV\_COMISSA", , ,SRA->RA\_FILIAL)  como no exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18585573351319)

**Para alterar o Parâmetro Acesse:** Configurador (**SIGACFG**) / Ambiente / Cadastros / Parâmetros (CFGX017) / Localize o parâmetro **MV\_COMISSA** através do Filtro da rotina, clique em Alterar e informe nos campos de conteúdo a quantidade de meses que será considerada para buscar as maiores médias:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18585573359127)

**Exemplo**Caso deseje que a apuração das médias seja sobre as 6 **maiores** comissões do período, deverá preencher o mnemônico **P\_COMISSA ou** parâmetro **MV\_COMISSA** com 6.  
  
**>** Conferência do Demonstrativo de Médias:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31728040798743)

O sistema buscou todas as médias do período de férias do funcionário, somou as 6 maiores médias (em amarelo) e depois dividiu por 6.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31728040800151)

**Importante:** Esta configuração é aplicável apenas para as Verbas de Comissão e DSR de Comissão (identificadores de cálculo 0165 e 0166).  
 **Saiba Mais**

[RH - Linha Protheus - GPE - Como funciona a memória de Cálculo das médias, adicionais e pensão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035430554-RH-Linha-Protheus-GPE-Como-funciona-a-mem%C3%B3ria-de-C%C3%A1lculo-das-m%C3%A9dias-adicionais-e-pens%C3%A3o)  
[RH - Linha Protheus - GPE - Coluna Valor Original e Valor Atual Demonstrativo de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024606114-RH-Linha-Protheus-GPE-Coluna-Valor-Original-e-Valor-Atual-Demonstrativo-de-M%C3%A9dias)  
[RH - Linha Protheus - GPE - Como conferir o Relatório de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025175673-RH-Linha-Protheus-GPE-Como-conferir-o-Relat%C3%B3rio-de-M%C3%A9dias-)  
[Manual de Férias](https://tdn.totvs.com/pages/viewpage.action?pageId=941247504)
