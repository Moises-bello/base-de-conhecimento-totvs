---
content_hash: e487b6304793dd9a2a4fab2bf133343d80240d5b78373dfd434bd4ba141f31f4
fetched_at: '2026-06-29T00:11:33.265561+00:00'
page_id: '754947778'
product: rm
source: tdn-rm
title: 8.2 - Histórico de Execuções
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=754947778
version: 17
---

# O que são?

O **Histórico de Execuções** oferece uma ferramenta de monitoramento dos status das execuções dos Agendamentos. Sua principal função é proporcionar uma visão abrangente e detalhada das execuções automáticas, permitindo uma administração mais eficiente das atividades e dos recursos envolvidos.

# Para que servem?

Serve para controlar, acompanhar, e visualizar o status e o desempenho das execuções do **Agendamento**, oferecendo logs e informações detalhadas para que os administradores possam gerenciar as execuções com eficiência.

* Visualizar resultados gerais e específicos de execuções.
* Ordenar e filtrar o histórico das execuções por diversos critérios.
* Acessar logs e detalhes de cada execução, incluindo notificações e informações de servidores.

# Exemplo de Uso

Como cadastrarComo Visualizar 1. Navegação para visualização

1.Navegue no menu do TOTVS Automação de Testes e clique em **Agendamentos → Histórico de execuções.**

2. Neste Menu são listadas todas execuções dos seus Agendamentos.

2. Funcionalidades do Histórico de Execuções Detalhes da Execução

No menu, é possível visualizar e identificar os seguintes elementos dos registros:

* Nome.
* Versão.
* Status.
* Início e fim da execução.

Na coluna "Ações", clique em **DETALHES** para acessar todas as informações do agendamento.

O cabeçalho traz as seguintes informações:

* A versão do agendamento.
* Início e fim da execução.
* Resultado da execução do Agendamento.
* Modo de execução.
* Modo de notificação.
* Quem executou o agendamento (Ele sempre será executado pelo Administrador).
* Servidores indisponíveis, caso existe algum na execução.

Mais detalhes do cabeçalho:

* Além das informações anteriores, são indicados os servidores configurados para a execução do agendamento e os destinatários notificados por e-mail
* Quem foi notificado (e-mail).

Atividades executadas

Nessa visão, é possível visualizar todos os logs gerados durante a execução da tarefa de agendamento.

Editar Agendamento

Nesta Visão o usuário também tem a opção de editar **Agendamentos** previamente configurados. Isso pode incluir a modificação de parâmetros como a data, hora de execução, servidores envolvidos ou qualquer outra configuração relevante.

Ícones e Filtros da TabelaStatus

## Status

**Sucesso:**

Indica que a atividade específica foi concluída com sucesso durante a execução do agendamento.

**Falha**: Indica que houve uma falha na execução da atividade durante o agendamento.

Filtros da Tabela 

## Filtros da Tabela

No menu inicial do Histórico de Execuções temos as seguintes opções de filtros:

* **Nome do Agendamento**: Filtre pelos nomes específicos dos agendamentos para localizar rapidamente o agendamento que deseja visualizar ou editar.
* **Agendamento** :Filtre os diferentes agendamentos para organizá-los e visualizá-los de forma mais eficiente.
* **Status:** Filtre pelos resultados de sucesso ou falha para identificar rapidamente o status das execuções e tomar as ações corretivas necessárias. Isso facilita a análise de desempenho e a resolução de problemas.
* **Versões:** Filtre por versões de cada agendamento para visualizar e gerenciar diferentes iterações e atualizações.
* **Grupos**: Filtre pelos grupos que associam ao seu Agendamento.

Exemplo Prático 

Imagine que você agendou uma limpeza nas máquinas dos funcionários para o final de semana. Na segunda-feira pela manhã, deseja verificar se a limpeza foi concluída corretamente.

Certifique-se de:

* Verificar se o agendamento foi executado com sucesso.
* Acessar o log de execução para revisar os detalhes do processo.
* Filtrar as execuções por status (sucesso ou erro) e revisar os resultados de dias ou versões diferentes do agendamento.
* Identificar se algum servidor estava indisponível durante a execução.
* Editar ou reconfigurar o agendamento conforme necessário.

---

# Saiba mais

Os logs de execução não apenas mostram o status final, mas também fornecem informações detalhadas, como quais servidores foram utilizados, quanto tempo cada tarefa levou e até se houve algum problema específico com um servidor.

Se algo deu errado, você pode reexecutar o agendamento sem precisar recriá-lo. Isso economiza tempo e permite que você resolva problemas rapidamente, testando novas configurações.

Além de enviar notificações padrão por e-mail, você pode configurar quem receberá alertas sobre a execução de um agendamento. Assim, apenas as pessoas envolvidas serão notificadas, evitando sobrecarga de informações.

## FAQ

**P: Como posso revisar execuções de dias anteriores?**  
R: Através da função de filtro, você pode pesquisar e revisar execuções anteriores, ajustando a busca por data, status ou versão.

**P: Como saber se as notificações de execução foram enviadas corretamente?**

R: Nos logs, há informações sobre os destinatários notificados por e-mail após a execução do agendamento.

**P: É possível monitorar a disponibilidade dos servidores durante a execução?**  
R: Sim, os logs indicam se algum servidor parametrizado estava indisponível durante o agendamento, permitindo ações corretivas se necessário.
