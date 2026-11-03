---
content_hash: b9e6ec13cf5bd699db873554d235728ef9d1e012ebb9b8271da5a8a0713051d0
fetched_at: '2026-06-29T00:10:18.934370+00:00'
page_id: '4812796'
product: rm
source: tdn-rm
title: Conversão para o Cálculo .NET
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4812796
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Folha de Pagamento                       **Versão:**11.8X |
| **Processo** | **:** | Conversão |
| **Subprocesso** | **:** | Conversão para Cálculo .Net |
| **Data da publicação** | **:** | 09/09/2014 |

Este “Como Fazer” visa auxiliar o usuário do sistema TOTVS Folha de Pagamento na conversão do cálculo DELPHI para o cálculo .NET. Neste, todo o cálculo passou por uma reestruturação, tendo como grande diferencial o desempenho. As interfaces estão mais modernas e amigáveis aos nossos usuários, além de recursos mais avançados e de fácil utilização.

Solução

### **1 - O que é a Migração Cálculo .NET**

O sistema RM Labore é composto por Cadastros, Cálculos, Rotinas mensais / Anuais e Relatórios. A migração do Cálculo está sendo reescrita para uma nova plataforma de desenvolvimento.  
Tecnicamente, o cálculo anterior foi desenvolvido na linguagem Object Pascal da Borland Delphi e o novo cálculo na linguagem .NET, da Microsoft.  
A migração do Cálculo .NET, consiste na substituição do antigo cálculo 32 bits (Delphi), para um novo Cálculo .NET, que traz grandes benefícios e vantagens operacionais aos nossos usuários.

**2 - Quais as vantagens da migração para Cálculo .NET**

Buscando sempre atender as necessidades dos nossos clientes com agilidade e eficiência, evoluímos o processo de cálculo do sistema. Esta evolução visa ampliar o os cálculos, garantindo avanço tecnológico, melhorias em interfaces e muitas outras vantagens, que apresentaremos a seguir:  
   
Veja as novidades no link abaixo

