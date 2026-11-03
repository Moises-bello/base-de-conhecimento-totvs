---
content_hash: 76adc4f6c68f8ae1b893446b1964ae7a84c5e386c536f0e623d62c485ba47d94
fetched_at: '2026-06-29T00:10:51.344087+00:00'
page_id: '566476942'
product: rm
source: tdn-rm
title: Middleware - Como validar divergências no relatório comparativo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=566476942
version: 26
---

# Objetivo:

---

       O objetivo deste documento é orientar como validar divergências entre os valores gerados pelo TOTVS Folha de Pagamento e retornados pelo Governo no Relatório de Conferência do Middleware.

Informações

A partir dos Patches:

* 12.1.32.154, 12.1.31.218, 12.1.29.300 ou Superiores.
Agrupador DadosApresentação do Relatório

### Menu

eSocial → Conferência INSS/FGTS

### Filtros

Ao selecionar no menu a opção "Relatório de Conferência (INSS)" será apresentado o Painel de Conferência do INSS:

Todos os filtros selecionados são exibidos no container abaixo da barra de campos de filtros. Também é possível remover um ou mais filtros, clicando no "X" à direita de cada ícone, ou por meio do botão "Remover todos":

### Processamento

Após selecionar os filtros desejados, é possível utilizar o botão "Aplicar Filtros" para iniciar a coleta e processamentos das informações para apresentação no painel. Durante esta operação, uma barra de progresso é exibida abaixo do container de filtros:

Ao final do processamento, o Relatório de Conferência irá apresentar os cards abaixo, que totalizam os valores encontrados nas fontes de informação (RH e Governo), exibem o somatório do INSS e INSS 13º calculados pela Folha e pela DCTFWeb, respectivamente.

### Apresentação das Informações

#### Cards Totalizadores da Consulta

Estes cards totalizam os valores encontrados nas fontes de informação ( RH e Governo ), desta forma, já é possível identificar se existem divergências nos valores de desconto de INSS.

Nesta tela, além do Valor de Recolhimento do INSS, também são apresentados os valores de Base de INSS, Base de INSS 13º Salário, Valor de Recolhimento de INSS 13º Salário, Salário Família, Salário Maternidade e Salário Maternidade 13º Salário para cada fonte de informação ( RH e Governo ):

Caso possua múltiplos vínculos será apresentada a descrição dos valores por cada vinculo

Validação de divergências

Para identificar os funcionários com divergência no valor total de recolhimento de INSS da empresa ou Governo selecione o parâmetro **Somente divergências.**

 Após filtro aplicado, será apresentado o valor de recolhimento total e os dados dos funcionários que possuem divergência.

  

Para uma análise mais detalhada, clique no link encontrado no conteúdo da coluna CPF de cada colaborador:

Agrupador de ValidaçãoBase INSS Folha

Apresentado divergência com a Base RH, será necessário verificar se os eventos de provento presentes no envelope de pagamento estão com as incidências de INSS corretas, pois o relatório irá consulta essa marcação.

Acesse o menu Administração de Pessoal | Cadastros | Funcionários

Selecione o funcionário que deseja visualizar o Envelope, na aba Incidências é possível identificar o valor da base de INSS RH.

 Diante do resultado acima, caso o valor não seja o esperado, será necessário verificar se os eventos estão com as incidências de INSS corretamente. Validações abaixo:

1. No envelope do funcionário, verifique os eventos e suas incidências.
2. Identificado algum incorreto, acesse o cadastro do evento desejado e ajuste a parametrização conforme necessidade.
3. Após ajuste, deverá enviar o evento S-1010 gerado na fila de eventos ao eSocial.

 Base INSS DCTFWEB

O valor Base INSS retornado no relatório, é o resultado que o eSocial encontrou de acordo com as incidências do S-1010. Dessa forma, verifique se os eventos que compõe a base de INSS estão com as incidências corretas. Siga os passos abaixo:

* Tipo de**rubrica incorreta** no eSocial Web

