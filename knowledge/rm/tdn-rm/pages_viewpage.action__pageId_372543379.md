---
content_hash: 6bf11be55c84b083ad5b004de89e3ac6f1ae90967dd0924097dfb0562b6a63f3
fetched_at: '2026-06-29T00:09:01.095545+00:00'
page_id: '372543379'
product: rm
source: tdn-rm
title: 3006762 FISCAL01-4946 DT Geração do registro T003 da REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372543379
version: 2
---

# Geração do registro T003 da REINF para Transportadoras de despacho

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Totvs Gestão Fiscal |
| **Função:** | Integração RM x TAF |
| **Situação/Requisito:** | INTERPRETAÇÃO DA DEMANDA Ao integrar o registro T013 referente a NF 222222 (cod. mod. doc. 08) foi apresentado a seguinte mensagem:  Erro 4 - Linha: 2 O valor '01' informado na coluna 8 para o campo Id. Participante Red. ( C3F\_CPARRE ) não existe na base de dados.  TESTES REALIZADOS Foi incluído o lançamento fiscal de saída nº 222222 (IDLAFAGRUP 53)- 06/06/2016, co código modelo de documento 08.  A aba Transporte / Remetente Destinatário foi preenchida com a transportadora 01.  De acordo com o layout único do TAF a transportadora preencherá o campo 08 COD\_PART\_RED do registro T013, o código da transportadora utilizado deve ser o mesmo Código do participante (campo 02 do Registro T003).  Essa informação será utilizada para geração do registro D130 - campo 3 COD\_PART\_RED - Sped Fiscal.  De acordo com o Sped Fiscal o campo 3 refere-se ao Código do participante (campo 02 do Registro 0150).  Geramos o Sped Fiscal no RM e verificamos que foi gerado o 0150 para o cadastro da transportadora.  Para que a NF seja integrada ao TAF com sucesso, o cadastro da transportadora deve gerar um registro T003. |
| **Solução/Implementação:** | Foi alterado o processo de geração dos registros de integração com TAF para que a transportadora de despacho passe a ser gerada no registro T003 |
