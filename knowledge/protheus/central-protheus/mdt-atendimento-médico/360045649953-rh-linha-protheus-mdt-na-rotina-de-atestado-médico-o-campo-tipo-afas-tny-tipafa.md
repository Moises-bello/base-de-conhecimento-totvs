---
article_id: 360045649953
category: MDT - Atendimento Médico
content_hash: da4ad26d574e5ba7406cb56754e8edda7264c49d870d8497de3f52d46670d8ba
fetched_at: '2026-06-28T22:44:21.373059+00:00'
product: protheus
section_id: 360010945694
source: central-protheus
title: RH - Linha Protheus - MDT - Na rotina de Atestado Médico o campo Tipo Afas.
  (TNY_TIPAFA) não habilita
type: support-article
updated_at: '2025-09-02T17:15:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045649953-RH-Linha-Protheus-MDT-Na-rotina-de-Atestado-M%C3%A9dico-o-campo-Tipo-Afas-TNY-TIPAFA-n%C3%A3o-habilita
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20283541777047)**Tempo aproximado para leitura:**00:03:00 min****Ocorrência**Na rotina de Atestado Médico (MDTA685) o campo Tipo Afas. (**TNY\_TIPAFA**) não está habilitado  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**O campo está desabilitado porque não é mais utilizado no produto. Houve uma alteração conceitual que impactou o uso desse campo. Atualmente, ele permanece visível apenas por questões de legado, sem interferir na inclusão do atestado.  
  
Exemplo  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102137173)  
 **Solução**A funcionalidade do campo Tipo Afas. (**TNY\_TIPAFA**) foi substituída pelo campo Cód. Ausência (**TNY\_CODAFA**). Nesse campo informe o código correspondente a ausência gerada pelo Atestado Médico.  
  
Para localizar o campo ao cadastrar um atestado no módulo 35 – SIGAMDT, siga o caminho: **Atualizações > Atendimento Médico > Atestado Médico (MDTA685)**. Em seguida, clique na aba **Afastamento**, onde está localizado o campo **Cód. Ausência (TNY\_CODAFA)**.

![2020-12-28_15-50-18.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099953894)

**Saiba Mais**  
[MDT - Atendimento Médico](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945694-MDT-Atendimento-M%C3%A9dico?page=1#articles)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)[MP - MDT - Erro "O valor atribuído difere do tamanho do campo (Tipo Afasta.)" quando informado o código de ausência na rotina atestado medico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053622674)
