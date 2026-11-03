---
content_hash: adbf973e152a0952d7aefc62512e4a578eded17974264d89a70c710a8c617d68
fetched_at: '2026-06-29T00:09:52.240598+00:00'
page_id: '438283602'
product: rm
source: tdn-rm
title: Bloqueio do RM por Inatividade do Usuário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=438283602
version: 2
---

# Índice

---

.\*ndice

# Objetivo

---

        O objetivo deste documento é demonstrar como explicar como funciona e como é feita a parametrização de bloqueio do RM por inatividade do usuário.

# Como Funciona

---

        O sistema RM.exe disponibiliza o bloqueio da estação após um tempo pré-determinado, afim de que se o usuário se ausentar da frente  de seu computador, outro usuário mal intencionado não possa utilizar as credenciais deste para executar operações no RM.

        Após realizar login no ERP e tendo ficado inativo, isto é, sem pressionar qualquer tecla do teclado ou sem movimentar o mouse durante o tempo mínimo e máximo, a estação é bloqueada. A tela de login sobrepõe as demais telas abertas, independente da execução de alguma tarefa.

        Quando o usuário retornar, será necessário informar novamente sua senha de acesso e o sistema será desbloqueado para uso, sem prejuízo dos processos que porventura estiverem sendo executados em segundo plano. Trata-se de uma funcionalidade semelhante ao bloqueio de estação do Windows.

# Parametrização Padrão

---

        Os tempos mínimo e máximo são variáveis. Por padrão vem definido em 10 minutos (tempo mínimo) e próximo de 20 minutos (tempo máximo).  Esses tempos estão na razão: tempo máximo = tempo mínimo x 2.

        Para alterar essa configuração padrão, acesse: Ambiente | Parâmetros Globais | Configurações Públicas | Tempo espera (min) p/ lock.  Altere o tempo em minutos e salve.

false

As alterações serão válidas apenas quando o usuário realizar logoff/login na aplicação.

# Permissões para Desbloqueio de Estação

---

        Caso a estação esteja bloqueada e outro usuário precise utilizá-la, é possível encerrá-la, desde que este usuário possua permissão para desbloqueio de estação.

        Para conceder tal permissão, acesse o módulo de Serviços Globais | Segurança | Perfis, em seguida edite o perfil do usuário e clique em "Acesso a Menus | Serviços Globais | Segurança | Acesso | Usuários | efetuar logoff em estação bloqueada".

Estando a estação bloqueada, Na tela de login clique no botão Trocar, informe usuário e senha, e clique no botão Sair. O RM será encerrado.

falsefalse

**Produto:** Framework

false

**Versão:** 11.XX, 12.01.18 ou superiores

false

**Processo:** Bloqueio do RM por Inatividade do Usuário

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
