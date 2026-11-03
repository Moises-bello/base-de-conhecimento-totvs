---
content_hash: 1fcac8a1d247260d50fb52feeb100e9b8c44067bbb4819eb33a900a526f42c95
fetched_at: '2026-06-29T00:05:54.241802+00:00'
page_id: '1077449290'
product: rm
source: tdn-rm
title: TOTVS RESPONDE  RM - API Crédito do Trabalhador - 08/06/2026
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1077449290
version: 5
---

A API está disponível no produto padrão, basta atualizar o patch disponível.

## **Gravação:**

## 

## **FAQ**

Material criado com o objetivo de compartilhar os principais questionamentos realizados no evento  **TOTVS RESPONDE  RM - API Crédito do Trabalhador**, realizado no dia 08 de Junho de 2026.

1. **Documentação e Atualização do Produto**
2. **Importação via API**

## **01.****Documentação e Atualização do Produto**

**1.1.** **Poderia disponibilizar o link do TDN referente a este assunto?**

Sim, segue link da documentação completa sobre a API do Crédito do Trabalhador

**1.2.** **A API está disponível a partir de qual versão do RM?**

Está disponível a partir da 12.1.2506, veja a partir de quais patches acessando o TDN:

**1.3.** **Atualização do TAF e TSS, ambas serão necessárias? Inclusive para quem utiliza o Middleware?**

Sim, ambas serão necessárias, o Middleware utilizará o endpoint do TAF e o serviço do TSS.

## **02.** **Importação Via API**

**2.1.** **Se eu deixar a opção de paralelismo ativada no parâmetro, mas quiser importar apenas uma empresa no momento, posso?**

Pode sim, a opção permite utilizar a importação para multi-coligadas mas não exclui a opção de importação individual.

**2.2.O usuário terá que entrar na tela de importação do mês?**

Sim, para realizar a importação via API será necessário entrar na tela e solicitar a comunicação com a API.

**2.3.** **É possível criar JOB para leitura da API de forma automática?**

Atualmente não é possível criar JOB, iremos disponibilizar em breve.

**2.4.** **Atualmente realizamos a importação via Json, o processo vai mudar?**

Não vai mudar, vai manter as mesmas opções de importação. Só vai ter mais uma possibilidade de importar, sem a necessidade de baixar um arquivo. Será pela integração do Governo via API.

**2.5.** **Será obrigatório utilizar a API??**

Atualmente não. Um novo campo na tela chamado "Importação via API" vai ser exibido, do tipo check box.

Porém, só será exibido se houver configuração TAF ou Middleware informados no parametrizador, conforme o tópico 3. Do contrário, o campo não será exibido na tela e não haverá mudança para o usuário.

Ao ser marcado, os demais campos referente ao carregamento de arquivo serão desabilitados. Validações do carregamento do arquivos também não serão executadas.

**2.6.** **API já é essa ferramenta ou teremos que adquirir da Totvs ou de terceiros, por exemplo?**

A API está disponivel no produto padrão, basta atualizar o patch disponivél.

**2.7.** **O campo Competência continua sendo atualizado no cadastro do empréstimo?**

Sim, Segue documentação sobre o assunto:

**2.8.** **Como fica a importação para fins de provisão de férias?**

O conceito da provisão não sofreu alteração, somente a forma de ler o arquivo do crédito do trabalhador.

**2.9.****Caso o Governo solicitar para importar novamente, será possível via API?**

Sim, poderá reprocessar a importação via API.

**2.10.** **A API incluirá automaticamente os zeros à esquerda no código do banco. Exemplo: código ‘1’ será convertido para ‘001’.?**

Sim, na verdade isso é um serviço que já existe hoje, essa mascara é configurada no parametrizador, a importação via API utiliza o mesmo padrão já existente hoje.

**2.11.** **Como a requisição é feita para o governo pelo RM?**

O RM utiliza os serviços do TAF / Middleware e o TAF / Middleware, utilizamos os serviços do TSS. Podemos visualmente ver como é montado a URL no item 10 do TDN  em Detalhes do Log. Onde está grifado em vermelho, é exibido a URL de requisição.

**2.12.** **É possível filtrar a filial para importação?**

Atualmente não.

**2.13.** **Se der erro na importação para apenas alguns funcionários, é possível realizar a importação novamente?  Será desconsiderado o que já foi importado?**

Nesse caso será importado todos os dados novamente, caso não haja nenhuma alteração nos funcionários que já haviam sido importados, serão apenas incluidos os que deram erro ou novos contratos.

**2.14.** **Como o sistema do governo irá entender o mês de competência que quero importar?**

Será enviado pela competência configurada do sistema.

**2.15.** **Hoje ainda precisamos criar vários eventos para o desconto, já há alguma previsão de mudar isso para um único evento de desconto?**

A necessidade de criar vários eventos vem do eSocial, para que sejam enviados separadamente por contrato.

**2.16.** **No caso, se não tiver nenhuma informação de empréstimo, vai retornar alguma informação de " não tem dados " a importar ?**

Não.

**2.17.** **No momento da leitura da API,  está gerando o erro "Falha ao efetuar a requisição. URI Requisitad", como devo proceder?**

1º - Conferir URL TAF ou Middleware (faça teste de conexão)  
2º - Conferir URL TSS (Se necessário atualizar certificado)  
3º - Conferir Endpoint na APILIST  
4º - Conferir se existe o serviço **TSSWSCONSIGNADO** no TSS

**2.18.** **O consumo da API valida algum certificado/procuração da empresa?**

Sim, consome o mesmo certificado utilizado para recebimento das informações do eSocial, o A1.

## **04.** **Documentações**

<https://tdn.totvs.com/pages/releaseview.action?pageId=946423249>

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/33227187529495-RH-RM-FOP-D%C3%BAvidas-frequentes-Cr%C3%A9dito-do-Trabalhador>
