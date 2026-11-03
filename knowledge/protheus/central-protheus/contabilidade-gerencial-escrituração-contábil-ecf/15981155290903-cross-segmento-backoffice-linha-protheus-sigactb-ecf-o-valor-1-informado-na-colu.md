---
article_id: 15981155290903
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 2e9a64b3a94a1af5ab4f4a0462226eff9d905798bdf0985aea89ebe3e1d7dd46
fetched_at: '2026-06-28T22:40:47.756712+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - O valor '1' informado
  na coluna 2 para o campo Identificador da Conta ( CAS_IDCODC ) não existe na base
  de dados.
type: support-article
updated_at: '2023-07-13T13:09:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15981155290903-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-O-valor-1-informado-na-coluna-2-para-o-campo-Identificador-da-Conta-CAS-IDCODC-n%C3%A3o-existe-na-base-de-dados
---

**Dúvida**

Erro apresentado a realizar a Interação com o TAF para geração da ECF

O valor '1' informado na coluna 2 para o campo Identificador da Conta ( **CAS\_IDCODC** ) não existe na base de dados.

**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 11.80

**Requisitos**

Veja com atenção :<http://tdn.totvs.com/pages/viewpage.action?pageId=372551207>

 Caso esteja utilizando visão gerencial de balanço e DRE,verifique  as conta informadas na visão gerencial

* [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)

**Não**, as informações do Balanço Patrimonial (Registros  L100, P100 e U100) e Demonstrativo de Resultado ( Registros L300, P150 e U150) devem ser demonstrados com as mesmas nomenclaturas existentes no Manual de Orientação do ECF.

Para apoio na configuração foi disponibilizado o modelo das visões gerenciais necessárias para a extração dos dados.

**Solução**

Erro 1 - Linha: 3 - O valor '1' informado na coluna 2 para o campo Identificador da Conta ( CAS\_IDCODC ) não existe na base de dados.  
   
Erro 2 - Linha: 4 - O valor '10' informado na coluna 2 para o campo Identificador da Conta ( CAS\_IDCODC ) não existe na base de dados.  
   
Erro 3 - Linha: 5 - O valor '15' informado na coluna 2 para o campo Identificador da Conta ( CAS\_IDCODC ) não existe na base de dados.  
   
Erro 4 - Linha: 6 - O valor '16' informado na coluna 2 para o campo Identificador da Conta ( CAS\_IDCODC ) não existe na base de dados.  
   
Erro 5 - Linha: 7 - O valor '18' informado na coluna 2 para o campo Identificador da Conta ( CAS\_IDCODC ) não existe na base de dados.  
   
Erro 6 - Linha: 8 - O valor '31' informado na coluna 2 para o campo Identificador da Conta ( CAS\_IDCODC ) não existe na base de dados.  
   
   
![](https://totvssuporte.zendesk.com/attachments/token/RSHy4c7Z27BzRsLxDX9cCS38o/?name=image.png)  
   
   
Através do [Leiaute do TAF](https://tdn.totvs.com/pages/viewpage.action?pageId=187534666) podemos  analisar a estrutura  
   
![](https://totvssuporte.zendesk.com/attachments/token/BMp82uVLT8pW2kyg62lYdnE1B/?name=image.png)  
   
   
 

* Solicito que verifique as[***Tabelas ECF***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)

***Registro            Tabela***[***TAFST1/TAFST2***](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)  
Reg L200          CSD / CSE         T088AB  
Reg L210          CSD / CSE         T088AC  
 



**Para conciliação dos saldos**

* Verifique a amarração da visão , veja se ao emitir relatório com a visão gerencial (CTBR500,CTBR040) o saldo é gerado correto , caso  o sistema apresente no relatório também o saldo errado ,  será necessário avaliar a configuração da visão gerencial
* Verifique a tabela CSD os registros foram gerados

***![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15981092382743)***

* Verifique o saldo CSE os registros foram gerados

![](https://totvssuporte.zendesk.com/attachments/token/GIfDuTYNnUcr6NVF2baYdBF9R/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/GVybjgZp9J11goLaUHsyyVsxn/?name=image.png)  
 

* Sistema tenta integrar com o TAF na tabela e rotina abaixo

   
[**Registro L210 - Informativo da Composição de Custos**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECFEscritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoN-C%C3%A1lculodoIRPJedaCSLL%E2%80%93LucroReal)

* Tabela - CAS (Informativo da Comp. de Custos)
* Registro do Layout TOTVS - T088AC
* Rotina - TAFA361 (Bloco L - Lucro Líquido)

   
Sistema tentando encontrar os codigo abaixo  na Rotina - TAFA361 , campo CAS\_IDCODC e tabela CH6  
   
![](https://totvssuporte.zendesk.com/attachments/token/Xzn98X73YcN7VcFoBOtRGUE36/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/wqZMyzKhFwrH81Ur16z6q5Flq/?name=image.png)  
   
Caso os código não existam na CH6 o sistema não irá permitir a integração e o erro será apresentado  
   
![](https://totvssuporte.zendesk.com/attachments/token/QiLTFP6rDvP2v0B9Byv0Nmh5x/?name=image.png)  
   
A CH6  é uma tabela autocontida, com isso é atualizada ao realizar a atualização do TAF

O procedimento indicado abaixo deve ser realizado após o sistema está devidamente atualizado, conforme artigo:

1. [Realize  a atualização doTAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004873211-MP-SIGACTB-ECF-Como-realizar-a-atualiza%C3%A7%C3%A3o-do-ECF-)

2.Limpe o conteúdo do parâmetro **MV\_VAUTCON**

3.Acesse o módulo **TAF (TOTVS Automação Fiscal)**

4.Acesse a rotina **Wizard de Configuração TAF (TAFLOAD)**

5**.**Execute o **Processamento** das Autocontidas para todas as empresas.
