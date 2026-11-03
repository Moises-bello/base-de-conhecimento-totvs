---
content_hash: 8f80ab1d1bf246484263e8f73617d599d534173526573e155a22aa9d7f3df7f6
fetched_at: '2026-06-29T00:11:38.256426+00:00'
page_id: '782325525'
product: rm
source: tdn-rm
title: Como Preparar o Ambiente para Testes
type: documentation
url: https://tdn.totvs.com/display/LRM/Como+Preparar+o+Ambiente+para+Testes
version: 8
---

Antes de realizar testes no novo PDC é necessário realizar as etapas abaixo para preparar o ambiente para teste.

## Guia passo a passo

1. Pelo Windows Explorer **crie uma** **nova pasta** (pode ser criada em qualquer local e com qualquer nome) e **entre** nessa pasta;
2. Clique na barra de endereço da pasta criada, apague o endereço dela, digite **cmd** no lugar e pressione **enter**;
3. Na janela do DOS que abriu:
   1. Digite **git clone <https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/portalclienteimoveis>** e espere terminar a execução do comando;¹
   2. Digite **cd portalclienteimoveis**;
      1. Caso na issue informe uma branch especifica onde o código está, digite **git checkout nome\_da\_branch\_informada\_na\_issue**; ²
   3. Digite **npm install**;³
   4. Digite **ng serve -o** e será aberto o navegador automaticamente para teste;£

Após os devidos testes a pasta criada poderá ser excluída.

## **Atenção:**

A partir da versão 2502 o portal passá a compor no folder wwwroot da bin da aplicaçao RM e ser disponibilizado pelo Host, na porta a ser definida no webConfig dentro do folder portalclienteimoveis e com isso ao subir o host sem alterar está porta, poderá acessar pela padrão já existente no arquivo (8051).  
o caminho para acessar o portal disponibilizado no wwwroot é:  
  
<http://localhost:8051/portalclienteimoveis/>

¹Caso o comando **git** não esteja reconhecido, baixar e instalar em: <https://git-scm.com/downloads>.

²Substituir o texto **<nome\_da\_branch>** pelo nome da *branch* informada na issue.

³Caso o comando **npm** não esteja reconhecido, baixar e instalar o Node.js em: <https://nodejs.org/en/download>.

£Caso o comando **ng** não esteja reconhecido, execute o comando "**npm install -g @angular/cli**" e depois repita o passo.
