---
article_id: 4407080924439
category: Financeiro - Viagens
content_hash: b6992065c2b4f680e961c8b912cf9af22f1c8f9fe4b8419f879dcf9d59cf8f1b
fetched_at: '2026-06-28T22:38:21.443718+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA677 - HELP: RECNO
  - Aprovação da Prestação de Contas'
type: support-article
updated_at: '2024-07-31T17:18:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407080924439-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA677-HELP-RECNO-Aprova%C3%A7%C3%A3o-da-Presta%C3%A7%C3%A3o-de-Contas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24244431983639) Tempo aproximado para leitura: **00:04:00min****Ocorrência**No módulo Financeiro/Viagens, ao tentar realizar a aprovação da prestação de contas, é apresentado o "HELP: RECNO: Não existem registros no arquivo em pauta" e não localiza a viagem mesmo estando dentro do período informado.

![aprovador.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4407083637655)  
**Ambiente**Cross Segmento - BackOffice Linha Protheus – Financeiro – FINA677 - A partir da versão 12.1.23  
  
**Causa**Esse incidente ocorre, pois o usuário logado no Protheus e informado para aprovação, não é o aprovador do solicitante ou não está cadastrado como aprovador na rotina **APDA020 - Cadastro de Participantes**  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
Acessar a rotina **APDA020**, acessar o cadastro do solicitante e na aba **Viagens**, verificar o código do aprovador (**RD0\_APROPC**) e aprovador substituto (**RD0\_APSUBS**), caso esteja em branco, preencha o campo com o **código do usuário**.

![APDA020_APROVADOR.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407083688343)

Acessar a **FINA677**, no momento da aprovação, informar o **código do aprovador**.

![fina677.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4407080606871)

**Importante**  
Somente o **aprovador** e **aprovador substituto** logado no Protheus podem aprovar a **Prestação de Contas e liberação para o financeiro**

Para aprovação com o **Aprovador Substituto**, deve informar o **código do aprovador** padrão da **solicitação no grid de viagens**.

![KCS1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419617390359)

**Importante**  
A rotina valida a tabela **FLN** para o campo **FLN\_APROV** o código de participante que estiver neste campo para a **Prestação de Contas, será o Aprovador da Viagem**.

**Saiba mais:**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - APDA020- Substituto para aprovação de viagens](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025782133-MP-SIGAFIN-APDA020-Substituto-para-aprova%C3%A7%C3%A3o-de-viagens-?source=search)
