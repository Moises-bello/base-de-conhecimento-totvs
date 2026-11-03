---
content_hash: 76eacd918fb55d5d344e59e1306ea89310753387c3e6daccfd47d7698bed5ba5
fetched_at: '2026-06-29T00:08:55.891068+00:00'
page_id: '351020944'
product: rm
source: tdn-rm
title: 2531072 MATFATCMPCRM01-3055 DT Bilhetes de Passagens Eletrônicos (BP-e)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=351020944
version: 1
---

# BP-e Bilhetes de Passagens Eletrônicos

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Movimento | MovMovimentoBaseAction | |
| **Cadastros Iniciais:** | Movimento |
| **Parâmetro(s):** | Parametrização por tipo de movimento:  Etapa 'Fis - Escrituração', Grupo 'Tipo Documento Escrituração' - Código Default - Outros Códigos  Etapa 'Fis - Conhecimento de Transporte' - Tipo de Operação do Conhecimento de Transporte |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | 2531072 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-3055 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQLServer e Oracle |
| **Tabelas Utilizadas:** | TMOV e TMOVTRANSP |
| **Sistema(s) Operacional(is):** | Windows |

## Objetivo

Criação de alguns campos no movimento para possibilitar a geração dos Bilhetes de Passagens Eletrônicos (BP-e), os quais serão utilizados para a geração do registro D100 no SPED.

**O que foi modificado**

* Foi criada uma consistência que impede a parametrização do tipo de movimento quando o mesmo for '2.x.xx', o campo **Código Default** e/ou o campo **Outros Códigos** do GroupBox **Tipo Documento Escrituração** (TTMVEXT.CODTDO e TTMVTIPODOC.CODTDO) possuir tipo de documento com CODMODDOC = 63 e o parâmetro **Tipo de Operação do Conhecimento de Transporte**(TITMTMV.USARCTRC) for diferente de Não Usar CTRC.

* Na tela de edição de movimento do tipo **2.x.xx**, quando o campo **Tipo de Documento** (TMOV.CODTDO) estiver preenchido com um tipo de documento com CODMODDOC = 63, em **Transporte | Identificação**, será apresentado o campo **Tipo BP-e**, o qual contém as seguintes opções: 0 - BP-e normal; 3 - BP-e substituição.  
    
  Em **Integrações**, será apresentada a aba **BP-e** e nessa tela será exibido o campo **Chave de Acesso do BP-e**, em que deverá ser informada a chave de acesso do BP-e.

* Na tela de edição de movimento do tipo **1.x.xx**, quando o campo **Tipo de Documento** (TMOV.CODTDO) estiver preenchido com um tipo de documento com CODMODDOC = 63, em **Integrações**, será exibida a aba **BP-e** e nessa tela deverá ser apresentado o campo **Chave de Acesso do BP-e**, em que deverá ser informada a chave de acesso do BP-e.

**Descrição da parametrização**

Para inclusão de BP-e de entrada ou de saída, os tipos de movimento devem ter o parâmetro CIF / FOB / Terceiros do GroupBox Tipo de Frete diferente de Não Edita e ter no campo Código Default e/ou no campo Outros Códigos do GroupBox Tipo Documento Escrituração um tipo de documento com Código do Modelo do Documento = 63.

Para BP-e de saída, o cliente deverá parametrizar dois tipos de movimentos, sendo que um será para a inclusão de BP-e do tipo normal e outro para inclusão do BP-e Substituto. Neste último deverá parametrizá-lo para utilizar Cópia por Referência, motivo 17.

Demais parametrizações são as mesmas parametrizações de uma NF de Saída normal.
