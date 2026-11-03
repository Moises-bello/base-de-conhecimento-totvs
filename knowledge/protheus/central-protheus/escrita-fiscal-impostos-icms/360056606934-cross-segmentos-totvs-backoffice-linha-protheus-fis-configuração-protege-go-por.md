---
article_id: 360056606934
category: Escrita Fiscal - Impostos - ICMS
content_hash: 5d610011eaf7f53ad92210afbd7ff473fd3f3cb86d325e8d086b06ab15b68449
fetched_at: '2026-06-28T22:39:25.612448+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Configuração PROTEGE
  - GO por Documento Fiscal
type: support-article
updated_at: '2024-08-22T17:27:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056606934-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Configura%C3%A7%C3%A3o-PROTEGE-GO-por-Documento-Fiscal
---

**Dúvida**Configuração do PROTEGE - GO por documento fiscal.

**Ambiente**  
Microsiga Protheus  – Livros Fiscais – A partir da versão 11.80  
  
**Solução**

1. No **Configurador (SIGACFG)** acesse **Ambientes/ Cadastros/ Parâmetros (CFGX017)**. Configure os parâmetros a seguir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360096146154)

#### 

#### Procedimentos Gerais

#### 

#### Cadastre uma **Natureza** e informe o parâmetro **MV\_PROTEGE**. Esta natureza será utilizada na geração dos títulos do PROTEGE gerados na apuração de ICMS ou, quando configurado, na emissão do documento de saída.

#### 

#### **Cálculo do PROTEGE-GO via Apuração de ICMS**

#### 

#### Para que o PROTEGE-GO seja calculado diretamente pela apuração de ICMS efetue as configurações abaixo:

1. #### Configure o parâmetro **MV\_GERPROT** = .F. para que o valor do fundo não seja apurado com base nos valores calculados nos documentos fiscais.
2. #### Efetue a apuração de ICMS.
3. #### Verifique na aba de "Informações Complementares" da apuração, na linha **063: PROTEGE-GO**, o valor do fundo calculado.

#### 

#### **Cálculo do PROTEGE-GO via Documento Fiscal**

#### 

#### Está disponível um método de cálculo e apuração do PROTEGE-GO por nota fiscal, para suprir a necessidade de cálculo com alíquotas diferenciadas por operação. Para configurar este método efetue as configurações abaixo:

1. #### Configure o parâmetro **MV\_GERPROT** = .T. para que o valor do fundo seja apurado com base nos valores calculados nos documentos fiscais.
2. #### Informe o valor da alíquota do PROTEGE-GO no campo **F4\_ALIQPRO (Aliq.PROT.GO)**da TES de entrada ou TES de saída.

#### Exemplo de calculo do Protege por nota fiscal - redução de base de calculo

Memoria de calculo

|  |  |
| --- | --- |
| VENDA INTERNA | 1.000,00 |
| REDUÇÃO BASE DE CALCULO ICM | 57,89% |
| VALOR DA BASE TRIBUTADA | 578,95 |
| BASE ISENTA | 421,05 |
| ALIQUOTA INTERNA | 19% |
| VALOR DO ICMS | 110,00 |
| VALOR DO ICMS BASE REDUZIDA | 80,00 |
| PROTEGE - GO ALIQ | 15% |
| VALOR DO PROTEGE-GO | 12,00 |

Configurações:

Paramentros

MV\_ESTADO = GO  
MV\_protege = PROTEGE  
MV\_RECSTGO = 000100;01  
MV\_ICMPAD = 19  
MV\_GERPROT = .T.  
   
Cadastrar o codigo 000100;01 no cadastro de fornecedores  
![](https://totvssuporte.zendesk.com/attachments/token/Dk8fR68fFpYHVwnBkQG4KTL0U/?name=image.png)  
   
Cliente = GO  
   
TES  
Calcula icms = sim  
L fiscal icms = outros  
CST = 20  
% red icm = 57,89  
mat consumo = não  
F4\_aliqpro = 15%  
   
![](https://totvssuporte.zendesk.com/attachments/token/BSV0NCW2yhH5QqG7tIAvQu6jQ/?name=image.png)  
   
Sit trib icm = 20  
![](https://totvssuporte.zendesk.com/attachments/token/Q1lCJwEtp6Zr5nW7JMScF7C2A/?name=image.png)  
 Pedido de vendas  
   
![](https://totvssuporte.zendesk.com/attachments/token/u6v2wjGpxdEeTNA528aa0neBT/?name=image.png)  
 

#### 

#### Parecer consultoria tributaria da TOTVS:

#### Fundo PROTEGE-GO – Percentuais aplicáveis

#### <https://tdn.totvs.com/pages/releaseview.action?pageId=244723817>

#### Informações adicionais:

#### <https://tdn.totvs.com/pages/releaseview.action?pageId=236590010>

#### Recolhimento Antecipado do ICMS e do PROTEGE-GO na Emissão da NF de Saída

#### <https://tdn.totvs.com/display/public/PROT/DSERFIS2-1872+DT+ANTECIPACAO+ICMS+E+PROTEGE+GO>

#### 

#### 

####
