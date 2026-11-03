---
article_id: 360043731394
category: LOGIN
content_hash: 2a4574331d79b24da04ff1e95d449e2a3904349c3c85403dfcb0ace20537379c
fetched_at: '2026-06-28T22:44:40.672087+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como associar o Usuário do Portal ao Cadastro
  de Participante para acesso ao MEU RH
type: support-article
updated_at: '2026-06-18T19:20:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043731394-RH-Linha-Protheus-MEU-RH-Como-associar-o-Usu%C3%A1rio-do-Portal-ao-Cadastro-de-Participante-para-acesso-ao-MEU-RH
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05:00 min****Dúvida**Como associar o Usuário do Portal ao Cadastro de Participante para acesso ao MEU RH?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Meu RH – Todas às versões  
  
**Solução**Para associar o **Usuário do Portal** ao **Cadastro de Participante** acesse no Protheus o módulo "**53 - SIGAAPD**" após o menu Atualizações → Participantes → Cadastro:  
  
![95On1GnL4N.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011889821/95On1GnL4N.gif)  
  
A rotina também está disponível no módulo **18 - SIGATCF - Terminal de Consulta do funcionário** no menu **Atualizações -> Configurações -> Usuários -> Cadastro de Participante**  
**[RH - Linha Protheus - MEU RH - Como configurar o Login quando não tem acesso ao módulo 53-SIGAAPD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056577154)**  
  
Na rotina edite um **Cadastro de Participante** e no campo "Usuar.Portal" informe o **Usuário do Portal**, aquele que foi criado via módulo "**18 - SIGATCF**" e no campo "F.Usr.Portal" informe a filial do usuário do portal.  
  
![1WtLtEPJB3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500011611902/1WtLtEPJB3.gif)  
  
Caso o ambiente não possua o campo "**F.Usr.Portal**"(RD0\_FILRH) será necessário aplicar o último acumulado do RH e atualizar o dicionário:  
  
Link: **[Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)**  
  
Para saber mais sobre o campo **RD0\_FILRH** acesse: **[O novo campo RD0\_FILRH](https://tdn.totvs.com/display/NPR/O+novo+campo+RD0_FILRH)**  
  
**Importante:** Caso não tenha nenhum ou faltem alguns Trabalhadores no **Cadastro de Participante** será necessário que realize as validações do artigo abaixo:  
  
**[RH - Linha Protheus - MEU RH - Como relacionar os Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050255013)**  
  
**Saiba Mais:  
[RH - Linha Protheus - MEU RH - Configuração para Login no MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044227453)**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
