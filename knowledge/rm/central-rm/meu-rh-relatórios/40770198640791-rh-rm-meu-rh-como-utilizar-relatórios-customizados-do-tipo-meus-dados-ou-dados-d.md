---
article_id: 40770198640791
category: Meu RH - Relatórios
content_hash: ba531927a98a4c682dd9f56a7baca17171fa1c3b5a32fc1925c29e16d9fae8b1
fetched_at: '2026-06-28T22:47:30.975309+00:00'
product: rm
section_id: 1500000861762
source: central-rm
title: RH - RM - Meu RH - Como utilizar relatórios customizados do tipo "Meus dados"
  ou "Dados da minha equipe" no Meu RH?
type: support-article
updated_at: '2026-05-27T18:46:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40770198640791-RH-RM-Meu-RH-Como-utilizar-relat%C3%B3rios-customizados-do-tipo-Meus-dados-ou-Dados-da-minha-equipe-no-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40770198611735) Tempo aproximado para leitura: **00:03:00min**  
  
**Dúvida**  
Como utilizar relatórios customizados do tipo **"Meus dados"** ou **"Dados da minha equipe"** no Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH -Todas as versões  
  
**Solução**  
Relatórios utilizados no RM via **RM Reports** podem não funcionar no **Meu RH**, pois a execução no Meu RH exige uma estrutura específica. Diferente do RM Reports, o Meu RH não possui suporte para definição de filtros antes da geração do relatório. Por esse motivo, é necessário adequar o relatório ao padrão compatível com o Meu RH. A seguir, apresentamos as orientações sobre o funcionamento e a estrutura necessária para utilização de relatórios no Meu RH.  
  
Para que o relatório funcione corretamente no Meu RH, é necessário estruturá-lo utilizando a tabela de funcionário (**PFUNC**) como tabela master. A passagem de parâmetros para a consulta SQL deve ser realizada obrigatoriamente através dos campos retornados desta estrutura principal.

A estrutura funcionará para ambos os tipos de relatório, utilizando a chapa do usuário logado como parâmetro base para a execução:

* **Tipo "Meus dados":** O sistema retornará exclusivamente os dados do próprio colaborador que está executando a geração do relatório.
* **Tipo "Dados da minha equipe"**: O sistema retornará os dados dos subordinados vinculados à chapa logada, respeitando a hierarquia definida previamente no cadastro da estrutura de chefe/supervisor.

A seguir, exemplificamos o passo a passo de como realizar a passagem de parâmetros em um relatório:

1. Acesse a edição do relatório e, na estrutura, defina o **Detalhe principal** (Detalhe 1) tendo como tabela **master** a **PFUNC**, contendo os campos essenciais como **CHAPA** e **Código da Coligada.**
2. Selecione o campo chave que deseja passar como parâmetro para a consulta SQL e verifique o nome exato do componente através da **Grade de Propriedade**s (por exemplo: **parametro1, parametro2**).  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40770187675159)  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40770198617367)
3. Crie um Sub-Detalhe para inserir a consulta SQL desejada. Na cláusula WHERE da consulta, utilize o nome do campo chave verificado no passo anterior como parâmetro. Exemplo:

   `pfunc.CHAPA =:parametro1`  
   `AND pfunc.CODCOLIGADA =:parametro2`  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40770198618775)
4. Após finalizar a estrutura, retorne à tela de visão dos relatórios RM Reports e edite o cadastro do relatório utilizado. No campo **"Tipo"**, selecione a opção **"Meus dados"** ou **"Dados da minha equipe"**, de acordo com o objetivo do relatório, e salve as alterações.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40770198619415)

Exemplo da geração do relatório no Meu RH:

**Meus Dados** (Imprime os dados da chapa logada):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40770198620567)

**Dados da minha equipe**(Imprime os dados dos subordinados da chapa logada, considerando a estrutura chefe/supervisor)**:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40770187687191)

**Importante:**A estrutura exemplo deste relatório customizado está disponível nos itens anexados e deve ser utilizada apenas como referência.

A ausência da passagem de parâmetros ou configurações incorretas na estrutura do relatório podem ocasionar:

* **Erros genéricos durante a geração;**
* **Relatórios exibidos em branco;**
* **Inconsistências na apresentação das informações.**

Ressaltamos que o suporte padrão não contempla análise, validação ou correção de estruturas customizadas de relatórios.

Caso ocorram dificuldades na configuração ou comportamentos inesperados na geração do relatório, e não seja possível realizar os ajustes necessários, recomendamos acionar o apoio da Consultoria TOTVS (serviço tarifado), que poderá auxiliar na análise e adequação da estrutura customizada do relatório.  
  
**Saiba Mais:**

[Cross Segmentos - Backoffice RM - BI - Como criar um novo relatório no RM Reports ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7399466927255-Cross-Segmentos-Backoffice-RM-BI-Como-criar-um-novo-relat%C3%B3rio-no-RM-Reports)

[Cross Segmentos - Backoffice RM - BI - Passagem de parâmetro através de campos da base na estrutura do relatório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044956914-Cross-Segmentos-Backoffice-RM-BI-Passagem-de-par%C3%A2metro-atrav%C3%A9s-de-campo-da-base?source=search)
