---
content_hash: 93d378228006a08e86841de8469efff6b7461e3b50b14d5c902d4d054566e656
fetched_at: '2026-06-29T00:12:10.120295+00:00'
page_id: '951328154'
product: rm
source: tdn-rm
title: Período de Apuração - Smart UI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=951328154
version: 87
---

**A partir das Versões:**

* [DT - Smart UI - Período Apuração eSocial](https://tdn.totvs.com/pages/viewpage.action?pageId=944246951)

## **CONTEÚ****DO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Neste registro, são estabelecidas as definições relacionadas ao período de movimentação que será enviada ao eSocial. O período de apuração corresponde à competência da movimentação a ser enviada ao eSocial.

O sinalizadores do Período de Apuração são:

* **Mensal:** movimentação da folha normal, utilizado mensalmente na geração do evento S-1299 - Fechamento dos Eventos Periódicos.
* **Anual:** apenas para o 13º Salário Anual, utilizado no mês de dezembro de cada ano na geração do evento S-1299 - Fechamento dos Eventos Periódicos.

## **02. EXEMPLO DE UTILIZAÇÃO**

Disponibilizamos a tela do **Período de Apuração** utilizando a tecnologia **Smart UI** a partir da versão **12.1.2510**. Essa implementação trouxe uma atualização visual para a página, aprimorando não apenas sua aparência, mas também a forma como ela é utilizada, proporcionando uma experiência mais moderna e eficiente.

Período de Apuraçãotrue1Periodo de Apuração

A tela **Período de Apuração** tem como objetivo registrar as informações que serão geradas no evento **S-1299 - Fechamento dos Eventos Periódicos** do eSocial.

Este evento refere-se ao encerramento da transmissão dos eventos periódicos dentro do período de apuração. Nesse momento, são consolidadas todas as informações enviadas nos eventos **S-2299**, **S-2399** e **S-1200 a S-1270**.

A aceitação deste evento pelo eSocial, após as devidas validações, conclui a totalização das bases de cálculo relacionadas à remuneração dos trabalhadores, bem como às informações sobre os fatos geradores de contribuições sociais previdenciárias e demais obrigações junto a outras entidades e fundos. Isso possibilita a integração e o envio dos débitos apurados para a **DCTFWeb**.

Para **Inclusão** de um novo registro basta clicar em 

Para **Edição** de um registro basta clicar no registro desejado e clicar em 

Para **Alteração** de um registroé necessário clicar em .

Para **Excluir**o registro, é necessário selecionar a linha desejada e clicar em , após a confirmação o registro será excluído:

IMPORTANTE:

Alguns campos podem estar desabilitados neste cadastro, pois sua habilitação depende de **regras específicas definidas no leiaute do eSocial**:

* O campo **"Indicativo de Período de Apuração (13º salário)"** será habilitado apenas se a competência for igual a 12 (dezembro);
* O campo **"Atividades Concomitantes"** será habilitado quando a Classificação Tributária for igual a 3;
* O campo **"DCTFWeb"** será habilitado quando a Classificação Tributária for igual a 4 ou a Natureza Jurídica for igual a 402-2;
* O campo **"Indicativo de Substituição"** será habilitado quando o Indicativo de Desoneração da Folha for igual a 1;
* O grupo **"Transformação em Sociedade de Fins Lucrativos (PE)"** será habilitado quando informada a Data de Transformação em Sociedade de Fins Lucrativos – Lei 11.096/2005.
2Remuneração de Trabalhadores Avulsos Não Portuários

A tela **Remuneração de Trabalhadores Avulsos Não Portuários** tem como objetivo registrar as informações que serão geradas no evento **S-1270 - Contratação de Trabalhadores Avulsos Não Portuários** do eSocial.

O Manual de Orientação do eSocial **(MOS)** traz informações complementares sobre esse leiaute, incluindo regras, orientações e definições importantes para os processos das empresas.

Essas informações adicionais estão disponíveis no [portal oficial do eSocial](https://www.gov.br/esocial). Recomendamos acessar a página de documentação técnica do site e fazer o download da versão mais atualizada do MOS para consultar os detalhes específicos desse leiaute.

 

Para acessar a tela. deverá editar um período de apuração onde o indicativo de período seja igual **Mensal.**

Para **Inclusão** de um novo registro basta clicar em

Para **Edição** de um registro basta clicar no registro desejado e clicar em 

Para **Exclusão** de um registro é necessário ir até a tela de detalhes conforme exemplo abaixo e clicar em 

1) Acessar o Período de Apuração **Mensal** que contenha **Remuneração de trabalhadores Avulsos não Portuários**, que deseja excluir e clicar na seta de detalhes

2) Na tela de detalhes deverá acessar a aba de **Remuneração de trabalhadores Avulsos não Portuários** e novamente na seta de detalhes da remuneração.

