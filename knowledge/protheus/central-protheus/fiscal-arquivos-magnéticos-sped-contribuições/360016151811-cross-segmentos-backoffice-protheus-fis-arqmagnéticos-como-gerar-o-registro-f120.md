---
article_id: 360016151811
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 445bbbcccc3bb377f868f4edc2aa3c05845c12afe323b107603a0790c20972f1
fetched_at: '2026-06-28T22:42:04.994464+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  Registro F120 EFD Contribuições
type: support-article
updated_at: '2025-04-17T20:07:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016151811-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-Registro-F120-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o Registro **F120 no EFD Contribuições**?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**O **Registro F120** trata ativos **sob depreciação (valor de operação)** que objetiva informar os valores de créditos apurados mensalmente, destacando a parcela apropriada no período e as condições associadas.

Recomendamos a apuração através de **Ativos** que possuem **vínculo com Nota Fiscal** com crédito de PIS e COFINS, ou seja, Ativos que foram incluídos via **Nota Fiscal de entrada.**  
  
**Passo 1.**Efetue o lançamento de uma **Nota Fiscal de entrada** no **Módulo Compras** e configure uma **TES (Tabela SF4)** de entrada conforme os campos abaixo:

**Atual Ativo** **(F4\_ATUATF)** =  Sim  
**Livro Fiscal de ICMS/ IPI** = Tributado/Outros/Isento. Para gerar as Tabelas dos Livros Fiscais **(SFT e SF3)**  
**PIS/COFINS (F4\_PISCOF) =**Ambos   
**Cred. PIS/COF (F4\_PISCRED) =**Credita  
**Sit Trib Pis** **(F4\_CSTPIS)** =  ?  
**Sit trib cof** **(F4\_CSTCOF)** = ?  
**Cod BC. CRED** **(F4\_CODBCC)** = 11 ou 09  
**Tp. Reg. (F4\_TPREG)** = ?  
  
**⚠️ Mesmo que os bens não possuam integração com o documento fiscal, os passos abaixos podem ser seguidos para geração correta do registro.****Passo 2.**   
Acesse o **Módulo 01 Ativo Fixo**, rotina **Classificação de Compras (ATFA240)**. Na classificação preencha os campos abaixo:

**Atualização de Ativos Imobilizados - Tabela SN1  
Calc. PIS** **(N1\_CALCPIS) =** 1- Sim  
**Ident. Bem** **(N1\_DETPATR) =** ?  
**Utiliz. Bem** **(N1\_UTIPATR) =**? **Orig. Cred (N1\_ORIGCRD) =** 0 ou 1  
**Sit. trib. PIS** **(N1\_CSTPIS) =**? **Aliq. PIS (N1\_ALIQPIS) =** ? **Sit. Trib. Cof (N1\_CSTCOFI) =** ? **Aliq. Cofins (N1\_ALIQCOF) =?**  
**Cod. BC. Cred (N1\_CODBCC) =** 09 ou 11 **Base Pis/Cof (N1\_CBCPIS ) =**1- "normal" ou 2 - "cadastro do bem"

A utilização do campo **N1\_CBCPIS** deve seguir o critério de apuração adotado pela empresa:

* **1 - Normal**: a situação tributária consideradas serão as informados na **TES de entrada**;
* **2 - Cadastro bem**: a situação tributária consideradas serão as inseridos diretamente na **aba fiscal do Ativo Fixo**.

A escolha correta garante que os créditos de **PIS/COFINS** sejam apurados conforme a origem dos dados definida no processo fiscal da empresa.

**📢️ Os campos que possuem "?" indicados nesta documentação, devem ser preenchidos de acordo com as regras de negocio de cada cliente, e não podem permanecer vazios.**

**Saldo e Valores - Tabela SN3**

**Tipo Ativo (N3\_TIPO)** = ? **Taxa depreciação  (N3\_TXDEPR1)** = ? **Conta contábil (N3\_CCONTAB)**= ?

**Passo 3.**Acesse a **rotina Calculo Mensal (ATFA050)**, atente-se para a data base do sistema, pois o cálculo deve ser feito **no último dia do mês.** Neste momento os valores depreciados são gerados na **Tabela SN4.**  
  
Importante: Verifique também se **todas as moedas foram cadastradas para todos os dias na rotina** **Cadastro de moedas (MATA090).****Passo 4.**Acesse a **Rotina FISA001** e **processe a Apuração do EFD Contribuiçõe**s. Na Apuração os **valores depreciados** serão levados na aba **Composição dos Créditos** e linha **Base de cálculo Ativo Fixo – Depreciação.** Neste processo, é gerado a **Tabela CL2.****Passo 5.**Gere o **Arquivo txt do EFD Contribuições** e verifique o **Registro F120**.  
  
Importante:   
Os valores de **créditos de PIS e COFINS** da **Nota Fiscal de entrada** que geram informações no módulo do **Ativo Fixo (SIGAATF)**, não são considerados no **bloco A, C e D** do **arquivo txt do EFD Contribuições**. Os valores de crédito são considerados **somente no registro F120**, para que não seja gerado crédito duplicado.  
  
Não devem ser considerados para apropriação e **créditos do PIS e da COFINS** no **registro F120 do EFD Contribuições**, os tipos de **ATIVO** **(Tipo Ativo (N3\_ATIVO)**: **02, 04, 05, 06, 07, 08, 09 e 10, //correspondentes a REAVALIAÇÃO e DEPRECIAÇAO ACELARADA dos bens**, conforme a **Instrução Normativa SRF n457/2004, de 18 de outubro de 2004 - DOU de 5.11.2004**As tabelas envolvidas para geração do F120 são : **SN1,SN3,SN4 e CL2.****Cálculo que o sistema efetua para depreciação:**Após o processo do **Calculo Mensal (ATF050)**, o sistema leva o valor no **campo N4\_VLROC1**. Segue a fórmula com o cálculo do **campo N4\_VLROC1.****N3\_TXDEPR1 / 12** =**(A)** Coeficiente para cálculo mensal a depreciar;  
**N3\_VORIG1 \*** **(A)** = **(B)** Valor Bruto Depreciado;  
**(B) Valor Bruto Depreciado /100 =**Valor a ser depreciado.  
  
Exemplo:   
10/12 = 0,8333  
400 \* 0,8333 =  333, 32  
333, 32/ 100: 3,33  
**N4\_VLROC1 = 3,33**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7920190583959)

Esse valor é levado para a **Apuração**, na **linha Base de Cálculo Ativo fixo - Depreciação**, da **aba Composição dos Créditos.**  
   
Cálculo **Depreciação** na **Apuração**:  
  
**(cArqAtiv)->VLRPIS      :=  (cArqAtiv)->(VLRBCPIS\*(ALIQPIS/100))**  
**(cArqAtiv)->VLRCOFINS   :=  (cArqAtiv)->(VLRBCCOFIN\*(ALIQCOFINS/100))**  
  
Exemplo:  
   
3,33\* 1,65/100 = 0,05 (valor PIS)  
3,33 \* 7,60/100 = 0,25 (valor COFINS)  
  
   
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7912175131799)

O Desenvolvimento da **TOTVS** disponibilizou uma documentação com orientação para a inclusão de Ativos que possuem depreciação ou são controlados fora do Protheus no SIGAATF.   
   
Segue *link*:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=811263527>
