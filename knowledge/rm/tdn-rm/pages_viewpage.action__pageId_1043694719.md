---
content_hash: 30a2195065a1b4285cbd516ba47e6aefea73f499cb429015532f930c47b35a36
fetched_at: '2026-06-29T00:05:49.941533+00:00'
page_id: '1043694719'
product: rm
source: tdn-rm
title: Crédito Trabalhador via API do Governo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1043694719
version: 37
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Configuração E-Social**
4. **Configuração Adicional (Folha/Crédito Trabalhador)**
5. **Tela de Importação do Crédito do Trabalhador com API**
6. **Como funciona a Importação**
7. **Como funciona o parâmetro Multi-Thread**
8. **Configuração De/Para de Filiais**
9. **Links Úteis**
10. **Log Integrador**

## **01. VERSÕES**

**A partir dos patches:**

* 12.1.2506.324
* 12.1.2510.253
* 12.1.2602.167
* 12.1.2606.1 e superiores

## **02.****VISÃO GERAL**

Nesta página contém a descrição completa para realizar a Importação do Crédito Trabalhador via API do Governo. Esta funcionalidade está presente na mesma tela onde hoje já ocorre a importação via arquivo.

Porém, a habilitação da importação via API será conforme configuração prévia do TAF ou Middleware. Mais detalhes serão explicados nos tópicos a seguir.

Importação para meses anteriores e posteriores ao atual

Caso seja necessário importar um arquivo para meses anteriores ou posteriores ao atual, será necessário a importação manual (Via arquivo), como era feito anteriormente.

## **03. CONFIGURAÇÃO E-Social**

Para que seja possível importar via API, é necessário que as configurações do **TAF ou Middleware** estejam preenchidas.

Atenção!

Para correto funcionamento da importação via API, é extremamente necessário que seu TAF e TSS estejam atualizados com os seguintes pacotes:  
  
TAF  
  
12.1.2210:<https://r.totvs.io/p/1231440> ;  
12.1.2310:<https://r.totvs.io/p/1231437> ;  
12.1.2410:<https://r.totvs.io/p/1231438> ;  
12.1.2510:<https://r.totvs.io/p/1231439> ;  
  
Com esses pacotes os endpoints, serão atualizados e inseridos na API List:/esocial/v1/wstafcredtrab/middleware

TSS  
  
12.1.2210:<https://r.totvs.io/p/1224405> ;   
12.1.2310:<https://r.totvs.io/p/1224403> ;   
12.1.2410:<https://r.totvs.io/p/1224404> ;   
12.1.2510:<https://r.totvs.io/p/1224406> ;  
  
Com esses pacotes do TSS, o serviço **TSSWSCONSIGNADO**será inserido na lista de serviços, permitindo o correto funcionamento da funcionalidade.

No parametrizador (Folha de Pagamento / 06.07 ESocial).

Conforme imagem a seguir, para importar via API são requisitos **obrigatórios** o preenchimento dos campos: Servidor, Porta, Usuário, Senha, (Código Filial TAF ou De/Para Filiais).

Todas as demais configurações são para uso do e-social e outras funcionalidades.

Exemplo Configuração TAFExemplo Configuração Middleware

## **04.****CONFIGURAÇÃO ADICIONAL**

No Parametrizador, em Folha de Pagamento/Folha Normal/Crédito Trabalhador, já existem hoje outras configurações pertinentes à importação.

Foi adicionado um novo agrupador chamado "Integração".

Neste agrupador temos dois campos:

* **Chamada API utilizando paralelismo**:  Quando for marcado, ele irá criar uma thread para cada coligada, para que todas chamem a api do governo simultâneamente. Quando todas finalizarem, o processo finaliza. Este recurso só deve ser utilizado em clientes que possuam elevados nºs de coligadas e/ou cuja chamada da API seja demorado.
* **Ambiente ( Produção e  Homologação)**: Em casos de utilização do Middleware, será necessário a marcação da flag de utilização do ambiente de produção ou desenvolvimento. Caso não esteja marcado nenhum o default é 2 - homologação.

Observação

O retorno da API é O mesmo sendo TAF ou Middleware. O que muda são os parâmetros enviados, que no caso do Middleware é enviado dois parâmetros a mais (Servidor TSS e Ambiente). Mas o formato do retorno é idêntico.

Observação 2

