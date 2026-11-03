---
article_id: 38572536838935
category: Financeiro - Viagens
content_hash: cb2b873109eafb21599498e9009bae9d6f3d4226d9e980b49292f686daa91f4d
fetched_at: '2026-06-28T22:38:21.283650+00:00'
product: protheus
section_id: 1500001539201
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA677 - Viagem não
  aparece para aprovação, o que fazer
type: support-article
updated_at: '2026-02-23T18:01:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38572536838935-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Viagem-n%C3%A3o-aparece-para-aprova%C3%A7%C3%A3o-o-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38572521723927) Tempo aproximado para leitura: **00:05 min**  
  
**Ocorrência**  
Viagens não são apresentadas para o aprovador vinculado a elas aprovar as mesmas.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões.  
  
**Causa**  
A causa mais provável para ambos os cenários é a **falta de vínculo correto** do usuário da analista nos cadastros dos participantes (viajantes) e/ou a parametrização do processo no **Assistente de Configuração (FINA691)**.

**Cenário 1:** O usuário da analista pode não ter sido adicionado no campo Cód. de Usuários de Dpto. de Viagens na rotina FINA691, ou o vínculo Aprovador Principal (RD0\_APROPC) no Cadastro de Pessoas (APDA020) não está correto para todos os participantes.

**Cenário 2:** O erro "Aprovador não autorizado" para o substituto acontece porque, para que o aprovador substituto consiga aprovar, é obrigatório que o seu código de usuário esteja preenchido no campo Substituto (RD0\_APSUBS) do Cadastro de Pessoas (APDA020) de cada participante (viajante) para o qual ela deve atuar  
  
**Solução**  
Realize os passos abaixo, por gentileza, após, verifique se o problema se manterá:  
Acesse a rotina Cadastro de Pessoas (APDA020) para cada participante cuja viagem deve ser aprovada pela sua analista.

* Acesse a Rotina: Cadastro de Pessoas (APDA020).
* Selecione o Participante: Busque e edite o cadastro de cada um dos viajantes.
* Aba Viagem: Navegue até a aba Viagem.
* Aprovador Principal: Preencha o campo Aprovador (RD0\_APROPC) com o código do aprovador principal (a gestora do departamento).
* Aprovador Substituto: Preencha o campo Substituto (RD0\_APSUBS) com o código do usuário da sua analista.

Importante: Após este procedimento, tanto o Aprovador Principal quanto o Substituto podem aprovar as solicitações de viagem do participante.  
   
Verifique se o usuário da analista está listado na configuração geral do módulo Viagens, o que pode influenciar a visibilidade das solicitações.

1. **Acesse a Rotina:** Assistente de Configuração (FINA691).
2. **Verifique a configuração:** na tela de **cadastros gerais**, verifique o campo **Cód. de Usuários de Dpto. de Viagens'** e inclua o código de usuário da analista do Protheus, caso ainda não esteja lá.

Em algumas versões do Protheus, ao aprovar como substituto na rotina **Solicitação de Viagem** (FINA666), o sistema pode exigir uma informação adicional:

* Ao tentar aprovar como Substituto, o sistema pode solicitar que o código do **Aprovador Padrão** (RD0\_APROPC) seja informado no *grid* de viagens. (Esta regra é mais comum na aprovação da Prestação de Contas, mas é válida para verificação na Solicitação de Viagem também).

**Saiba Mais**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA666 - HELP: VLDPARTIC - Usuário não é aprovador da solicitação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402820079767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA666-HELP-VLDPARTIC-Usu%C3%A1rio-n%C3%A3o-%C3%A9-aprovador-da-solicita%C3%A7%C3%A3o)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA677 - HELP: RECNO - Aprovação da Prestação de Contas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407080924439-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA677-HELP-RECNO-Aprova%C3%A7%C3%A3o-da-Presta%C3%A7%C3%A3o-de-Contas)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAFIN - FINA677 - Prestação não aparece para o aprovador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20836622273687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA677-Presta%C3%A7%C3%A3o-n%C3%A3o-aparece-para-o-aprovador)
