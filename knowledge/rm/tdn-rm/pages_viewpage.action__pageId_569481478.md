---
content_hash: d463100adbbee132542d936a2eff948b3e95e59f1e66b183ab78f71559729fe5
fetched_at: '2026-06-29T00:10:51.619598+00:00'
page_id: '569481478'
product: rm
source: tdn-rm
title: Parâmetros Integrações EAI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=569481478
version: 14
---

**Integrações EAI**

Parâmetros gerais das integrações através do TOTVS Message (mensagem única).

Inicialmente temos alguns parâmetros gerais para mensagens de solicitações (manipulação dos movimentos) provenientes do EAI e também parâmetros relativos à integração "Manutenção de Ativos Protheus (SIGAMNT)".

**Integração TOTVS Message**

**Solicitação Emissão Remessa:**Tipo de movimento a ser utilizado na criação do movimento quando a solicitação for de tal tipo.   
Inicialmente a mensagem preparada para este fim é a *order* e quando sua *tag* **OrderTypeCode** estiver com o valor "002" então será criado no TOTVS RM um movimento cujo tipo de movimento será o informado neste parâmetro.

**Solicitação Emissão Fatura:**Tipo de movimento a ser utilizado na criação do movimento quando a solicitação for de tal tipo.   
Inicialmente a mensagem preparada para este fim é a *order* e quando sua *tag***OrderTypeCode** estiver com o valor "003" então será criado no TOTVS RM um movimento cujo tipo de movimento será o informado neste parâmetro.

**Solicitação Emissão NFS-e:**Tipo de movimento a ser utilizado na criação do movimento quando a solicitação for de tal tipo.   
Inicialmente a mensagem preparada para este fim é a *order* e quando sua *tag***OrderTypeCode** estiver com o valor "004" então será criado no TOTVS RM um movimento cujo tipo de movimento será o informado neste parâmetro.

**Solicitação Emissão NF-e:**Tipo de movimento a ser utilizado na criação do movimento quando a solicitação for de tal tipo.   
Inicialmente a mensagem preparada para este fim é a *order* e quando sua *tag***OrderTypeCode** estiver com o valor "005" então será criado no TOTVS RM um movimento cujo tipo de movimento será o informado neste parâmetro.

***Observação:***

São apresentados para seleção todos os tipos de movimentos e é possível o uso de mesmo tipo de movimento para tipos de solicitação distintos (repetição de tipos de movimentos entre os tipos de solicitações).

**Definições SigaMNT Protheus**

**Gera movimento para produto não estocável:**Campo para indicar que será gerado movimento para produto não estocável na filial.

**Movimento Gerado (Default):**Tipo de movimento a ser utilizado na criação do movimento quando a solicitação for de tal tipo.   
Campo editável e obrigatório quando marcado o parâmetro Gera movimento para produto não estocável.  
São apresentados para seleção apenas os tipos de movimentos com as seguintes configurações:  
Integrado com SigaMNT marcado (Etapa Manutenção).

***Observação***:

A consistência ao salvar os parâmetros será que a série do tipo de movimento selecionado neste campo não pode ser igual a série dos tipos de movimento de Solicitação de Armazém e Solicitação de Compra nos parâmetros da integração (Sistema Integrações | EAI 2.0 | Parâmetros Adapter, parâmetros TMVSolicitacaoArmazem e TMVSolicitacaoCompra).

**Os parâmetros de integração com o Manutenção de Ativos Protheus ficarão disponíveis apenas quando existir integração ativa entre Manutenção de Ativos e BackOffice RM no EAI 2.0.IMPORTANTE!**

**Exemplo de utilização**:

Quando for gerado uma Ordem de Serviço no módulo SIGAMNT do Protheus será integrado ao BackOffice RM via EAI as mensagens para criação dos movimentos de Ordem de Serviço e Solicitações vinculadas à Ordem de Serviço.  
O adapter de recebimento da Solicitação (mensagem *Request* versão 1.010) irá verificar se o produto é Estocável ou Não Estocável e realizará a seguinte verificação para criação dos movimentos:

* Se todos os produtos forem estocáveis, segue fluxo normal do adapter para criação do movimento. Será utilizado o tipo de movimento definido nos parâmetros de integração TMVSolicitacaoArmazem quando for Solicitação de Armazém ou  tipo de movimento definido no parâmetro TMVSolicitacaoCompra quando for Solicitação de Compra. Os parâmetros de integração ficam no módulo Integrações menu EAI 2.0 \ Parâmetros Adapter;
* Se todos os produtos forem não estocáveis, será utilizado o tipo de movimento definido na Etapa 04.03.06 - Manutenção de Ativos (Protheus) campo Movimento Gerado (Default) dos parâmetros do Gestão de Estoque, Compras e Faturamento;
* Quando a solicitação possuir itens estocáveis e não estocáveis então será realizado a quebra destes itens em tipos de movimentos distintos, onde os produtos não estocáveis serão gravados no tipo de movimento definido na Etapa 04.03.06 - Manutenção de Ativos (Protheus) campo Movimento Gerado (Default) dos parâmetros do Gestão de Estoque, Compras e Faturamento.

A informação se o produto é estocável está localizado no cadastro de Produtos na pasta Informações Por Filial.

]]>
