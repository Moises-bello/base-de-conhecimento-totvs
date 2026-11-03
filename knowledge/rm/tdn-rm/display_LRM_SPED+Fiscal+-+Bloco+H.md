---
content_hash: 109ea03de9c1280e318955eefca503f51f1bba7cb51cb93784f7cbacb6fea467
fetched_at: '2026-06-29T00:09:19.617269+00:00'
page_id: '422545624'
product: rm
source: tdn-rm
title: SPED Fiscal - Bloco H
type: documentation
url: https://tdn.totvs.com/display/LRM/SPED+Fiscal+-+Bloco+H
version: 24
---

Este bloco é composto pelos registros:

BLOCOHleftH005H005

**Totais do Inventário**

Este registro deve ser apresentado para discriminar os valores totais do inventário por itens/produtos existentes à data do balanço. Se a escrituração se referir ao mês de fevereiro, este registro deve obrigatoriamente ser informado. Neste caso, os dados apresentados devem considerar a posição em 31 de dezembro do exercício anterior. Em outros meses, pode ou não ser informado, conforme previsão legal da obrigação de inventariar o estoque.

Quando a flag "Ressarcimento/Complemento ICMS-ST" estiver marcada, o campo 04  (Motivo de Referência) será gerado com o código 6 (Para controle das mercadorias sujeitas ao regime de substituição tributária – restituição/ ressarcimento/ complementação).

H010H010

**Inventário**

Este registro deve ser informado para discriminar os itens existentes no estoque. Este registro não pode ser fornecido se o campo 03 (VL\_INV) do registro H005 for igual a "0" (zero).

**Campo 05 - (VL\_UNIT) Valor unitário do item**

Este campo apresentará o custo média da filial, conforme regra abaixo:

* O sistema verifica o Saldo da Filial (TRELSLD.SALDOFILIAL):  
  Se ele for maior que 0 (zero), divide o valor total da filial (TRELSLD.TOTALFILIAL) pela quantidade (saldo) da Filial (TRELSLD.SALDOFILIAL).  
  Se ele for menor ou igual a zero, gera o campo com 0 (zero).

**Campo 11 - (VL\_ITEM\_IR) Valor do item utilizando os critérios previstos na legislação do Imposto de Renda.**

O VL\_ITEM\_IR verifica os campos TOTALMOVAJUSTADOITEM, quando não utiliza "Custo por Filial" e TOTALFILIALAJUSTADOIR, quando utiliza o "Custo por Filial". Porém estes campos só são preenchidos pelo processo de "[Situação Estoque](https://tdn.totvs.com/pages/releaseview.action?pageId=422546131)", processo este que é utilizado quando os clientes não possuem o Totvs Gestão de Estoque, Compras e Faturamento e precisam inserir os valores diretamente através de um XML.

Quando os clientes possuem o Totvs Gestão de Estoque, Compras e Faturamento o campo será preenchido com a mesma regra do VL\_UNIT.

H020H020

## **Informação complementar do Inventário**

Este registro deve ser preenchido para complementar as informações do inventário, quando o campo MOT\_INV (Campo localizado na tela de geração do Sped Fiscal) do registro H005 for de "02" a "05". Não deve ser informado, se o campo 03 (VL\_INV) do registro H005 for igual a "0" (zero).

No caso de mudança da forma de tributação do ICMS da mercadoria (MOT\_INV=2 do H005), somente deverá ser gerado esse registro para os itens que sofreram alteração da tributação do ICMS.

O Registro H020 será gerado com as informações da tela "Dados Fiscais por UF" que fica localizada no Cadastro do Produto, menu ANEXOS > DADOS FISCAIS POR UF.

Na tela de geração da rotina caso selecione a opção 02 no Motivo do Inventário (mudança da forma de tributação da mercadoria de ICMS) somente serão gerados os registros H010 e H020 para os produtos que sofreram alteração da Tributação de ICMS. Para identificação desses produtos será necessário verificar se houve alteração nos campos "CST Produto", "Alíquota Interna de ICMS", "Tributado pelo ICMS-ST" e "Modalidade de Determ. da BC do ICMSST" e se o Fim da Vigência no Log de Alteração do Anexo Produto por UF foi no Mês anterior a data do Inventário da Geração da Rotina.

Quando se escolhe o motivo inventário 02, a Data do Inventário na Parametrização do Sped Fiscal deve ser igual a Data do Fim do Período Parametrizada.

