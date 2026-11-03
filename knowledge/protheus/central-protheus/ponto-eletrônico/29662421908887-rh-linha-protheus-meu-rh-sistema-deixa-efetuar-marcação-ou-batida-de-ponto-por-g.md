---
article_id: 29662421908887
category: PONTO ELETRÔNICO
content_hash: 591c468109c4f8d6573f7352fb7ff8f814867d88cc2a39d205004f03e7dcca1b
fetched_at: '2026-06-28T22:44:36.465629+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - MEU RH - Sistema deixa efetuar marcação ou batida de
  ponto por geolocalização de funcionário em férias.
type: support-article
updated_at: '2026-06-24T12:22:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29662421908887-RH-Linha-Protheus-MEU-RH-Sistema-deixa-efetuar-marca%C3%A7%C3%A3o-ou-batida-de-ponto-por-geolocaliza%C3%A7%C3%A3o-de-funcion%C3%A1rio-em-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29662421886871) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Sistema deixa efetuar marcação ou batida de ponto por geolocalização de funcionário em férias.  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
Conforme as regras atualmente previstas nas **Portarias 373/2011 e 671/2022 do Ministério do Trabalho e Emprego (MTE)**, as marcações de ponto realizadas por **Geolocalização** não possuem bloqueio automático com base na situação funcional do colaborador, incluindo cenários de afastamento temporário, como período de gozo de férias.  
  
Dessa forma, caso um funcionário realize uma marcação por geolocalização enquanto estiver em férias, o registro será incluído normalmente pelo sistema, não havendo, no comportamento padrão da ferramenta, validações impeditivas para esse tipo de marcação no momento da captura.  
  
Isso ocorre porque a marcação via geolocalização segue a premissa de registrar o evento conforme a ação efetivamente realizada pelo usuário, preservando a rastreabilidade e a integridade do registro de ponto, sem aplicar bloqueios preventivos nesse fluxo específico.  
  
Por outro lado, essa validação existe em um cenário diferente: nas **marcações incluídas manualmente**. Nesses casos, o sistema realiza verificações adicionais para validar a situação do funcionário na data informada para a inclusão da batida, analisando se o colaborador se encontrava em condição apta para possuir registros de ponto naquela competência.  
  
Portanto, no comportamento atual do produto, somente as **inclusões manuais de marcação** passam por essa validação de status funcional, enquanto as marcações efetuadas diretamente por **geolocalização** não sofrem esse bloqueio, mesmo em períodos como férias.  
  
**Saiba Mais**  
[**CLIQUE AQUI para acessar a documentação completa sobre o assunto.**](https://tdn.totvs.com/pages/viewpage.action?pageId=334338837)
