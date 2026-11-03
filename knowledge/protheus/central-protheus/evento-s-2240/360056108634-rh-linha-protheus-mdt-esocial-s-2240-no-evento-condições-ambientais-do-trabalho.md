---
article_id: 360056108634
category: Evento S-2240
content_hash: 642cdc0e539d0053c1441b4ee5ddcbd242938cb3e66a54039de3b9d8b25e8d14
fetched_at: '2026-06-28T22:45:23.476727+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2240 - No evento Condições Ambientais
  do Trabalho (S-2240) de onde são geradas informações do grupo de tags agNoc '
type: support-article
updated_at: '2022-11-08T17:03:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056108634-RH-Linha-Protheus-MDT-eSocial-S-2240-No-evento-Condi%C3%A7%C3%B5es-Ambientais-do-Trabalho-S-2240-de-onde-s%C3%A3o-geradas-informa%C3%A7%C3%B5es-do-grupo-de-tags-agNoc
---

**Dúvida**  
No evento Condições Ambientais do Trabalho (**S-2240**) de onde são geradas informações do grupo de tags *agNoc*(**agentes nocivos**)?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**  
O grupo de tag *agNoc*(agentes nocivos) do evento **S-2240** é formando pela informações do cadastro de risco, agentes e ambientes físico que estão no modulo medicina e segurança do trabalho (SIGAMDT).

1. No cadastro de Agentes no caminho: atualizações > PPRA > Agentes, nessa rotina é necessário o preenchimento dos campos **Descrição** (TMA\_DESCRI) tag *dscAgNoc*, **Cod. eSocial** (TMA\_ESOC) tag *codAgNoc* , **Avaliação** (TMA\_AVALIA) tag *tpAval*; **Limite de Tolerancia** (TLK\_DEQTDE) tag *limTol.*
2. Na rotina ambiente físico no caminho: atualizações > PPRA > Ambiente Físico, é necessário vincular com a entidade escolhida pela empresa conforme parâmetro **MV\_NG2EAMB** para maiores informações consulte [Novas Entidades de Relacionamento ao Ambiente Físico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409384342679-RH-Linha-Protheus-MDT-eSocial-S-2240-Novas-Entidades-de-Relacionamento-ao-Ambiente-F%C3%ADsico)
3. Os demais campos ficam disponíveis dentro do cadastro de risco no caminho: atualizações > PPRA > Riscos. Nessa rotina os campos utilizados para gerar informações no grupo de tags *agNoc*são: **Quantidade Agente** (TN0\_QTAGEN) tag ***intConc***, **Unidade de Medica** (TN0\_UNIMED) tag *unMed*, **Tec. Utiliz.** (TN0\_TECUTI) tag *tecMedicao***.**

**Observação**

* As informações acima são apenas para o grupo de tags *agNoc*gerado no S-2240, esse evento contém muitos outros grupos de tags. Para saber a origem de todas as informações do evento completo consulte o link: **[S-2240 De / Para de campos Protheus com layout eSocial](https://tdn.totvs.com/x/zUqlGw)**
* Após a geração do evento S-2240 é possível ver as informações do grupo de tags *agNoc* no modulo SIGATAF no caminho: atualizações > eventos eSocial > não periódicos > Cond. Amb. Trabalho, acesse o trabalhador e veja o conteúdo na aba Fator de Risco.  
    
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414757030423/mceclip0.png)

**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Ajuste no Envio da Informação da CAT Origem](https://tdn.totvs.com/pages/releaseview.action?pageId=632829426)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
