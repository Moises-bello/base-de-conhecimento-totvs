---
content_hash: f304fffb2d51070df53268735e4bed0d5bcefd2ab55a85e6599df16d80a2932c
fetched_at: '2026-06-29T00:08:20.946081+00:00'
page_id: '268796712'
product: rm
source: tdn-rm
title: DT_Melhorias_LicenseServer_Versão_1.03.010
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268796712
version: 114
---

# Melhorias da Linha de Produto RM para o LicenseServer Versão 1.03.010

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *FRAMEWORK* |
| **Módulo:** | *FRAMEWORK* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Consumo de Licenças* | *-* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *Inclusão/Exclusão de Usuários* | *SaveRecord - GlbUsuarioData* | |  |  | |
| **Cadastros Iniciais:** | *-* |
| **Parâmetro(s):** | *-* |
| **Ponto de Entrada:** | *-* |
| **Chamados Relacionados** | *-* |
| **Requisito (ISSUE):** | FRW\_FRW002-182 |
| **País(es):** | *-* |
| **Banco(s) de Dados:** | *-* |
| **Tabelas Utilizadas:** | *-* |
| **Sistema(s) Operacional(is):** | *-* |

## Descrição

Melhorias na comunicação com o License Server, enviando novos dados requeridos pela versão 1.03.010.

1) A Mensagem SetInfo de usuário é enviada toda a vez um usuário for incluído ou modificado em nossos softwares.

2) A Mensagem SetInfo de usuário envia novos dados: Id do Identity e email. Estas informações serão utilizadas para que não haja duplicação de consumo entre nossos softwares.

3) A mensagem SetInfo de Instalação da linha de produto inclui informações extras que são especificas da linha e serão enviadas para o GCAD local.\*

4) Conexão entre a linha RM e o License Server utiliza SSL/TLS over TCP.\*\*

\* Caso o GCAD local considere necessário e faça a implementação necessária.

\*\* Será finalizado quando do License Server suportar a comunicação SSL com as linhas de produto.

Controle do consumo de licenças pelos WebServices expostos pelo RM.Host.

Todos os WebServices SOAP e REST expostos pelo RM.Host farão o controle do consumo de Licenças. O padrão de consumo de licenças continua o mesmo: primeiramente o *slot on demand* e, caso ele não exista, utiliza-se o *slot* TOTVS I e TOTVS *Full* respectivamente.

Para que esta melhoria fosse possível, padronizamos também o mecanismo de autenticação dos webservices. Agora todos eles, *SOAP* e *REST* exigirão HTTP BASIC com a possibilidade de utilização de *SSL*.

## Procedimento para Implantação

Atualização da Linha RM para versão 12.1.15 ou superior.

divs
