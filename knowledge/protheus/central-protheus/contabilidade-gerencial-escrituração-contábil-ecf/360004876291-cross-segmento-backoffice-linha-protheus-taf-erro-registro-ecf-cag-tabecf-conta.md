---
article_id: 360004876291
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 380ed6c48dad4cc1a35015fe6dcedf7e26ad407a5321902a789e8a122664bd67
fetched_at: '2026-06-28T22:40:47.542600+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - TAF- ERRO: Registro _ECF (CAG_TABECF)
  Conta Referencial _ (CAG_CTAREF) não existe na base de dados'
type: support-article
updated_at: '2023-08-10T14:40:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004876291-Cross-Segmento-Backoffice-Linha-Protheus-TAF-ERRO-Registro-ECF-CAG-TABECF-Conta-Referencial-CAG-CTAREF-n%C3%A3o-existe-na-base-de-dados
---

**Ocorrência**

 O valor '04' informado na coluna 2 o campo Tabela Registro ECF(CAG\_TABECF)somado ao valor '2.03.04.01.90'informado na coluna 3 para o campo Conta Referencial (CAG\_CTAREF) não existe na base de dados

**Ambiente**

Protheus – Contabilidade Gerencial – 12.1.17

**Solução**

Com base na no link abaixo verifique a estrutura do Layout do Bloco T087 e T087AB

[http://tdn.totvs.com/pages/releaseview.action?pageId=187534666](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

![](https://tdn.totvs.com/download/attachments/284873624/image2017-7-17%2018%3A24%3A7.png?version=1&modificationDate=1500327805000&api=v2)|

![](https://tdn.totvs.com/download/attachments/284873624/image2017-7-17%2018%3A24%3A37.png?version=1&modificationDate=1500327805000&api=v2)

**Registro K356 - Mapeamento Referencial dos Saldos Finais das Contas de Resultado Antes do Encerramento**

* Tabela - CAG (Map. Ref. Saldo Final Antes Enc)
* Registro do Layout TOTVS - T087AD
* Rotina - **TAFA311** (Identificação dos Períodos e Formas de Apuração do IRPJ e da CSLL)

[http://tdn.totvs.com/pages/releaseview.action?pageId=187534666](https://tdn.totvs.com/pages/releaseview.action?pageId=187534666)

Através da rotina **TAFA311**verificar a validação do campo **CAG\_CTAREF**

![](https://tdn.totvs.com/download/attachments/284873624/image2017-7-17%2018%3A25%3A48.png?version=1&modificationDate=1500327805000&api=v2)

Veja na **CHA** que a conta em questão está disponível somente para **L100A** e **P100**

Diante disso o bloco T010AA Deveria ter sido gerado conforme abaixo

L100A =**01**

|T087AB|**01**|2.03.04.01.90|3089443.59|2|

P100 =**07**

|T087AB|**07**|2.03.04.01.90|3089443.59|2|

![](https://tdn.totvs.com/download/attachments/284873624/image2017-7-17%2018%3A28%3A9.png?version=1&modificationDate=1500327805000&api=v2)

Neste caso Veja  que T127 o parâmetro “Forma de [Trib.no](http://trib.no/) Periodo” foi preenchido para Lucro presumido “PPPP”

![](https://tdn.totvs.com/download/attachments/284873624/image2017-7-17%2018%3A29%3A48.png?version=1&modificationDate=1500327805000&api=v2)

![](https://tdn.totvs.com/download/attachments/284873624/image2017-7-17%2018%3A30%3A11.png?version=1&modificationDate=1500327805000&api=v2)

-o registro deveria ter sido gerado  P100 =07

|T087AB|07|2.03.04.01.90|3089443.59|2|

Com isso solicito que verifique a amarração da contas e suas devidas naturezas

![](https://tdn.totvs.com/download/attachments/284873624/image2017-7-17%2018%3A42%3A16.png?version=1&modificationDate=1500327805000&api=v2)

Diante disso solicito que verifique se a conta contábil está amarrada a conta referencial corretas

Ativo com conta de Ativo

Passivo com conta de Passivo

Resultado com conta de Resultado

- verifique a amarração das contas e suas devidas naturezas  
-Verifique se a conta contábil e a conta referencial possuem a mesma natureza

Veja a documentação abaixo com atenção:

[Premissa J050/J051](https://tdn.totvs.com/pages/releaseview.action?pageId=284465420)

Caso esteja utilizando visão gerencial de balanço e DRE Verifique  as conta informadas na visão gerencial

**· É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)?**

Não, as informações do Balanço Patrimonial (Registros  L100, P100 e U100) e Demonstrativo de Resultado ( Registros L300, P150 e U150) devem ser demonstrados com as mesmas nomenclaturas existentes no Manual de Orientação do ECF.

Para apoio na configuração foi disponibilizado o modelo das visões gerenciais necessárias para a extração dos dados.

- verifique se está sendo utilizado o plano referencial que se enquadra no regime tributário da empresa

Código Grupo/Conta

1 PJ em Geral (L100A + L300A da ECF)

2 PJ em Geral – Lucro Presumido (P100 + P150 da ECF)

3 Financeiras (L100B + L300B da ECF)

4 Seguradoras (L100C + L300C da ECF)

5 Imunes e Isentas em Geral (U100A + U150A da ECF)

6 Financeiras – Imunes e Isentas (U100B + U150B da ECF)

7 Seguradoras – Imunes e Isentas (U100C + U150C da ECF)

8 Entidades Fechadas de Previdência Complementar (U100D + U150D da ECF)

9 Partidos Políticos (U100E + U150E da ECF)

Como converter e importar o plano referencial da Receita Federal

[Converter plano Referencial](https://tdn.totvs.com.br/display/public/mp/Como+converter+e+importar+o+plano+referencial+da+Receita+Federal)

Arquivos Modelos - Plano Referencial

[http://tdn.totvs.com/pages/releaseview.action?pageId=189314312](https://tdn.totvs.com/pages/releaseview.action?pageId=189314312)

**Saiba mais:**

[Obrigação ECF - Escrituração Contábil Fiscal](http://tdn.totvs.com/pages/releaseview.action?pageId=192089512)

[Wizard ECF](https://tdn.totvs.com/display/public/PROT/ECF0003_Help_wizard_rotina_central_escrituracao_ECF)

[Página centralizadora ECF](https://tdn.totvs.com/display/PROT/ECF)

[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF)
