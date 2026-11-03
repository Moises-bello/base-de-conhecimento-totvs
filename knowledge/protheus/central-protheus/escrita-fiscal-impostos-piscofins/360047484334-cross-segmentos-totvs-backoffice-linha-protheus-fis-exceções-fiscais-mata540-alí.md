---
article_id: 360047484334
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 5b599216e0937e26bd9736e89f25293abb28d5b86be3df627c1ce2d4e11cefbf
fetched_at: '2026-06-28T22:39:36.944281+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Exceções fiscais
  (MATA540) - Alíquotas de PIS/COFINS para notas de importação
type: support-article
updated_at: '2021-06-22T13:52:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047484334-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Exce%C3%A7%C3%B5es-fiscais-MATA540-Al%C3%ADquotas-de-PIS-COFINS-para-notas-de-importa%C3%A7%C3%A3o
---

**Dúvida**Como cadastrar as alíquotas de Pis/Cofins para as notas de importação através da rotina de Exceções Fiscais?  
  
**Ambiente**Protheus - Fiscal - Todas as versões.

**Solução**

No módulo Fiscal acessar Atualizações/ Cadastros/ Exceções Fiscais (MATA540).

**1- Cadastro das Exceções Fiscais.**

Grupo de Trib. (F7\_GRTRIB) = O código preenchido nesse campo deverá ser informado no cadastro do produto através do campo Grp. Trib. (B1\_GRTRIB).

Obs.: para a inclusão de novos códigos acessar a tabela 21 do configurador.

Estado (F7\_EST) = EX

Tipo (F7\_TIPOCLI) = Todos

Aliq. Pis (F7\_ALIQPIS) = Definir a alíquota do Pis importação (2,10 por exemplo)

Aliq. Cof. (F7\_ALIQCOF) = Definir a alíquota do Cofins importação (9,65 por exemplo - nesse campo não deverá considerar a alíquota majorada).

Obs.: a alíquota majorada do Cofins deverá ser informada no cadastro da tes no campo Aliq. COF M. (F4\_MALQCOF).

GRP. Cli/For (F7\_GRPCLI) = Esse campo não é de preenchimento obrigatório para validar a exceção fiscal, porém caso ele seja preenchido o mesmo conteúdo deverá ser informado no cadastro do fornecedor através do campo Grp. Tribut (A2\_GRPTRIB).

UF Busca (F7\_UFBUSCA) = Origem

**2 - Cadastro do Produto.**

Amarrar a Exceção Fiscal ao cadastro do produto através do campo Grupo Trib. (B1\_GRTRIB).

Nesse campo deverá ser informado o grupo de tributação cadastrado no campo GRUPO (F7\_GRTRIB) da exceção fiscal.

**3 – Cadastro do Fornecedor**

Quando é cadastrado algum código no campo Grp. Cli/For (F7\_GRPCLI), esse mesmo código deverá ser vinculado no campo Grp. Tribut (A2\_GRPTRIB).

Lembrado que os campos F7\_GRPCLI e A2\_GRPTRIB devem estar com o mesmo conteúdo (ambos em branco ou ambos preenchidos com o mesmo código).

**4 - Verifique no configurador se o tamanho campos abaixo estão corretos:**

 Obs.: Se o tamanho de algum deles estiver diferente, a exceção fiscal não será aplicada corretamente.

F7\_GRTRIB = CARACTER, 6

F7\_GRPCLI = CARACTER, 3

A1\_GRPTRIB = CARACTER, 3

A2\_GRPTRIB = CARACTER, 3

B1\_GRTRIB = CARACTER, 6
