---
content_hash: c336359ba96338c8759d769c5cf2da428283073e78a14adc5b6f852a99b49807
fetched_at: '2026-06-29T00:08:05.872986+00:00'
page_id: '235601768'
product: rm
source: tdn-rm
title: BD0009_Commands_NGEN
type: documentation
url: https://tdn.totvs.com/display/LRM/BD0009_Commands_NGEN
version: 3
---

|  |  |
| --- | --- |
| **Produto:** | Commands (NGEN) |
| **Versões:** | Todas |
| **Ocorrência:** | Registro dos componentes no Assembly |
| **Ambiente:** | RM |
| **Passo a passo:** | O Gerador de Imagem Nativa (NGEN) é uma ferramenta que melhora o desempenho de aplicativos gerenciados. O NGEN cria imagens nativas, que são arquivos que contém o código de máquina específico do processamento compilado e as instala no cache de imagem nativa do computador local. O tempo de execução pode usar imagens nativas do cache em vez de usar o compilador JIT (Just-In-Time) para compilar o assembly original.  Obs.: O procedimento abaixo deve ser executado em todas as camadas APP, Client e JOB  **PROCEDIMENTO NOVO (SENTINELA):**  1 - Acesse o Sentinela:   * *Ir na opção de Executar na tela principal da Nova MDI;* * *Digitar “Sentinela”;* * *Clicar sobre o item apresentado.*     2 - Tarefas de execução agendada    3 - Execução do NGEN    4 - Determine a Camada a ser executada:      **5 - Aguarde a execução do Processo:**    **Observações:**   * O procedimento deve ser executado em todas as camadas: APP, Client e JOB; * Agende a execução semanalmente, de preferencia fora do horário de utilização do sistema.   **PROCEDIMENTO ANTIGO**  Para baixar o arquivo, clique .  Obs.: O diretório de instalação descrito no Commands.bat está direcionando para o default (C:\TOTVS\CorporeRM\RM.Net) caso o cliente tenha instalado em outro diretório é necessário alterar no Commands.bat para que os registros dos componentes no Assembly e NGEN ocorram, lembrando que os comandos citados acima já estão no arquivo, não sendo necessário rodar separadamente.  Segue abaixo manual de como deixar de forma programada a execução:  Passo 1: Acessar o Agendador de tarefas;    Passo 2: Criar Tarefa Básica    Passo 3: Nomear e inserir a descrição    Passo 4: Semanalmente    Passo 5: Selecionar 4 dias por semana as 23hrs (ou em melhor horário disponível)    Passo 6: Iniciar um programa    Passo 7: Selecionar o arquivo commands.bat    Passo 8: Marcar opção para Abrir a caixa de propriedades quando concluir    Passo 9: Desmarcar a opção “Interromper a tarefa se ela for executada por mais de:”      Para baixar o arquivo, clique . |
| **Observações:** | Para mais informações:  **COMUNIDADE** [R@Tecnologia](http://fluig.totvs.com/portal/p/10097/post/rtecnologia-community/1639774)   **Canais de Atendimento:**  **Abertura de Chamados** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 8 – (Tecnologia), 2 – (Banco de Dados) |
