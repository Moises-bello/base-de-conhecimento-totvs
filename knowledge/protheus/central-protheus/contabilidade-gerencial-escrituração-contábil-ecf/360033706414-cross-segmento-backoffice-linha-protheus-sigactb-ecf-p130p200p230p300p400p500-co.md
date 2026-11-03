---
article_id: 360033706414
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 6e12c332166af23ce7b8dd459fc251e2e86142dc33bec0b7397828bde1a3daf6
fetched_at: '2026-06-28T22:40:47.614609+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus  - SIGACTB - ECF : P130,P200,P230,P300,P400,P500
  COMO GERAR'
type: support-article
updated_at: '2022-10-25T18:21:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033706414-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-P130-P200-P230-P300-P400-P500-COMO-GERAR
---

**Dúvida**Procedimento para gerar o P130,P200,P230,P300,P400,P500  
  
**Ambiente**

Microsiga Protheus  – Contabilidade Gerencial  – A partir da versão 11.80  
  
**Solução**

Utilize a visão do P130,P200,P230,P300,P400,P500 : 

* [Arquivos modelos Visão Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006687252-MP-SIGACTB-CTBA161-Arquivos-modelos-Vis%C3%A3o-Gerencial?source=search)
* [Como importar Visão Gerencial?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007545672-MP-SIGACTB-Como-importar-Vis%C3%A3o-Gerencial-?source=search)
* Através da rotina CTBA130 realize a[Amarração Visão Gerencial ao Livro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006908012-MP-SIGACTB-CTBA161-CTBA130-Amarra%C3%A7%C3%A3o-Vis%C3%A3o-Gerencial-ao-Livro?source=search)
* Verifique todos os pontos  [É permitido utilizar o mesmo modelo de Visão Gerencial já usado no Sped Contábil (ECD)Balanço e DRE?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006823491-MP-SIGACTB-ECF-%C3%89-permitido-utilizar-o-mesmo-modelo-de-Vis%C3%A3o-Gerencial-j%C3%A1-usado-no-Sped-Cont%C3%A1bil-ECD-?source=search)
* **Emita relatório CTBR040** e informe a visão gerencial (P130,P200,P230,P300,P400,P500)no campo![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9784312441111) , **para conferencia dos valores apresentados**
* Os saldos apresentado neste relatório deve refletir nas tabelas a rotinas abaixo

Ao gerar o arquivo informe as visões gerencias Abaixo

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044809334/mceclip0.png)  
  
1º Passo Veja se a tabelas CS foram populada   
  
[MP - SIGACTB - ECF - Tabelas ECF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006861411-MP-SIGACTB-ECF-Tabelas-ECF?source=search)  
  
  
Registro            Tabela              TAFST1/TAFST2  
Reg P130          CSD / CSE         T092AB   
Reg P200          CSD / CSE         T092AB  
Reg P230          CSD / CSE         T092AB  
Reg P300          CSD / CSE         T092AB  
Reg P400          CSD / CSE         T092AB  
Reg P500          CSD / CSE         T092AB  
  
  
  
CSD - Veja se o registro foi gerado

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045671893/mceclip1.png)

CSE - Veja se o registro foi gerado com os mesmos valores apresentados no relatório CTBR040 , emitido anteriormente

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045672093/mceclip2.png)

2º Passo tabela TAFST1 e TAFST2  e veja se o bloco T092AB foi gerado  
  
  
- no registro da conta verifique T092AB  
  
  \*posicione o Mouse no  "TAFKEY"  na Conta que possui amarração  
     \* Editar > Alterar -  Verifique  se a conta referencial está sendo apresentada  
  
   Ex: 

|T092|20180601|20180630|A06|

|T092AB|02|1|489750|

|T092AB|02|2|489750|

- Verifique o TAFSTATUS = 3

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045672353/mceclip3.png)

Através do [Layout Único do TAF](https://tdn.totvs.com/pages/viewpage.action?pageId=498722271)campo abaixo está preenchido  
  
"Código correspondente ao registro do ECF  
  
01 = P130 - Demonstração das Receitas Incentivadas do Lucro Presumido  
  
02 = P200 - Apuração da Base de Cálculo do Lucro Presumido  
  
03 = P230 - Cálculo da Isenção e Redução do Lucro Presumido  
  
04 = P300 - Cálculo do IRPJ com Base no Lucro Presumido  
  
05 = P400 -Apuração da Base de Cálculo da CSLL com Base no Lucro Presumido  
  
06 = P500 - Cálculo da CSLL com Base no Lucro Líquido"

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043385294/mceclip3.png)

3º Passo Acesse a rotina **TAFA321** do TAF e veja se o bloco P foi gerado   
  
<http://tdn.totvs.com/pages/releaseview.action?pageId=192089512#Obriga%C3%A7%C3%A3oECF-Escritura%C3%A7%C3%A3oCont%C3%A1bilFiscal-BlocoK-SaldosdasContasCont%C3%A1beiseReferenciais>

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044230433/mceclip4.png)

Exemplo P200

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044810894/mceclip4.png)

Veja todos os pontos abaixo :  
[MP - SIGACTB : ECF PRÉ-REQUISITOS PARA GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024565514-MP-SIGACTB-ECF-PR%C3%89-REQUISITOS-PARA-GERAR-?source=search)

* [Como realizar a exportação no Regime tributário Lucro Presumido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004838052-MP-SIGACTB-ECF-Como-realizar-a-exporta%C3%A7%C3%A3o-no-Regime-tribut%C3%A1rio-Lucro-Presumido?source=search)
* [Arquivo Fracionado e ou Situação Especial (Extinção,Fusão,Incorporação,Transformação ...)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007208532-MP-SIGACTB-ECF-Arquivo-Fracionado-e-ou-Situa%C3%A7%C3%A3o-Especial-Extin%C3%A7%C3%A3o-Fus%C3%A3o-Incorpora%C3%A7%C3%A3o-Transforma%C3%A7%C3%A3o-?source=search)  
  *Obs: orientações informadas são exemplos , o contador deve se basear no manual da receita para preenchimento dos parâmetros*

[MP - SIGACTB - ECF : K156 COMO GERAR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026082773-MP-SIGACTB-ECF-K156-COMO-GERAR?source=search)
