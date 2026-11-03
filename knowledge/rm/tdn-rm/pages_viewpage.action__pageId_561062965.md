---
content_hash: bf884f2221c49046ee00b11b79e5bbe4eff895aa8421b89ab22cced5c77ff4ad
fetched_at: '2026-06-29T00:10:47.874239+00:00'
page_id: '561062965'
product: rm
source: tdn-rm
title: Fórmula Visual - Certificado Digital Expirando
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=561062965
version: 48
---

## **Objetivo**

Este documento visa demonstrar como implementar uma fórmula visual no RM Gestão Fiscal para informar ao responsável quando o Certificado Digital utilizado na emissão da Nota Fiscal Eletrônica e demais rotinas estiver expirando seu prazo de validade e também desativar os certificados digitais já vencidos.

O passo a passo deve ser como base para criação da fórmula visual para atender está necessidade e nada impede em caso existir mais regras especificas da empresa de serem também incrementadas ou alteradas na fórmula visual.

[Documentação da Fórmula Visual - RM](http://tdn.totvs.com)

## **Passo a Passo**

**1 -** Inserir as consultas SQL para consultar os certificados digitais que estão vencendo e que estão expirados.

**1.1 -**Consulta SQL para buscar certificados digitais que estão vencendo conforme a parametrização

Está consulta busca no banco de dados os certificados digitais de uma determinada coligada que estão prestes a vencer de acordo com os números de dias definidos no parâmetro : DIASVENCIMENTO

Anexo: 

**1.2 -** Consulta SQL para buscar certificados digitais vencidos para desativa-los

Está consulta busca no banco de dados os certificados digitais de uma determinada coligada que estão vencidos para desativa-los na execução da fórmula visual.

Anexo: 

**2 -** Acessar o menu RM\Gestão Fiscal\Gestão\Fórmula Visual\Categorias para cadastrar uma categoria de fórmulas visuais da NF-e

Incluir nova categoria para ser utilizado como um agrupador de fórmulas visuais da NF-e, também é necessário informar os perfis de permissão desta categoria.

**2.1** **-** Em RM\Gestão Fiscal\Gestão\Fórmula Visual\Fórmula Visual  Inserir nova fórmula visual agrupadora de fórmulas para NF-e associando a categoria inserida no passo anterior.

**2.1 -** Seguindo no mesmo cadastro incluir uma nova fórmula visual desta vez associando a fórmula anterior. Nesta fórmula é que vamos implementar os Workflows da fórmula visual

**2.2 -** Fluxo da primeira parte da Fórmula Visual responsável por verificar os certificados ativos que estão Vencendo e informa o responsável por e-mail.

**2.2.1 -** A primeira atividade é uma atividade do tipo "Expressão" nela será parametrizado os dias de limite para que o RM avise o responsável do certificado digital, neste caso foi informado 50. Este valor será informado por parâmetro na consulta **SQL\_FV\_CERT**.

Após nomear a atividade deverá ser informado um valor inteiro no campo **Expressões**.

**2.2.2 -** A segunda atividade é uma atividade do tipo "Executar Consulta SQL" nela vamos associar a SQL código SQL\_FV\_CERT

Dica para associar a consulta SQL SQL\_FV\_CERT após arrastar a atividade "Executar Consulta SQL" para o fluxo de trabalho sequencial:  clicar com o botão direito sobre ela e selecionar a opção Selecionar Consulta SQL.

Também é necessário associar o valor informador na expressão anterior a parâmetro DIASVENCIMENTO.

O parâmetro CODCOLIGADA deve ser preenchido com o código da Coligada do contexto clicando nos três pontinhos e selecionando a opção abaixo:

**2.3 -**  Após a consulta SQL adicionar a atividade "Para cada Iteração", para que as linhas do retorno da consulta SQL sejam percorridas é necessário adicionar também a atividade "Sequência".

**2.3.1 -** Na atividade "Para cada Iteração" devemos configurar  a propriedade Lista de Items

**2.3.2 -** Associar no campo Rows das linhas retornadas da Consulta

**2.4 -** Dentro da atividade Sequência Vamos adicionar 2 atividades onde a primeira será uma Expressão onde vai ser informado os dados do certificado retornado da atividade "Para cada Iteração"  para a montagem do corpo do e-mail de aviso ao responsável.

**2.4.1 -** Preencher a propriedade Expressões como no exemplo abaixo, em Parâmetros ficam disponíveis os campos a serem utilizados de forma dinâmica.

**2.5 -** Para que o RM envie e-mail é necessário configurar o mesmo previamente:  

**2.6 -** A segunda atividade a ser adicionada é "Enviar E-mail", está atividade devemos configurar de fato o e-mail a ser enviado para o responsável e na atividade possui propriedades para este Fim.

Preencher o campo de assunto do E-mail como por exemplo "Aviso Certificado Vencendo" e destinatários com e-mail do responsável

**2.7 -** A propriedade Texto do e-mail deverá ser associado a atividade expressão anterior

**2.8 -** Neste Ponto é possível testar o se está enviado e-mail quando o certificado está vencendo, na atividade rmsExpActParametroDiasParaVencer configure o parâmetro da consulta SQL para por exemplo 50, ou seja, consultar certificados que vencem de hoje até 50 dias.

*Lembrando que você pode parametrizar sua regra de negócio da forma que bem entender.*

**2.8.1 -** Clique em Salvar e Executar.

*é boa prática ir salvando sua fórmula visual durante o desenvolvimento para não ter retrabalho.*

**2.8.2 -**A fórmula visual foi executada com sucesso!

**2.8.3 -** O e-mail foi enviado conforme o esperado;

**2.9 -** Incluir nova atividade "Executar Consulta SQL" está atividade deve ser associado a consulta SQL\_CERT\_INVALID. o parâmetro CODCOLIGADA deve ser informado com informação do contexto.

**3.0 -** Incluir atividade "Para Cada Iteração" e dentro dela incluir atividade de Sequência "*está atividade é necessária para iterar todas as linhas da consulta SQL*" .

**3.1 -** Dentro da atividade Sequência incluir atividade "Ler Registro", nesta atividade é necessário informar a propriedade nome do DataServer: **FisCertificadoDigitalData.**

**3.1.1 -** Na aba Propriedades clique no ícone amarelo e em CODCOLIGADA clique nos três pontinhos para selecionar o campo

**3.1.2 -** Selecione o campo AsShort do field CODCOLIGADA

**3.1.3 -** Faça o mesmo procedimento para IDCERTIFICADO

**3.1.4 -** os passos 3.1 até 3.1.2 é necessário para Ler o registro do certificado no Cadastro de Certificados Digitais que retornou da consulta.

**4 -** Incluir atividade Expressão que visa alterar o Status do campo Ativo para 0 "Zero".

**4.1 -** Clique no ícone amarelo e em Valor Calculado selecione o Field ATIVO

**4.1.1 -** na propriedade Expressões coloque o valor 0 "zero" para que o cadastro seja alterado.

**5 -** Incluir atividade Salvar Registro e na propriedade Atividade Ler informar rmsReadRecordActivity1

**6 -** Ao executar está fórmula visual ela terá como efeito desativar os certificados digitais que já estão Vencidos

Teste - Antes de Executar a fórmula visual

Teste - Depois de executar a fórmula visual implementada

**7 -** Agendar a fórmula visual para ser executada conforme necessidade, clicar na setinha e selecionar a opção Salvar e Agendar Execução

**7.1 -** Ao clicar no botão Salvar e Agendar Execução é exibida a tela abaixo e pronto só deixar o serviço ser executado automaticamente conforme a demanda que você necessita.
