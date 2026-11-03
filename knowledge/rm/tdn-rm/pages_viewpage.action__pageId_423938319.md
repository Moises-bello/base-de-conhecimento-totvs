---
content_hash: 57ac2bbfba193f4ff5f384df75dd112e74a6e57d626dbed6e18e8a20e2ca1667
fetched_at: '2026-06-29T00:09:26.559135+00:00'
page_id: '423938319'
product: rm
source: tdn-rm
title: Layout Importação de Patrimônio 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938319
version: 11
---

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
|  | **Descrição** | **Tipo** | **Tamanho** | **Obrigatório** | **Observação** |
| **1** | Código do Patrimônio | Alfanumérico | 25 | X |  |
| **2** | Código do Grupo de Patrimônio | Alfanumérico | 10 | X |  |
| **3** | Tipo Patrimônio | Numérico | - | X | 0 = Bem; 2 = Bens de Terceiros |
| **4** | Ativo | Numérico |  | X | Não = 0; Sim = 1 |
| **5** | Descrição | Alfanumérico | 240 | X |  |
| **6** | Reavaliação | Numérico | - | x | 1 = Sim; 0 = Não |
| **7** | Data da Aquisição | Data | 8 | X | DD/MM/YYYY |
| **8** | Valor de Aquisição | Numérico(15,2) | 9 | X |  |
| **9** | Código do Patrimônio Agregador | Alfanumérico | 25 |  |  |
| **10** | Nº do Patrimônio | Alfanumérico | 30 |  |  |
| **11** | Quantidade | Numérico(15,4) | 9 |  |  |
| **12** | Unidade | Alfanumérico | 20 |  |  |
| **13** | Código do Fornecedor | Alfanumérico | 25 |  |  |
| **14** | Observações | MEMO(text) | - |  |  |
| **15** | Código de Barra | Alfanumérico | 30 |  |  |
| **16** | Tipo de Documento | Alfanumérico | 10 |  |  |
| **17** | Série do Documento | Alfanumérico | 4 |  |  |
| **18** | Número do Documento | Alfanumérico | 20 |  |  |
| **19** | Código da Filial | Numérico | - | X |  |
| **20** | Código do Centro de Custo | Alfanumérico | 25 | X |  |
| **21** | Código do Responsável | Alfanumérico | 16 |  |  |
| **22** | Chapa | Alfanumérico | 16 |  |  |
| **23** | Código do Departamento | Alfanumérico | 25 |  |  |
| **24** | Código Local | Alfanumérico | 40 |  |  |
| **25** | Contabilizar Aquisição | Alfanumérico | - | X | 0 = Não Contabilizar;                   2 = Contabilização Pendente. |
| **26** | Valor de depreciação corrigida | Numérico c/ 2 decimais | - |  |  |
| **27** | Valor taxa de depreciação | Numérico c/ 2 decimais | - |  | Caso deseje buscar a taxa de depreciação Grupo de Patrimônio,  deixe o campo em branco. |
| **28** | Código do Fornecedor Global | Alfanumérico | - |  | N = Não; S= Sim |

Para casos em que o usuário deseja realizar a importação com o valor base diferente do valor de aquisição, deverá ser utilizado o layout de importação "CONPAT0049 - Importação Patrimônio com valor base diferente do valor de aquisição".  
Esse layout possui um campo a mais:

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **29** | Valor Base de Depreciação | Numérico(15,2) | 9 |  |  |

ATENÇÃO: Não será permitido a importação de patrimônios com o status de Contabilizar Aquisição = Contabilizado.
