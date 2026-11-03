---
article_id: 16706590343447
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 2472ee3db581095e63420110f4ca9d81dc3e99bbf1cb9a0fc7cb574f6e6da524
fetched_at: '2026-06-28T22:40:47.735334+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - ERRO: Reg. ECF
  ( CHG_TABECF )e Código ( CHG_CODIGO )'
type: support-article
updated_at: '2023-08-11T20:27:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16706590343447-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-ERRO-Reg-ECF-CHG-TABECF-e-C%C3%B3digo-CHG-CODIGO
---

**Dúvida**

Erro 1 - Linha: 48 - O valor '1' informado na coluna 2 para o campo Tab Reg. ECF ( CHG\_TABECF ) somado ao valor '2.05.01.01.01' informado na coluna 3 para o campo Código ( CHG\_CODIGO ) não existe na base de dados.  
   
|T094AC|1|2.05.01.01.01|57986.65|1|  
   
   
![](https://totvssuporte.zendesk.com/attachments/token/1sJl8KgCkTNDmuzeQf9hWVFj8/?name=image.png)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – **A partir da versão 12**  
  
**Solução**

* [Verificar o Layout Único](https://tdn.totvs.com/pages/viewpage.action?pageId=498722271) do TAF  o  1=U150A (DRE = Contas Receitas e Despesa)

   
![](https://totvssuporte.zendesk.com/attachments/token/7ioyu8hyF1AwrSQoozkDY7ZJJ/?name=image.png)  
   
[**Registro U150 - Demonstração do Resultado**](https://tdn.totvs.com/pages/releaseview.action?pageId=192089512)

* Tabelas - C2R (Natureza Conta/Grupo Contab.) / CHA (Código de Conta Referencial) / CHG (Demonstração do Resultado) / CAH (Período de Apuração)
* Registro do Layout TOTVS - T094AC
* Rotina - TAFA324 (Identificação Apuração do IRPJ e da CSLL das Empresas Imunes e Isentas)

   
CHG\_TABECF = 1=U150A (DRE = Contas Receitas e Despesa)    
CHG\_CODIGO = 2.05.01.01.01  
   
Através da rotina **TAFA324**verificar a validação dos campos **CHG\_TABECF e CHG\_CODIGO**  
   
**Veja que ao tentar seleciona  CHG\_TABECF = 1 U150A  e CHG\_CODIGO = 2.05.01.01.01 , o sistema apresenta a mensagem**  
   
![](https://totvssuporte.zendesk.com/attachments/token/q07zZ84hqSuPbNAi8EKOkTITl/?name=image.png)  
   
**Veja que o sistema busca  o campo CHG\_CODIGO da tabela CHA , ao filtrar a conta 2.05.01.01.01 veja que não existe para o  " 1 - U150A "**  
   
![](https://totvssuporte.zendesk.com/attachments/token/LEsbarCqdZiFmGOIzBVQ2MdJL/?name=image.png)  
   
Necessário que a conta **conta referencial 2.05.01.01.01 (passivo) seja amarrada através da rotina Cadastro Plano de contas (CTBA020) a uma conta de passivo**  
   
Diante disso avalie se existe alguma conta que não seja  do passivo amarrada na tabela CVD  
   
E ao gerar a revisão no modulo contabil deve informar o parâmetro abaixo de forma correta  
   
![](https://totvssuporte.zendesk.com/attachments/token/2cFzi2g6hE4uNZZBs2GHVtn5M/?name=image.png)
