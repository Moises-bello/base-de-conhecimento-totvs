---
content_hash: 248f4d5942196d7ede0058b2c5893b27965718b0ffaecc5e2e4fa00fa937a14a
fetched_at: '2026-06-29T00:05:54.079504+00:00'
page_id: '107382434'
product: rm
source: tdn-rm
title: Configuração de bloqueio de usuário por erro ao logar no sistema
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=107382434
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                     **Versão:**11.XX |
| **Processo** | **:** | Parâmetros Globais |
| **Subprocesso** | **:** | Configuração de bloqueio de usuário por erro ao logar no sistema |
| **Data da publicação** | **:** | 10/12/2013 |

No RM é possível configurar o número de tentativas de login para usuários, através do Menu Opções Parâmetros -> Globais.

O campo "Número de Tentativas de Login" é utilizado para o controle de tentativas de login permitidas para um usuário.

O campo "Tempo de Bloqueio do Usuário" utilizado para limitar um tempo mínimo em minutos de bloqueio para um usuário que excedeu as tentativas de login configuradas no primeiro campo.   
 Durante este tempo, o usuário não poderá nem mesmo requisitar uma troca ou lembrete de senha. Após este tempo, o usuário poderá fazer novas tentativas, bem como alterar ou recuperar a senha.

**Configuração dos parâmetros pela nova MDI:**

**Acesse a guia Ambiente – Menu Parâmetros – Globais:**

**Nesse parâmetro será possível configurar o tempo que o usuário ficará bloqueado e quantas tentativas de login poderão ser realizadas antes de ser DESATIVADO.**

**OBS.: Caso as tentativas sejam esgotadas, o usuário será reativado após a liberação de um usuário supervisor no sistema.**

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
