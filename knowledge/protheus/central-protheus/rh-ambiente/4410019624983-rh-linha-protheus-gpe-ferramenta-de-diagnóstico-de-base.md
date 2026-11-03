---
article_id: 4410019624983
category: RH - Ambiente
content_hash: db08f67e6f8f9362248394e46bafa1e3f59c2067a82835606b84741b6f49b5ff
fetched_at: '2026-06-28T22:43:09.568661+00:00'
product: protheus
section_id: 20669342808471
source: central-protheus
title: Rh - Linha Protheus - GPE - Ferramenta de Diagnóstico de Base
type: support-article
updated_at: '2026-06-25T13:23:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410019624983-Rh-Linha-Protheus-GPE-Ferramenta-de-Diagn%C3%B3stico-de-Base
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26819567276695)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Ferramenta de **Diagnóstico de Base****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A rotina de **Diagnóstico de Base** foi criada para **diagnosticar** possíveis erros de **cadastro** e/ou **parametrização** da base, auxiliando identificar erros causados por configuração indevida.   
A rotina consiste em uma tela que apresentará **12 itens** que poderão ser selecionados para executar a validação da base. O resultado da validação será apresentado em um Log.  
  
Acesse a rotina através do menu padrão do SIGAGPE em **Miscelânea > Diagnóstico > Diagnóstico de Base:**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26819551374231)  
  
Os itens para validação serão os seguintes:  
**Movimentos:****1.** Verificar se o **tipo das verbas condiz com o que está no cadastro de verbas** (**SRV**), por exemplo, uma verba do tipo H (horas), não pode estar lançada no histórico (**SRD**) com o tipo V (Valor);

**2.** Verificar se **existe registro sem os campos chave preenchidos** (Filial,Cód. Verba, Período, Roteiro, Nro. Pagamento e Processo), tanto na **SRD** quanto na **SRC**;  
**3.** Verificar se existe a **verba de ID 0318 nos cálculos efetuados** (tanto histórico - **SRD**, quando mensal - **SRC**), exceto para os funcionários de categoria "C" (Comissionados) e "A" (Autônomos).  
  
**Provisão**:  
**1.** Verificar se existem **meses anteriores ao em aberto da folha**, **sem provisão calculada** (validará apenas os últimos 3 meses).  
  
**Cadastro de Funcionários**:  
**1.** Verificar se o **funcionário** está com a **situação "D"** e não possui data de demissão preenchida e/ou está com o campo **RA\_RESCRAI** em branco;  
**2.** Verificar se o **salário** é o mesmo da **última atualização da SR7** (histórico salarial);  
**3.** Verificar se o funcionário já foi transferido, caso positivo, checar se os dados são os mesmos da última transferência.  
  
**Dias de direito**:  
**1.** Verificar se os **períodos da SRF** condizem com os dados da **SRH**, ou seja, se os dias pagos realmente estão pagos na **SRH** e se os dias a pagar realmente ainda estão pendentes.  
  
**Cadastro de Verbas**:

**1.** Verificar se a **verba com** **"S"** **para IRRF** contém o código de geração da DIRF (esse item já está presente na rotina de diagnóstico da DIRF, porém também será disponibilizado nessa ferramenta);  
**2.** Verificar se há **verbas de férias mês seguinte que estão com "N" no campo RV\_REFFER** (o fechamento de período já realiza essa validação, porém também será disponibilizada nessa ferramenta);

**3.** Verificar se o **código do mês seguinte** está configurado corretamente para as **verbas com ID de cálculo**.  
    **3.1**Para os ID's que não existirem na base, não haverá validação.  
  
**Comparação das verbas com um cadastro padrão:  
1.** Para as verbas com ID de cálculo serão comparadas as incidências com um cadastro padrão de verbas.  
  
**Data de Pagamento de verbas de férias****Avaliação Estrutural  
1.** Verificações no **campo filial**, comparando o **cadastro de empresas (SIGAMAT)** com o campo **filial** das tabelas **SRA/SRC/SRD****Exibe definição de Gestão Corporativa  
1.** Mostra o leiaute do campo filial  
  
**Validação Grupo de Campos x SX3 x Tabelas**

**1.** Validar os tamanhos dos campos Centro de Custo, Matrícula, Filial, Item Contábil e Classe de Valor da tabela **SRA** comparado com a estrutura dos mesmo no configurador e respectivos grupos de campos  
**2.** Verificar se o tamanho no dicionário (Configurador) dos campos Centro de Custo, Matrícula, Filial, Item Contábil e Classe de Valor da tabela **SRA** está divergente do tamanho especificado no respectivo grupo de campos e se o tamanho do campo na tabela física da **SRA** está divergente do tamanho no dicionário.  
  
**Validação de Centros de Custos  
1.** Verificar se existem centros de custo no cadastro de funcionários (**SRA**) ou movimento de cálculo (**SRC**/**SRD**) que não estão cadastrados no cadastro de centro de custos (**CTT**).  
  
**Modo de Compartilhamento:  
1.** Listará todas as tabelas do módulo Gestão de Pessoal, e os respectivos compartilhamentos.![](https://centraldeatendimento.totvs.com/hc/article_attachments/26819551388567)

O log com os resultados será demonstrado de forma separada pelos itens acima, exemplo:

* Cadastro de Verbas:
  + A Verba **"123"** está com **"S"** para IRRF e não contém o código de geração da DIRF;
* Cadastro de Funcionários:
  + O funcionário de matrícula **"000001"** está com a situação **"D"**, porém não possui data de demissão preenchida;

**Observação:**O log acima é apenas um exemplo de como a demonstração no log será separada pelos itens, porém as descrições podem não ser exatamente as apresentadas acima.

**Saiba Mais**

[Pacote de Expedição Contínua do RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de acumulado do eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)

[Artigos Gestão de Pessoas (SIGAGPE)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000926522-Gest%C3%A3o-de-Pessoas-SIGAGPE)

[Artigos Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
