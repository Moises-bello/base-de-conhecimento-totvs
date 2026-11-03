---
article_id: 17448867907351
category: Financeiro - Contas a Pagar
content_hash: 0e464af8d735638d5f5773170c05b4ee7e544414f0c8f325526da6b17ad03c39
fetched_at: '2026-06-28T22:38:07.105438+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - IR Simplificado
type: support-article
updated_at: '2025-10-17T20:06:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17448867907351-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-IR-Simplificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17448876911383) Tempo aproximado para leitura **08:00 min** **Dúvida**Como parametrizar IRRF de autônomo com dedução simplificada?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro REINF - Todas as versões  
  
**Solução**A Medida Provisória nº 1.171/23 que posteriormente foi convertida na Instrução Normativa nº 2.141/2023, trouxe novo cálculo do imposto de renda, que passou a vigorar a partir de 01/05/23. Trata-se da Dedução Simplificada, que é uma alternativa de dedução para definir a base do Imposto de renda, onde seu valor de R$ 607,20 corresponde a 25% sobre o teto da faixa de isenção da Tabela Progressiva do Imposto de Renda (valor baseado na tabela de 2024).  
  
Considerando o novo modelo de tributação, caberá ao responsável pelo recolhimento do IRRF verificar qual modelo de tributação será mais vantajoso (via deduções legais ou dedução simplificada).   
  
- Se o mais vantajoso para a Pessoa Física for a **Dedução simplificada**, não haverá descontado da base os valores de **Deduções legais**(INSS, Pensão alimentícia, Dependente, Previdência Privada).  
- Para os casos inversos (que foi realizada as **Deduções legais**), não pode ser utilizada a **Dedução simplificada =** R$ 607,20  
  
**Configuração**Para parametrizar o módulo **Financeiro** (**SIGAFIN**) com os novos valores e orientações do imposto de renda, realize os passos a seguir:  
  
**1.** Configure as faixas da **tabela progressiva do IRRF** com os valores vigentes: acessando pelo **Configurador** (**SIGACFG > Ambiente > Cadastros >** **Tabela IRRF**):  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32319706707223)  
  
2.** Configure através do **Configurador** (**SIGACFG**) os seguintes parâmetros:  
**MV\_FMP1171 =** .T.**MV\_FVL1171 = 607.20**

Obs: Utilizar ponto ao invés de vírgula no valor do parâmetro.  
  
**3.** No cadastro do **Fornecedor** configure os campos conforme abaixo:  
**A2\_TIPO** = F - Físico  
**A2\_CALCIRF** = 1 - Normal ou 2 - IRRF Baixa  
**A2\_IRPROG** = 1 - Sim  
**DKE\_IRSIMP** = 1 - Sim  
  
![Gravar_2024_07_26_13_45_28_513.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25195690221335)

**Importante**:

Temos um campo chamado "**IR SIMP**" DKE\_IRSIMP.

Veja se o compartilhamento da tabela (SX2) condiz com o conteúdo gravado no campo DKE\_FILIAL

**Exemplo:**

Se o sigamat possui a estrutura EEUUFF, onde seu conteúdo é 010203

EE = 2 caracteres para gravar o código da empresa

UU = 2 caracteres para gravar o código da unidade de negócio

FF = 2 caracteres para gravar o código da filial.

Ao verificar o compartilhamento na tabela SX2 da tabela DKE for:

Compartilhado por filial

Exclusivo por Unidade de negócio

Exclusivo por empresa

Logo o conteúdo gravado no campo DKE\_FILIAL deverá ser DKE\_FILIAL="0102" (não será gravado o conteúdo "03", pois neste exemplo a DKE é compartilhada por filial)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29470511618583)

**4.** No cadastro do **Natureza** configure o campo conforme abaixo:  
**ED\_CALCIRF** = S - Sim  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25195713567383)

**Saiba mais**

[IRRF de autônomo com dedução simplificada (MP 1.171/2023)](https://tdn.totvs.com/pages/releaseview.action?pageId=695202577)  
[EFD-Reinf 2.1.1 - Documento de Entrada](https://tdn.totvs.com/display/public/PROT/PCOM12065+-+EFD-Reinf+2.1.1+-+Documento+de+Entrada)
