---
content_hash: 8ed81e37411a25c9caa4b0ce2505903f1fe19430d4fa7e1c86f156f850d8c0c2
fetched_at: '2026-06-29T00:08:46.368252+00:00'
page_id: '317003653'
product: rm
source: tdn-rm
title: Dificuldades - Automação - Controle/Execução
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=317003653
version: 3
---

## Dificuldades de Estrutura

1. Servidor com base Protheus Oracle e RM Oracle só para Automação.
2. Ambiente PROTHEUS Integrado x RM   
   Este item tem agravante quanto as dificuldades para manutenção desses ambientes, visto que o Protheus não é "atualizável" como o RM é via restore, e essa manutenção de versões do Protheus gera um custo enorme para manter o ambiente para rodar as automações íntegro.  
   Exemplo: Hoje temos 3 tipos de integrações, Stored Procedure, EAI 1.0 e EAI 2.0, teríamos que ter 3 ambientes e nestes 3 ambientes mantê-los atualizados e integrados com as versões do RM. Isto pra nossa squad é um cenário diferente das demais no que diz respeito aos ambientes em que rodam automação.

## Dificuldades de Ferramenta - TestFlow 2.0

1. Agendamentos sempre com problemas. Observado que este problema é recorrente, mesmo em Squads que só realizam automação do lado RM. Todas os agendamentos continuam não rodando e com vários problemas de execução. Entendemos como primordial esse item estar estável para que garanta todas as nossas automações, uma vez que se o agendamento não roda, não adianta o esforço realizado nos demais itens.

## Dificuldades de Estratégia da Equipe

1. Definição de uma estratégia para organizações dos projetos de testes.

## Possíveis Soluções

1. Termos um servidor e este servidor ser dividido em 3 Vm's para cada tipo de integração. Dessa forma, manteríamos cada ambiente separado para realizar as gravações, rodar as automações agendadas e manter suas atualizações.

2. É preciso que haja uma padronização entre os integrantes da Squad para que todos os projetos sejam orientados a mesma estrutura, para que seja fácil a manutenção dos mesmo e de suas atividades.  
Exemplos:

* Criação de projetos pequenos,
* Projetos com atividades descentralizadas para melhor manuseio em demais projetos e facilidade de reaproveitamento de atividades em novos projetos.
* Criação de atividades C# com padrão e comentários para melhor entendimento em seu uso e manutenção.
* Atividades específicas de um projeto, serem colocadas em grupos e descritas exatamente para o que foi desenvolvida.

## Aprendizado:

* Curso da Alura para Selenium: <https://www.alura.com.br/curso-online-selenium>

## Conclusão:

Entendemos que os itens de Dificuldade citados na parte de **Estrutura e Ferramenta *(Agendamento)*** são primordiais para que possamos automatizar nossos fluxos, uma vez que sem termos uma estrutura definida e clara, corremos os mesmos riscos que tivemos quando automatizamos em uma máquina todos os cadastros TOP x Protheus em uma base da engenharia que foi desativada posteriormente.    
  
Todos os projetos estavam todos apontados para rodar somente nesse ambiente, trazendo grandes retrabalhos e por fim perdendo várias automações, uma vez que a base foi atualizada e/ou desativada por ter seu controle total na engenharia.   
  
Outro ponto primordial, é que o agendamento na ferramenta funcione de forma íntegra, para que não precisemos ter retrabalhos como tivemos, pois, todos os dias tínhamos que conferir agendamento a agendamento o porque não foi executado e se não rodou qual foi o problema, se da execução ou da ferramenta. **Entendemos que este item é o principal para que a ferramenta realmente seja eficaz e garanta os nossos testes.**
