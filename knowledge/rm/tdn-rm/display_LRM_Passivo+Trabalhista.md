---
content_hash: 4d6105d11a754514328cad88b40ef3f7bbcde85d037af176295537dc2367d9fc
fetched_at: '2026-06-29T00:10:07.290835+00:00'
page_id: '452719393'
product: rm
source: tdn-rm
title: Passivo Trabalhista
type: documentation
url: https://tdn.totvs.com/display/LRM/Passivo+Trabalhista
version: 14
---

## 

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tela Passivo Trabalhista Parâmetros**
5. **Tela Parâmetros Coligada**
6. **Tabelas utilizadas**

## **01.****VERSÕES**

false

**A partir do Release:**

* 12.1.2209 e Superiores

## **02.** **VISÃO GERAL**

Processo que permite emitir em relatório a provisão das principais verbas que deverão ser pagas aos funcionários em caso de rescisão.

Para o cálculo do passivo trabalhista informe a parametrização necessária no módulo. Essa parametrização poderá ser global ou nos parâmetros da coligada

O Usuário deverá informar qual relatório será usado para geração.   
  
A opção de usar Parâmetros específicos por coligada estará disponível após avançar da primeira tela do processo. Dentro dos parâmetros por coligada é que será possível informar a seleção de funcionários para os quais deseja fazer a provisão do Passivo Trabalhista e outras informações específicas da coligada, podendo inclusive gerar para mais de uma coligada ao mesmo tempo.  
  
**Observações:**

01 -  Não serão calculados e nem armazenados os eventos de CC 329, 330 e 331

02 -  Na transferência entre coligadas tabelas PSIMULADEMISSAO e PSIMULADEMISSAOEVENTOS não serão transferidas porque as parametrizações da seção podem ser diferentes.

## **03. EXEMPLO DE UTILIZAÇÃO**

Quando a competência atual é julho e existe uma simulação de rescisão para 30 de novembro informando dados nos parâmetros da coligada.

Lançando Evento Adicional de Rescisão do parametrizador

Lançando Evento de Código Fixo

Lançando Evento Programado

Lançando Evento Adicional

Na primeira tela foi parametrizado da seguinte forma:

Na tela por coligada foi parametrizado da seguinte forma:

Veja que foram calculados os eventos previamente cadastrados – Veja no log de cálculo todos os cálculos executados:

O relatório será apresentado da seguinte forma:

## **04. TELA Passivo Trabalhista Parâmetros**

**Funcionamento dos parâmetros que existem de forma global:**

Considera rescisão por comum acordo (tipo V) - Quando marcado, o processo altera o percentual do valor pago para FGTS para 20% e não mais 40% (normal).

**Exemplo**:

Parâmetro marcado: Desconsiderando o acréscimo de 10% na multa FGTS será calculado com Saldo para Fins Rescisórios (R$5000,00) \* Multa (0,20) = R$1000,00

Parâmetro desmarcado: Considerando o acréscimo de 10% na multa FGTS será calculado com Saldo para Fins Rescisórios (R$5000,00) \* Multa (0,30) = R$1500,00

Calcular desconto de INSS: Para calcular o INSS, armazenar na tabela PSIMULADEMISSAO para ser utilizado no relatório do passivo trabalhista.

Calcular INSS Empresa:

