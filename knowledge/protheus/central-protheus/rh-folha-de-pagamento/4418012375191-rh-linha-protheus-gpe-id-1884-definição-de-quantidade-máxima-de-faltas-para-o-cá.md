---
article_id: 4418012375191
category: RH - Folha de Pagamento
content_hash: 7bc8d9450cc40241ed79792508b77d1a29281765841ff2b3f6e412a32dea6013
fetched_at: '2026-06-28T22:44:14.981646+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - ID 1884 Definição de quantidade máxima de faltas
  para o cálculo
type: support-article
updated_at: '2025-05-05T18:40:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418012375191-RH-Linha-Protheus-GPE-ID-1884-Defini%C3%A7%C3%A3o-de-quantidade-m%C3%A1xima-de-faltas-para-o-c%C3%A1lculo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26356791196055)**Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Solicita-se que seja possível definir a quantidade máxima de faltas que o funcionário pode possuir no período de apontamento do ponto para que seja realizado o cálculo do adiantamento, além de deduzir o valor das faltas do provento de adiantamento. Criado identificador de cálculo 1884.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Para possibilitar determinar se o cálculo do adiantamento será realizado de acordo com quantidade de faltas do funcionário, foi criada a tabela auxiliar S147, que poderá ser preenchida conforme o exemplo abaixo:![](https://tdn.totvs.com/download/attachments/656605609/image2021-12-21_9-26-34.png?version=1&modificationDate=1640089733123&api=v2)  
  
**Dica**Os campos **"Filial", "Mes / Ano" e "Cód. do Sindicato"** **não são obrigatórios**. Caso não estejam preenchidos, a quantidade máxima de faltas irá ser considerada para funcionários de qualquer filial, para qualquer período e para qualquer sindicato. Logo, o preenchimento da tabela deverá ser efetuado conforme a necessidade.  
  
Para obter os **dias trabalhados** o sistema irá verificar e **contar as faltas do período do ponto.** As faltas serão obtidas através da tabela de apontamentos do ponto eletrônico (SPC) do período de apontamento que estiver ativo no ponto. Os eventos de faltas do ponto que devem ser considerados devem ser incluídos no novo mnemônico **P\_PDFALADI**, separados por vírgula, conforme exemplo abaixo:

![](https://tdn.totvs.com/download/attachments/656605609/image2021-12-21_9-20-58.png?version=1&modificationDate=1640089733170&api=v2)

O sistema irá **valorizar as faltas de acordo com o salário/dia e irá descontar do provento recebido no adiantamento**, caso o funcionário não tenha ultrapassado o limite máximo de faltas para receber o adiantamento. Para facilitar a conferência, foi criado o ID de cálculo **1884** (Faltas descontadas no adiantamento) para que seja vinculado uma verba de base (desconto) sem incidências, que irá conter na referência a quantidade de faltas e o valor descontado.

**Importante****Apenas** os **funcionários** que **possuam percentual de adiantamento** definido no cadastro de funcionários (RA\_PERCADT) serão calculados. Se o percentual no cadastro estiver zerado, o cálculo **NÃO** será feito.  
  
A funcionalidade da tabela auxiliar S143 descrita na documentação disponível em: [DT Adiantamento - Definição de percentuais por dias trabalhados](https://tdn.totvs.com/pages/viewpage.action?pageId=636525530) será prioritária em relação à configuração da tabela auxiliar S147, ou seja, o sistema primeiro irá verificar se existe configuração válida de cálculo para a funcionalidade da tabela auxiliar S143, e apenas se não houver configuração válida, irá validar se existe configuração descrita nesta documentação.  
  
Ou seja, **NÃO** é possível que para um mesmo sindicato seja realizado as funcionalidades implementadas das tabelas auxiliares S143 e S147 juntas; ou será realizado a funcionalidade da tabela auxiliar S143 ou será realizada a funcionalidade da tabela auxiliar S147.

**Exemplos:**Considerando o exemplo de preenchimento da tabela S147 citada no início da documentação, sem filial e mês/ano preenchido, para o sindicato 01 e com quantidade máxima de faltas 5, segue exemplos de cálculos, **clique em cada um deles para ser direcionado ao boletim técnico.**

* [Exemplo1](https://tdn.totvs.com/pages/releaseview.action?pageId=656605609# "Exemplo1")
* [Exemplo2](https://tdn.totvs.com/pages/releaseview.action?pageId=656605609# "Exemplo2")
* [Exemplo3](https://tdn.totvs.com/pages/releaseview.action?pageId=656605609# "Exemplo3")
* [Exemplo3](https://tdn.totvs.com/pages/releaseview.action?pageId=656605609# "Exemplo3")

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
