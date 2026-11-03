---
content_hash: b416ffa28c28aef0e3ea7bc3a0f446bd0064dbca79cd2a32f15651218114d050
fetched_at: '2026-06-29T00:08:45.377246+00:00'
page_id: '311628677'
product: rm
source: tdn-rm
title: Utilizando Gatilhos de Processos
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+Gatilhos+de+Processos
version: 18
---

# Índice

---

.\*ndice:

# Objetivo

---

       Neste documento será explicado quando são executadas fórmulas visuais com gatilhos de processos, e serão apresentados exemplos simples para cada um deles.

Em todos exemplos foram apresentadas fórmulas visuais simples.Consulte o documento  para mais informações sobre outras atividades de Fórmula Visual.

# Gatilho Antes de submeter o processo e Após submeter o processo

---

**Gatilho Antes de Submeter o Processo:** Utilizando o gatilho Antes de Submeter o Processo, a fórmula visual será executada antes do sistema colocar o processo na fila para execução do job.

     **Gatilho Após Submeter o Processo:** Utilizando o gatilho Após Submeter o Processo, a fórmula visual será executada após o sistema colocar o processo na fila para execução do job e antes da execução do mesmo.

     A seguir será apresentado um exemplo, onde foram criadas duas Fórmulas Visuais gerando no mesmo arquivo de log o horário do computador. As fórmulas irão armazenar o horário da sua execução.

falseExemploPasso 1Passo 1Passo 1

1º - Crie a fórmula Visual que deseja executar antes da inclusão do processo na fila de execução de jobs.

No exemplo abaixo, adicionamos duas atividades: Consulta SQL e Gerar log, respectivamente.

A consulta SQL retorna a hora, minuto, segundo do computador e o log irá gerar um arquivo em C:\RM\Atual\Processos\FV (Esse caminho corresponde ao local de instalação do seu ambiente). 

Passo 2Passo 2Passo 2

2º - Configure o gatilho Processos - Antes de submeter  o processo. Neste exemplo utilizamos o processo Cópia de Permissões de Usuários.

Passo 3Passo 3Passo 3

3º - Para vermos a execução do gatilho, acesse o menu Serviços Globais > Segurança > Usuários. Selecione um usuário para receber a cópia de permissões, acesse o menu Processos > Cópia de Permissões de Usuários. Clique em Próximo, selecione o usuário de origem, clique em Avançar, Executar.

Neste instante a fórmula visual será executada. Ou seja, o processo de cópia de permissão de usuário nem entrou para a fila de execução de jobs ainda:

Passo 4Passo 4Passo 4

4º - Agora criaremos outra Fórmula Visual  que gera no mesmo arquivo de log o horário da sua execução com o gatilho Após submeter o processo. Ela será executada após a inclusão do processo na fila de execução de jobs e antes da sua execução.

No exemplo abaixo, adicionamos duas atividades: Consulta SQL e Gerar log, respectivamente.

A consulta SQL retorna a hora, minuto, segundo do computador e o log irá gerar um arquivo em C:\RM\Atual\Processos\FV (Esse caminho corresponde ao local de instalação do seu ambiente). 

Passo 5Passo 5Passo 5

5º - Configure o gatilho Processos - Após submeter  o processo. Neste exemplo utilizamos o processo Cópia de Permissões de Usuários.

Passo 6Passo 6Passo 6

6º - Mantendo as Fórmulas Visuais vistas neste exemplo ativas, acesse o menu Serviços Globais > Segurança > Usuários. Selecione um usuário para receber a cópia de permissões, acesse o menu Processos > Cópia de Permissões de Usuários. Clique em Próximo, selecione o usuário de origem, clique em Avançar, Executar.

Neste instante as fórmulas visuais serão executadas. Observe que o arquivo de LOG será criado:

# Gatilho Antes da execução e Após a execução

---

**Gatilho Antes da Execução:** Utilizando o gatilho Antes da Execução, a fórmula visual será executada antes do sistema executar o processo. Note que o processo está pronto para execução, já está em primeiro lugar na fila para execução de jobs.

**Gatilho Após a Execução:** Utilizando o gatilho Após a Execução, a fórmula visual será executada após o sistema executar o processo.

    A seguir será apresentado um exemplo, onde foram criadas duas Fórmulas Visuais gerando no mesmo arquivo de log o horário do computador. As fórmulas irão armazenar no log o horário da sua execução.

falseExemploPasso 1Passo 1Passo 1

1º - Crie a fórmula Visual que deseja executar antes da execução do processo.

No exemplo abaixo, adicionamos duas atividades: Consulta SQL e Gerar log, respectivamente.

A consulta SQL retorna a hora, minuto, segundo do computador e o log irá gerar um arquivo em C:\RM\Atual\Processos\FV (Esse caminho corresponde ao local de instalação do seu ambiente).

Passo 2Passo 2Passo 2

2º - Configure o gatilho Processos - Após submeter  o processo. Neste exemplo utilizamos o processo Cópia de Permissões de Usuários.

Passo 3Passo 3Passo 3

3º - Para vermos a execução do gatilho, acesse o menu Serviços Globais > Segurança > Usuários. Selecione um usuário para receber a cópia de permissões, acesse o menu Processos > Cópia de Permissões de Usuários. Clique em Próximo, selecione o usuário de origem, clique em Avançar, Executar.

Neste instante a fórmula visual será executada. Ou seja, o processo de cópia de permissão de usuário ainda não foi executado, mas já está pronto na fila de execução de jobs. Observe que o arquivo de LOG será criado antes da execução do processo:

Passo 4Passo 4Passo 4

4º Agora criaremos outra Fórmula Visual  que gera no mesmo arquivo de log o horário da sua execução com o gatilho Após a Execução.

Crie a fórmula Visual que deseja executar após a execução do processo.

No exemplo abaixo, adicionamos duas atividades: Consulta SQL e Gerar log, respectivamente.

A consulta SQL retorna a hora, minuto, segundo do computador e o log irá gerar um arquivo em C:\RM\Atual\Processos\FV (Esse caminho corresponde ao local de instalação do seu ambiente).

Passo 5Passo 5Passo 5

5º - Configure o gatilho Processos - Após submeter  o processo. Neste exemplo utilizamos o processo Cópia de Permissões de Usuários.

Passo 6Passo 6Passo 6

6º - Mantendo as Fórmulas Visuais vistas neste exemplo ativas, acesse o menu Serviços Globais > Segurança > Usuários. Selecione um usuário para receber a cópia de permissões, acesse o menu Processos > Cópia de Permissões de Usuários. Clique em Próximo, selecione o usuário de origem, clique em Avançar, Executar.

Neste instante as fórmulas visuais serão executadas. Observe que o arquivo de LOG será criado:

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.44 ou Superiores

false

**Processo:** Gatilhos de Processos

falsefalse

**Status:** Finalizado

false

**Data:** 07/11/2017

false

**Autores:**
