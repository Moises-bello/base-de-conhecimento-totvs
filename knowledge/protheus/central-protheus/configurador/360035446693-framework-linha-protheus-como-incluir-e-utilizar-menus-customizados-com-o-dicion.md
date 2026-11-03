---
article_id: 360035446693
category: Configurador
content_hash: 4ba438cb44408954b1e8a8f89e29dcfd9f86e73abbd944d6418beac1cc861fed
fetched_at: '2026-06-28T22:42:18.945237+00:00'
product: protheus
section_id: 360000076767
source: central-protheus
title: Framework - Linha Protheus  - Como incluir e utilizar menus customizados com
  o dicionário no banco de dados
type: support-article
updated_at: '2026-02-23T19:51:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035446693-Framework-Linha-Protheus-Como-incluir-e-utilizar-menus-customizados-com-o-dicion%C3%A1rio-no-banco-de-dados
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17889124379543)** Tempo aproximado para leitura: **00:01:20 min  
  
Dúvida**Como incluir e utilizar menus customizados com o dicionário no banco de dados ?  
  
**Ambiente**MP – SIGACFG – A partir da versão 12.1.23  
  
**Solução**A partir da versão 12.1.23 existe de a possibilidade de utilização do dicionário de dados do **Protheus** incluído no banco de dados, para estes cenários o cliente não pode mais manipular os arquivos **XNU** da pasta system e nem alterar os menus padrões do Sistema, caso se altere o menu padrão via configurador o Sistema acaba quebrando a estrutura padrão do menu deixando menu desconfigurado, para utilização dos menus será necessário executar os passos abaixo:

Cenário de criação de um novo menu customizado

1- Acessar a rotina de menus no configurador e selecionar o menu padrão a ser alterado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046312373)

2-Clicar em adicionar para que o Sistema crie uma copia do menu padrão.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046312433)

3-Realizar as alterações desejadas e clicar em Gerar.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045452494)

4- Aguarde a finalização da geração do menu, feche a rotina e retorne ao menu do configurador.

5- A utilização do menu deve ser feita associando o menu via usuário ou grupo de usuários.

- Para vincular o menu a um usuário, acesse o usuário na rotina do **configurador > Usuário > Senhas > Usuários**. Selecione o usuário e clique em alterar.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046312693)

 -Para vincular a um grupo de usuários acesse o **configurado > Usuário > Senhas > Grupos**, posicione no grupo desejado e clique em alterar.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045453114)

Utilização de um Menu customizado já criado em outras versões do Sistema.

1-Copie o arquivo XNU para a pasta Protheus\_Data\System do Sistema, tenha certeza que o nome do arquivo não corresponde a nenhum menu padrão do Sistema.

2-Acesse a rotina de menus no configurador.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046312993)

3-Após este passo o menu já estará incluso no banco de dados, basta efetuar o Passo 5 da explicação anterior para efetuar sua vinculação.
