---
article_id: 30457140576663
category: RH - Benefícios
content_hash: 81db611776c602a12f9a563cf9d0b18115d17578f01b9844b1254ee12027d14f
fetched_at: '2026-06-28T22:44:04.723909+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Novo filtro do cálculo do Plano de Saúde
type: support-article
updated_at: '2025-08-08T17:48:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30457140576663-RH-Linha-Protheus-GPE-Novo-filtro-do-c%C3%A1lculo-do-Plano-de-Sa%C3%BAde
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30457140536727)Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**Funcionamento do cálculo do Plano de Saúde com o novo Filtro.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.2310

**Solução**Na rotina de cálculo, caso o roteiro PLA for selecionado, será apresentada uma nova pegunta que inclui os campos: **Fornecedor do Plano** e **Código do Plano**.  
As perguntas são do tipo *range*, permitindo a seleção de múltiplos fornecedores e planos ao mesmo tempo.  
Se as perguntas **não** forem preenchidas, o cálculo será realizado para **todos os fornecedores e planos** dos funcionários relacionados ao processo e período em questão, caso contrário, o cálculo será feito apenas para os fornecedores e planos selecionados nas perguntas subsequentes.  
  
A melhoria depende da aplicação da **atualização** liberada no **pacote de expedição do módulo RH** com **data superior à 15/11/2024**, e da execução do **UPDDISTR** com o dicionário diferencial.  
  
Foi efetuada a criação do **grupo de perguntas GPEM016P** no dicionário SX1, conforme estrutura abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30459832831767)  
  
  
**OBS:** Para o **correto funcionamento** das novas perguntas no momento do cálculo do roteiro PLA, acesse o cadastro de roteiros no SIGAGPE em > Atualizações > Definições de Cálculo > Roteiros de Cálculo e verifique se foi atualizado o **roteiro PLA** com a pergunta **GPEM016P** no campo Grp Pergunte (RY\_PERGUNT).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30459832834711)  
  
  
**->** Exemplo de funcionamento 1:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30457124328471)

![](https://tdn.totvs.com/download/attachments/864986234/image-2024-8-27_15-41-21.png?version=1&modificationDate=1724784086613&api=v2)

**ATENÇÃO**: É importante ressaltar que no recálculo, a rotina GPEM020 possui o comportamento de **apagar os registros existentes de cálculos anteriores**, daqueles dados selecionados. Isso pode causar uma sobreposição dos cálculos, quando um funcionário possuir mais de um plano ativo de fornecedores diferentes. Neste sentido, o procedimento correto foi descrito no cenário abaixo:  
  
**->** Exemplo de funcionamento 2:  
Funcionário com plano **médico** e **odontológico ativos**, fornecedores diferentes.  
![](https://tdn.totvs.com/download/attachments/864986234/image-2024-11-13_11-41-31.png?version=1&modificationDate=1731508891660&api=v2)  
  
  
Cálculo realizado filtrando **somente** o plano médico:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30459789679127)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/30459832837655)  
![image-2024-11-13_11-42-24.png](https://tdn.totvs.com/download/attachments/864986234/image-2024-11-13_11-42-24.png?version=1&modificationDate=1731508945097&api=v2)  
  
  
Para que o plano odontológico não **sobrescreva** o médico, o filtro deve ser feito informando ambos fornecedores no parâmetro:  
![](https://tdn.totvs.com/download/attachments/864986234/image-2024-11-13_11-42-48.png?version=1&modificationDate=1731508969127&api=v2)  
![](https://tdn.totvs.com/download/attachments/864986234/image-2024-11-13_11-42-59.png?version=1&modificationDate=1731508979297&api=v2)

**Saiba Mais:**[Boletim Técnico](https://tdn.totvs.com/pages/releaseview.action?pageId=864986234)  
[RH - Linha Protheus - GPE - Como funciona a rotina de Planos Saúde Ativos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056072793-RH-Linha-Protheus-GPE-Como-funciona-a-rotina-de-Planos-Sa%C3%BAde-Ativos)
