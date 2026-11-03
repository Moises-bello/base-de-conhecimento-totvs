---
article_id: 360016791991
category: Financeiro
content_hash: 4f62143a4395feabac0b2200e902a1cbc751fad7444320705162fe707f2d9667
fetched_at: '2026-06-28T22:38:03.279144+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Invalid macro source
  (SSYacc0105e: Error token failed, no valid token)'
type: support-article
updated_at: '2022-06-15T00:44:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016791991-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Invalid-macro-source-SSYacc0105e-Error-token-failed-no-valid-token
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**Invalid macro source (SSYacc0105e: Error token failed, no valid token) :FWMntFilDt('E1\_VENCTO','Maior ou igual a','01/07/18','D','>=','SQL') AND FWMntFilDt('E1\_VENCTO','Menor ou igual a','31/07/18','D','<=','SQL') on FWBRWTABLE:EXECUTEFILTER(FWBRWTABLE.PRW) 20/06/2018 09:14:54 line : 498  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
   
**Causa**Este erro ocorre devido à falta de informações dentro do dicionário de dados do ambiente Financeiro.  
   
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o portal do cliente e realize o *download* do **último** dicionário completo e diferencial disponibilizado.  
Ex:

* 18-01-12-BRA-DICIONARIOS\_COMPL\_12\_1\_17 - Completo
* 18-01-12-BRA-DICIONARIOS\_DIF\_12\_1\_17 - Diferencial

**Obs.: Lembrando que em caso de dicionários para outros países, deve-se realizar o *download* do pais respectivo**.  
2. Realize o *download* do último pacote "**GERAL ACUMULADO**" do Protheus, contendo todas as correções liberadas de Julho/2017 até hoje. Outra atualização importante de pacotes recomendados que está disponível no link é [Pacotes Recomendados](https://suporte.totvs.com/portal/p/10098/download#detail/675550).  
3. Realizar o *backup* do seu ambiente (dicionário, RPO e dados)  
4. Excluir os arquivos de *log* abaixo:

**Dentro da pasta *system*:**

*mpupdlog.log*  
*mpupdlog.fpt*  
*mpwizard.hlp*  
*mpwizardhlp.lck*

**Dentro da pasta *Appserver*:**

*mpupddistri.tsk*  
  
5. Copiar os arquivos do dicionário para a sua pasta ***systemload***6. Aplicar o pacote "GERAL ACUMULADO" em seu ambiente.  
7. Realizar a execução do ***UPDDISTR* do acumulado e diferencial (sem a execução deste processo o erro não e corrigido).**
