---
content_hash: c5500749b203b39c8329122b2ee816b64644086c4ade3b9d7e77cb97ecdd9e57
fetched_at: '2026-06-29T00:09:10.967529+00:00'
page_id: '403739969'
product: rm
source: tdn-rm
title: FISCAL01-6209 DT - SPED FISCAL - Geração do Registro C173
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403739969
version: 2
---

# Sped Fiscal - Geração do Registro C173

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Geração do Arquivo Sped Fiscal |
| **Situação/Requisito:** | Na geração do registro C173 do SPED FISCAL deve ser feito a mesma consistência do grupo de Medicamentos da NF-e 4.00, onde não será realizada consistência de acordo com os NCM's 3003 e 3004. |
| **Solução/Implementação:** | Alterada a geração do Registro  C173: OPERAÇÕES COM MEDICAMENTOS (CÓDIGO 01 e 55), onde será realizado as seguintes consistências:  - O parâmetro "Produto Sujeito a Regulações Sanitárias" deve ser marcado no Cadastro do Produto, Anexo Dados Fiscais do Produto, pasta Tributação.  - Será gerado para Produtos Controlados por Lote e que esteja com Registro da Anvisa Preenchido no Cadastro Produto, (Anexo do Saúde ou Dados do Produto Aba Integração).  Obs.: Não será mais verificado se o Produto utiliza NCM's pertencentes aos grupos de NCM 3003 e 3004. |
