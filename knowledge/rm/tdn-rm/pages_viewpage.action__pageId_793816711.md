---
content_hash: 6fdfa836947f0eba2c69a58f73073e970d92975bff53e9e189bdd836fb6e149f
fetched_at: '2026-06-29T00:11:40.023749+00:00'
page_id: '793816711'
product: rm
source: tdn-rm
title: TOTVS Saúde Hospitais e Clínicas - Inovação 12.1.2310
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=793816711
version: 10
---

# **Descontinuação dos módulos Delphi**

Dando continuidade ao processo de atualização tecnológica de nossos produtos de saúde e em linha com o compromisso da TOTVS proporcionar a melhor experiência em tecnologia para a gestão de hospitais e clínicas, estamos lançando a release 12.1.2310 do sistema TOTVS Saúde Hospitais e Clínicas (expedição prevista para 06/10/2023), com importantes melhorias para otimizar seu ambiente de trabalho e oferecer maior eficiência operacional.

## **01. TROCA DOS MENUS NA MDI DELPHI PARA ROTINAS JÁ MIGRADAS**

Algumas rotinas migradas em releases anteriores já estavam disponíveis na MDI .Net (Novas MDI) porém não estavam sendo chamadas na MDI Delphi. Nessa release, todas as rotinas já migradas para a tecnologia .Net estão disponíveis para serem utilizadas dentro da MDI principal do módulo em Delphi, unificando assim a experiência do usuário independente da plataforma utilizada.

* Itens Brasíndice
* Itens SIMPRO
* Mapa de Trabalho
* Painel de Dispensação
* Monta/Desfaz Kit de Mat/Med
* Mapa de Dispensação
* Emissão de Faturas para Convênio
* Registro de Entrega de Faturas
* Faturamento AIH, BPA e APAC
* Folha de Pagamento de Prestadores
* Informações para o Ministério da Saúde (Tela de Lançamento)
* Lançamento na Conta do Paciente (Elaboração de Contas)
* Controle de Glosa (Gestão de Glosa)
* Recurso de Glosa (Gestão de Glosa)

## **02. REMOÇÃO DE ROTINAS DESCONTINUADAS**

Devido à evolução funcional, melhores práticas do mercado de saúde, atualização tecnológica e maturidade na ferramenta, algumas funcionalidades existente em delphi passaram a não fazer mais sentido ou foram substituídas por processos mais maduros no sistema. Dado esse contexto, a partir da 12.1.2310, as funcionalidades listadas abaixo foram removidas dos menus do sistema.

* Correlação com Form. Dinâmico (PEP 2)
* Posologia
* Esquema de Soroterapia
* Locais para registro de presença - UMov.me
* Usuários do registro de presença - UMov.me
* Depósito
* Listagem de Exames Faturados por Remessa
* Controles de Gasoterapia
* Manutenção de Aprazamentos
* PEP 2.0
* Etiquetas de Estoque
* Lista de Preços
* Consumo de Medicamentos Alíquota Zero
* Transferência de Atendimentos
* Menu Consultas e Relatórios (Faturamento Part./Convênios)
* Lançamento de Procedimentos BPA - Anterior
* Menu Relatórios (Faturamento SUS)
* Alteração na Folha de Produção dos Prestadores
* Recibo de Honorários Médicos
* Controle de Depósitos
* Análise de Anestesistas
* Parâmetros da Assinatura Digital (PEP 1)
* Parâmetros de Integração MultiPEP
* Etiquetas de Endereçamento
* Automatizador de Informações CIHA
* Pesquisa CID
* Identificação de Faturamento Eletrônico
* Acerta situação de Leitos
* Importa atendimentos de outro banco
* Importa atendimentos para faturamento
* Gerenciamento de Mensagens TISS
* Assistente de credenciamento
* Exporta prestadores fatmed.br
* Exporta prestadores Unimed BH
* Assistente de Exportação de dados para a Central de Documentos (PEP 2.0)

## **03. REESTRUTURAÇÃO DOS MENUS DE FARMÁCIA**

Reestruturados os menus da MDI Delphi para contemplar os mesmos processos de farmácia / enfermagem da Nova MDI (.Net) (Processos Farmacêuticos, Movimentação de Estoque, Nova requisição).

## **04. PRONTUÁRIO ELETRÔNICO**

Visando apoiar os clientes na evolução e digitalização da assistência, na release 12.1.2310, todos os usuários do prontuário eletrônico em delphi (PEP 1) receberão a mensagem abaixo informando sua descontinuidade e apresentando o novo prontuário eletrônico Web.

Se sua instituição ainda não utiliza o novo prontuário eletrônico, procure seu executivo de contas. Estamos confiantes de que o novo prontuário trará muitos benefícios a sua instituição. Saiba mais em:

A partir da Release 12.1.2402, prevista para se expedida em , o prontuário eletrônico Delphi será removido das soluções tendo seu acesso revogado em todos os menus do sistema.

## **05. REMOÇÃO DO GERADOR DELPHI**

O gerador de relatórios Delphi será removido das soluções da linha RM tendo seu acesso revogado em todas as MDIs (Delphi e .Net) por se tratar de uma tecnologia obsoleta e incompatível com os sistemas operacionais e bancos de dados atuais.

Sugerimos a todos os clientes que ainda utilizem soluções desenvolvidas em Delphi, seja para geração de relatórios, planilhas e/ou outros objetos gerenciais, que façam uso dos respectivos recursos já disponíveis com tecnologias mais inovadoras, como por exemplo: RM-Reports, TReports, Gerador de Saídas entre outros.

Descubra mais em [**RM BI**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115004113148-RM-BI).

## **06. COMUNICADOS SOBRE AS ROTINAS DESCONTINUADAS**

Considerando que todas as mudanças descritas possuem um impacto condideravel nos processos da instrituições, a TOTVS previamente comunicou todos seus clientes sobre as ações descritas nesse documento através do tema "Descontinuidade dos produtos com tecnologias em  Delphi" através de comunicados publicados na área de ciclo de vida de software na central de atendimento ao cliente.

* Módulos em Delphi do TOTVS Saúde Hospitais e Clínicas (RM Saúde): Publicado em 06/05/2021 o comunicado pode ser acessado por esse link: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009557562>
* Gerador de Relatórios em Delphi: Publicado em 30/03/2023 o comunicado pode ser acessado por esse link: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/13493831089303>

## **07. NOVIDADES DA RELEASE 12.1.2310**
