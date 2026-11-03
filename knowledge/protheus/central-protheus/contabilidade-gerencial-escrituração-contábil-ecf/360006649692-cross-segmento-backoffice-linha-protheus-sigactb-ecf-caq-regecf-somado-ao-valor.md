---
article_id: 360006649692
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 8409ebf2fb7aa9e63f2b2d1b932287aecfe41068d4282fda6af2e7c037c21c71
fetched_at: '2026-06-28T22:40:47.720114+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - ( CAQ_REGECF )
  somado ao valor
type: support-article
updated_at: '2023-06-29T19:01:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006649692-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-CAQ-REGECF-somado-ao-valor
---

**Dúvida**

**Erro apresentado a realizar a Interação com o TAF para geração da ECF**

O valor '1' informado na coluna 2 para o campo Registro ECF ( CAQ\_REGECF ) somado ao valor '11010010001' informado na coluna 3 para o campo Codigo Conta Referencial ( CAQ\_CODCTA ) não existe na base de dados.  
  
**Ambiente**

Protheus – Contabilidade Gerencial – A partir da versão 11.80  
  
  
**Solução**

Erro 4 - Linha: 6

O valor '1' informado na coluna 2 para o campo Registro ECF ( CAQ\_REGECF ) somado ao valor '11010010001' informado na coluna 3 para o campo Codigo Conta Referencial ( CAQ\_CODCTA ) não existe na base de dados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016121931)

# [Layout Único Do TAF](https://tdn.totvs.com/pages/viewpage.action?pageId=498722271)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016073472)

Veja que com base no [layout do TAF](https://tdn.totvs.com/pages/releaseview.action?pageId=498722271) o deveria ter sido gerada uma conta referencial no lugar do numero “**11010010001 “**

Ex

|T088AA|1|**1.0.01.01.01**|1261.48|1|1646.83|1|

**Registro L100 - Balanço Patrimonial**

* Tabela - CAQ (Balanço Patrimonial)
* Registro do Layout TOTVS - T088AA
* Rotina - TAFA361 (Bloco L - Lucro Líquido)

**O registro pode ser gerado de duas formas Com visão e sem Visão gerencial**

Registro        Tabela CTB                TAFST1/TAFST2

Reg L100    CSC / CSK,           T088AA quando não utilizado Visão Gerencial o sistema considera  plano referencial  
Reg L100    CSD / CSE,           T088AA quando utilizado Visão Gerencial.

* [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)

**Não**, as informações do Balanço Patrimonial (Registros  L100, P100 e U100) e Demonstrativo de Resultado ( Registros L300, P150 e U150) devem ser demonstrados com as mesmas nomenclaturas existentes no Manual de Orientação do ECF.

Para apoio na configuração foi disponibilizado o modelo das visões gerenciais necessárias para a extração dos dados.

modelo visão : [Visões Gerenciais](http://tdn.totvs.com/pages/viewpage.action?pageId=189314312)

Veja : [Como importar Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial?source=search)

Veja que o modelo de Visão gerencial (CTBA161) disponibilizada possui a conta referencial no campo "Enti Gerenc" , se o campo não estiver preenchido com a conta referencial o erro será apresentado

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360039904413)

Veja: <http://tdn.totvs.com/pages/releaseview.action?pageId=284471783>

Veja tratamento das Autocontidas  
[MP - SIGACTB - CTBS001 - Atualização das Tabelas Autocontidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006985071-MP-SIGACTB-CTBS001-Atualiza%C3%A7%C3%A3o-das-Tabelas-Autocontidas-)  
Veja as tabelas   
[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)
