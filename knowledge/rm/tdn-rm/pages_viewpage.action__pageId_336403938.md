---
content_hash: a90a00bd4d81e570d3d67ae5132c18d4caaa54b0249d295a653111a17c038615
fetched_at: '2026-06-29T00:08:51.073647+00:00'
page_id: '336403938'
product: rm
source: tdn-rm
title: DT Informações do Projeto para EFD - REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=336403938
version: 16
---

# INFORMAÇÕES DO PROJETO PARA EFD - REINF

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Obras e Projetos |
| **Função:** | Cadastro de Projetos |
| **Situação/Requisito:** | Enviar para o PROTHEUS as informações de projetos necessárias para atender a EFD - REINF. |
| **Solução/Implementação:** | O sistema passa a enviar as informações de projetos necessárias para atender as exigências da EFD - REINF.  As informações enviadas são:   * Indicativo de prestação de serviços;    + Se não informado ou informada a opção "Não se aplica" as informações de CNO , CPF ou CNPJ não serão enviadas;   + Quando utilizada a opção "Não é obra de construção civil ou não está sujeita a matrícula de obra" o sistema envia o CNPJ da filial no lugar do código CNO. * Código Nacional de Obras (CNO); * Tipo de Projeto pode ser "Próprio" ou "Terceiros".   + Quando informado "Terceiros" é enviado o CPF ou CNPJ do proprietário (campo Cod. Cliente). Quando informado "Próprio" é enviado o CNPJ da filial do projeto.   **Integrações por mensagem única (EAI 1.0 e 2.0)**  Utiliza a versão 2.001 da mensagem padronizada PROJECT. As informações são enviadas na inclusão / alteração de projeto e no sincronismo de projetos.  **Integração Stored Procedure**  Utiliza a VIEW VSINCRONISMO\_SOLUM\_PROTHEUS. As informações são sincronizadas ao acessar o módulo de compras no PROTHEUS. |
| **Conversores e Parâmetros:** | Integração EAI 1.0: Executar o configurador da integração "*TOTVS Obras e Projetos x BackOffice Protheus (Novo Modelo)*".  Integração EAI 2.0: Configurar a versão 2.001 da mensagem PROJECT.  Integração por Stored Procedure: Executar o configurador da integração "*TOTVS Obras e Projetos x BackOffice Protheus (Modelo Antigo)*".  Cadastrar no SIGACOM -> Atualização - Cadastros - Cadastro nacional de obra. |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | EAI 1.0 - TOPEXECONTROL01-2166  EAI 2.0 - TOPEXECONTROL01-1854  Procedure - TOPEXECONTROL01-2167  TOPEXECONTROL01-2367  TOPEXECONTROL01-2638 |
| **Documento de Referência:** | Não se aplica. |

**Documentações Relacionadas :**
