---
article_id: 360028540832
category: RH - Benefícios
content_hash: 9b3894fc567134cb5075c85b59453ed36b87ceb1d74dc6b416a34d0dd237c5da
fetched_at: '2026-06-28T22:44:03.541503+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Cadastro e Cálculo do Plano de Saúde Automático
type: support-article
updated_at: '2025-09-29T21:43:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028540832-RH-Linha-Protheus-GPE-Cadastro-e-C%C3%A1lculo-do-Plano-de-Sa%C3%BAde-Autom%C3%A1tico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32737280901655) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como cadastrar e calcular o Plano de Saúde de forma automática?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões   
  
**Solução**A Rotina **Definição do Plano de Saúde** é responsável pelo cadastro das informações para **cálculo automático** de Plano de Saúde (**Assistência Médica e/ou Odontológica**), **desvinculada** do cadastro de funcionários. Por meio deste cadastro é possível definir as informações de fornecedores, tipos de plano, códigos de planos e vigência para funcionários, dependentes e agregados de forma automática.   
  
Diferentemente da rotina de Plano de Saúde Ativos, na Definição de Plano de Saúde **é permitida apenas uma configuração** de Assistência Médica e/ou Assistência Odontológica para funcionários e uma configuração para Dependentes/Agregados.  
  
Para configurar do cadastro automático do Plano de Saúde, realize os seguintes passos:  
  
1. Em Gestão de Pessoas, Acesse: **Atualizações** /**Definições de Cálculo / Manutenção de Tabelas /**Tabelas **S016 ou S017 ,** e informe os dados do Fornecedor da Assistência Médica ou Odontológica.  
No exemplo abaixo, iremos utilizar o Fornecedor Plano de Assistência Médica:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737280903831)

2. Acesse: **Atualizações** /**Definições de Cálculo / Manutenção de Tabelas** e defina as regras de desconto da Assistências Médica/Odontológica de acordo com a demanda da empresa (Tabelas: S008, S009, S013, S014, S028, S029, S030 ou S031).  
No exemplo abaixo, iremos utilizar a tabela S008:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737297279895)  
  
  
3. Acesse: **Atualizações** / **Benefícios** / **Cálculo Automático / Definição do Plano de Saúde,** e preencha as informações para cálculo do benefício;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737280906135)

4. Acesse: **Atualizações** / **Benefícios** / **Cálculo Automático / Critérios de Benefícios ,** e informe os critérios para cadastro do Plano de saúde;  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737297281431)  
  
  
5. Acesse: **Atualizações** / **Benefícios** / **Cálculo Automático / Lançamento de Vínculos ,** na coluna **Tipo Ben**, selecione a opção **PS** **Plano de Saúde** e informe no campo **Chave Ent**. o critério do Benefício, e as informações do Plano de Saúde nos demais campos;![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737297283479)  
  
  
6. Acesse: **Atualizações** / **Benefícios** / **Cálculo Automático / Processamento ,** e preencha os parâmetros para inclusão do cadastro do Benefício.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737280909079)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737297284759)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737280910359)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/32737297285527)  
  
  
Após realizar a configuração acima, os dados do Plano de Saúde serão cadastrados de forma automática para os funcionários de acordo com os Critérios de Benefícios, e podem ser visualizadas na rotina **Plano de Saúde Ativos.****Observação 1***:* Caso o **funcionário** tenha **mais de uma configuração de Plano de Saúde,** indicamos que a parametrização do cálculo seja realizada diretamente pela rotina **Plano de Saúde Ativos**.  
  
**Observação 2:**Verificar se na rotina Cadastro de Funcionários, na aba Benefícios, o campo **Pl. Saúde** está **= sim.** Caso contrário, alterar = 1.  
  
  
**Saiba Mais**[RH - Linha Protheus - GPE - Memória de Cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043182293-RH-Linha-Protheus-GPE-Mem%C3%B3ria-de-C%C3%A1lculo-de-Benef%C3%ADcios?source=search)  
[RH - Linha Protheus - GPE - Como é feito o cálculo automático de benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031353154-RH-Linha-Protheus-GPE-Como-%C3%A9-feito-o-c%C3%A1lculo-autom%C3%A1tico-de-benef%C3%ADcios?source=search)  
[RH - Linha Protheus - GPE - Como funciona a hierarquia do cálculo automático de benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051276674-RH-Linha-Protheus-GPE-Como-funciona-a-hierarquia-do-c%C3%A1lculo-autom%C3%A1tico-de-benef%C3%ADcios?source=search)  
[RH - Linha Protheus - GPE - Relatório de Conferência para Cálculo de Benefícios Automáticos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052106234-RH-Linha-Protheus-GPE-Relat%C3%B3rio-de-Confer%C3%AAncia-para-C%C3%A1lculo-de-Benef%C3%ADcios-Autom%C3%A1ticos?source=search)  
[RH - Linha Protheus - GPE - No cálculo automático de benefícios, o sistema faz o cálculo normalmente mesmo que não haja vínculo para receber benefício.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052034193-RH-Linha-Protheus-GPE-No-c%C3%A1lculo-autom%C3%A1tico-de-benef%C3%ADcios-o-sistema-faz-o-c%C3%A1lculo-normalmente-mesmo-que-n%C3%A3o-haja-v%C3%ADnculo-para-receber-benef%C3%ADcio-?source=search)