Clicar no ícone

IMPORTANTE:

Alguns campos podem estar desabilitados neste cadastro, pois dependem de **regras específicas de parametrização**:

* O campo **"Indicativo de Período de Apuração"** ficará desabilitado, pois é preenchido automaticamente com base nas informações do cadastro do Período de Apuração;
* O campo "**Cód. Tomador"** será exibido e preenchido somente se o parâmetro "Utiliza Tomadores de Serviço", localizado em Configurações | Parametrizador | Folha Normal | Tomador de Serviço, estiver marcado. Caso o parâmetro esteja desmarcado, esse campo não aparecerá na tela;
* O campo **"CEI"** será habilitadosomente se o tomador de serviço selecionado possuir um CEI cadastrado;
* O campo **"Cód. Seção"** exibirá as seções com base no código de quebra para CNPJ, conforme configurado em Configurações | Parametrizador | RH-Máscaras e Quebras.  
  Serão consideradas apenas as seções ativas caso o parâmetro **"Desconsidera Seções Inativas"**, localizado em Configurações | Parametrizador | eSocial | Registros Inativos, esteja marcado.
3Copiar Período de Apuração entre Coligadas

Este parâmetro permite a cópia do Período de Apuração para outras coligadas.

Ao selecionar um período para ser copiado para outra coligada, o parâmetro de cópia será habilitado automaticamente, conforme demonstrado abaixo:

Nesta tela, será parametrizada a coligada para a qual será feita a cópia. Também é possível selecionar o parâmetro **"Substitui registro no destino se existir"**.

Nesta tela, selecionamos a coligada 6 para receber a cópia do Período de Apuração e marcamos o parâmetro para substituir as informações do período caso já existam na coligada destino 6.

Clicando em avançar a tela abaixo é apresentada.

Esta tela indica que o processo foi concluído.

Clicando em "**Acompanhar Processo"**, verificamos que o processo foi executado com 100% de conclusão e sucesso.

4Copiar Período de Apuração para próximo Período

Através deste parâmetro, é possível copiar o Período de Apuração na coligada corrente.

**Observação:** Para habilitar o parâmetro "**Copiar Período de Apuração na Coligada Corrente**", é necessário selecionar o período que deseja copiar.

Nesta tela, informamos o novo mês e ano para onde serão copiadas as informações do Período de Apuração selecionado.

Também é possível copiar os registros de **Remuneração de Trabalhadores Avulsos Não Portuários**; para isso, basta selecionar a opção **Copiar** e clicar em **Avançar**.

Esta tela apresenta um resumo da cópia. Para verificar o status do processo, clique em **Acompanhar Processo**.

Nesta tela, temos uma visão geral do processo e é possível visualizar o log de execução.

Exemplo de log **SEM** erros:

Exemplo de log **COM** erros:

5Acompanhar Processo

Para acompanhar o processo, clique em **Ações Relacionadas** e depois em **Acompanhar Processo**.

Nesta tela, podemos filtrar os agendamentos recentes ou antigos e analisar se o processo foi concluído com sucesso ou apresentou erros.

Após a execução do processo, podemos conferir se ele foi gerado com sucesso e visualizar o log.