Caso não exista configuração TAF ou Midleware, este novo agrupador com os campos novos não irão aparecer no Parametrizador.

# **05.****TELA DE IMPORTAÇÃO DO CRÉDITO TRABALHADOR COM API**

Um novo campo na tela chamado "Importação via API" vai ser exibido, do tipo checkbox.

Porém, só será exibido se houver configuração TAF ou Middleware informados no parametrizador, conforme o tópico 3. Do contrário, o campo não será exibido na tela e não haverá mudança para o usuário.

Ao ser marcado, os demais campos referente ao carregamento de arquivo serão desabilitados. Validações do carregamento do arquivos também não serão executadas.

Ao avançar, deve-se selecionar a(s) coligada(s) desejadas e depois clicar em "Executar".

# **06. COMO FUNCIONA A IMPORTAÇÃO**

Ele irá pegar as coligadas selecionadas na tela.

Para cada coligada, busca os dados parametrizados, sendo eles: 

| Do sistema: |
| --- |
| Mês competência atual do sistema |
| Ano competência atual do sistema |
| Multi-Thread habilitado (bool) |

| Dados TAF (Se configurado TAF) |
| --- |
| Servidor e porta TAF |
| Filial TAF |
| Usuário e senha |
| Usa DePara Filial (RM X TAF) |

| Dados Middleware (Se configurado Middleware) |
| --- |
| Servidor e porta middleware |
| Usuário e senha |
| Ambiente (1 - Produção - 2 Homologação) |

# **06.1 O QUE A API RETORNA**

A API retorna dados no formato JSON. Dentre os vários campos que ela retorna, o mais importante que está sendo extraído pelo sistema é o campo "**Arquivo**".

Ao ser descriptografado, o campo arquivo se transforma no mesmo conteúdo do arquivo físico Json já importado pelas empresas:

A partir deste ponto em diante utiliza-se a mesma lógica já existente anteriormente, que é chamada na leitura dos arquivos.

Esta lógica irá validar **os mesmos campos obrigatórios da importação "manual" já existente,** extrair os dados necessários, definir o evento e no final atualizar ou incluir o empréstimo.

Como resultado, ao final do processamento devemos visualizar os mesmos dados de quando está sendo feito via Arquivo:

## **07.** **COMO FUNCIONA O PARÂMETRO HABILITAR MULTI-THREAD**

Este parâmetro pega a lista de coligadas que foi selecionado na tela e dispara para todas elas a chamada na API do TAF e/ou Middleware de forma simultânea.

A lógica fica aguardando o retorno de todas as chamadas e quando todas finalizam, ele inicia a importação dos dados.

## **08.** **CONFIGURAÇÃO DE/PARA DE FILIAIS**

No parametrizador, nas configurações do TAF, existe a possibilidade de informar a filial do TAF, (campo Código da Filial TAF).

Este dado vai ser utilizado para montar a URL que chama a API, conforme descrito no tópico 6.

No entanto, caso o checkbox "Utilizar relacionamento Filial RM X TAF p/ eventos de funcionario" esteja marcado, a filial será buscada em outro lugar, conforme mostra a 2ª fugra abaixo:

Abaixo é onde fica o cadastro de Filial RM X Filial TAF.

Portanto, caso não seja informado uma filial única e tenha que ir no cadastro puxar o De/Para, o sistema irá montar a URL e chamar a API para cada filial encontrada.

No final, vai juntar o retorno obtido e efetuar a importação de uma única vez.

Obs: Neste cenário, todas as filiais pertencem a mesma coligada.

## **09. LINKS ÚTEIS**

Site que formata JSON → [https://jsonformatter.curiousconcept.com/#](https://jsonformatter.curiousconcept.com/)

 Site que Decodifica o valor do campo criptografado: <https://www.base64decode.org/>

## **10. LOG INTEGRADOR**

No próprio RM temos uma rotina que monitora chamadas ao TAF.

Menu: Configurações/Log de Integração.

Basta selecionar as opções nos combos referente à API e ativar o LOG.

No ícone de exclamação ao final da linha podemos clicar para ver os detalhes.

Nos detalhes conseguimos ver a URL chamada e o retorno recebido:

Neste retorno, extraímos o conteúdo do campo "Arquivo" e descriptografamos os dados (pode ser utilizado o site genérico que faz isso, conforme tópico 9).

O conteúdo depois que descriptografado vira o arquivo json já conhecido.
