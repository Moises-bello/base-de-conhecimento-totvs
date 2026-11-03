---
content_hash: 0889c50e6a3fe46080ede5e4a2279d032db9da975a6715a4431d5ac9b184e413
fetched_at: '2026-06-29T00:08:46.605240+00:00'
page_id: '317306543'
product: rm
source: tdn-rm
title: DT Personalização de plano de pagamento - Parâmetros e Informações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317306543
version: 3
---

# PERSONALIZAÇÃO DE PLANO DE PAGAMENTO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **TOTVS Gestão Educacional** |
| **Módulo:** | **TOTVS Educacional** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Cadastro de Plano de Pagamento* | *Cadastro de Plano de Pagamento.* | | *Cadastro de Contrato* | *Cadastro de Contrato* | | *Personalização do Plano de Pagamento* | *Personalização do Plano de Pagamento* | | *Perfil do usuário* | *Cadastro de perfil* | |
| **Cadastros Iniciais:** | *Plano de pagamento, Contrato, Perfil do usuário* |
| **Parâmetro(s):** | *N/A* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *DEDUINTEGRACOES-720* |
| **País(es):** | *Todos* |
| **Banco(s) de Dados:** | *N/A* |
| **Tabelas Utilizadas:** | *SPLANOPGTO, SCONTRATO e SPARAMPERFIL* |
| **Sistema(s) Operacional(is):** | *N/A* |

## Descrição

Com o objetivo de aumentar a segurança e transparência na visualização de informações na personalização de plano de pagamento, foram criados campos no cadastro de plano de pagamento, cadastro de contratos e uma opção nos parâmetros educacionais no perfil do usuário conforme abaixo.

1) Cadastro de plano de pagamento   
    - Campo "Bloqueia alteração do valor base do plano de pagamento para serviços obrigatórios."  
    Opção default é o campo desmarcado, ou seja, não existe bloqueio ou verificação de valor base para serviços obrigatórios.  
    Caso seja marcado, bloqueia alteração do valor base do plano de pagamento para serviços obrigatórios na personalização do plano de pagamento.

    Os serviços serão obrigatórios se estiverem com o campo "Obrigatório" marcado no anexo "Serviços do plano de pagamento".

    Caso não existam serviços definidos como obrigatórios no plano de pagamento, o bloqueio não será verificado na personalização.  
    Usuário poderá alterar o valor base para personalização do plano com esse campo marcado desde que marque a permissão "Permite alteração do valor base do contrato bloqueado no plano de pagamento" dos parâmetros educacionais do perfil do usuário. Vide abaixo.  
  
      
2) Cadastro de contrato  
    - Informações de personalização de plano de pagamento somente ficarão visíveis se houver informações de personalização preenchidas no contrato. Sistema verificará o preenchimento do campo código do plano de pagamento de personalização, caso o mesmo esteja preenchido, as informações serão exibidas.  
        a) Plano de pagamento de personalização - SCONTRATO.CODPLANOPGTOPERSONALIZ.   
            -> FUNÇÃO: Plano de pagamento escolhido pelo usuário na personalização do plano de pagamento  
        b) Usuário responsável pela personalização - SCONTRATO.CODUSUARIOPERSONALIZ  
            -> FUNÇÃO: Usuário responsável pela personalização do plano de pagamento  
        c) Última data de personalização - SCONTRATO.DATAPERSONALIZ  
            -> FUNÇÃO: Data em que o plano de pagamento foi personalizado  
        d) Valor base do contrato pré-personalização - SCONTRATO.VALORBASEPERSONALIZ   
            -> FUNÇÃO: Valor do plano de pagamento antes de ser personalizado  
        e) Valor do contrato após personalização - SCONTRATO.VALORCONTRATOAPOSPERSONALIZ   
            -> FUNÇÃO: Valor do plano de pagamento após ser personalizado

          
3) Personalização do plano de pagamento do contrato  
    - Após personalização do plano de pagamento vide documento técnico:  (Tela de personalização do plano de pagamento), serão gravadas as respectivas informações de personalização no cadastro de contrato. Essas informações aparecerão após contrato ser editado e personalizado.  
  
4) Opção "Permite alteração do valor base do contrato bloqueado no plano de pagamento" nos parâmetros Educacionais do cadastro de perfil de usuário  
    Indicará se o usuário poderá alterar o valor base para personalização do plano mesmo com o campo "Bloqueia alteração do valor base do plano de pagamento para serviços obrigatórios." marcado no cadastro do plano de pagamento utilizado para personalização.
