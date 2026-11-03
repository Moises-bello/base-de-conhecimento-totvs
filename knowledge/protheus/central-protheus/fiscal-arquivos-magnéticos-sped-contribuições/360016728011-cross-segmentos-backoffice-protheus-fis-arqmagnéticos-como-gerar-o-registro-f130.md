---
article_id: 360016728011
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: c2d7444179bcfbafaa864da9508b59d03fce2e9dacffaadbb036b730e64130f1
fetched_at: '2026-06-28T22:42:05.003872+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar o
  registro F130 EFD Contribuições
type: support-article
updated_at: '2025-04-17T18:29:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016728011-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-o-registro-F130-EFD-Contribui%C3%A7%C3%B5es
---

**Dúvida**Como gerar o **registro F130** do **EFD Contribuições**?  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12.1.7   
  
**Solução**O **Registro F130** trata ativos **sob valor do bem (valor de aquisição)** que objetiva informar os valores de créditos apurados com base no valor da aquisição, destacando a parcela apropriada no período e as condições associadas.

Recomendamos a apuração através de **Ativos** que possuem vínculo com **Nota Fiscal** com **crédito de PIS e COFINS**, ou seja, **Ativos** que foram incluídos via **Nota Fiscal de entrada**.

**Passo 1.**Efetue o lançamento de uma **Nota Fiscal de entrada** no **Módulo Compras** e configure uma **TES (Tabela SF4)** de entrada conforme os campos abaixo:

**Atual Ativo (F4\_ATUATF)** =  Sim  
**Livro Fiscal de ICMS/ IPI =** Tributado/Outros/Isento. Para gerar as Tabelas dos Livros Fiscais **(SFT e SF3)**  
**PIS/COFINS (F4\_PISCOF)** = Ambos   
**Cred. PIS/COF (F4\_PISCRED)** = Credita  
**Sit Trib Pis (F4\_CSTPIS)**=  ?  
**Sit trib cof (F4\_CSTCOF)**= ?  
**Cod BC. CRED (F4\_CODBCC)** =10  
**Tp. Reg. (F4\_TPREG)** = ?  
  
**⚠️ Mesmo que os bens não possuam integração com o documento fiscal, os passos abaixo podem ser seguidos para geração correta do registro.****Passo 2.**   
Acesse o **Módulo 01 Ativo Fixo**, rotina **Classificação de Compras (ATFA240)**. Na classificação preencha os campos abaixo:

**Atualização de Ativos Imobilizados - Tabela SN1  
Calc. PIS (N1\_CALCPIS)** = 1-Sim ou 3 - Fração   
**Ident. Bem (N1\_DETPATR)** = ?  
**Utiliz. BEm (N1\_UTIPATR)** =? **Orig. Cred (N1\_ORIGCRD)** = 0 ou 1  
**Sit. trib. PIS (N1\_CSTPIS)** =  ? **Aliq. PIS (N1\_ALIQPIS)** = ? **Sit. Trib. Cof (N1\_CSTCOFI)** = ? **Aliq. Cofins (N1\_ALIQCOF)** = ? **Cod. BC. Cred (N1\_CODBCC)** = 10 **Base Pis/Cof (N1\_CBCPIS )** =  1- normal

Importante: Configure os campos **Calc. PIS (N1\_CALCPIS) = 3 - Fração** e **(N1\_MESCPIS)**, indica o número de meses em que deverá ser efetuado o cálculo do crédito, caso seja necessário realizar a apropriação pelo número de meses definidos por avos, exemplo: **12/24/48 (máximo de 48 meses)**

**📢️ Os campos que possuem "?" indicados nesta documentação, devem ser preenchidos de acordo com as regras de negocio de cada cliente, e não podem permanecer vazios.**

**Saldo e Valores - Tabela SN3**

**Tipo Ativo (N3\_TIPO)** = ? **Taxa depreciação  (N3\_TXDEPR1)** = ? **Conta contábil (N3\_CCONTAB)**= ?**Importante:** Esse registro é gerado **de acordo com a Classificação do Bem**.  
  
**Passo 3.**Acesse a **Rotina FISA001 e processe a Apuração do EFD Contribuições**. Na Apuração os **valores de aquisição** serão levados na aba **Composição dos Créditos** e linha **Base de cálculo Ativo Fixo** **– Aquisição**. Neste processo, é gerado a Tabela **CL2.****Passo 5.**

Gere o **Arquivo txt do EFD Contribuições** e verifique **o Registro F130.  
  
📢️ Importante:**Os valores de **créditos de PIS e COFINS** da **Nota Fiscal de entrada** que geram informações **no módulo do Ativo Fixo (SIGAATF),** não são considerados no bloco **A, C e D do arquivo txt do EFD Contribuições.** Os valores de crédito são considerados **somente no registro F130,** para que não seja gerado crédito duplicado.Não devem ser considerados para apropriação e créditos do **PIS** e da **COFINS** no registro **F130** do EFD Contribuições, os tipos de ATIVO **(Tipo Ativo (N3\_TIPO): 02, 04, 05, 06, 07, 08, 09 e 10, //correspondentes a REAVALIAÇÃO e DEPRECIAÇAO ACELARADA dos bens, conforme a Instrução Normativa SRF n457/2004, de 18 de outubro de 2004 - DOU de 5.11.2004**As tabelas envolvidas para geração do **F130** são **: SN1, SN3,SN4 e CL2.**

Vídeo completo do processo em anexo.O Desenvolvimento da **TOTVS** disponibilizou uma documentação com orientação para a inclusão de Ativos que possuem depreciação ou são controlados fora do Protheus no **SIGAATF**.

Segue *link*:

<https://tdn.totvs.com/pages/releaseview.action?pageId=811263527>
