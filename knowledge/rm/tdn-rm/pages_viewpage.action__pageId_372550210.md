---
content_hash: 97d40902ad09d2174680de46c47083b97122fba448e0bc105437d829727d6863
fetched_at: '2026-06-29T00:09:01.151883+00:00'
page_id: '372550210'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-3387 - Alteração em layouts de Importação via Conceito e Exportação
  de Movimentos via TXT.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=372550210
version: 4
---

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| **Segmento Executor:** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento | | |
| **Rotina:** | Alteração em layouts de Importação via Conceito e Exportação de Movimentos via TXT. | | |
| **Ticket:** | N/D | | |
| **Requisito (ISSUE):** | MATFATCMPCRM01-3387 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Definição da Regra de Negócio:

**Exportação (Gerador de Saídas):**

Os layouts V3 e V4 de exportação do gerador de saídas sofreram alterações/inclusão dos campos abaixo conforme o layout já utilizado na versão Delphi.

**Layout de Exportação V3:**

**Ord Campo                           Tam    Pos.Ini.  Tipo           Descricao**  
**--- ------------------------------ --- -------- ------------- --------------------------------------------------**

144 NATUREZAVOLUMES                 030     2192          CARACTER    Natureza dos Volumes   
145 VALORMERCADORIAS               020     2222          VALOR            Valor das Mercadorias   
146 CODVIATRANSPORTE                001    2242           CARACTER    Código Via de Transporte   
147 VRBASEINSSOUTRAEMPRESA 020    2243           VALOR            Base Contrib.pra INSS em outras empresas   
148 VALORDESCCONDICIONAL       020    2263           VALOR            Valor do desconto condicional   
149 VALORDESPCONDICIONAL       020    2283            VALOR           Valor do despesa condicional

**Layout de Exportação V4:**

**Ord Campo                           Tam    Pos.Ini.  Tipo           Descricao**  
**--- ------------------------------ --- -------- ------------- --------------------------------------------------**

146 NATUREZAVOLUMES                 030     2217          CARACTER    Natureza dos Volumes   
147 VALORMERCADORIAS               020     2247          VALOR            Valor das Mercadorias   
148 CODVIATRANSPORTE                001    2267           CARACTER    Código Via de Transporte   
149 VRBASEINSSOUTRAEMPRESA 020    2268           VALOR            Base Contrib.pra INSS em outras empresas   
150 VALORDESCCONDICIONAL       020    2288           VALOR            Valor do desconto condicional   
151 VALORDESPCONDICIONAL       020    2308            VALOR           Valor do despesa condicional

**Importação (Conceito):**

Na importação via conceito, os layouts "V3" e "V4" também sofreram alterações/inclusão dos campos abaixo conforme o layout já utilizado na versão Delphi.

**Conceito V3:**

**Campo                            Tam  Tipo          Descricao  
--- ------------------------------ --- -------- ------------- --------------------------------------------------**

NATUREZAVOLUMES                 030    CARACTER   (Natureza dos Volumes)  
VALORMERCADORIAS               020    VALOR           (Valor das Mercadorias)   
CODVIATRANSPORTE                001    CARACTER   (Código Via de Transporte )  
VRBASEINSSOUTRAEMPRESA 020    VALOR           (Base Contrib.pra INSS em outras empresas)

**Conceito V4:**

**Campo                            Tam  Tipo          Descricao  
--- ------------------------------ --- -------- ------------- --------------------------------------------------**

NATUREZAVOLUMES                 030    CARACTER   (Natureza dos Volumes)

VALORMERCADORIAS               020    VALOR           (Valor das Mercadorias)   
CODVIATRANSPORTE                001    CARACTER   (Código Via de Transporte )  
VRBASEINSSOUTRAEMPRESA 020    VALOR           (Base Contrib.pra INSS em outras empresas)

**OBS:** Os campos **VALORDESCCONDICIONAL** (Valor do desconto condicional) e **VALORDESPCONDICIONAL** (Valor do despesa condicional) não foram inclusos no conceito por se tratarem de campos calculados. Os valores para este estes campos serão calculados e inseridos na base de acordo com a formula informada nos parâmetros do tipo de movimento utilizado, etapa 13 (Mov. Valores Financeiros 2/4).