[TOTVS Folha de Pagamento - Cálculo. Net - Máquina de Cálculo da Folha](http://totvsconnect.blogspot.com.br/2011/01/totvs-folha-de-pagamento-calculo-net.html)

### **3 – O que é necessário para migrar**

Conhecer as mudanças do novo cálculo – O Cálculo .NET do RMLabore.  
Utilizar o RMConversor XX.YY.ZZ.msi (onde as letras 'XX', 'YY' e 'ZZ' representam a versão - RMConversor 11.82.30.msi, por exemplo)  
 

| **Atenção!** *A partir da versão 11.40, os clientes que possuem coligada em Belo Horizonte, terão a conversão realizada automaticamente, assim que acessarem o sistema RMLabore.exe.* *Para os clientes com coligada em Minas Gerais, a conversão automática será feita a partir da 11.50.* *Na versão 11.80 e superiores, todos os clientes passarão pelo processo de conversão para o .Net assim que realizarem o acesso ao aplicativo RMLabore.exe.* |
| --- |

### **4 – Convertendo para .NET utilizando o conversor de Cálculo .NET**

**4.1 - O que é o conversor do Cálculo .NET**

É um processo que irá adaptar a base para o novo Cálculo .NET, criando os novos códigos de cálculos convertendo os dados de férias para o novo modelo de férias e disponibilizando novos recursos.

**4.2 Procedimentos a serem executados no RMLabore antes da conversão****:**

**4.2.1 - Gerar um backup da base de dados.**

Observação:  
Sugerimos primeiro a conversão em uma base de teste compatível à base de produção, para depois rodar na base oficial.

### **5 –** **Conversor do Cálculo**

**Passo 1:** Executar o ConversorCalculo.exe (No caso da conversão para 11.8X, o conversor será executado automaticamente ao logar no RMLabore.exe)  
 **Passo 2:** Informar o usuário e a senha do Banco de dados (normalmente, usuário rm)  
 **Passo 3:** Selecionar o alias do banco de dados

**Passo 4:** Será aberta uma tela para informação dos dados dos arquivos de log.  
Estes arquivos serão gravados dentro da pasta onde está o arquivo ConversorCalculo.exe, no momento em que é selecionado o botão **“Validar Conversão”.**  
É extremamente importante que seja feita a análise do log do conversor , ‘Log Completo.txt’ e ‘Logerros.txt’, gerados no momento da validação da conversão, conforme explicações do item 5.

Antes de iniciar a conversão da base de dados, estes logs deverão ser analisados e todos os avisos informados nos mesmos, deverão ser corrigidos. Este procedimento irá garantir maior integridade da base de dados após a conversão.

Abaixo um exemplo de um log completo.

Durante a validação será verificado o histórico de férias, como exemplo o preenchimento correto dos períodos de gozos.  
Caso detectar inconsistências cadastrais, deverá sair do conversor e corrigir na base de dados , em seguida repetir a validação.  
Não ocorrendo registros com inconsistências, clicar no botão “Iniciar Conversão.”

### **6 - Procedimentos a serem executados após a conversão**

***- Revisão das permissões dos usuários:***

Caso o usuário não efetue a revisão das permissões dos perfis associados aos usuários o sistema irá apresentar a seguinte mensagem ao acessar o Módulo de férias:

O usuário mestre deverá acessar o módulo, Cadastro | Segurança | Perfis, para rever as permissões de novos módulos criados, como por exemplo ícones dos períodos de gozo de férias.

***- Férias***

Em Opções | Parâmetros | RM Labore | Param. Férias

Para uma melhor usabilidade do sistema, foram disponibilizados os campos abaixo onde o usuário deverá informar o Evento e o Motivo da Licença Remunerada para férias coletivas:  
‘Férias coletivas: Evento para pagamento de Licença Remunerada’ e ‘Férias coletivas: Motivo de afastamento por licença remunerada’

Foi disponibilizado o recurso para gravar o histórico da mudança de situação de férias.  
Para isso será necessário preencher os parâmetros:  
‘Motivo da situação: Motivo Início das Férias’ e ‘Motivo da situação: Motivo Retorno das Férias’  
Este histórico será gravado no momento do lançamento e finalização das férias.

*- **Criar os EVENTOS referente aos novos códigos de cálculos:***

Cód. Cálculo 302 - BASE DE IRRF FOLHA OUTROS VÍNCULOS

Cód. Cálculo 303 - BASE DE IRRF 13º SALÁRIO OUTROS VÍNCULOS

Cód. Cálculo 304 - BASE DE IRRF PARTICIPAÇÃO LUCROS OUTROS VÍNCULOS

Cód. Cálculo 305 - IRRF FOLHA BASE PENSÃO

Cód. Cálculo 306 - IRRF FÉRIAS RECIBO BASE PENSÃO

Cód. Cálculo 307 - IRRF 13º SALÁRIO BASE PENSÃO

Cód. Cálculo 308 - IRRF PARTICIPAÇÃO NOS LUCROS BASE PENSÃO

Cód. Cálculo 309 - FÉRIAS EM DOBRO

Cód. Cálculo 310 - ADICIONAL 1/3 DE FÉRIAS EM DOBRO

Cód. Cálculo 311 - ABONO DE FÉRIAS EM DOBRO

Cód. Cálculo 312 - ADICIONAL 1/3 DE ABONO DE FÉRIAS EM DOBRO

Cód. Cálculo 313 - JORNADA MENSAL CONSIDERANDO HORAS TRABALHADAS

Cód. Cálculo 314 - ARREDONDAMENTO DESCONTO BASE

Cód. Cálculo 315 - BASE DE FGTS DE AFASTADOS

Cód. Cálculo 316 - IRRF FÉRIAS ENVELOPE BASE PENSÃO

Cód. Cálculo 317 - BASE DE IRRF FÉRIAS RECIBO OUTROS VÍNCULOS

Cód. Cálculo 318 - BASE DE IRRF FÉRIAS ENVELOPE OUTROS VÍNCULOS

Cód. Cálculo 319 – PENSÃO ALIMENTÍCIA FÉRIAS NA RESCISAO

Cód. Cálculo 320 – PENSÃO ALIMENTÍCIA FÉRIAS INFORMADA

Cód. Cálculo 321 – PENSÃO ALIMENTÍCIA PL INFORMADA

Cód. Cálculo 322 – SEGUNDA PARCELA 13º SALÁRIO LICENÇA MATERNIDADE

Cód. Cálculo 323 – DIFERENÇA DE 13º SALARIO LICENÇA MATERNIDADE

Cód. Cálculo 324 – 13º SALÁRIO RESCISÃO LICENÇA MATERNIDADE

Cód. Cálculo 325 – DIFERENÇA 13º SALARIO RESCISÃO LICENÇA MATERNIDADE

**Atenção!**

Veja detalhes em [Códigos de Cálculos](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.CodigosCalculo.aspx).

***- Salário Família***

Para maior facilidade na conferência e/ou cálculo do Salário Família, o sistema passou a considerar a incidência do evento, não utilizando nenhum tratamento interno, como era feito anteriormente em Delphi.

Sendo assim, será necessário uma revisão nas incidências de ‘Salário Família’ dos eventos com código de cálculo 1 e 2.

**Observação I:**

No cálculo em Delphi sempre era considerado os eventos com código de cálculo 1 e 2 para compor a base de salário família, independente dos mesmos estarem incidindo salário família.

**Atenção!**

Este tratamento será adotado quando o parâmetro ‘Usa salário nominal’ existente em Opções | Parâmetros | RMLabore | Param. de Cálculo | Parâmetros, não estiver marcado.

***- Diferença Salarial***

O Cálculo .NET passou a consistir se os eventos com código de cálculo 37 (um com incidência em INSS e outro sem esta incidência) são do tipo PROVENTO.

### **7 – Alterações nas funções de fórmulas**

Houve migração das fórmulas de cálculo para .NET e com isto mudança de comportamento entre a versão Delphi e a .NET, deverá analisar as fórmulas abaixo e verificar se utiliza alguma função, caso afirmativo deverá analisar a lógica da fórmula e adequar ao novo cálculo.  
  
Utilize o módulo de comparação de fórmulas disponível em Rotinas/Comparativo de Fórmulas Delphi x .NET

(disponível a partir da versão 11.40)

Abaixo um log com diferenças entre Delphi e .NET após comparação de funcionários.

Deverá analisar através dos logs de cálculo o motivo dos valores gerarem diferentes.

Exemplo:

Fórmula EVT0023 – Base de cálculo de IRRF

Chapa 00001 – Na versão Delphi gerou 2915,55 , já na versão .NET gerou 3836,53

**Atenção!**

Deverá analisar e ser for necessário, adequar as fórmulas conforme necessidade da empresa, caso contrário, ocorrerá diferenças de cálculo na folha de pagamento do cliente.

Veja nas informações complementares, as mudanças de comportamento entre o cálculo Delphi e o .NET.

### **8 - Mudança de Comportamento Cálculo Delphi X Cálculo .NET**

***- Cálculo / Arredondamento***

O arredondamento no valor do evento é sempre a partir da 3ª casa decimal, porém, quando a 3ª casa decimal é “5” (cinco), o DELPHI ora arredonda para cima, ora arredonda para baixo, característica da linguagem de fórmula DELPHI. O .NET sempre arredonda para cima.

Exemplo:

Resultado da fórmula => 184,**635**

DELPHI => 184,63

.NET => 184,64

Dízimas

No caso de dízimas, ao invés de entender como “18,635”, o DELPHI entende como “18,6344444444444”.

Essas diferenças de centavos poderão ocorrer em todos os processos de cálculos do sistema.

***- Cálculo / Data de pagamento***

No cálculo será verificada a data de pagamento e depois o período para pagamento dos eventos. Quando existirem dois períodos com a mesma data, a segunda ordem será o período. As situações são quando existe um evento desconto onde tem que buscar o valor de um evento provento. As situações onde é necessário seguir uma seqüência de data de pagamento são as abaixo:

· Código de cálculo 51 - Adiantamentos 13º Salário buscando o valor do Código de cálculo 102 - 2ª parcela 13º Salário;

· Código de cálculo 35 - Adiantamentos13º Salário buscando o valor do Código de cálculo 9 - 1ª Parcela 13º Salário;

· Código de cálculo 21 - Arredondamento Descontos buscando o valor do Código de cálculo 20 - Arredondamento Proventos.

\* Versão Delphi verificava a ordem dos períodos, o maior era calculado por último.

***- Código de Cálculo 145 – Atestado Médico***

Quando em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros o parâmetro ‘Lança o evento de atestado médico via grupo de eventos’ estiver marcado, o Cálculo .NET somente irá lançar o evento com cc145, quando for lançado o evento com cc1 ou cc2.

Foi retirado o parâmetro *‘Soma dias afastados dentro período de carência pelo mesmo motivo’* existente em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros. O cálculo. Net passou a verificar quantidade de dias de atestado pagos pela empresa, de acordo com o período de carência e paga até um total de 15 dias.

**Exemplo:**

Período de carência 60 dias.

*Período de afastamento         Qt dias Afastamento   Tipo      Motivo*

01/11/2010 a 14/11/2010                     14                       P           3

01/12/2010 a 05/12/2010                     05                       P           3

***- Lançamentos dos eventos Atestado Médico e Dias Trabalhados:***

*Competência:*

Novembro/2010: 16 Dias Trabalhados e 14 dias de atestado médico.

Dezembro/2010: 25 Dias Trabalhados e 1 dia de atestado médico.

O restando dos dias, ou seja, quatro dias, para completar 30 dias trabalhados, quem irá pagar é a previdência.

### **9 - Informações Complementares**

Conforme já mencionado neste documento, ao rodar o comparativo de fórmulas, pode ser que ocorra divergência de valores. Leia o documento Fórmulas .NET ou acesse o help sobre Migração .NET do sistema TOTVS Folha de Pagamento (<http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.Labore.aspx>).