1. Para corrigir o tipo de rubrica e incidência da Contribuição Previdenciária divergentes, no módulo Folha de Pagamento acesse **Administração de Pessoal | Eventos** e altere a parametrização conforme a sua necessidade.
2. Em seguida, acesse **eSocial | Fila de Eventos** e gere o XML do evento criado a partir da alteração para envio ao eSocial.

* Inclusões, exclusões ou alterações nas bases e/ou valores operados diretamente no Portal eSocial.

      1.Deverá ajustar as informações no envelope de pagamento do funcionário.  
      2.Depois, envie uma retificação da Remuneração/Desligamento ao eSocial.

* **Vigência** em desacordo com o Período de Apuração

      1.  Neste caso, verifique a necessidade de uma alteração do S-1010 ou inclusão com o inicio de vigência desejado.

**Importante**  
Para facilitar a validação do XML, execute o processo **Validar S-1200 com Envelope** presente em **eSocial | Eventos Periódicos**.

**Saiba mais**  
Para mais informações acesse: 

* [S-1010 - Tabela de Rubricas](http://tdninterno.totvs.com/display/public/LRM/S-1010+-+Tabela+de+Rubricas)

Desconto INSS Folha

O valor INSS RH é a soma encontrada no envelope de pagamento.

Para isso, segue algumas validações:

* Nova **Tabela INSS** Progressiva

      1.Verifique se Versão/Patch contempla a [Nova Tabela INSS Progressiva](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042321514-RM-FOP-Como-criar-Tabela-INSS-Progressiva-?source=search) conforme eSocial.

      2.Em seguida, acesse o menu Administração de Pessoal | Cadastros | Funcionários | Envelope  e recalcule o envelope de pagamento.

* Incidência incorreta nos eventos do **Tipo Provento**  
  O sistema irá somar os valores dos eventos que possuem incidência em INSS para montar a Base de Cálculo da Contribuição Previdenciária e, consequentemente, calcular o INSS.
* Valor de **desconto INSS R$0,01 a maior** no RM  
  Geralmente o valor de desconto INSS fica a maior no RM em R$ 0,01 quando o RM está parametrizado para arredondar o valor de desconto INSS. No cálculo de desconto INSS do governo não é realizado este arredondamento. Para que os valores sejam calculados conforme eSocial acesse **Administração de Pessoal | Cálculos | Tabelas de Cálculo**e desmarque o parâmetro**Arredondar Valores.  
    
    
  Importante**Após o ajuste do parâmetro deverá realizar o recálculo do envelope.

Desconto INSS DCTFWEB

O valor Desconto INSS Governo será considerado de acordo com o retornado pelo evento S-5001 do RET (Governo), após o envio dos Eventos de Remuneração.

Lembrando que o valor do Segurado calculado pelo eSocial, é um cruzamento das informações enviadas no S-1010- Tabela de Rubrica  e S-1200 - Folha de Pagamento ou S-2299/2399 - Desligamento.

* **Categoria** eSocial incorreta  
  O eSocial irá consultar a Categoria do Empregado para aplicar o cálculo do Segurado.  
  Para mais informações de Alteração de Categoria acesse:  
  •[Alteração da categoria eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037527033-RM-eSocial-Altera%C3%A7%C3%A3o-da-categoria-eSocial-?source=search)
* Tipo de**rubrica incorreta** no eSocial Web  
  Verifique se as incidências estão corretas no eSocial, pois o Governo utiliza a parametrização dos eventos S-1010 para identificar a forma de cálculo.  
  1.Para corrigir o tipo de rubrica e incidência da Contribuição Previdenciária divergentes, no módulo Folha de Pagamento acesse **Administração de Pessoal | Eventos** e altere a parametrização conforme a sua necessidade.   
  2. Em seguida, acesse **eSocial | Fila de Eventos** e gere o XML do evento criado a partir da alteração para envio ao eSocial.  
    
  **Observação:**Lembre-se que o inicio de vigência deverá estar de acordo com o Período de Apuração validado.
