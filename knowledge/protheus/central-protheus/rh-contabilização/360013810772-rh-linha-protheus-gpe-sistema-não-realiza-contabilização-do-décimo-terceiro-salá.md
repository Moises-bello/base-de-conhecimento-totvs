---
article_id: 360013810772
category: RH - Contabilização
content_hash: 2f5779e8d9f54ddc53fba89241f7d6064da5f48275f78fa12281abf6b7f989ab
fetched_at: '2026-06-28T22:43:46.054993+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não realiza contabilização do Décimo Terceiro
  Salário pagos no mês, roteiros 131 - 1ª parcela do 13º e 132 - 2ª parcela de 13º
type: support-article
updated_at: '2026-03-18T17:29:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013810772-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-realiza-contabiliza%C3%A7%C3%A3o-do-D%C3%A9cimo-Terceiro-Sal%C3%A1rio-pagos-no-m%C3%AAs-roteiros-131-1%C2%AA-parcela-do-13%C2%BA-e-132-2%C2%AA-parcela-de-13%C2%BA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15272334470807) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Sistema não realiza contabilização do Décimo Terceiro Salário pagos no mês, roteiros 131 - 1ª parcela do 13º e 132 - 2ª parcela de 13º. Contabilização de decimo terceiro zerada, o que verificar?  
  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Para solucionar essa dúvida, realize os seguintes passos:  
**1.** É necessário possuir o sistema **devidamente atualizado**, para que seja ajustado o grupo de perguntas da rotina GPEM110 com a finalidade demonstrar as opções de contabilizar: Folha, 13 Salário ou Ambos;  
**2.**Para **contabilização da 1ª parcela**, criar o parâmetro MV\_131SEP do tipo lógico , onde:  
  
**.T.** = Gera a primeira parcela do 13 (roteiro 131) com tipo "13" na tabela SRZ(contabilização)  
**.F.**(*Default*) = Gera a primeira parcela do 13(roteiro 131) com tipo "FL" na tabela SRZ(contabilização).  
Caso o parâmetro não seja criado, o sistema irá trabalhar com o retorno .F. gravando o tipo como "FL" para o roteiro 131.  
  
**3.** Para efetuar a contabilização da primeira parcela do 13º você deve verificar se o **roteiro 131** está parametrizado para contabilizar acessando a rotina Roteiros de Cálculo (GPEA160);  
**4.** Altere o campo Contabiliza? (RY\_CONTAB) para "SIM";  
**5.** Ao clicar em OK o sistema emitirá as opções de contabilização: Folha, 13 Salário e Ambos:  
  
Folha → Contabiliza roteiro FOL e demais que estiverem configurados para serem contabilizados. No caso do 131 irá contabilizar de acordo com o MV\_131SEP;  
13º Salário → Contabiliza 131 de acordo com o parâmetro MV\_131SEP e 132 com tipo "13". Não verifica demais roteiros de cálculo;  
Ambos → Contabiliza roteiro FOL e demais que estiverem configurados para serem contabilizados. No caso do 131 irá contabilizar com o tipo "FL" caso MV\_131SEP esteja como .F. e para 132 com o tipo "13".  
  
**6.** Para efetuar a contabilização da segunda parcela do 13º você deve confirmar se o roteiro 132 também está parametrizado para contabilizar;  
**7.** Após realizada a parametrização do roteiro, acessar a rotina GPEM110 (Miscelânea - Fechamentos - Contabilização) preenchendo as perguntas para contabilização.

**Importante:** Se realizado em algum momento o processo de recriação de formulas o campo RY\_CONTAB volta para a configuração padrão "NÃO". Sendo necessário realizar novamente a alteração conforme passo 3.   
  
**Saiba Mais**[Artigos Contabilização](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109092-RH-Contabiliza%C3%A7%C3%A3o?page=2#articles)  
[RH - Linha Protheus - GPE - Contabilização do FGTS de 13º Salário quando o Pagamento do 13º e Rescisão ocorrem no mesmo mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10845216293015-RH-Linha-Protheus-GPE-Contabiliza%C3%A7%C3%A3o-do-FGTS-de-13%C2%BA-Sal%C3%A1rio-quando-o-Pagamento-do-13%C2%BA-e-Rescis%C3%A3o-ocorrem-no-mesmo-m%C3%AAs?source=search)

[RH - Linha Protheus - GPE - Como contabilizar 1º parcela de 13º paga nas férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8844025642135-RH-Linha-Protheus-GPE-Como-contabilizar-1%C2%BA-parcela-de-13%C2%BA-paga-nas-f%C3%A9rias?source=search)
