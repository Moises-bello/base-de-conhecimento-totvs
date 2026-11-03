---
article_id: 360050369493
category: RH - Cadastros
content_hash: b5a07c3cd09b09a7b6515f3bbb576ec7546645a7509457be8f248d51a7ddf97b
fetched_at: '2026-06-28T22:44:53.018955+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Funcionamento da Tolerância para Hora Extra e Horas
  Não Realizadas
type: support-article
updated_at: '2026-01-15T14:16:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050369493-RH-Linha-Protheus-PON-Funcionamento-da-Toler%C3%A2ncia-para-Hora-Extra-e-Horas-N%C3%A3o-Realizadas
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35192376884631) Tempo aproximado para leitura: 00:02:00 min**  
  
**Dúvida**  
Como funciona a configuração de Tolerância para Hora Extra e Horas não realizadas cadastradas na Regra de Apontamento?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Este documento tem como objetivo explicar o funcionamento da tolerância de Hora Extra e Atrasos cadastradas na Regra de Apontamento;

A rotina pode ser localizada no menu **Atualizações - Cadastro do Ponto - Regra de Apontamento.** Selecione a Regra que deseja ajustar e clique em **'Alterar'**, selecione a Aba **'Tolerâncias'**.   
Para Hora Extra, a configuração dos campos **"Tol. H. Ex. Per"** e **"Tol. H. Extra"** fará com que o sistema tenha três comportamentos possíveis.

* O campo "**Tol. H. Ex. Per**" indica a quantidade da tolerância de Hora Extra por período. Quando preenchido, o sistema irá somar todos minutos feitos a mais da jornada de trabalho de todas as marcações do período e, se a somatória ultrapassar o limite preenchido, será gerado um evento de Hora Extra com o total de minutos.   
  O período referente à Hora Extra ou Atraso é configurado através da aba 'Apuração', onde existem as seguintes opções: diária, semanal, quinzenal ou mensal. Entretanto, quando é cadastrada uma apuração diferente da diária, as tolerâncias por período ainda são computadas diariamente e, somente no cálculo mensal, os apontamentos são exibidos de forma analítica ou sintética, conforme a apuração (no caso de escalonamento, por exemplo).
* O campo "**Tol. H. Extra**" indica a quantidade da tolerância de Hora Extra por marcação. Quando preenchido, qualquer marcação que ultrapassar o valor do campo será gerado um evento de Hora Extra, ou seja, o sistema irá verificar individualmente cada batida, respeitando o valor preenchido no campo. Por exemplo, se um funcionário possui duas batidas excedentes a tabela de horário padrão, para Hora Extra, e apenas uma delas passou do limite, o sistema irá gerar Hora Extra apenas para a batida que ultrapassou o limite.
* Quando ambos os campos **("Tol. H. Ex. Per" e "Tol. H. Extra")** estiverem preenchido as duas regras citadas no item 1 e 2 irão trabalhar juntas. Caso uma marcação passe do valor preenchido no campo **"Tol. H. Extra"**, porém a somatória não ultrapassou o limite preenchido no campo **"Tol. H. Ex. Per"**, será gerada uma Hora Extra apenas da marcação excedente. Se a somatória de todas as marcações ultrapassar o valor do campo **"Tol. H. Ex. Per"**, será gerado o evento de Hora Extra com a total de minutos excedentes.  
    
  **Observação: Não é obrigatório a utilização do dois campos juntos, podendo utilizar apenas um deles Tol. H. Ex. Per ou Tol. H. Extra.**   
    
  **Para Atraso e Saída Antecipada**, ocorre os mesmos comportamentos das tolerâncias de hora extra, porém utilizando os campos "**Tol. Atr. Per**", "**Tol. S. A. Per.**", **"Tol. Atr. S. An"** e "**Tol. Hr. NReal**".

1. Os campos "**Tol. Atr. Per**", "**Tol. S. A. Per.**" e "**Tol. Hr. NReal**" são referentes à tolerância por período para eventos de desconto (Atraso e Saída antecipada). As tolerâncias de atraso e saída antecipada irão validar os eventos de desconto separadamente, ou seja, se o funcionário teve atraso e saída antecipada no mesmo dia, cada evento será validado com sua respectiva tolerância (Atraso ou saída antecipada, por período). No entanto, se utilizarmos a tolerância de horas não realizadas ("**Tol. Hr. NReal**"), ambos os eventos serão somados e validados apenas pela tolerância de horas não realizadas. Para que o sistema utilize a regra mencionada anteriormente, apenas o campo "**Tol. Hr. NReal**" deverá estar preenchido.
2. O campo "**Tol. Atr. S. An"**é referente a tolerância de marcação, onde ambos os eventos (Atraso e Saída Antecipada) utilizarão a mesma tolerância para a apuração de descontos por marcação.
3. A mesma regra citada acima para apuração de horas extras, quando ambas as tolerância estão preenchidas (Tolerância por período e marcação), será utilizada para os eventos de descontos, porém existe uma condição de qual tolerância por período será utilizada, conforme mencionado no primeiro item.  
     
   **Observação: Para a configuração correta da regra de apontamento, o sistema irá validar o preenchimento dos campos "Tol. Atr. Per" e "Tol. S. A. Per.". Caso um deles esteja preenchido com algum valor maior que zero, o campo "Tol. Hr. NReal" terá seu valor zerado e será desabilitado para edição.**

**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)  
[RH - Linha Protheus - PON - Como alterar a Regra de Apontamento de um Funcionário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18869900945687-RH-Linha-Protheus-PON-Como-alterar-a-Regra-de-Apontamento-de-um-Funcion%C3%A1rio)  
[Tolerância para Hora Extra e Horas Não Realizadas](https://tdn.totvs.com/pages/releaseview.action?pageId=496398394)
