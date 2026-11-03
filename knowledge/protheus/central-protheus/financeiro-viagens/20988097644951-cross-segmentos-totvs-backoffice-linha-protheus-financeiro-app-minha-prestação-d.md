---
article_id: 20988097644951
category: Financeiro - Viagens
content_hash: 9e14a4d5fbf19b99ec3ffa2a7db4a5b62885005f6da11db7b74c815cff6b407e
fetched_at: '2026-06-28T22:38:21.525807+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos TOTVS BackOffice (Linha Protheus) - Financeiro - App Minha
  Prestação de Contas - O usuário não está configurado como Participante
type: support-article
updated_at: '2024-06-19T17:30:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20988097644951-Cross-Segmentos-TOTVS-BackOffice-Linha-Protheus-Financeiro-App-Minha-Presta%C3%A7%C3%A3o-de-Contas-O-usu%C3%A1rio-n%C3%A3o-est%C3%A1-configurado-como-Participante
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20988068643607) Tempo aproximado para leitura: **00:10:00 min****Ocorrência**No Aplicativo de **Viagens-Minha Prestação de Contas**, ao tentar realizar login na aplicação, ocorre a mensagem***” O usuário não está configurado como Participante”***  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20988097621271)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o usuário não está cadastrado na rotina **APDA020 - Cadastro de Participantes** ou no próprio cadastro de participantes, o campo **RD0\_USER**não está preenchido com o código de usuário Protheus **(Configurador)**  
  
**Solução**Acessar a rotina **APDA020 - Cadastro de Participantes**, criar o usuário e adicionar   
1 - **Usuário não cadastrado** - Criar o usuário como "Interno" e cadastrar o código de usuário do Protheus **RD0\_USER**

2 - **Usuário já cadastrado** - Informar o código do usuário Protheus, no campo **RD0\_USER**![](https://centraldeatendimento.totvs.com/hc/article_attachments/20988833757463)

Na aba "Viagens" o campo Permite viagem deve estar igual a "SIM"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24293370457367)

**Saiba mais**

[Viagens - Financeiro - P12](https://tdn.totvs.com/display/PROT/Viagens+-+Financeiro+-+P12)  
[Guia de uso - Minha Prestação de Contas](https://tdn.totvs.com/pages/viewpage.action?pageId=287057777)
