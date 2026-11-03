---
article_id: 360043059473
category: RH - Definições de Cálculo
content_hash: 4d0411ecba08ad1c3b0cb473913aa72c35620390bbdb3c2054244bb4434783e9
fetched_at: '2026-06-28T22:43:22.326757+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar ou atualizar a tabela de INSS
type: support-article
updated_at: '2026-04-22T12:16:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043059473-RH-Linha-Protheus-GPE-Como-cadastrar-ou-atualizar-a-tabela-de-INSS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20624174687383)** Tempo aproximado para leitura: **00:02:20 min**  
  
**Dúvida**  
Como cadastrar ou atualizar a **tabela de INSS?**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
1. Acesse a rotina **GPEA320** em **Atualizações > Definições de cálculo > Manutenção de tabela**;

2. Selecione a tabela **S001 - Tabela de INSS**

3. Caso seja a primeira vez que está cadastrando-a, clique em **incluir**. Caso deseje atualizar o conteúdo dela, clique em **Outras Ações > Alterar**

4. Preencha o **Ano/ Mês início** e **Ano/ Mês Final** de sua vigência. No caso utilizamos **202501** e **202512.**  
Informe para cada linha o salário de Contribuição até, percentual de desconto e percentual de dedução na base do IRRF de acordo com a tabela Progressiva do ano calendário em questão:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37678669181975)

No Sistema o cadastro deve ficar da seguinte forma:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37678632280855)  
Cada **linha** desta tabela será destinada a **uma faixa salarial diferente.** Para o ano de 2025 temos 4 faixas salariais, portanto para este ano teremos 4 linhas com o mesmo ano/ mês início e ano/ mês final.  
  
Caso já tenha informações do ano anterior, basta **incluir** novas linhas com as novas faixas. 

**INSS:**  
**1º Faixa =** 1.621,00  \* 0,075 => 121,575  
**2º Faixa =** 2.902,84 – 1.621,00  => 1.281,84 \* 0,09 => 115,365  
**3º Faixa =** 4.354,27 – 2.902,84 => 1.451,43\* 0,12 => 174,171  
**4º Faixa =** 8.475,55 – 4.354,27 =>  4.121,28 \* 0,14 => 576,979

INSS Total => 121,57 + 115,36 + 174,17 + 576,97 = **988,07\***

\* O cálculo acima demonstrado está relacionado ao truncamento exposto no MOS do eSocial, o qual utiliza duas casas decimais para cálculo.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Tabelas que sofrem alterações de um ano para o outro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000152881-RH-Linha-Protheus-GPE-Tabelas-que-sofrem-altera%C3%A7%C3%B5es-de-um-ano-para-o-outro?source=search)  
[Atualização das Tabelas de INSS, Piso Salarial e Salário Família para 2025](https://www.totvs.com/blog/fiscal-clientes/atualizacao-das-tabelas-de-inss-piso-salarial-e-salario-familia-para-2025/)
