---
article_id: 26950994778263
category: Financeiro - Viagens
content_hash: 1a9d9988ae11a4703fbadb08f7d4cd21a6a9cb3ec27abc0ef1f908a7567924c2
fetched_at: '2026-06-28T22:38:21.409210+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA666 - Viajante
  não aparece na opção de Participante para criação de viagens
type: support-article
updated_at: '2024-10-09T18:17:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26950994778263-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA666-Viajante-n%C3%A3o-aparece-na-op%C3%A7%C3%A3o-de-Participante-para-cria%C3%A7%C3%A3o-de-viagens
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26950994751383) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**No módulo Financeiro, ao tentar realizar uma solicitação de viagens para um participante, o código de participante não aparece para selecionar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26950994752535)  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Esse incidente ocorre, pois para atender legislações de LGPD, foi efetuado uma trava para somente apresentar o participante na lupa de "**Participante**", o aprovador e aprovador substituto do mesmo cadastrado na rotina **APDA020 - Cadastro de Pessoas** e assim impedir outros colaboradores de ter acesso a dados como CPF e outras informações pessoais dos viajantes

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26950978234775)  
  
  
**Solução**Solicitar ao **Aprovador** ou **Aprovador Substituto** que solicite a viagem para seu viajante através da rotina **FINA666**, ou alterar o **Cadastro do aprovador substituto** para o **código de participante** responsável pelas **Solicitações de Viagens**   
  
**Saiba mais**  
**[20644514 DSFIN-9862 DT FINA666 - Solicitação de viagem permitindo visualizar dados de outro viajante](https://tdn.totvs.com/pages/releaseview.action?pageId=856921329)**  
**[Viagens - Financeiro - P12](https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12)**
