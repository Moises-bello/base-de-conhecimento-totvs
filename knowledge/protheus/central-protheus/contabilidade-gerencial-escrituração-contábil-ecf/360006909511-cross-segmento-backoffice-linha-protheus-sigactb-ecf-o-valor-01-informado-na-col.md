---
article_id: 360006909511
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: efeec60f65fea7e04a896b9fba8039828e766e0dd50771ac200bc86f36c2649a
fetched_at: '2026-06-28T22:40:47.447694+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF -O valor '01' informado
  na coluna 2 para o campo ID Conta Referencial ( CEH_IDCODC ) não existe na base
  de dados.
type: support-article
updated_at: '2022-07-12T18:38:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006909511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-O-valor-01-informado-na-coluna-2-para-o-campo-ID-Conta-Referencial-CEH-IDCODC-n%C3%A3o-existe-na-base-de-dados
---

**Dúvida**

**Erro apresentado a realizar a Interação com o TAF para geração da ECF**

O valor '**01**' informado na coluna 2 para o campo ID Conta Referencial (**CEH\_IDCODC** ) não existe na base de dados.  
  
**Ambiente**

#### Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 11.80 **Solução**

Veja com atenção :<http://tdn.totvs.com/pages/viewpage.action?pageId=372551207>

 Caso esteja utilizando visão gerencial de balanço e DRE,verifique  as conta informadas na visão gerencial

* [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)

**Não**, as informações do Balanço Patrimonial (Registros  L100, P100 e U100) e Demonstrativo de Resultado ( Registros L300, P150 e U150) devem ser demonstrados com as mesmas nomenclaturas existentes no Manual de Orientação do ECF.

Para apoio na configuração foi disponibilizado o modelo das visões gerenciais necessárias para a extração dos dados.

Veja que o modelo de Visão gerencial disponibilizada possui a conta referencial no campo "Enti Gerenc" , se o campo não estiver preenchido com a conta referencial o erro será apresentado

![](http://tdn.totvs.com/download/attachments/372551207/image2018-6-18_9-19-6.png?version=1&modificationDate=1529324411000&api=v2)

* Para gerar o Balanço Patrimonial (Registros P100) e Demonstrativo de Resultado ( Registros  P150  ) o sistema considera a visão gerencial informada  ou caso **não** informe a visão gerencial ,o sistema **considera o plano referencial amarrado ao plano de contas**

Reg P100          CSC / CSK         T092AA quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg P100          CSD / CSE         T092AA quando utilizado Visão Gerencial.   
Reg P150          CSC / CSK         T092AC quando **não** utilizado Visão Gerencial,o sistema irá considerar a amarração do plano de contas com o plano referencial  
Reg P150          CSD / CSE         T092AC quando utilizado Visão Gerencial.

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)

Segue abaixo modelo de Visão gerencial

<http://tdn.totvs.com/pages/releaseview.action?pageId=189314312>

- verifique  o plano referencial utilizado   se o mesmo se enquadra ao regime tributário da empresa

Veja tratamento das Autocontidas  
[MP - SIGACTB - CTBS001 - Atualização das Tabelas Autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGACTB-CTBS001-Atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-)

Veja as tabelas   
[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)
