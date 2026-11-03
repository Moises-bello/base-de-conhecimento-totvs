---
content_hash: 2eeaa5d76d34295a37f341e1b00ed1f278c729faef0c6302e0585fc27b3d52a4
fetched_at: '2026-06-29T00:11:40.422536+00:00'
page_id: '794389448'
product: rm
source: tdn-rm
title: Layout Importação de Patrimônio com Campo Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=794389448
version: 3
---

Atenção

Este recurso está disponível a partir da versão 12.1.2310.

**Patrimônio (I)**  
Os campos devem ser informados utilizando o separador **;** "ponto e vírgula".

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Ordem** | **Descrição** | **Tipo** | **Obrigatório** | **Observação** |
| **1** | Identificador de Patrimônio | Char | X | O identificador é letra **I** |
| **2** | Código do Patrimônio | Alfanumérico | X |  |
| **3** | Código do Grupo de Patrimônio | Alfanumérico | X |  |
| **4** | Tipo Patrimônio | Numérico | X | 0 = Bem; 2 = Bens de Terceiros |
| **5** | Ativo | Numérico | X | Não = 0; Sim = 1 |
| **6** | Descrição | Alfanumérico | X |  |
| **7** | Reavaliação | Numérico | x | 1 = Sim; 0 = Não |
| **8** | Data da Aquisição | Data | X | DD/MM/YYYY |
| **9** | Valor de Aquisição | Numérico(15,2) | X |  |
| **10** | Código do Patrimônio Agregador | Alfanumérico |  |  |
| **11** | Nº do Patrimônio | Alfanumérico |  |  |
| **12** | Quantidade | Numérico(15,4) |  |  |
| **13** | Unidade | Alfanumérico |  |  |
| **14** | Código do Fornecedor | Alfanumérico |  |  |
| **15** | Observações | MEMO(text) |  |  |
| **16** | Código de Barra | Alfanumérico |  |  |
| **17** | Tipo de Documento | Alfanumérico |  |  |
| **18** | Série do Documento | Alfanumérico |  |  |
| **19** | Número do Documento | Alfanumérico |  |  |
| **20** | Código da Filial | Numérico | X |  |
| **21** | Código do Centro de Custo | Alfanumérico | X |  |
| **22** | Código do Responsável | Alfanumérico |  |  |
| **23** | Chapa | Alfanumérico |  |  |
| **24** | Código do Departamento | Alfanumérico |  |  |
| **25** | Código Local | Alfanumérico |  |  |
| **26** | Contabilizar Aquisição | Alfanumérico | X | 0 = Não Contabilizar;                   2 = Contabilização Pendente. |
| **27** | Valor de depreciação corrigida | Numérico c/ 2 decimais |  |  |
| **28** | Valor taxa de depreciação | Numérico c/ 2 decimais |  | Caso deseje buscar a taxa de depreciação Grupo de Patrimônio, deixe o campo em branco. |
| **29** | Código do Fornecedor Global | Alfanumérico |  | N = Não; S= Sim |

Para casos em que o usuário deseja realizar a importação com o valor base diferente do valor de aquisição, **deverá ser utilizado** o layout de importação "CONPAT0049 - Importação Patrimônio com valor base diferente do valor de aquisição".  
Esse layout possui um campo a mais:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **30** | Valor Base de Depreciação | Numérico(15,2) |  |  |

**ATENÇÃO**: Não será permitido a importação de patrimônios com o status de Contabilizar Aquisição = Contabilizado.

---

**Campo Complementar (C)**  
Os campos devem ser informados utilizando o separador **;** "ponto e vírgula".

| **Ordem** | **Descrição** | **Tipo** | **Obrigatório** | **Observação** |
| --- | --- | --- | --- | --- |
| **1** | Identificador de campo complementar | Char | X | O identificador é letra **C** |
| **2** | Nome do campo complementar | Alfanumérico | X | O nome deve respeitar o que foi informado no cadastro do campo complementar. |
| **3** | Valor do campo complementar | Alfanumérico | X | O formato do valor deve respeitar o que foi informado no cadastro do campo complementar. |

Exemplo:

I;1.01.01.001;01;0;1;Patrimonio de teste;0 ...   
C;DOCUMENTO;1252  
C;VALOR;1000  
C;COR;PRETO
