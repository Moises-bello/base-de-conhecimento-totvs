---
article_id: 360022023172
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: a7fc34ce36291539cac15bd042f987fac4a25c677af73e5b808e35b94f79eeee
fetched_at: '2026-06-28T22:37:19.761901+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao tentar realizar
  medição não aparece o contrato ou planilha
type: support-article
updated_at: '2026-06-22T21:48:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022023172-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-tentar-realizar-medi%C3%A7%C3%A3o-n%C3%A3o-aparece-o-contrato-ou-planilha
---

**Ocorrência**  
Ao tentar realizar medição não aparece o contrato ou planilha  
  
**Ambiente**  
Microsiga Protheus – Gestão de Contratos – A partir da versão 12

**Causa**  
Esse incidente pode ocorrer quando em migração de versão ou inconsistência de base de dados alguns campos da planilha e cronograma financeiro do contrato estão gravados com informação incorreta ou em branco.  
  
**Solução**  
Abaixo seguem os pontos que se tem mapeados para esta ocorrência:

**1.** Verificar se os campos abaixo estão devidamente preenchidos:

**Planilha**:   
**CNA\_CRONOG** -> deve estar preenchido com o número do cronograma referente a esta planilha;  
**CNA\_CONTRA** -> deve estar preenchido com o número do contrato referente a esta planilha.  
Cronograma financeiro:   
**CNF\_NUMPLA** -> deve estar preenchido com o número da planilha correspondente a este cronograma;  
**CNF\_CONTRA** -> deve estar preenchido número do contrato referente a esta cronograma.

**2.** Também quando o contrato/planilha do contrato está fora da vigência, a rotina por padrão não trará o mesmo para medir, por isso, deve-se verificar se a Database que está sendo acessado o sistema para realizar a medição está contemplada entre as datas de Inicio e Fim do Contrato/Planilha dos campos **CN9\_DTINIC** (Data Inicial do Contrato) / **CN9\_DTFIM** (Data Final do Contrato) e **CNA\_DTINI** (Data Inicial da Planilha) / **CNA\_DTFIM** (Data Final da planilha).  
Além destes campos, o contrato deve estar com a legenda "verde - Vigente"/Campo CN9\_SITUAC = 05.

**3.** Falta de saldo para o contrato/planilha/competência, ou seja, contrato ou planilha está com saldo zerado, necessitando assim a revisão do contrato para se inserir mais saldo caso desejado.

Em relação a checagem de saldo do contrato/planilha/competência da opção 3, um teste que pode ser realizado em ambiente de homologação, é a realização do Processamento do Recalculo dos Saldos do Contrato, mencionada artigo do link abaixo, verificando se ocorre alguma alteração de valores de saldos, alteração essa que possa corrigir o problema em questão da medição do contrato em específico ou verificando a falta do saldo após o recálculo.

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o Reajuste de Saldo em contratos, planilhas e cronograma financeiro ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020124591-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-o-Ajuste-de-Saldos-em-Contratos-Planilhas-e-Cronograma-Financeiro?source=search)

**4.** Referente a compartilhamento de tabelas no Gestão de Contratos, todas as tabelas envolvidas do módulo possuem seu compartilhamento "Exclusivo".

No caso de compartilhamento de alguma tabela do módulo, é recomendado que todo o conjunto de tabelas do módulo possuam o mesmo compartilhamento entre si, conforme orientações do artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Compartilhamento de Tabelas no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20142986747287)

**5.** Checar se existe para o contrato em questão, registro ativo (não deletado) na tabela CPD com as informações corretas de Filial, Contrato e Planilha de acordo com o contrato e compartilhamento das tabelas, da mesma forma que o de um contrato em que este problema não acontece.

**6.** Caso possua controle de acesso no contrato habilitado, com o campo ***CN9\_VLDCTR = Sim***, deve-se verificar se o usuário que está realizando a medição possui acesso concedido a realizar medição do contrato, e se o contrato possui acesso autorizado a realizar medições na Filial que está se tentando fazer a medição, conforme informações contidas no artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Controle de Acesso ao contrato no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Controle-de-Acesso-ao-contrato-no-Gest%C3%A3o-de-Contratos?source=search)

**7.** Verifique se não possui Medição com alçada Rejeitada para essa Planilha. Caso possua e tenha necessidade de medir será necessário excluir a Medição rejeitada, para incluir uma nova Medição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24847828852887)

**8.** Caso o contrato possua mais de uma planilha e, ao incluir a medição, alguma delas não seja exibida, verifique se não há medições em aberto para a planilha que não apareceu no contrato.

***Saiba Mais:***  
[Ao tentar realizar medição não aparece o contrato/planilha](http://tdn.totvs.com/pages/releaseview.action?pageId=359470641)

[GCT0102 - Aviso de Help CNNOTRANS ao realizar a Medição](https://tdn.totvs.com/pages/viewpage.action?pageId=318606402)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Controle de Acesso ao contrato no Gestão de Contratos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016499391-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Controle-de-Acesso-ao-contrato-no-Gest%C3%A3o-de-Contratos?source=search)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
