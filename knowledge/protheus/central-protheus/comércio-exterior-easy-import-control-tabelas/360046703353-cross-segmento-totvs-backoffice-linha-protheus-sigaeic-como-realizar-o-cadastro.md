---
article_id: 360046703353
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: f6aaa38e16566677da6ba699e9863c70111194df74264e2f1afda1739a521ba6
fetched_at: '2026-06-28T22:39:47.740605+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Como realizar
  o cadastro ou a atualização das alíquotas vinculadas à NCM (Nomenclatura Comum do
  Mercosul)?
type: support-article
updated_at: '2026-01-02T17:52:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046703353-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Como-realizar-o-cadastro-ou-a-atualiza%C3%A7%C3%A3o-das-al%C3%ADquotas-vinculadas-%C3%A0-NCM-Nomenclatura-Comum-do-Mercosul
---

**Dúvida**  
Como realizar o cadastro ou a atualização das alíquotas vinculadas à NCM (Nomenclatura Comum do Mercosul)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – A partir da versão 12.1.2210.

**Solução**  
A manutenção das alíquotas da NCM é vital para a precisão do cálculo de impostos na importação e apuração de custos. Devido à Reforma Tributária, a estrutura de alíquotas foi atualizada para comportar os novos tributos.

**Importante:** **Devido à Reforma Tributária, a estrutura de alíquotas foi atualizada para comportar os novos tributos.**

**Existem duas formas principais de realizar essa atualização: manualmente ou via integração automática.**

**1ª Para cadastrar ou atualizar as alíquotas, realize o seguinte procedimento manualmente**  
Para realizar o cadastro ou a alteração manual das alíquotas por **N.C.M.**, siga os procedimentos descritos a seguir:

1. Acesse o módulo de importação (SIGAEIC).
2. Navegue até Atualizações -> Tabelas -> N.C.M. (**Rotina EICA130**).
3. Posicione-se sobre o código da **N.C.M.** desejada e clique em Alterar.
4. Selecione a aba Alíquotas e, no campo Alíquota, informe o percentual correspondente.
5. Clique em Confirmar para salvar as modificações.

![0b7fb2cf-523b-4a0d-9dcf-291b08cdf6ac.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/37400648286743)

**A. Novos Campos - Reforma Tributária**   
A partir da expedição de novembro de 2025, foram criados agrupadores específicos para os novos tributos:

* **Agrupador CBS (Contribuição sobre Bens e Serviços)**
  + **% CBS (YD\_ALADCBS)**: Informe a alíquota *ad valorem* da Contribuição sobre Bens e Serviços.
  + **Redução CBS (YD\_ALRDCBS)**: Informe o percentual de redução da alíquota *ad valorem* da CBS.
  + **Red.Base CBS (YD\_ALRBCBS)**: Informe o percentual de redução da base de cálculo da CBS.
* **Agrupador IBS (Imposto sobre Bens e Serviços)**
  + **% IBS (YD\_ALADIBS)**: Informe a alíquota *ad valorem* do Imposto sobre Bens e Serviços.
  + **Redução IBS (YD\_ALRDIBS)**: Informe o percentual de redução da alíquota *ad valorem* do IBS.
  + **Red.Base IBS (YD\_ALRBIBS)**: Informe o percentual de redução da base de cálculo do IBS.

**B. Outros Tributos (Legado)**

* **Agrupador Outros Tributos**: Utilize este agrupador para informar as alíquotas dos tributos já existentes (II, IPI, PIS, COFINS, entre outros).

1. Após preencher as alíquotas, clique em **Confirmar** para salvar as alterações.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37151839475095)

**2ª Atualização Automática (TOTVS Comex Conteúdo)**  
O **TOTVS Comex Conteúdo** permite a atualização automática de alíquotas oficiais e exceções (II, IPI, PIS e COFINS), incluindo percentuais de majoração, mediante assinatura do serviço. 

1. Na rotina **N.C.M (EICA130)**, clique em **Outras Ações** > **Totvs Comex Conteúdo** > **Totvs Comex Conteúdo – NCM**.
2. Selecione se deseja atualizar a NCM posicionada ou **Várias NCMs**.
3. Defina os parâmetros (NCM Inicial e Final) e confirme.
4. O sistema integrará com a base de dados (**Fiscosoft**) e exibirá um log das atualizações realizadas.

**Saiba mais:**  
[**NCM (EICA130)**](https://tdn.totvs.com/pages/releaseview.action?pageId=878904533)
