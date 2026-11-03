---
content_hash: f9a848592b65e574675e04347a4a23878ca451d2d3095fadeb4bc03e60b37ca1
fetched_at: '2026-06-29T00:05:55.004989+00:00'
page_id: '118885895'
product: rm
source: tdn-rm
title: ALTERAÇÃO DE INICIALIZAÇÃO MENU NO PORTAL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=118885895
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.5x, 11.8X |
| **Processo** | **:** | Portal |
| **Subprocesso** | **:** | *Alterar a página inicial do portal* |
| **Data da publicação** | **:** | 07/02/2014 |

Para altear o menu inicial do portal, efetue as seguintes alterações:

No arquivo web.confg (C:\totvs\CorporeRM\Corpore.Net) altera a tag abaixo para True:

<add key="LoadDefaultMenuOnLogin" value="true" />

Após este procedimento, devemos efetuar alteração no arquivo Menu.xml, informando no código, qual Main deverá ser inicializado primeiro.

Para efetuar esta alteração, deverá ser copiado toda a árvore referente ao menu desejado.

 Abaixo, será executado a alteração do menu RH como exemplo:

Copie toda a árvore do menu .

Recortando toda a árvore referente ao menu RH, cole o mesmo para a primeira opção do arquivo menu.xml. Lembrando que o item <ID>INICIO<ID> é inalterado. Em nosso exemplo, a nova estrutura ficará conforme print abaixo:

Conforme imagem abaixo, a estrutura original inicia com “MainPortal”. Lembrando que o “MenuItem” é inalterado.

Recortando toda a árvore referente ao menu desejado, cole o mesmo para a primeira opção do arquivo menu.xml. Lembrando que o item <ID>INICIO<ID> é inalterado. Em nosso exemplo, a nova estrutura ficará conforme print abaixo:

Feito todo este procedimento, ao iniciar o portal, o menu escolhido será a primeira opção de exibição.

Dicas:

1. Apenas um usuário com conhecimento de desenvolvimento WEB deverá atuar neste processo;

2. Sempre efetue um backup do arquivo original;

3. Em caso de qualquer erro, o HelpDesk poderá solicitar a estrutura default do portal para testes.

|  |  |
| --- | --- |
|  | **Para maiores informações:**     **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha); |