Para os outros Motivos 01, 03, 04 e 05 o sistema irá buscar os Logs conforme a Data do Inventário (Verificando se existe registro com Data de inventário dentro do Início e Fim da Vigência do Log). Caso exista log para o Produto o sistema irá gerar o registro com o CST e a Alíquota baseado no Log, caso não exista log será  Baseado no Cadastro de Produto Fiscal por UF.

A partir da versão 12.1.21 da Biblioteca RM foi disponibilizado o parâmetro "**Gerar Registro: H020**" localizado na aba Dados do Inventário, onde o registro H020 passa a ser gerado quando o mesmo estiver habilitado, ficando a cargo do usuário definir se o registro deve ser gerado ou não no arquivo do Sped Fiscal. Esta alteração se fez necessária para suprir demanda do Estado do Rio Grande do Sul na GIA RS.

## **H020 -  Ressarcimento ICMS ST.**

Na aba Dados do Inventário foi implementado o parâmetro **Gerar Estoque - Ressarcimento ICMS ST**.

Este parâmetro será exibido quando for selecionado o Motivo do Inventário 1 ou Motivo do Inventário 2:  for igual a **"Por determinação do Fisco"**.

**Observação:** Será possível gerar o Inventário 2 com H020 referente às informações do ICMS-ST e o inventário 1 ser gerado normalmente com as informações do ICMS.

Sempre que o parâmetro **"Gerar Estoque - Ressarcimento ICMS ST"** estiver habilitado o registro H020 será gerado com informação do ICMS-ST se for encontrado lançamento de entrada do produto em questão conforme as regras de seleção abaixo.

Seleção dos Lançamentos Fiscais para recuperar os valores da Base de Cálculo do ICMS ST e Valor do ICMS + Valor do ICMS ST:

**Tipo de Lançamento:** Entrada  
**Status do Lançamento**: Normal  
**Data do Lançamento:** Menor ou igual a Data do Inventário  
**Tipo Natureza:** Não seja de Devolução  
**Valor de ICMS ST:** Tenha valor do ICMS ST no item  
**Produto tributo pelo ICMS-ST:** O produto deve ser tributado pelo ICMS-ST com data igual ou anterior a data parametrizada do inventário. Cadastro do produto > Anexos > Dados Fiscais por UF.  
**Seleção de Lançamento:** Será selecionado o lançamento fiscal mais recente.

H030H030

**Informações Complementares do Inventário das Mercadorias sujeitas ao regime de Substituição Tributária**

Este registro é obrigatório quando o Motivo do Inventário for igual “06” (Para controle das mercadorias sujeitas ao regime de substituição tributária – restituição/ ressarcimento/ complementação).  
Quando a quantidade total de produtos tiverem saída no mesmo mês de entrada no estoque este registro será gerado com os valores zerados.

**Campo 02** (VL\_ICMS\_OP) - Informar o valor médio unitário do ICMS OP a que o informante teria direito ao crédito, pelas entradas, caso a mercadoria não estivesse sujeita ao regime de substituição tributária, ou seja, caso esta fosse submetida ao regime comum de tributação. (DITEM.VLRICMSPRD / H010.QTD)

**Campo 03** (VL\_BC\_ICMS\_ST) - Informar o valor médio unitário da base de cálculo ICMS ST pago ou retido, considerando redução de base de cálculo, se houver (DITEM.BASEICMSSTPRD / H010.QTD)

**Campo 04** (VL\_ICMS\_ST) - Informar o valor médio unitário do ICMS ST pago ou retido limitado à parcela do ICMS ST correspondente ao fato gerador presumido que ainda não se realizou. Quando a mercadoria estiver sujeita, também, ao FCP adicionado ao ICMS ST, neste campo deve ser informado o valor médio unitário total da parcela do ICMS ST + a parcela do FCP vinculado a este.  (DITEM.VLRICMSSTPRD / H010.QTD)

**Campo 05** (VL\_FCP) -: Informar o valor médio unitário da parcela do FCP adicionado ao ICMS que tenha sido informado no campo “VL\_ICMS\_ST”. (DITEM.VLRICMSITEMFCPESTDEST/ H010.QTD)

Quando são gerados os registros C180, C185 automaticamente o sistema ira gerar um registro H005 com Motivo "06", H010 e H030 dos produtos que houveram movimentação.
