---
article_id: 7974211719447
category: Férias
content_hash: d3452a67475217b492d7fd1d1d624da818516ad5a09b4785392a84a00f391b8c
fetched_at: '2026-06-28T22:46:56.239045+00:00'
product: rm
section_id: 1500000861102
source: central-rm
title: RH - RM - FOP - Cadastrar Férias Múltiplos Vínculos Outro emprego
type: support-article
updated_at: '2025-01-16T23:29:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7974211719447-RH-RM-FOP-Cadastrar-F%C3%A9rias-M%C3%BAltiplos-V%C3%ADnculos-Outro-emprego
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29294337815191)**Tempo aproximado para leitura:**00:04:07 min  
  
Dúvida**  
Como realizar calculo férias partidas ou integrais Múltiplos Vínculos Outro emprego?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**

Para solucionar esta dúvida, realize os seguintes passos:  
  
**1.**Parametrizar o sistema para o processo de múltiplos vínculos para atender o cálculo de INSS conforme o eSocial.

* Para calcular o INSS conforme o eSocial, será necessário marcar o parâmetro “Calcula INSS conforme eSocial” e informar a partir de quando o sistema iniciará a calcular desta forma, em Configurações | Parametrizador | Folha Normal | Geral;
* O sistema não irá trabalhar mais com chapa centralizadora, para atender o eSocial;
* Marcando esse parâmetro em uma coligada, todas deverão estar marcadas;
* O sistema irá validar a base de calculo através do CPF do funcionário.

Acessando o caminho: **Configurações | Parametrizador | Folha normal | Geral  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10376057564695)**

**2.**Cadastrar os códigos de cálculo abaixo para atenderem às situações de múltiplos vínculos:

[Código de Cálculo 186 - Base INSS Férias Mês Outro Emprego Desc. Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=452719931)

[Código de Cálculo 159 - INSS de Férias Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452718222)

[Código de Cálculo 185 - INSS de Férias Próximo Mês Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452719942)

[Código de Cálculo 187 - Base INSS Férias Próx. Mês Outro Emprego Desc. Complementar](https://tdn.totvs.com/pages/viewpage.action?pageId=452719926)

[Código de Cálculo 192 - Base INSS Férias Mês Anterior Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452719930)

[Código de Cálculo 193 - INSS de Férias Mês Anterior Outro Emprego](https://tdn.totvs.com/pages/viewpage.action?pageId=452719896)  
  
**Para maiores informações quanto a parametrização e funcionalidades dos códigos de cálculos acima, [CLIQUE AQUI.](https://tdn.totvs.com/pages/releaseview.action?pageId=452719279)  
  
3.**Com a parametrização e o cadastro do evento acima, o sistema poderá processar o cálculo de múltiplos vínculos.   
  
Veja abaixo um exemplo do cálculo para esta situação:  
  
Cadastro férias partidas:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7972470550679)  
  
Após **Salvar,**será necessário informar os eventos em Eventos Adicionais com os valores.  
  
CC(159) INSS DE FERIAS OUTRO EMPREGO ,  
CC(186) BASE INSS FER MES OUTRO EMP DESC COMPL,  
CC(185) INSS FERIAS PROX MES OUTRO EMPREGO e  
CC(187) BASE INSS FER PROX MES OUTRO EMP DESC COMPL  
  
Obs.: Deverá ser informada a base de cálculo de INSS férias no mês de outro emprego já acrescido 1/3.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7972482381207)  
  
Visualize o Recibo e o Log de calculo:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7972576399511)  
  
Print log de calculo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7972581271575)  
  
O sistema realiza o abatimento do valor da Base.  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7972630054551)  
  
Ao virar competência para o Mês de retorno das férias ( Finalização), será necessário realizar alteração no Adicionais de Férias.  
  
Acessar **Cadastros | Funcionários | Férias |** pasta **Adicionais de Férias** retirar os eventos com códigos de cálculo:   
  
CC(185) INSS FERIAS PROX MES OUTRO EMPREGO e  
CC(187) BASE INSS FER PROX MES OUTRO EMP DESC COMPL  
  
Informar em **Cadastros | Funcionários | Férias |** pasta **Adicionais de Férias** os eventos com os códigos de cálculo e seus respectivos valores:   
  
CC(192) - BASE INSS FERIAS MES ANTERIOR OUTRO EMPREGO e  
CC (193) - INSS DE FERIAS MES ANTERIOR OUTRO EMPREGO

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7974171133463)  
  
Print envelope finalização férias:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7974147367447)
