---
article_id: 24969133490455
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 7b913893c774561cfe19d63c08cb1688b3b24164fb88348f6f779fb9c5eec828
fetched_at: '2026-06-28T22:40:48.794101+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF : P300 COMO GERAR'
type: support-article
updated_at: '2024-10-03T11:03:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24969133490455-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-P300-COMO-GERAR
---

**Dúvida**Procedimento para gerar o  P300   
  
**Ambiente**

Microsiga Protheus  – Contabilidade Gerencial  – A partir da versão 11.80  
  
**Solução**

Utilize a visão do P130,P200,P230,P300,P400,P500 : 

* [Arquivos modelos Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006687252-MP-SIGACTB-CTBA161-Arquivos-modelos-Vis%C3%A3o-Gerencial?source=search)
* [Como importar Visão Gerencial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-MP-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial-?source=search)
* Através da rotina CTBA130 realize a[Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)
* Verifique todos os pontos  [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)Balanço e DRE?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)
* **Emita relatório CTBR040** e informe a visão gerencial ( P300 )no campo![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24969164954263) , **para conferencia dos valores apresentados**
* Os saldos apresentado neste relatório deve refletir nas tabelas a rotinas abaixo
* [Veja: Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)

Ao gerar o arquivo informe as visões gerencias Abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24969133459991)  
  
1º Passo Veja se a tabelas CS foram populada   
  
[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)  
  
  
Registro            Tabela              TAFST1/TAFST2  
  
Reg P300          CSD / CSE         T092AB  
  
  
  
  
CSD - Veja se o registro foi gerado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24969133461399)

CSE - Veja se o registro foi gerado com os mesmos valores apresentados no relatório CTBR040 , emitido anteriormente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24969133462295)

2º Passo tabela TAFST1 e TAFST2  e veja se o bloco T092AB foi gerado  
  
  
- no registro da conta verifique T092AB  
  
  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração  
     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada  
  
   Ex: 

|T092|20230101|20230331|T01|

|T092AB|04|1|1350|

|T092AB|04|2|1350|

|T092AB|04|6|1350|

|T092AB|04|7|1350|

- Verifique o TAFSTATUS = 3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24969164960663)

Através do [Layout Único do TAF](https://tdn.totvs.com/pages/viewpage.action?pageId=498722271)campo abaixo está preenchido  
  
"Código correspondente ao registro do ECF  
  
  
04 = P300 - Cálculo do IRPJ com Base no Lucro Presumido

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24969133469335)

3º Passo Acesse a rotina **TAFA321** do TAF e veja se o bloco P foi gerado   
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais>

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24969133470743)

Exemplo P300

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24969164965399)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24969133473687)

Veja todos os pontos abaixo :  
[MP - SIGACTB : ECF PRÉ-REQUISITOS PARA GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-MP-SIGACTB-ECF-PR%C3%89-REQUISITOS-PARA-GERAR-?source=search)

* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* [Arquivo Fracionado e ou Situação Especial (Extinção,Fusão,Incorporação,Transformação ...)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007208532-MP-SIGACTB-ECF-Arquivo-Fracionado-e-ou-Situa%C3%A7%C3%A3o-Especial-Extin%C3%A7%C3%A3o-Fus%C3%A3o-Incorpora%C3%A7%C3%A3o-Transforma%C3%A7%C3%A3o-?source=search)  
  *Obs: orientações informadas são exemplos , o contador deve se basear no manual da receita para preenchimento dos parâmetros*

[MP - SIGACTB - ECF : K156 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search)
