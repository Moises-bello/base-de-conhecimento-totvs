---
article_id: 16949179237015
category: REQUISIÇÕES
content_hash: 8dfac89df309b14e17fe9964021631191a344054a0a963f4b6f8fa9ef87cb204
fetched_at: '2026-06-28T22:44:37.606206+00:00'
product: protheus
section_id: 10299632459799
source: central-protheus
title: RH - Linha Protheus - Meu RH - Tipos de rescisão, na seleção de uma Requisição
  de Desligamento feita pelo Gestor
type: support-article
updated_at: '2025-03-12T19:41:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16949179237015-RH-Linha-Protheus-Meu-RH-Tipos-de-rescis%C3%A3o-na-sele%C3%A7%C3%A3o-de-uma-Requisi%C3%A7%C3%A3o-de-Desligamento-feita-pelo-Gestor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16949147674775) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Tipos de rescisão, na seleção de uma Requisição de Desligamento feita pelo Gestor  
  
**Ambiente**TOTVS RH - (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**O objetivo desta tela é permitir que o Gestor **inclua uma requisição de desligamento para seus colaboradores subordinados diretos.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16948849610519)  
  
A requisição após ser concluída, será submetida **à hierarquia de aprovação dos demais Gestores, se houver,** antes de efetivamente ser levada ao RH para que, **via Protheus, seja efetivada.**  
  
O campo Tipo de Desligamento, é composto pelo cadastros dos Tipos de Rescisão, **via módulo 07 - SIGAGPE, rotina Atualizações -> Definições de Cálculo -> Manutenção de Tabelas, especificamente na tabela S043.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16948967263383)  
  
Em relação ao campo **"Gera nova contratação"**, é uma seleção meramente informativa e utilizada para que o Gestor que está desligando o Colaborador, **somente informe ao RH** pela efetivação de solicitação do Portal. Pode ser usado em qualquer tipo de hierarquia, ou seja, Visão por Departamento (**MV\_ORGCFG=2**), Visão com Controle de Postos (**MV\_ORGCFG=1**) e Estrutura de Departamentos (**MV\_ORGCFG=0**).  
  
Nesta rotina, ainda é possível **inserir um anexo**, justificando essa requisição, se necessário.  
  
**Obs.:** Esta função, ao ser Efetivada pelo RH em última instância, **na rotina de Efetivar Solicitações** no Protheus, **NÃO realiza o cálculo** ou **abre a rotina de Rescisão**, sendo então uma funcionalidade para captação de histórico de solicitação de desligamento para um funcionário entre o Gestor e o RH, **ficando à cargo do RH a realizar o desligamento** do funcionário na melhor oportunidade declarada pela própria empresa.  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
