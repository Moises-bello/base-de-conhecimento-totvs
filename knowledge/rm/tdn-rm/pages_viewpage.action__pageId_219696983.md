---
content_hash: fee61e0c80f5b03ce7d91d3f3ded5729773c610658ac7c58e139c11fed7c9081
fetched_at: '2026-06-29T00:06:19.379716+00:00'
page_id: '219696983'
product: rm
source: tdn-rm
title: CLB_0001_Parametrizações_TOTVS_Colaboração_2.00
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=219696983
version: 10
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS Colaboração 2.00 |
| **Versões:** | 12.1 e superiores |
| **Ocorrência:** | Parametrizações TOTVS Colaboração 2.00 |
| **Ambiente:** | Parametrizações necessárias para o TOTVS Colaboração 2.00 |
| **Passo a passo:** | Parametrizações TOTVS Colaboração 2.00 1.1 Parametrização Global para a Coligada A configuração principal deve ser feita através do módulo BackOffice  “Gestão de Estoque, Compras e Faturamento (RM Nucleus)” , através do menu “Ambiente >> Parâmetros >> Gestão de Estoque, Compras e Faturamento >> Integrações >> Fiscal >> Dados Fiscais”, etapa “TOTVS Colaboração”.  É necessário informar a versão da integração TOTVS Colaboração (neste caso, 2.0) e o diretório raiz do ClientEDI NeoGrid, onde estão as pastas responsáveis pelo compartilhamento dos arquivos XML (IN, OUT, SENT, etc.).         **Observação:** O diretório parametrizado poderá ser utilizado para várias Coligadas.   1.2 Parametrização por Filial É necessário parametrizar as filiais que irão trabalhar com o TOTVS Colaboração. Através dos parâmetros da Filial (menu “Ambiente >> Parâmetros >> Gestão de Estoque, Compras e Faturamento >> Integrações >> Fiscal >> Dados Fiscais >> Parâmetros por Filial”,  acesse a etapa “Informações TOTVS Colaboração” e selecione quais Tipos de Documentos terão a integração TOTVS Colaboração 2.00.   **Observações:**    * Ao marcar a opção ‘Todos’ não é necessário selecionar outras opções de tipo de documentos. * Caso desmarque todas as opções de tipo de documentos a integração será desativada.     Além dessa informação, os seguintes campos devem ser informados:    * Usuário/Senha TOTVS Colaboração: estes dados inicialmente seriam necessários somente para o TOTVS Colaboração 1.0, entretanto, com a migração do TOTVS Colabração 2.0, a obrigatoriedade não foi retirada. Dessa forma, é necessário o preenchimento, mas não há validação das informações preenchidas. * Ambiente TOTVS Colaboração – Recebimento. * Número máximo de documentos para Retorno.   Tipo de Movimento para Inclusão Automática de CT-e: Somente caso tenha marcado o tipo de documento ‘Recebimento CT-e’ ou ‘Todos’ os tipos de documento. |
| **Observações:** | Para mais informações:    [Consulte o WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.ECF.aspx)    **COMUNIDADE** [R@Materiais e Suprimentos](http://fluig.totvs.com/portal/p/10097/subject/rmateriais)    **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 5 – (Materiais) |

divs
