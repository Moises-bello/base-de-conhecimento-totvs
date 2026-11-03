---
content_hash: a1f9a84b94bf9c4aa6c8641ed044e20b379c2e511e33a808ea3a33d5a5fc5011
fetched_at: '2026-06-29T00:11:06.838406+00:00'
page_id: '635552464'
product: rm
source: tdn-rm
title: FISCAL01-16449 - R-2055 Campo CPF
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-16449+-+R-2055+Campo+CPF
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16449 |

## **02. SITUAÇÃO/REQUISITO**

Em Base exemplo realizamos a geração do evento R-2055, com um cliente pessoa física situado no estado de São Paulo, que possui CNPJ informado no campo CPF/CNPJ do cadastro do cliente/fornecedor.

Ao gerar o evento R-2055 e tentar transmitir, ocorre o seguinte erro:  
Falha ao processar o evento de identificador 367 e tipo R-2055: O evento foi rejeitado, pelo(s) seguinte(s) motivo(s):  
Código MS1451: Indicativo de aquisição inválido para o tipo de contribuinte informado. Para Pessoa Jurídica, o tipo de aquisição deve ser igual a 3 ou 6.

* Campo: indAquis - XPATH: /Reinf/evtAqProd/infoAquisProd/ideEstabAdquir/ideProdutor/detAquis/indAquis  
  TESTES REALIZADOS

## **03. SOLUÇÃO.**

Conforme Legislação CAT 45 21/08/2008, os Produtores Rurais do Estado de SP pode ter o CNPJ para a  
Emissão da NFe e para a REINF deve ser utilizado o CPF.  
Vamos utilizar o Campo CPF criado para o eSocial - No cadastro do Cliente\Fornecedor – Anexo – eSocial –  
CFP  
Este campo somente é habilitado para o Estado SP – Categoria igual a Pessoa Física – CNPJ e Produtor Rural.  
Se o Cliente\Fornecedor for Pessoa Física, com CNPJ e Produtor Rural, as Tags tpInscAdq e nrInscAdq, deve ser  
gerado conforme:  
**<tpInscProd>** Tipo de inscrição do produtor:  
1 - CNPJ;  
2 - CPF.

**<nrInscProd>** tag número do documento.  
Deve ser gerada com o CPF informado no cadastro do Cliente\Fornecedor – Anexo – eSocial – CPF  
(PESOCIALCLIFOR.CPF)
