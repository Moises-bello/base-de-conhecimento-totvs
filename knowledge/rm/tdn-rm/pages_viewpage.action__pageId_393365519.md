---
content_hash: e347abfd3b679f61a1b280d6a883601e5c07ba75f8e44cb8c1a241493ecb7c09
fetched_at: '2026-06-29T00:09:09.719258+00:00'
page_id: '393365519'
product: rm
source: tdn-rm
title: 3542230 FISCAL01-6173 DT NF-e Produtos com NCM 3003 e 3004 não regulamentados
  pela ANVISA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=393365519
version: 1
---

# Produtos com NCM 3003 e 3004 não regulamentados pela ANVISA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Envio de NF-e |
| **Situação/Requisito:** | O cliente necessita enviar notas fiscais com alguns produtos que não são regulamentados pela ANVISA,  porém utilizam NCM's pertencentes aos grupos de NCM 3003 e 3004 como(30049099, 30043999, 30049062).  Atualmente o ERP realiza a seguinte validação:  Se o produto possui NCM no grupo 3003 e 3004, logo o código da ANVISA deve ser preenchido. |
| **Solução/Implementação:** | Alterada a forma de identificar o Produto Tipo Medicamento no Envio da NF-e 4.00, agora o Grupo de Medicamento apenas será gerado para Produtos Controlados por Lote e que estejam com Registro da Anvisa Preenchido no Cadastro Produto, (Anexo do Saúde ou Dados do Produto Aba Integração)  Obs.: Não será mais verificado se o Produto utiliza NCM's pertencentes aos grupos de NCM 3003 e 3004.  Obs.: O grupo de rastro e Obrigatório para Produto tipo Medicamento. para  gerar este grupo deve estar marcado o parâmetro "produto sujeito a regulações Sanitárias" |
