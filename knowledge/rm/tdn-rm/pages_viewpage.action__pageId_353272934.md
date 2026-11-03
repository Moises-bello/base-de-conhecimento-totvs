---
content_hash: d16f92283095577d3f646b2e25119abfd721c3b3376a47400101b05d40081eb3
fetched_at: '2026-06-29T00:08:57.048110+00:00'
page_id: '353272934'
product: rm
source: tdn-rm
title: 1926438 MATFATCMPCRM01-2539 DT DataServer do Quadro Comparativo da Cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=353272934
version: 2
---

# DataServer do Quadro comparativo da Cotação

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | DataServer do Quadro Comparativo | CmpQuadroComparativoTBCData | |
| **Cadastros Iniciais:** | N/A |
| **Parâmetro(s):** | N/A |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | 1926438 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQLServer e Oracle |
| **Tabelas Utilizadas:** | TCITMORCAMENTO, TCCOTACAO, TPRODUTO, TCORCAMENTO e TMARCA |
| **Sistema(s) Operacional(is):** | Windows |

## Descrição

Implementação realizada com o objetivo de permitir que o serviço ReadView possa ser utilizado no DataServer do Quadro comparativo da cotação.

## Procedimento para utilização

**DataServer**: CmpQuadroComparativoTBCData  
**Filtro**: Filtro no padrão SQL  
**Contexto**: Contexto do sistema. Obrigatórios são: Coligada, Usuário e Sistema.

**Exemplo**:

**Padrão do XML:**

<soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
        <soapenv:Header/>  
         <soapenv:Body>  
                 <tot:ReadView>  
                         <!--Optional:-->  
                         <tot:DataServerName>CmpQuadroComparativoTBCData</tot:DataServerName>  
                         <!--Optional:-->  
                         <tot:Filtro>CODCOLIGADA = 1 AND CODCOTACAO='2011.000002'  
                         </tot:Filtro>  
                         <!--Optional:-->  
                         <tot:Contexto>CODCOLIGADA=1;USUARIO=mestre;SISTEMA=T</tot:Contexto>  
                 </tot:ReadView>  
        </soapenv:Body>  
</soapenv:Envelope>
