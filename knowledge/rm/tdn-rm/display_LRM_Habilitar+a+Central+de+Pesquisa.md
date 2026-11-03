---
content_hash: 1f445a84febcf3994b8ebb6a9ad506f363dd77470c69ba9ff7252c9aba25b272
fetched_at: '2026-06-29T00:11:27.562241+00:00'
page_id: '727360372'
product: rm
source: tdn-rm
title: Habilitar a Central de Pesquisa
type: documentation
url: https://tdn.totvs.com/display/LRM/Habilitar+a+Central+de+Pesquisa
version: 3
---

## **Introdução**

 A central de pesquisa é um novo recurso desenvolvido pela TOTVS, que possibilita aos usuários da nova MDI a buscarem dentro do sistema informações de várias tabelas em uma só pesquisa.

## **Desenvolvimento/Procedimento**

O recurso Central de Pesquisa está disponível do lado direito da nova MDI.  
    
 

Inicialmente a Central de pesquisa estará desabilitada e irá informar a seguinte mensagem:  
   
“Essa base de dados não tem o serviço de busca de texto avançado habilitado. Verifique na documentação do seu SGBD para saber como habilitar este serviço.”  
   
Essa mensagem ocorre, pois são necessárias configurações no Banco de Dados e também no sistema. Para configurarmos a Central de Pesquisa, é necessário ativarmos o FULL TEXT SEARCH no Banco de Dados. Importante lembrar que o serviço do Windows SQL Full-text, também deve estar instalado e Iniciado antes de fazer essa configuração.  
   
O comando a seguir, mostra se a base em questão está ou não com o FullText Enable.

c#RDark

Notamos que não encontramos a informação IsFullTextEnabled no texto acima. Para incluirmos essa opção, iremos executar o comando abaixo:

c#RDark

Caso o sistema esteja aberto, feche-o e entre novamente. Após novo login, note que a opção agora da Central de Pesquisa não apresta mais o X com a informação anterior.  
   
A partir desse momento, poderemos configurar quais serão as tabelas que comporão o nosso catalogo de pesquisa. Clique no Botão Configurar da parte inferior da Central de Pesquisa para iniciar o *Wizard.*

Selecione as tabelas e consequentemente os campos desejados. Na nossa configuração, deixaremos todas as tabelas marcadas. Seguiremos clicando no botão Avançar.

Essa é a tela padrão de Processo, basta deixar marcada a opção “Agora” e seguiremos clicando no botão Executar

Após o processo finalizado, será necessário logar no sistema novamente para que as configurações entrem em vigor.  
   
Agora a Central de Pesquisa ficará com essa aparência:

Podemos agora realizar uma pesquisa por qualquer informação e ela será buscada em todos os campos que havíamos selecionado na etapa de configuração.  
   
Pesquisando pela palavra “joão”, encontramos em 7 tabelas diferentes a informação desejada.

Podemos então expandir algum dos grupos acima e dar um duplo clique com o mouse no registro para abrirmos a visão correspondente.