* Para calcular o INSS patronal e INSS terceiros será considerado os percentuais informados do Histórico de Percentual para INSS cadastrado na seção, dentro do período de vigência da data de demissão do passivo.
* Para calcular o acidente de trabalho será considerando o valor cadastrado dentro da vigência no cadastro de FAP por estabelecimento, que está no cadastro de Seção | Anexos, multiplicado pelo percentual informado no histórico de percentual de seção do respectivo campo.
* Será considerado somente o valor cadastrado nas seções centralizadoras, assim como ocorre para o eSocial.
* Documentação de referência do Histórico de Percentuais para INSS: [Histórico de Percentuais para INSS](https://tdn.totvs.com/pages/releaseview.action?pageId=496388652)
* A Documentação de como cadastrar o FAP por estabelecimento:  [FAP por Estabelecimento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014456151-RH-RM-FOP-Como-cadastrar-o-FAP-ou-alterar-sua-vig%C3%AAncia)

**Observações:**

1. Caso existam compensações de INSS não serão consideradas nesse cálculo.
2. Não será possível o usuário informar percentual parte empresa na tela do passivo como ocorre com a Guia de INSS e Folha Analítica.
3. Não será feito leitura dos campos ‘% Acid. Trabalho’ e ‘%Terceiros’ da pasta Dados p/INSS do cadastro de Seção. Esses percentuais serão considerados do histórico
4. Não serão armazenados os valores na tabela detalhe. Caso seja necessária essa informação deverá ser customizada por fórmula.

Calcular Desconto de IRRF: Para calcular o IRRF, armazenar na tabela PSIMULADEMISSAO para ser utilizado no relatório do passivo trabalhista.

Carregar eventos já lançados no envelope: Com esta opção marcada irá considerar os valores lançados para o envelope de pagamento dentro da competência da base para compor a remuneração base. Caso, contrário, os valores não serão considerados para o cálculo do processo do passivo trabalhista.

**Observações:** Independente da marcação ou não deste parâmetro será calculado o salario base (CC1 ou CC2) no passivo trabalhista mesmo se existir o evento com código de calculo lançado no envelope e o parâmetro desmarcado

## **05. TELA Parâmetros Coligada**

**Funcionamento dos parâmetros que existem de forma global e por coligada:**

Quebra de seção e seleção de funcionários, sendo que a seleção de funcionários para funcionários específicos somente será possível pelos parâmetros da coligada.

Data de demissão: para informar a data para o cálculo do passivo trabalhista

Aviso Prévio Indenizado: Quando o cálculo do passivo tiver necessidade de calcular o aviso prévio indenizado. E ao marcar o parâmetro habilitará a Data de Início do Aviso Indenizado indenizado, Dias de Aviso, Aviso prévio indenizado abate 0.5 dias e Executa fórmula de aviso.

Aviso Prévio indenizado abate 0,5 dia: Quando marcado, o processo abate metade do dia para o cálculo do valor dos dias de aviso prévio de direito. Este parâmetro deve ser utilizado junto ao parâmetro "Considera Rescisão por comum acordo" quando estiver marcado.

**Exemplo:**

Parâmetro marcado: Dias de Aviso: 17 Salário Base: R$1.500,00 Salário Dia: 1.500,00 / 30 = 50,00 Valor do Aviso Prévio: **16,5** \* 50,00 = R$825,00

Parâmetro desmarcado: Dias de Aviso: 17 Salário Base: R$1.500,00 Salário Dia: 1.500,00 / 30 = 50,00 Valor do Aviso Prévio: **17** \* 50,00 = R$850,00

Executa fórmula de aviso prévio: Será executada a Fórmula de número de dias de aviso prévio informada no cadastro de sindicato indicado no cadastro de funcionários.

Incidência de FGTS para calcular os valores de FGTS para Remuneração, 13º Salário e/ou Aviso Prévio

Ordenação: O relatório poderá ser emitido ordenado por chapa ou nome.

Emissão do Passivo Trabalhista em Relatório: Emite o relatório de acordo com o layout selecionado. Se não marcar o parâmetro somente calcula e preenche as tabelas.

Detalhar verbas consideradas no cálculo: Ficará habilitado quando o parâmetro Emissão do Passivo Trabalhista em Relatório estiver marcado. No relatório retorna os eventos cadastrados na PSIMULADEMISSAOEVENTOS, separados por Provento, Desconto e Base.

Lançar Eventos Adicionais dos parâmetros de rescisão: Será considerado apenas eventos que estiverem no parametrizador para eventos adicionais de rescisão. Para os eventos cadastrados nos eventos adicionais de férias e 13º salário serão considerados de acordo com o parâmetro “Lançar eventos adicionais de férias na rescisão” e “Lança eventos adicionais de 13º na rescisão” nos parâmetros de rescisão do parametrizador em seus respectivos itens.

**Observações:**

01 – Os eventos lançados por marcar o parâmetro “Lançar eventos adicionais dos parâmetros de rescisão” serão somados na remuneração do passivo trabalhista desde que tenha o código de cálculo 0 (zero).

02 - Os eventos cadastrados nos eventos adicionais de férias e 13º salário serão somados na remuneração do passivo trabalhista de acordo com os parâmetros “Lançar eventos adicionais de férias na rescisão” e “Lança eventos adicionais de 13º na rescisão” marcados no parametrizador e com o código de cálculo do evento. Se o evento tiver código de cálculo 0 (zero) será somando na remuneração, se tiver código de cálculo relacionado ao processo será somado no processo, ou seja, evento com código de cálculo de férias será somado em férias e evento com código de cálculo de 13º salário será somado ao 13º salário.

Lançar Códigos Fixos do funcionário: Serão considerados os eventos cadastrados nos códigos fixos do Funcionário conforme configurado no parametrizador em Rescisão | Códigos Fixos.

Serão considerados todos os eventos cadastrados como códigos fixos, onde a quantidade de vezes é maior que 0.

Lançar Eventos Programados do funcionário: Serão considerados os eventos cadastrados nos Eventos programados do Funcionário conforme configurado no parametrizador Rescisão | Eventos programados:

Serão considerados todos os eventos onde a competência inicial e final estiverem dentro do mês da data de demissão informada no processo do passivo trabalhista.

Desconsidera acréscimo de 10% na multa FGTS: Contribuição social de 10% sobre os depósitos do Fundo de Garantia do Tempo de Serviço (FGTS) pagas na demissão sem justa causa que pode ser desconsiderada caso o usuário opte por marcar esse parâmetro.

**Funcionamento dos parâmetros que existem de forma por coligada:**

Lançar Eventos Informados: Parâmetro para habilitar a pasta Eventos Informados.

Fórmulas Adicionais: Pasta para informar fórmula para somar na remuneração calculada pelo passivo trabalhista.

Eventos Informados: Pasta para informar os eventos adicionais que serão lançados somente neste momento do cálculo.

Caso informe um evento já informado nos parâmetros Globais, o mesmo será substituído, considerando o evento informado nos parâmetros da coligada do processo do passivo.

Caso tenha fórmula no evento, sempre vai considerar o valor retornado pela Fórmula, mesmo se o evento for informado neste grid com o campo valor preenchido e no parametrizador estiver sem valor.

Os eventos informados serão considerados para todos os funcionários da seleção do cálculo do passivo, não podendo informar por funcionário, exceto se existir fórmula customizada para não lançar.

## **06. TABELAS UTILIZADAS**

* PSIMULADEMISSAO

* PSIMULADEMISSAOEVENTOS
