---
content_hash: 011fafa4a58d6e85db4f6e957fc52991f778ac33fc97b5074a2f62a1208e3259
fetched_at: '2026-06-29T00:11:03.273945+00:00'
page_id: '620544156'
product: rm
source: tdn-rm
title: RMFIS00006_DES Contagem
type: documentation
url: https://tdn.totvs.com/display/LRM/RMFIS00006_DES+Contagem
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Gestão Fiscal                      **Versão:** 12.1 |
| **Processo** | **:** | DES Contagem |
| **Subprocesso** | **:** |  |
| **Data da publicação** | **:** |  |

# **Introdução**

O objetivo deste documento é oferecer uma visão geral a respeito da **Declaração Eletrônica de Serviços** – DES e os processos necessários no sistema de Gestão Fiscal para geração do arquivo para posterior importação no programa da Prefeitura.  
   
**Regras Gerais**

Registro H - Dados do Contribuinte

Esse Registro é preenchido de acordo com as informações da Filial declarante.

Registro N - Dados das Notas

Para a geração das linhas referentes às notas fiscais recebidas ou emitidas, o sistema estará selecionando os Lançamentos Fiscais da coligada corrente e filial selecionada na tela da rotina. A Data LF deverá se encontrar dentro do período informado na tela da rotina.

Não serão selecionados Lançamentos Fiscais estornados ou para Estado. Além disso, os Lançamentos Fiscais devem possuir, em pelo menos uma das parcelas, um item do tipo Serviço.

Tipo: (N)F e (R)PA: para o preenchimento deste campo o sistema estará selecionando o Modelo ISS correspondente ao Tipo de Documento associado ao Lançamento Fiscal. Este Modelo ISS deverá ser informado em Opções / Parâmetros / Gerais / Tabelas. Para a filial selecionada deverá ser informado para cada tipo de documento o Modelo ISS correspondente: N ou R. Se não existir Modelo ISS associado ao Tipo de Documento da NF, o sistema estará preenchendo o valor "N".

CNPJ: o sistema estará preenchendo este campo com o CNPJ/CPF do emitente ou destinatário. Se o Lançamento Fiscal for do tipo Empresa, o sistema estará considerando o CNPJ/CPF da filial associada.

Valor Bruto da NF: valor contábil total da NF, incluindo todas as parcelas, se o Lançamento Fiscal for parcelado.

Tipo de Recolhimento: para o preenchimento deste campo, o sistema estará utilizando o campo Tipo Recolhimento, dos Outros Tributos do tipo ISS. Se existirem mais de um tributo do tipo ISS no Lançamento Fiscal, o sistema estará considerando o Tipo Recolhimento do último tributo encontrado.

(C): este valor será preenchido neste campo se a NF é cancelada.

(M): Para o Município do Prestador de Serviço diferente do município da Filial, o sistema estará preenchendo o campo Tipo de Recolhimento com o Valor igual a M.

As opções abaixo somente serão válidas quando o Município do Prestador de Serviço for igual ao município da Filial.

Observação: O Município do Prestador de Serviço corresponde ao valor do campo Código Município, localizado na subpasta Prestação Serviços da pasta Outros Dados. Trata-se do município onde o serviço é devido.

(O): se o Tipo Recolhimento associado ao tributo é ISS Devido e a NF é de Entrada, este será o valor deste campo.

(P): se o Tipo Recolhimento associado ao tributo é ISS Devido e a NF é de Saída, este será o valor deste campo.

(I): se o Tipo Recolhimento associado ao tributo é ISS Isento, este será o valor deste campo.

(S) ou (F): se o Tipo Recolhimento associado ao tributo é ISS Retido Fonte ou ISS Retido Fonte Deduzido, o sistema estará preenchendo o campo Tipo de Recolhimento da GIPS com estes valores nas seguintes condições:

(S): município do Cliente/Fornecedor ou Empresa é igual ao município da filial selecionada.

(F): município do Cliente/Fornecedor ou Empresa é diferente do município da filial selecionada.

Se não existir movimentação de entrada ou saída, será gerada uma linha N correspondente ao tipo de movimento, com o tipo de recolhimento (Z): sem movimentação.

Não será gerado o tipo de recolhimento (A): Avulsa.

Observação: Se o lançamento fiscal não se enquadrar em nenhuma das opções acima, o sistema estará preenchendo o campo Tipo de Recolhimento com o Valor igual a (O).

Registro I - Itens Notas

Código da Atividade: preenchido conforme o campo Código Serviço da pasta Outros Dados | Prestação Serviços do Lançamento Fiscal.

Alíquota da Atividade: preenchida conforme Alíquota informada na Pasta Outros Tributos do Lançamento Fiscal.

Valor da Base de Cálculo do Item: preenchido com a quantidade x preço do Item do tipo serviço.

Linha T - Trailer

Registro totalizador.
