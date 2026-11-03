---
article_id: 23765466976151
category: GPE - eSocial - FGTS Digital
content_hash: 8b4c95e085dd8ee38f49977e77ae0c7f9f968c7cbca46c16f6338823aad97e47
fetched_at: '2026-06-28T22:44:59.377554+00:00'
product: protheus
section_id: 17829152532503
source: central-protheus
title: RH - Linha Protheus - GPE - FGTS Digital - Como será tratado o FGTS 13º salário
  na Rescisão quando houver antecipação do 13º calculada
type: support-article
updated_at: '2024-07-17T18:56:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23765466976151-RH-Linha-Protheus-GPE-FGTS-Digital-Como-ser%C3%A1-tratado-o-FGTS-13%C2%BA-sal%C3%A1rio-na-Rescis%C3%A3o-quando-houver-antecipa%C3%A7%C3%A3o-do-13%C2%BA-calculada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23765466963735) Tempo aproximado para leitura: **00:01:00 min**

**Duvida**Funcionário recebeu antecipação do 13º salário e foi desligado posteriormente com perda de avos. Como fica o FGTS 13º neste caso?

**Ambiente**TOTVS RH - (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O sistema foi ajustado para ser compatível com as normas do FGTS Digital, especialmente para situações de rescisão que envolvem descontos de adiantamento do 13º salário superiores ao valor pago.  
  
Essa dúvida também foi respondida pelo eSocial no [Perguntas Frequentes](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes), veja abaixo:

**02.14 (15/03/2024) Trabalhador recebeu adiantamento de 50% do décimo terceiro salário em fevereiro, mas foi demitido em abril e o valor de 13º proporcional ficou menor que o recebido a título de adiantamento. Como fica a devolução do FGTS sobre essa parcela no desligamento?**

Quando houver desligamento do trabalhador e o valor pago a título de adiantamento de 13º salário for maior que o valor de 13º salário proporcional a pagar na rescisão, o empregador poderá compensar esse adiantamento com outras verbas rescisórias, conforme legislação vigente. É preciso observar que o código de incidência de FGTS da parcela a ser compensada em outras verbas não deve ser igual a [12 - Base de cálculo do FGTS 13º salário] e sim o mesmo da remuneração mensal da qual está sendo subtraída a parcela (codIncFGTS = [11- Base de cálculo do FGTS mensal]). Caso contrário, a base de cálculo da parcela mensal não sofre a devida redução.  
  
**Procedimento no sistema**- Cadastrar verbas vinculadas aos [Ids 1676 e 1677](https://tdn.totvs.com/pages/releaseview.action?pageId=469452222) com o Tipo Cód = 4- Base Desconto;  
- Conforme instrução do eSocial, a verba com o Id 1677 deve ter incidência FGTS = 11;  
- Calcular a Rescisão e conferir os valores de FGTS 13º Salário;  
- Transmitir o evento S-2299 e conferir os valores de FGTS no eSocial e FGTS Digital; 

No [Relatório S-2299](https://centraldeatendimento.totvs.com/hc/pt-br/articles/12927984951191-RH-Linha-Protheus-GPE-eSocial-S-2299-Como-gerar-o-relat%C3%B3rio-de-conferencia-do-evento-S-2299) gerado através da rotina de rescisão, é possível verificar as incidências das verbas/rubricas que estão no cadastro de verbas. As informações são demonstradas da mesma forma que o relatório S-1200, porém com as verbas calculadas na rescisão.

No módulo Automação Fiscal foi disponibilizado o [Painel de Conferência de FGTS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055612014-Automa%C3%A7%C3%A3o-Fiscal-Relat%C3%B3rio-Acessando-o-Painel-de-Confer%C3%AAncia-de-FGTS) para verificação dos trabalhadores com divergências.  
  
**Saiba Mais**Para saber mais consulte os links abaixo:  
[Tabela 23 - Leiaute eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#23)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes FGTS Digital](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus#:~:text=Assistente%20Virtual%20Carolina-,Carolina%20%2D%20Assistente%20Virtual%20%2D%20Como%20usar%20a%20Carolina,pelo%20%C3%ADcone%20no%20produto%20Protheus&text=Como%20usar%20a%20Carolina%20pelo%20%C3%ADcone%20no%20produto%20Protheus%3F&text=A%20partir%20da%20vers%C3%A3o%20de,para%20a%20linha%20TOTVS%20RH)
