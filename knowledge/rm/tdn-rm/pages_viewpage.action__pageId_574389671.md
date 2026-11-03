---
content_hash: 73ae62d0c19a102d5787c0f94c474513604f8fbf5377baaff40939cbab334173
fetched_at: '2026-06-29T00:10:53.048731+00:00'
page_id: '574389671'
product: rm
source: tdn-rm
title: Middleware - Como validar divergências no relatório de conferência INSS 13º
  Salário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=574389671
version: 11
---

# Objetivo:

---

       O objetivo deste documento é orientar como validar divergências entre os valores gerados pelo TOTVS Folha de Pagamento e retornados pelo Governo no Relatório de Conferência do Middleware.

Informações

A partir dos Patches:

* 12.1.26.216
* 12.1.27.172
* 12.1.28.106
Agrupador DadosApresentação do Relatório

O Relatório de Conferência irá apresentar os cards abaixo, que totalizam os valores encontrados nas fontes de informação (RH e Governo), exibem o somatório do INSS e INSS 13º calculados pela Folha e pela DCTFWeb, respectivamente.

### Apresentação das Informações

#### Cards Totalizadores da Consulta

Estes cards totalizam os valores encontrados nas fontes de informação ( RH e Governo ), desta forma, já é possível identificar se existem divergências nos valores de desconto de INSS.

É possível acessar o detalhamento de mais valores analíticos de cada colaborador ao clicar no link encontrado no conteúdo da coluna CPF ou Nome:

Nesta tela, além do Valor de Recolhimento do INSS, também são apresentados os valores de Base de INSS, Base de INSS 13º Salário, Valor de Recolhimento de INSS 13º Salário, Salário Família, Salário Maternidade e Salário Maternidade 13º Salário para cada fonte de informação ( RH e Governo ):

Caso possua múltiplos vínculos será apresentada a descrição dos valores por cada vinculo

Validação de divergências

Ao ser apresentada uma divergência no valor total de recolhimento de INSS da empresa, a primeira coisa a ser feita é identificar qual(is) funcionário(s) apresenta(m) divergência.

Para isso, ao realizar a geração do relatório, selecione o parâmetro "Somente Divergência" no filtro inicial alterando o botão para "Sim":

Após o filtro aplicado, será apresentado os dados dos funcionários que possuem divergência.

Nesta tabela, é apresentado apenas o Valor de Recolhimento de INSS.

Para identificarmos os valores do 13º Salário, deverá  acessar o detalhamento de valores analíticos de cada colaborador ao clicar no link encontrado no conteúdo da coluna Estabelecimento:

Nesta tela, além do Valor de Recolhimento do INSS, também são apresentados os valores de Base de INSS, Base de INSS 13º Salário, Valor de Recolhimento de INSS 13º Salário, Salário Família, Salário Maternidade e Salário Maternidade 13º Salário para cada fonte de informação ( RH e Governo):

Agrupador de ValidaçãoBase INSS RH

Apresentado divergência com a Base RH, será necessário verificar se os eventos de provento presentes no envelope de pagamento estão com as incidências de INSS corretas, pois o relatório irá consulta essa marcação.

Acesse o menu Administração de Pessoal | Cadastros | Funcionários

Selecione o funcionário que deseja visualizar o Envelope, na aba Incidências é possivel identificar o valor da base 13º Salário.

 Diante do resultado acima, caso o valor não seja o esperado, será necessário verificar se os eventos estão com as incidências de INSS corretamente. Validações abaixo:

1. No envelope do funcionário, verifique os eventos e suas incidências.
2. Identificado algum incorreto, acesse o cadastro do evento desejado e marque a incidência desejada. Exemplo:

 Base INSS Governo

O valor Base INSS retornado no relatório, é o resultado que o eSocial encontrou de acordo com as incidências do S-1010. Dessa forma, verifique se os eventos que compõe a base de INSS estão com as incidências corretas. Siga os passos abaixo:

* Tipo de**rubrica incorreta** no eSocial Web

1. Para corrigir o tipo de rubrica e incidência da Contribuição Previdenciária divergentes, no módulo Folha de Pagamento acesse **Administração de Pessoal | Eventos** e altere a parametrização conforme a sua necessidade.
2. Em seguida, acesse **eSocial | Fila de Eventos** e gere o XML do evento criado a partir da alteração para envio ao eSocial.

* Inclusões, exclusões ou alterações nas bases e/ou valores operados diretamente no Portal eSocial.

      1.Deverá ajustar as informações no envelope de pagamento do funcionário.  
      2.Depois, envie uma retificação da Rememureção/Desligamento ao eSocial.

* **Vigência** em desacordo com o Período de Apuração

      1.  Neste caso, verifique a necessidade de uma alteração do S-1010 ou inclusão com o inicio de vigência desejado.

**Importante**  
Para facilitar a validação do XML, execute o processo **Validar S-1200 com Envelope** presente em **eSocial | Eventos Periódicos**.

**Saiba mais**  
Para mais informações acesse: 

* [S-1010 - Tabela de Rubricas](http://tdninterno.totvs.com/display/public/LRM/S-1010+-+Tabela+de+Rubricas)

Desconto INSS RH

O valor INSS RH é a soma encontrada no envelope de pagamento.

Para isso, segue algumas validações:

* Nova **Tabela INSS** Progressiva

      1.Verifique se Versão/Patch contempla a [Nova Tabela INSS Progressiva](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042321514-RM-FOP-Como-criar-Tabela-INSS-Progressiva-?source=search) conforme eSocial.

      2.Em seguida, acesse o menu Administração de Pessoal | Cadastros | Funcionários | Envelope  e recalcule o envelope de pagamento.

* Incidência incorreta nos eventos do **Tipo Provento**  
  O sistema irá somar os valores dos eventos que possuem incidência em INSS para montar a Base de Cálculo da Contribuição Previdenciária e, consequentemente, calcular o INSS.

Desconto INSS Governo

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

**Saiba mais**  
Para mais informações acesse: 

* [S-1010 - Tabela de Rubricas](http://tdninterno.totvs.com/display/public/LRM/S-1010+-+Tabela+de+Rubricas)
