---
article_id: 15767921235479
category: RH - Rescisão
content_hash: 19cc0f4e8451e298f2f4b2006fe56e40de4180e938e3fbd34a59ca6a9641d8bd
fetched_at: '2026-06-28T22:43:51.920601+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Cálculo de rescisão apresenta somente uma verba
  e ao confirmar o cálculo é gerado aviso: Atenção O tamanho dos campos RR_HORAS,
  RC_HORAS, RD_HORAS e RGB_HORAS está divergente e deveriam ser iguais.'
type: support-article
updated_at: '2023-07-04T12:51:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15767921235479-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-somente-uma-verba-e-ao-confirmar-o-c%C3%A1lculo-%C3%A9-gerado-aviso-Aten%C3%A7%C3%A3o-O-tamanho-dos-campos-RR-HORAS-RC-HORAS-RD-HORAS-e-RGB-HORAS-est%C3%A1-divergente-e-deveriam-ser-iguais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15767893851031) Tempo aproximado para leitura: **HH:MM:SS min****Dúvida**Por que cálculo de rescisão apresenta somente uma verba e ao confirmar o cálculo é gerado aviso: O tamanho dos campos RR\_HORAS, RC\_HORAS, RD\_HORAS e RGB\_HORAS está divergente e deveriam ser iguais?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/15767394253079)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**

O problema ocorre pois o tamanho do campo Horas entre as tabelas SRR, SRC, SRD e RGB estão diferentes.  
É necessário ajustar o tamanho do campo Horas entre as tabelas mencionadas.

Após validação e correção do tamanho do campo Horas, o cálculo da rescisão apresentará todas a verbas

**SRR - Campo RR\_HORAS**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15767549692567)**

**SRC - Campo RC\_HORAS**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15767583272087)**

**SRD - Campo RD\_HORAS**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15767606877207)**

**RGB - Campo RGB\_HORAS**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15767639084183)**

**Após editar os campos, clique no disquete (atualizar banco de dados), assim as edições serão salvas.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/15767643588887)**

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo

[MP - GPE - Cálculo de rescisão apresenta somente uma verba e ao confirmar o cálculo é gerado aviso: FWNOWIDTH Valor atribuído difere do campo (C. de Custo)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005380601-MP-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-somente-uma-verba-e-ao-confirmar-o-c%C3%A1lculo-%C3%A9-gerado-aviso-FWNOWIDTH-Valor-atribu%C3%ADdo-difere-do-campo-C-de-Custo-?source=search)  
   
[RH - Linha Protheus - GPE - Cálculo de rescisão apresenta somente uma verba e ao confirmar o cálculo é gerado aviso: FWNOLIST Valor atribuído difere da lista de valores válidos (Tipo)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6674466519319-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-rescis%C3%A3o-apresenta-somente-uma-verba-e-ao-confirmar-o-c%C3%A1lculo-%C3%A9-gerado-aviso-FWNOLIST-Valor-atribu%C3%ADdo-difere-da-lista-de-valores-v%C3%A1lidos-Tipo-?source=search)
