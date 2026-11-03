---
content_hash: 18eead62c6a8a90ce0d534aca78096ce796a2b354700cf6df2eaf7678f4d6a83
fetched_at: '2026-06-29T00:10:04.855481+00:00'
page_id: '452719263'
product: rm
source: tdn-rm
title: Geral 1/2 - FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719263
version: 37
---

Nesta etapa será possível fazer configurações gerais no modulo TOTVS Folha de Pagamento  
   
**Parâmetros e Campos**

Cálculo IRRF/INSS de múltiplos vínculos sem chapa centralizadora  
Este parâmetro tem o objetivo de tratar o cálculo de IRRF para as pessoas que tiverem mais de um vínculo na mesma coligada e o cálculo de INSS para as pessoas que tiverem mais de um vínculo considerando todas as coligadas. No cálculo, o sistema irá verificar as bases das demais chapas que tem o mesmo código de pessoa, porém cada chapa terá o seu desconto de INSS e IRRF.

Calcula INSS conforme eSocial

Para calcular o INSS conforme o eSocial será necessário marcar o parâmetro "Calcula INSS conforme eSocial' e informar a partir de qual competência o sistema iniciará o cálculo desta forma.

Marcado este parâmetro, no envelope de pagamento dos vínculos relacionados serão lançando o evento de CC387 e/ou CC388 para funcionários Normais e o CC417 para Autônomos,Diretores e Conselheiros , conforme a regra de cada código de cálculo.

**Observação**

Este parâmetro só será habilitado quando o parâmetro 'Calculo IRRF/INSS de múltiplos vínculos sem chapa centralizadora' estiver marcado.

Marcando este parâmetro, o sistema sempre irá verificar se existe outras chapas/vínculos do mesmo funcionário para encontrar a alíquota de INSS, independente se o outro vínculo for na coligada corrente ou em outra coligada.

**Atenção**

Para o correto funcionamento do cálculo de INSS conforme o eSocial, todas as coligadas de vínculos relacionados deverão ter este parâmetro marcado e a competência 'a partir de' preenchidos com o mesmo valor.

A partir de

Este parâmetro foi criado para informar a partir de qual competência/ano será considerado para fazer o cálculo de INSS de múltiplos vínculos conforme o eSocial.

**Observação:**

Este parâmetro somente será habilitado quando o parâmetro 'Calculo IRRF/INSS de múltiplos vínculos sem chapa centralizadora' estiver marcado.

Não bloquear liberação de competência caso exista pendência de recálculo de múltiplos vínculos:  Este parâmetro somente será habilitado quando o parâmetro 'Calcula INSS Conforme eSocial' estiver marcado.

Parâmetro Desmarcado: Caso exista pendência de recálculo para funcionários com múltiplos vínculos, ocorrerá **"Erro"** nas rotinas de  Liberação/Validação de competência e não será possível realizar o processo até que o recálculo da movimentação mensal seja realizado para os funcionários identificados em: Folha Mensal | Consultas | Múltiplos Vínculos que Necessitam Recálculo. 

Parâmetro Marcado: Caso exista pendência de recálculo para funcionários com múltiplos vínculos, ocorrerá **"Aviso"**  nas rotinas de  Liberação/Validação de competência e **não será impeditivo** para a realização do processo.

**Lança Grupo de eventos sem recalcular envelope**

Este parâmetro serve para ganho de performance que ao lançar o grupo de eventos não seja necessário acionar o recálculo automático do sistema. Sendo assim, quando terminar todos os lançamentos incluindo o grupo de eventos será necessário um recálculo geral para ficar com o movimento coerente com os cálculos necessários.

Com este parâmetro marcado, ao realizar o lançamento de Grupos de Eventos (em Folha Mensal | Lançamentos | Grupo de Eventos) o envelope do funcionário **não será recalculado no momento do lançamento**. 

Atenção:

O envelope de pagamento no cadastro de funcionários será recalculado automaticamente quando for acessado logo após o lançamento do grupo de eventos com este parâmetro marcado. Veja informação Importante do Recálculo Automático em [Envelope de Pagamento](https://tdn.totvs.com/display/LRM/Envelope+de+Pagamento).

Caso o parâmetro não estiver marcado, o recálculo do envelope acontecerá **em conjunto ao processo de Lançamento de Grupos de Eventos**.

**Lança líquido insuficiente separado do arredondamento**  
   
   
**Caminho padrão para gravação\importação de arquivos .TXT**  
   
   
**Diretório utilizado para processos que geram arquivos em .net (Jobserver)**

 A partir da versão 12.1.2306.103 o uso deste parâmetro será descontinuado.

Para isso fizemos uma modernização, para garantir escalabilidade e compatibilidade com cloud, e agora ele é capaz de identificar automaticamente o local mais adequado para salvar esses arquivos. Caso haja necessidade de especificar manualmente esse diretório, é possível utilizar o parâmetro FILESERVERPATH no arquivo rm.host.exe.config, porém é recomendável deixar que o local seja escolhido de forma automática.  
  
**Debug de fórmulas adicionais no arquivo de médias**  
Com este parâmetro marcado, as fórmulas adicionais serão discriminadas no log de média dos cálculos de Férias, 13º Salário e Rescisão.  
   
**Bloquear lançamento financeiro do mesmo fator gerador**  
Com esse parâmetro marcado, ao realizar o lançamento financeiro, o sistema irá validar os seguintes campos: Coligada, Filial, Data Emissão, Valor e Histórico. Caso eles sejam iguais em um lançamento já existente, o sistema não gerará o lançamento enviando uma mensagem de aviso no log de execução do processo.  
   
**Ativar Alterações da Reforma Trabalhista de acordo com a Lei Nº 13.467 de 13 de Julho de 2017**  
   
   
**Armazena Geração de Guia de INSS por Chapa**  
Marcando este parâmetro, os valores da guia de INSS detalhados por funcionários no log da geração, serão armazenados no banco de dados podendo ser utilizados de acordo com a necessidade da empresa, como por exemplo, a emissão de relatórios gerenciais.   
Quando marcado, os valores serão armazenados nas tabelas PGPSLOGCALC e PGPSLOGCALCDETALHE.

**Observação**  
O maior valor do campo IDGPS sempre corresponderá a ultima Guia gerada pelo sistema.

**Considerar dados do histórico de funcionário ao gerar Folha Analítica na competência atual**

Este parâmetro permite definir a origem das informações da **Seção, Situação e Função** do funcionário que serão utilizados na geração da Folha Analítica.

* Com o parâmetro marcado  
  Ao gerar a Folha Analítica para a competência atual, o relatório utilizará os dados registrados nos **Históricos de Seção, Histórico de Situação e Histórico de Função** do funcionário.
* Com o parâmetro desmarcado  
  Ao gerar a Folha Analítica para a competência atual, o relatório considerará os dados atuais do cadastro do funcionário (tabela **PFUNC**), utilizando as informações dos campos de **Seção**, **Situação** e **Função** exibidas na tela de funcionários.
* Para geração retroativa (competências anteriores)  
  Independente do parâmetro estar marcado ou desmarcado, o relatório sempre utilizará os dados conforme os **Históricos de Seção, Históricos de Situação e Histórico de Função** do funcionário.

false⚠️ Atenção

Este parâmetro foi implementado para oferecer ao usuário a **flexibilidade de escolha** quanto ao uso dos históricos na geração da Folha Analítica para a competência atual.

A análise dos históricos pode impactar a **performance do processo**, por isso o uso desse parâmetro torna-se essencial para controlar esse comportamento conforme a necessidade do cliente.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

<<Voltar para tela anterior **Folha Normal**
