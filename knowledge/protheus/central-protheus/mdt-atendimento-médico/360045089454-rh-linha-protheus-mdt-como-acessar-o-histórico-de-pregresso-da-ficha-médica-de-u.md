---
article_id: 360045089454
category: MDT - Atendimento Médico
content_hash: 4173d5d697c3ca703efd36c7e690c90c91b1bdd1c90b191abaaf86b0f5bdddab
fetched_at: '2026-06-28T22:44:20.458994+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT -   Como acessar o histórico de pregresso da ficha
  médica de um funcionário quando ele é transferido de filial
type: support-article
updated_at: '2025-08-14T18:52:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045089454-RH-Linha-Protheus-MDT-Como-acessar-o-hist%C3%B3rico-de-pregresso-da-ficha-m%C3%A9dica-de-um-funcion%C3%A1rio-quando-ele-%C3%A9-transferido-de-filial
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27570950983831)**Tempo aproximado para leitura: 00:02:00 min  
Dúvida**Como acessar o **Histórico de Pregresso** da ficha médica de um funcionário quando ele é transferido de filial?  
 **Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Há a opção de Histórico de Pregresso para permitir a consulta de informações pregressas referentes ao prontuário médico do funcionário quando este é transferido de filial.  
  
As rotinas de Ficha Médica (MDTA005), Ocorrências Ficha (MDTA110), Diagnóstico Médico (MDTA155) e Ficha Médica Mod 2 (MDTA410) apresentam a opção.  
  
Em cada rotina é apresentada a opção de visualizar, imprimir cadastro e listagem dos registros do prontuário médico. Na pasta de Exame é possível visualizar o resultado do exame e em Diag. Med. é apresentada a opção de visualizar os medicamentos utilizados.  
  
A opção de visualizar o histórico pregresso estará disponível quando o parâmetro **MV\_NG2TRAN** estiver desabilitado, indicando que os dados do prontuário médico não foram transferidos diretamente.   
  
Ao habilitar o parâmetro a consulta não é apresentada, pois os dados da ficha médica foram transferidos, é exibida uma mensagem informando que o parâmetro **MV\_NG2TRAN** deve estar desativado. Ao transferir somente a ficha médica, utilizando Transf. de Filial (**MDTA970**) A consulta será apresentada.  
  
A rotina Histórico de Pregresso está disponível no modulo SIGAMDT no caminho: Atualizações > Atendimento Medico > Ocorrencias Ficha. Clique em Outras Ações > Hist. Pregresso.  
  
**Saiba Mais**  
[Artigos Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico)  
[Artigos sobre Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT)
