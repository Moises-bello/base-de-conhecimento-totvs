---
article_id: 20761894292503
category: Financeiro - Contas a Pagar - Dirf
content_hash: 2af3151874675eaf63fc11e8f5aad9ad0fcca8dfac58768d62dc10ad578fe949
fetched_at: '2026-06-28T22:38:10.658907+00:00'
product: protheus
section_id: 1500001550482
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA401 - Informações
  e atualizações sobre a DIRF 2025 (Ano-Calendário 2024)
type: support-article
updated_at: '2025-01-31T19:54:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20761894292503-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA401-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-a-DIRF-2025-Ano-Calend%C3%A1rio-2024
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20761906906135) Tempo aproximado para leitura: **00:06:00 min** **Dúvida**Informações e atualizações sobre a DIRF 2025 (Ano-Calendário 2024) no módulo Financeiro (**FINA401**)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**Essa documentação tem o intuito de centralizar as atualizações, links e vídeos para o processo da DIRF no módulo Financeiro  
  
**Importante**:  
No ano de 2025 não houve atualização para o processo no **modulo Financeiro**, a ultima correção liberada para adequação da entrega **DIRF 2024**, ano calendário 2023, foi para adicionar as deduções simplificada de **Imposto de Renda Pessoa Física (IRPF)** a última data do fonte **FINA401** atualizado está na data 29/04/2024   
  
Quando o **IRPF** for simplificado será criado uma linha a mais no processamento da rotina **FINA401** com essa dedução e que ira gravar na tabela **SR4**  
Exemplo do processamento da rotina FINA401 com a versão atualizada  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21456568432663)  
Gravação na tabela **SR4** com o tipo **R4\_TIPOREN = "B4**" para ser identificado apenas para retenções em que a dedução simplificada foi a mais vantajosa para o contribuinte  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21456523357591)  
  
**Importante:** Caso precisa reprocessar os dados para o **IRPF na tabela SR4** necessário executar o reprocessamento [Opção Reprocessamento (FINA401 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312161877)   
  
**Patch:  
  
**12.1.2310**:<https://suporte.totvs.com/portal/p/10098/download?e=1145712> ;  
**12.1.2210**:<https://suporte.totvs.com/portal/p/10098/download?e=1145711> ;  
**12.1.33**:<https://suporte.totvs.com/portal/p/10098/download?e=1145713> ;****(Somente para clientes com garantia estendida)**

**Links:**  
  
**How To | MP - SIGAFIN - FINA401 - Gera dados para DIRF | #TOTVSBackofficeLinha\_Protheus**

Documentações  
[Geração de Dados para DIRF (FINA401)](https://tdn.totvs.com/pages/releaseview.action?pageId=312161841)  
[Gerar Dirf para fornecedores residentes no exterior](https://tdn.totvs.com/display/public/PROT/Gerar+Dirf+para+fornecedores+residentes+no+exterior)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA401 - Como gerar a DIRF com as informações do financeiro, sem acesso ao módulo de Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023373931-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA401-Como-gerar-a-DIRF-com-as-informa%C3%A7%C3%B5es-do-financeiro-sem-acesso-ao-m%C3%B3dulo-de-Gest%C3%A3o-de-Pessoal)  
[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como gravar o campo Gera DIRF( E2\_DIRF)=Sim para PIS , COFINS, CSLL e IRRF , a partir da Nota Fiscal de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001851882-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-gravar-o-campo-Gera-DIRF-E2-DIRF-Sim-para-PIS-COFINS-CSLL-e-IRRF-a-partir-da-Nota-Fiscal-de-Entrada)  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Qual a gravação correta dos campos no Financeiro para geração da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413978579223-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Qual-a-grava%C3%A7%C3%A3o-correta-dos-campos-no-Financeiro-para-gera%C3%A7%C3%A3o-da-DIRF)

[Opção Reprocessamento (FINA401 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312161877)  
[Valor de rendimento dos impostos incorreto na FINA401 quando título tem parcelas](https://tdn.totvs.com.br/display/public/PROT/FIN0101_CPAG_Rendimento_do_imposto_incorreto_na_DIRF_para_titulos_desdobrados)

**Saiba Mais**  
[Financeiro - Contas a Pagar - Dirf](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550482-Financeiro-Contas-a-Pagar-Dirf)  
[RH - Linha Protheus - GPE - Informações e atualizações sobre a DIRF 2025 (Ano-Calendário 2024)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28490771612183-RH-Linha-Protheus-GPE-Informa%C3%A7%C3%B5es-e-atualiza%C3%A7%C3%B5es-sobre-a-DIRF-2025-Ano-Calend%C3%A1rio-2024)
