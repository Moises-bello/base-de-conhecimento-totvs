---
article_id: 17884073444119
category: Importação
content_hash: 8a13932cb84a8249188ad2b9923e2417f6dada929cbb6565a59681153fcce005
fetched_at: '2026-06-28T22:46:33.722822+00:00'
product: rm
section_id: 6045469428631
source: central-rm
title: 'RH - RM - PTO - Erro ao importar batidas: Não encontrado o funcionário conforme
  o filtro de seleção e o CPF ou PIS'
type: support-article
updated_at: '2025-01-07T19:24:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17884073444119-RH-RM-PTO-Erro-ao-importar-batidas-N%C3%A3o-encontrado-o-funcion%C3%A1rio-conforme-o-filtro-de-sele%C3%A7%C3%A3o-e-o-CPF-ou-PIS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17884058612247) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**  
No módulo Automação de Ponto, ao tentar realizar o processo de importação de batidas é apresentada a mensagem [Não encontrado o funcionário conforme o filtro de seleção e o CPF ou PIS].   
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - 12.1.2302 e superiores.  
  
**Causa**

**Abaixo segue situações que podem causar o erro:**

* Antes de realizar a importação, faça a validação dos filtros utilizados no processo de importação.

Na tela de importação,  no campo 'Quebra de Seção', selecione a Quebra Padrão:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/29044308249495)

Clique no botão 'Seleção de Funcionários'  e faça a seguinte validação:  
  1 - Se há algum funcionario selecionado,   
  2 - Se a Situação, Tipo de Funcionários e Recebimentos estão marcados corretamente, conforme os dados dos funcionários no qual irá importar as batidas.   
  3 - Valide se não há nenhuma consulta SQL, utilizada para fazer o filtro caso tenha a remova.![](https://centraldeatendimento.totvs.com/hc/article_attachments/29044308255639)

* Atualmente com a entrada da Portaria 671, onde há uma orientação que as linhas referentes as marcações do arquivo AFD, a posição do CPF é de **12 dígitos**, (mesmo que a quantidade de dígitos padrão seja 11 para o CPF):

A partir  31/08/2023 o MTE atualizou o layout para a importação de batidas, onde permite duas possibilidades válidas de preenchimento dos campos CPF. Supondo o CPF “XXXXXXXXXXX” e o espaço reservado para o campo tenha tamanho 12(doze). 

a)   Alinhamento com zero à esquerda: “0XXXXXXXXXXX”;

b)   Alinhamento com espaço à direita: “XXXXXXXXXXX ”. 

![](https://totvssuporte.zendesk.com/attachments/token/5xmftGa84ZnajXeckVKodQUEB/?name=image.png)

Assim , a partir das versões 12.1.2302.226, 12.1.2306.171 e 12.1.2310.105 foi liberado o ajuste que para possa ser realizado a importação de batida conforme os dois exemplos acima.

**Para maiores detalhes de como deve ser o layout acesse o documento abaixo:**

**[RH - RM - PTO - Tipos de REPs (Registros Eletrônicos de Ponto) de acordo com a Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22760840044183)**

Caso não esteja nas versões que comtempla os tipos de layout, **faça o seguinte paliativo (medida de contorno)** no arquivo de importação gerado pelo relógio: ajuste as linhas referentes as marcações para que fiquem **sem o zero '0' antes** do CPF e um **espaço após** o CPF. Conforme o exemplo abaixo:

00000049332023-08-31T08:23:00-0300**16661696061** b722

Observação: O layout utilizado na importação, deve considerar a portaria 671.    
  
 ![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29044318406679)  
  
**Saiba Mais:**  
[PORTARIA/MTP Nº 671, DE 8 DE NOVEMBRO DE 2021](https://in.gov.br/en/web/dou/-/portaria-359094139)  
[Perguntas e Respostas - Portaria n° 671/2021](https://www.gov.br/trabalho-e-emprego/pt-br/assuntos/inspecao-do-trabalho/fiscalizacao-do-trabalho/Perguntas%20e%20Respostas%20REP)  
[Layout de Relógio](https://tdn.totvs.com/pages/viewpage.action?pageId=452718923)  
[RH - RM - PTO - Tipos de REPs (Registros Eletrônicos de Ponto) de acordo com a Portaria 671](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22760840044183)
