---
article_id: 31355180660887
category: RH - Feedz
content_hash: f5fe5c2481362256ec3a3bdb815948b1587df1449958e4128531e3f67f40ec2e
fetched_at: '2026-06-28T22:43:08.578639+00:00'
product: protheus
section_id: 30156142614039
source: central-protheus
title: RH - Linha Protheus - GPE - Integração de Cargos para Feedz
type: support-article
updated_at: '2025-04-11T21:12:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31355180660887-RH-Linha-Protheus-GPE-Integra%C3%A7%C3%A3o-de-Cargos-para-Feedz
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31355225253911) Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como realizar a integração de Cargos do Protheus para Feedz?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**A integração de **Cargos** do Protheus para Feedz deve ser feita via rotina de **Carga Inicial (GPEM939)**, após validação dos passos abaixo:  
  
**1 -** Verificar como está o **compartilhamento da tabela SQ3** - Cargos, para avaliar a necessidade ou não de criação do **[DexPara de Cargos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31354619113239-RH-Linha-Protheus-GPE-Cadastro-do-DexPara-de-Cargos-para-integra%C3%A7%C3%A3o-com-a-Feedz).**  
**>** Se houver **qualquer nível de exclusividade na SQ3**: se torna **obrigatório o cadastro de DexPara** através da rotina **GPEA944B** para que não ocorra duplicidade de cadastros na Feedz, visto que a plataforma **não aceita registros com descrições iguais, mesmo quando os códigos são diferentes.**  
**>** Se a SQ3 for **totalmente compartilhada:** **não é necessário o cadastro do DexPara.**  
  
**2 -** Se a tabela **SQ3** for **totalmente compartilhada**, verificar se não existem **Cargos** com **Descrição/Nome iguais**, mesmo se o código dos cadastros forem diferentes.  
  
Cabe ressaltar que estas medidas são **essenciais** para garantir a integração correta dos dados, caso contrário, a cada integração feita os dados podem ser sobrescritos na Feedz, e a plataforma acaba não recebendo todos os cadastros necessários.  
  
Após as validações acima, para **integrar os Cargos** para a Feedz deve ser acessada a rotina de C**arga Inicial (GPEM939)**, onde deve ser selecionada a opção de Cargos e o código das Filiais onde serão buscados os cadastros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31355180642455)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31355180642583)  
  
Se for parametrizado na Carga Inicial para **aguardar o retorno da integração**, o *log* em tela será exibido com o ***status* do envio dos dados.**  
Não existindo nenhuma inconsistência nos dados, a integração será concluída com sucesso:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31355180642967)  
  
  
**Saiba Mais:**[RH - Linha Protheus - GPE - Cadastro do DexPara de Cargos para integração com a Feedz](https://centraldeatendimento.totvs.com/hc/pt-br/articles/31354619113239-RH-Linha-Protheus-GPE-Cadastro-do-DexPara-de-Cargos-para-integra%C3%A7%C3%A3o-com-a-Feedz)  
[Documentação Técnica - Integração com a Feedz - Pt. 1](https://tdn.totvs.com/pages/releaseview.action?pageId=756450483#jsons-funcionarios)  
[Documentação Técnica - Integração com a Feedz - Pt. 2](https://tdn.totvs.com/pages/viewpage.action?pageId=756451624)
