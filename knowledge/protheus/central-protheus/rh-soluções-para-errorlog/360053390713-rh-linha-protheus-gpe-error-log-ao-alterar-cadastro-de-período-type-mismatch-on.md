---
article_id: 360053390713
category: RH - Soluções para error.log
content_hash: 4e0eb4369f20687125e7d0d66b8872e9b59a8b3ce43cbce48f41f98c3a28291e
fetched_at: '2026-06-28T22:44:08.870486+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log ao alterar Cadastro de Período - type
  mismatch on compare on GPEA400AMBPREP
type: support-article
updated_at: '2025-08-05T14:58:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053390713-RH-Linha-Protheus-GPE-Error-log-ao-alterar-Cadastro-de-Per%C3%ADodo-type-mismatch-on-compare-on-GPEA400AMBPREP
---

**Ocorrência**  
Ao realizar a alterações no Cadastro de Período, através da rotina **GPEA400**, é gerado ***error log**: **type mismatch on compare  on*** **GPEA400AMBPREP(GPEA400.PRW)**  
  
**Ambiente**TOTVS RH - OTVS RH (Linha Protheus) - Gestão de Pessoal - todas as versões  
  
**Causa**Este erro ocorre devido à inconsistência no parâmetro **MV\_DIASPER**  
  
**Solução**Para solucionar esta ocorrência realize o processo conforme descrito abaixo:  
  
**1.** Acesse o Programa **Configurador(SIGACFG) e clique em OK:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33959133984023)  
  
**2.** Acesse a rotina de **Base de Dados/Dicionário/Base de Dados**;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33959117623447)  
  
**3.** Acesse o caminho Abrir a Empresa e selecione em Parâmetros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33959117625111)  
  
**4.** Clique em Parâmetros e opte pela Lupa, conforme abaixo:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33959133990807)  
  
Pesquise na seção '**Procurar por:**' informando o parâmetro **MV\_DIASPER** e depois clicar em **'Buscar' conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33959133991959)**  
Após **'Buscar'** o parâmetro clique na opção da **'Lupa com uma folha(Visualizar)', conforme abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33959133995799)****5.** Após filtrar o parâmetro verifique se o mesmo se encontra conforme demonstrado no print abaixo:  
O tipo deve constar como **2-Caractere** e o conteúdo deve ser **1** ou **2 de acordo com a necessidade, sendo:   
1=Se o divisor será a quantidade de dias do mês do período;  
2=Se o divisor será sempre 30;**

Exemplo de configuração padrão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33959117632663)  
  
**3.** Após ajuste o ambiente não apresentará mais o erro ao alterar o período;  
  
**Saiba mais:**  
[Pacote Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
