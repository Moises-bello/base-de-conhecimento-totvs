---
content_hash: cc269e7ff2e21a7215a2f66a411c9891b90a6bf46cdb78832a169fc814a84892
fetched_at: '2026-06-29T00:10:22.522173+00:00'
page_id: '496818172'
product: rm
source: tdn-rm
title: 5121300 FISCAL01-8109 DT Gerador de Saída - SEF II ICMS LA Registro E020
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496818172
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Gerador de Saídas |
| Ticket: | 5121300 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8109 |

## **02. SITUAÇÃO/REQUISITO**

Na geração do SEFII o arquivo ICMS-LA não gera as numerações inutilizadas para os modelos 55 e 65.

## **03. SOLUÇÃO**

Foi alterado o Layout SEF II - ICMS LA, nesta rotina foi implementado a geração de NFe e NFCe Inutilizadas, para o \_Layout SEF II - ICMS LA (\_registro E020 e E025). Para ser gerado, vá em Filial -> Anexos -> Nfe/NFCe Inutilizadas,e cadastre as notas Inutilizadas.

Para o Layout SEF II eDOC(registro C020), segundo a Sefaz PE, no eDOC não deve ser informado notas inutilizadas, conforme legislação:

*"As notas fiscais canceladas, denegadas e as relativas ao desfazimento do negócio devem ser registradas*  
*no eDOC 2012 conforme foram emitidas. No caso das notas fiscais inutilizadas, estas não devem ser*  
*informadas no eDOC 2012, visto que não houve emissão de notas fiscais, mas apenas inutilização da*  
*numeração das notas fiscais. Esta informação será registrada no SEF 2012.*  
*Os contribuintes que utilizarem o processo de migração do SEF 2003 para o eDOC 2012 não conseguirão*  
*trazer os dados relativos às notas canceladas ou denegadas. Estas devem ser digitadas manualmente ou*  
*importadas diretamente do sistema de gestão do contribuinte.*  
*A regra prevista no artigo 129-A, inciso IX do Decreto n° 14.876/1991, que dispõe que as notas fiscais*  
*canceladas, denegadas e os números inutilizados devem ser lançados sem valores monetários, de acordo*  
*com as regras gerais de escrituração, aplica-se ao SEF e não ao eDOC 2012, pois estas são normas de*  
*escrituração fiscal e o eDOC 2012 não trata de livro fiscal, mas de registro de documentos fiscais."*

Disponível em:  <https://www.sefaz.pe.gov.br/Publicacoes/Manuais%20de%20Duvidas%20Tributrias%20%20Informativos%20Fiscai/SEF%202012%20e%20eDOC%202012.pdf>
