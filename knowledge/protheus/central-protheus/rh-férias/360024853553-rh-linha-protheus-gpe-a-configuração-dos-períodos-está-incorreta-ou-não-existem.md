---
article_id: 360024853553
category: RH - Férias
content_hash: 20237fd9b1440381fd73428c45cc70bfa73f2125568747e4b780d3d2466fe01d
fetched_at: '2026-06-28T22:43:57.914271+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - A configuração dos períodos está incorreta ou não
  existem dados válidos para o período que esta sendo calculado. Verifique se existe
  período que corresponda a data final das férias
type: support-article
updated_at: '2026-04-29T17:27:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024853553-RH-Linha-Protheus-GPE-A-configura%C3%A7%C3%A3o-dos-per%C3%ADodos-est%C3%A1-incorreta-ou-n%C3%A3o-existem-dados-v%C3%A1lidos-para-o-per%C3%ADodo-que-esta-sendo-calculado-Verifique-se-existe-per%C3%ADodo-que-corresponda-a-data-final-das-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26594333323415) Tempo aproximado para leitura: **00:02:00 min**  
**Ocorrência**Ao calcular as férias apresenta log com a seguinte mensagem:**A configuração dos períodos está incorreta ou não existem dados válidos para o período que esta sendo calculado. Verifique se existe período que corresponda a data final das férias**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360038092814)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**O sistema encontra divergência no cadastro de período (RFQ) com data fim invalida ou sem roteiro FER cadastrado (RCH).  
  
**Solução**Realize as seguintes validações:

**1.**Verifique se a data fim do período que corresponde ao cálculo está correto.   
**Exemplo:**Na imagem abaixo, o mês 12/2025 está com data fim de 30/12/2025, porem o mês na verdade termina em 31/12/2025.   
Nesse cenário, o período **deve ser excluído** e cadastrado corretamente. Verifique [esta documentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060741313-RH-Linha-Protheus-GPE-Como-excluir-um-per%C3%ADodo-aberto-indevidamente-ou-com-informa%C3%A7%C3%B5es-incorretas) de como excluir um período.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35757699613335)

**2.** Verifique também se existe o roteiro FER criado para o período de cálculo e período seguinte, caso as férias sejam partidas ou com abono pecuniário.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35757699616407)

**Saiba Mais**[RH - Linha Protheus - GPE - Tabelas utilizadas para o Cadastro de Período](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8426220799511-RH-Linha-Protheus-GPE-Tabelas-utilizadas-para-o-Cadastro-de-Per%C3%ADodo-GPEA400)  
[RH - Linha Protheus - GPE - Como configurar o compartilhamento das tabelas do Cadastro de Períodos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017451292-RH-Linha-Protheus-GPE-Como-configurar-o-compartilhamento-das-tabelas-do-Cadastro-de-Per%C3%ADodos)  
[RH - Linha Protheus - GPE - Help: Atenção - Problema: Fim das Férias não corresponde a quantidade de dias de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052338674-RH-Linha-Protheus-GPE-Help-Aten%C3%A7%C3%A3o-Problema-Fim-das-F%C3%A9rias-n%C3%A3o-corresponde-a-quantidade-de-dias-de-F%C3%A9rias)
