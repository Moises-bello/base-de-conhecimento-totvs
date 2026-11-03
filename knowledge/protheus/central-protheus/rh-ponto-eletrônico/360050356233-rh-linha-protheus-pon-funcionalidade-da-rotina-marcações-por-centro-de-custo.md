---
article_id: 360050356233
category: RH - Ponto Eletrônico
content_hash: 16d3ca95707cbc7db15a4c9ec64d34c49c19d2c65ce8e6f36b1274dde85c5c0e
fetched_at: '2026-06-28T22:44:58.318618+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Funcionalidade da rotina Marcações por Centro de
  Custo
type: support-article
updated_at: '2021-09-10T20:20:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050356233-RH-Linha-Protheus-PON-Funcionalidade-da-rotina-Marca%C3%A7%C3%B5es-por-Centro-de-Custo
---

**Dúvida**Funcionalidade da rotina Marcações por Centro de Custo - PONA230  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões **Solução**Permite que sejam realizadas alterações de ajustes das marcações geradas pelo relógio de ponto na opção Leitura/Apontamento, por Centro de Custo.  
  
Para atender a Portaria MTE 1.510/2009, ao realizar manutenção das marcações é necessário justificar o motivo da alteração, através da caixa de diálogo exibida no momento da alteração. Os motivos devem ser cadastrados na rotina Motivo da Manutenção.  
Para carregar as marcações automáticas nos processos de leitura/apontamento e manutenção das marcações, deve ser configurado o parâmetro **MV\_GETMAUT**.  
**Carregar as Marcações automáticas** nos processos de Leitura/Apontamento de Marcações. **"S" - Carrega (Valor Padrão)** e **"N" - Nao Carrega   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408257447703/mceclip0.png)**No processo tradicional, conforme a regra adotada, as marcações não registradas pelo funcionário serão geradas automaticamente no processo de leitura e manutenções. No entanto, caso sejam verificadas novas marcações para um dia em leituras posteriores, onde anteriormente foram geradas marcações para as mesmas entradas e saídas, o Sistema apresentará lançamentos em duplicidade. A ativação desse parâmetro possibilita que marcações geradas automaticamente sejam desconsideradas na leitura e nas manutenções, caso o funcionário registre marcações para as mesmas entradas e saídas.  
  
O Sistema permite que a geração das Marcações Automáticas seja feita com minutos aleatórios. Para isso, é necessário que o parâmetro **MV\_MCALEAT** esteja com o conteúdo preenchido com valor superior a zero. Este parâmetro irá definir a quantidade máxima de minutos que poderão ser utilizados para gerar as marcações de forma aleatória, exemplo: 05, 10.  
  
De acordo com o controle de marcações, existe a geração de calendário do funcionário com base nas informações do cadastro do funcionário. Ou seja, a geração do calendário depende do turno e regra cadastrados para o funcionário, e a partir dessas informações é que são geradas as informações referentes aos horários a serem cumpridos, conferidos e comparados com os do funcionário durante a sua jornada de trabalho.  
  
Para o cadastramento das ausências, as informações a serem lançadas no cadastramento de Ausências (tabela SR8) estão no cadastro de Tipo de Ausências(tabela RCM).  
  
**Saiba Mais**  
Manual do Ponto Eletrônico: https://tdn.totvs.com/pages/viewpage.action?pageId=630823373
