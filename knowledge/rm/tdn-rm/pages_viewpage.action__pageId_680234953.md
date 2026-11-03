---
content_hash: 96c73e96bebf8b742824d1a22ae29b44eb8282f65a5387549e5315e052c3dd5a
fetched_at: '2026-06-29T00:11:17.417652+00:00'
page_id: '680234953'
product: rm
source: tdn-rm
title: 1 - Gráficos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=680234953
version: 14
---

## O que são?

Os **Gráficos** oferecem uma visão geral dos status de execução dos Projetos de Testes, destacando erros, alertas e pendentes de execução, com base no grupo e versão informados.

## Para que servem?

Serve para acompanhar o estado das execuções de Projetos, identificando rapidamente onde ocorreram falhas, sucessos e quais grupos ou versões estão a gerar mais erros ou alertas. Isso facilita a análise e tomada de decisões para melhorar o desempenho dos Projetos.

# Exemplo de Uso

Como FiltrarComo filtrar 1. Navegação para Filtrar

1. Navegue no menu TOTVS Automação de Testes e clique em **Relatórios**→ **Status de Execução → Gráficos.**

2. Visualização do Relatório

## Visualização do Relatório

Para obter uma visão geral do status de execução dos Projetos de Testes, estão disponíveis os seguintes filtros:

**Versão**: Permite filtrar os Projetos de Teste com base na versão específica da Atividade.

**Grupos**: Este filtro permite selecionar projetos de teste com base nos grupos aos quais pertencem. [(Saiba mais sobre os Grupos clicando aqui)](https://tdn.totvs.com/display/public/LRM/6+-+Grupos#Cria%C3%A7%C3%A3odeumgrupo--1840173891).

Após a aplicação do filtro, os seguintes dados são apresentados:

**Status Geral de Execução:** Este gráfico oferece uma visão ampla da distribuição dos status das últimas execuções dos Projetos em percentuais, incluindo aqueles ainda não executados. Ele permite identificar rapidamente o progresso de cada status contendo os seguintes recursos: 

* **Sucesso**: Indica os Projetos que foram executados com êxito, sem erros ou alertas.
* **Falha ou alerta**: Refere-se a execuções de Projetos que encontraram erros (falhas) ou que geraram avisos (alertas) durante a execução, necessitando de atenção.
* **Pendente de Execução:** Representa os Projetos que ainda não foram executados e estão aguardando processamento.

**Status de Execução por Grupo:** Este gráfico exibe a distribuição dos status das últimas execuções dos Projetos em quantidade de Projetos, bem como dos Projetos ainda não executados, por Grupo de usuários e Versão, contendo os seguintes recursos:

* **Sucesso**: Exibe a quantidade de Projetos que foram executados com sucesso, sem erros ou alertas.
* **Falha ou Alerta**: Mostra a quantidade de Projetos onde ocorreram erros (falhas) ou alertas durante a execução, sinalizando a necessidade de revisão ou correção.
* **Pendente de Execução**: Identifica a quantidade de Projetos que ainda não foram executados, indicando que estão aguardando processamento ou agendamento

**Distribuição de Erros/Alertas:** Este gráfico mostra a quantidade de erros e alertas por Grupo e Versão filtrados.

Para a interpretação do gráfico, é possível visualizar os números de cada atividade diretamente em suas respectivas legendas.

---

# Saiba mais

A identificação precoce através do gráfico ajuda a evitar que falhas se tornem recorrentes.

A ferramenta permite que você filtre os relatórios de execução por **Versão** e **Grupos**. Isso é essencial para focar em áreas específicas, como Versões com mais falhas ou Grupos com melhor desempenho

# FAQ

**P: Com que frequência os dados são atualizados?**  
R: Os dados são atualizados automaticamente após cada execução de um Projeto de Teste, garantindo que as informações estejam sempre atualizadas.

**P:Como o gráfico ajuda na gestão de projetos?**  
R: O gráfico de status de execução permite aos usuários acompanhar o progresso dos Projetos, identificar antecipadamente problemas como falhas ou alertas, e verificar quais grupos ou equipes têm Projetos pendentes. Esta funcionalidade melhora o monitoramento e facilita a tomada de decisões estratégicas.
