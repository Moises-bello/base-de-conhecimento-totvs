---
content_hash: ac0e1916eb71c229b9fb0f09061ccb3fe4e3eb196552132f67fdae8b0182df4c
fetched_at: '2026-06-29T00:09:10.064385+00:00'
page_id: '397377661'
product: rm
source: tdn-rm
title: 3365600 FISCAL01-6159 DT NF-e DIFAL - Gerar o grupo de partilha de ICMS na
  devolução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=397377661
version: 11
---

# NF-e DIFAL - Gerar o grupo de partilha de ICMS na devolução

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Envio de NF-e |
| **Situação/Requisito:** | Devolução de Venda Consumidor Final com DIfal.  É necessário gerar o Grupo B de Tributação do ICMS para a UF de destino para NFe de Devolução (Devolução de Venda – NF-e Entrada – Emissão Própria). Os Cálculos destas Tags devem ser igual aos Cálculos realizados nas Operações de Saída com DIFAL. |
| **Solução/Implementação:** | Foi modificado o processo de geração da NF-e de devolução para gerar o grupo de partilha do ICMS nas operações de devolução de saídas que incidiram o imposto.  Para gerar o grupo devem ser consideradas as seguintes parametrizações:  1- O movimento de devolução precisa ser criado através do processo de cópia por referência utilizando o motivo "Devolução de Venda de Mercadorias"  2- A regra de ICMS da CFOP de devolução precisa ser igual a regra de ICMS da CFOP da venda. Exceto o percentual da partilha.  3- O Percentual da partilha da regra de ICMS da CFOP de devolução precisa ser o inverso do percentual utilizado na CFOP da venda. Exemplo: Se a venda for com 80% a devolução precisa ser 20%.  4- No movimento de devolução precisa ser informado que é uma operação com Consumidor Final.  **NOTA FISCAL ELETRÔNICA**  Exemplo de XML gerado: xmlVenda MG ==> RJ 500.00 500.00 2.00 18.00 12.00 80.00 10.00 24.00 6.00 ]]> **Na Venda**   ``` <vICMSUFDest>24.00</vICMSUFDest> RJ <vICMSUFRemet>6.00</vICMSUFRemet> MG ```  xmlDevolução de Venda RJ ==> MG 500.00 500.00 2.00 18.00 12.00 80.00 10.00 6.00 24.00 ]]> **Na devolução**   ``` <vICMSUFDest>6.00</vICMSUFDest> MG <vICMSUFRemet>24.00</vICMSUFRemet> RJ ```   Apesar da regra de ICMS está preenchida com o percentual de 20% o XML será gerado com 80%, pois a SEFAZ exige este valor. Conforme o  ["Parecer Consultoria Tributária Segmentos - EC 87-2015 - Difal Notas de Devolução"](http://tdn.totvs.com/pages/viewpage.action?pageId=224104756)  os campos referente ao FECP serão gerados iguais ao XML da venda.  **LANÇAMENTO FISCAL**  Após a escrituração os valores serão apresentados no lançamento conforme abaixo.  **Venda:**    **Devolução:**    **APURAÇÃO** |
