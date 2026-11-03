---
content_hash: 30d4a1acb825392b0a027a7bad861a0b6387dc5b0cfbf882aa81f2b4a7a0cfa3
fetched_at: '2026-06-29T00:08:13.302313+00:00'
page_id: '243662499'
product: rm
source: tdn-rm
title: CONFIGURAÇÃO DE BLOQUEIO POR ERRO AO LOGAR NO SISTEMA
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243662499
version: 3
---

# Configuração de bloqueio de usuário por erro ao logar no sistema

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 11.XX; 12.XX |
| **Ocorrência:** | Configuração de bloqueio de usuário por erro ao logar no sistema |
| **Ambiente:** | Parâmetros Globais |
| **Passo a passo:** | No RM, é possível configurar o número de tentativas de login para usuários, através do Menu Opções Parâmetros -> Globais.  **Nesse parâmetro será possível configurar o tempo que o usuário ficará bloqueado e quantas tentativas de login poderão ser realizadas antes de ser DESATIVADO.**  Configuração dos parâmetros pela nova MDI. Acesse a guia Ambiente – Menu Parâmetros – Globais. Aba Gerais:      O campo "Número de Tentativas de Login" é utilizado para o controle de tentativas de login permitidas para um usuário.  O campo "Tempo de Bloqueio do Usuário" utilizado para limitar um tempo mínimo em minutos de bloqueio para um usuário que excedeu as tentativas de login configuradas no primeiro campo.  Durante este tempo, o usuário não poderá nem mesmo requisitar uma troca ou lembrete de senha. Após este tempo, o usuário poderá fazer novas tentativas, bem como alterar ou recuperar a senha.    **Exemplo da utilização dos recursos:**  Em um cenário onde estejam configurados os campos da seguinte forma:    **Tempo de Bloqueio do Usuário: 2**  **Número de Tentativas de Login: 3**    Ao logar no RM, o usuário erra a senha por 3 vezes, será apresentada a mensagem:  "Usuário ou Senha inválidos! O usuário ou senha utilizados para login não são válidos para acesso ao sistema. Verifique se o código do usuário está digitado corretamente e redigite sua senha. Verifique se a tecla CAPS LOCK não está pressionada acidentalmente."   Após o tempo de bloqueio, que está configurado para 2 minutos, caso o usuário lembre a senha correta, poderá digitar a senha correta e automaticamente reativar o seu usuário.  Caso o usuário não lembre a senha correta, deverá solicitar a um usuário supervisor para ativar o seu usuário novamente. |
| **Observações:** | **Caso as tentativas sejam esgotadas, o usuário será reativado após a liberação de um usuário supervisor no sistema ou após o mesmo informar a senha correta ao logar novamente.** |
