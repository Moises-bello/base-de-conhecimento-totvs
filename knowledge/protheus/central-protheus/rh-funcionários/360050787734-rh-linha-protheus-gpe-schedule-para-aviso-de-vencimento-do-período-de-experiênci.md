---
article_id: 360050787734
category: RH - Funcionários
content_hash: 51e268b073e3345a9dbd7c7bbed77b4141d5db5524221e5df7461891001decc4
fetched_at: '2026-06-28T22:43:28.688517+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Schedule para Aviso de Vencimento do Período de
  Experiência
type: support-article
updated_at: '2025-09-04T18:15:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050787734-RH-Linha-Protheus-GPE-Schedule-para-Aviso-de-Vencimento-do-Per%C3%ADodo-de-Experi%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32103808887447) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Schedule para Aviso de Vencimento do Período de Experiência   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Essa rotina realiza o envio de e-mail para o superior direto dos funcionários que o período de experiência se encerra dentro dos dias estipulados no parâmetro MV\_WFFIMXP, para isso é necessário configurar:

1. Parâmetros

**MV\_WFFIMXP:**Quantidade de dias somados a data atual para a busca.

**MV\_RHCONTA:** Conta de e-mail utilizada para envio

**MV\_RHSERV:** Servidor de e-mail utilizado para o envio

**MV\_RHSENHA:** Senha do e-mail utilizado para o envio

**MV\_RHAUTEN:** Determina se o servidor de e-mail requer autenticação. Conteúdo .T. requer, .F. não requer autenticação.  Conteúdo padrão: .F.  

Exemplo: MV\_WFFIMXP = 10  
Executando a rotina no dia 03/10/2019 o sistema irá procurar os funcionários  que o período de experiência termina no dia 13/10/2019

2. Schedule  
Será necessário cadastrar manualmente o schedule da rotina no **Módulo Configurador.**  
Acesse: **Ambiente > Schedule > Schedule**, clique em **Agendamento > Cadastro** e inclua a rotina GPEW050 com **recorrência diária.**

**![](https://tdn.totvs.com/download/attachments/516636429/image2019-10-3_17-52-46.png?version=1&modificationDate=1570137377987&api=v2)**

3. Cadastro do funcionário

O sistema busca os funcionários que possuem os campos RA\_VCTOEXP e/ou RA\_VCTEXP2 preenchidos, e que estejam na data definida pelo parâmetro MV\_WFFIMXP. 

Data atual + MV\_WFFIMXP  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14219123924759)

Após selecionar os funcionários o sistema busca o superior hierárquico que irá receber o e-mail, caso o funcionário não tenha um superior definido ou o superior não tenha o e-mail informado no cadastro o aviso será enviado para o e-mail informado no parâmetro MV\_WFFEREM.

**Observação:** Por ser uma alteração no dicionário de dados o parâmetro MV\_WFFIMXP será disponibilizado no produto padrão na release 12.1.27

Caso queira utilizá-lo, será necessário incluir no configurador as seguintes informações:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360078426334)

**Saiba Mais:**  
[Aviso Vencimento Período de Experiência](https://tdn.totvs.com/pages/viewpage.action?pageId=516636429) [GPEW050](https://tdn.totvs.com/pages/viewpage.action?pageId=516636429)  
[Schedule - Como agendar a execução de rotinas](https://tdn.totvs.com/x/2bEpE)

#
