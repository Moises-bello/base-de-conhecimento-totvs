---
article_id: 19150590379799
category: RH - Folha de Pagamento
content_hash: a92f2be09b3f0cfb621e97e5b48dfd6d7b08393dda2fa395509618301f710fab
fetched_at: '2026-06-28T22:44:13.559797+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como informar verbas a serem deduzidas na base
  de cálculo de Imposto de Renda no modo simplificado
type: support-article
updated_at: '2025-04-15T13:36:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19150590379799-RH-Linha-Protheus-GPE-Como-informar-verbas-a-serem-deduzidas-na-base-de-c%C3%A1lculo-de-Imposto-de-Renda-no-modo-simplificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19150618573335) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Cálculo de IRRF com a utilização do mnemônico **P\_DEDIRSIM**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**Não existe diferença na **incidência** de verbas no modelo de tributação **completo** e no modelo de tributação **simplificado.** Isto é, caso alguma verba de provento ou desconto esteja configurada com incidência para **IR,** seu valor será **considerado** na **base** de cálculo para apuração do **IR** tanto no modelo de tributação completo quanto no modelo de tributação simplificado; não há possibilidade de uma verba ser considerada em um modelo de tributação e no outro não.

A **diferença** entre os dois modelos de tributação é que a **dedução simplificada** mensal no modelo de tributação simplificado **substitui** a dedução dos valores de **INSS** (IDs 0064/0065/0070 ou 0167/0168/0169), **pensão alimentícia** (conforme configuração da tabela SRQ (Beneficiários), dependente (IDs 0059/0060/0062) e **previdência privada** (IDs 0215/0216/0302, ou sem ID, mas vinculada na tabela auxiliar S073 nos campos **Prev. Privada** ou **13o-Prev. Privada** e com **vínculo** com o **fornecedor** na tabela **SMU** (Prev. Compl Funcionário) feito através da rotina **GPEA551).**

Entretanto, a MP **não** citou se houve **alteração** na forma de cálculo da **pensão alimentícia.** Sabemos que o cálculo da pensão alimentícia precisa **deduzir** o **IR** em sua **base** de cálculo, enquanto que o **IR** precisa **deduzir** a **pensão** em sua base de cálculo. Nessa situação, há a hipótese de o cálculo da pensão ter considerado o IR no modelo de tributação completo, enquanto que no cálculo haja o desconto efetivo do IR no modelo de tributação simplificado.

Devido a isso, foi efetuado a criação do mnemônico **P\_DEDIRSIM**que permitirá interferir nas **verbas** que o modelo de tributação **simplificado substitui,** cancelando a substituição na dedução.

Por exemplo: se no cálculo foi gerado as verbas **416** e **514,** referente a **pensão alimentícia,** e haja algum entendimento que estas verbas também devam ser deduzidas na base de cálculo do IR do modelo de tributação **simplificado,** o mnemônico deverá ser preenchido com o conteúdo "416/514". 

Para configurar o mnemônico **P\_NDEDIRSI**, acesse **Atualizações > Definições de cálculos > Mnemônicos (GPEA300) >** **Pesquise pelo P\_DEDIRSIM > Clique em Alterar**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310857090711)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310881233175)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19150899402135)

**Obs.**: as verbas deverão estar separadas pelo caractere **/** (barra).  
  
**Observação**

O mnemônico **P\_DEDIRSIM**apenas permite interferir nas verbas citadas anteriormente, que são: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19150777382551)

Isto significa que **NÃO**é possível informar qualquer verba no mnemônico para cancelar sua dedução na base de IR do modelo de tributação simplificado; apenas as listadas acima serão consideradas.

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[16963963 DRHCALCPRT-8420 DT Cálculo do IRRF - MP 1.171/2023](https://tdn.totvs.com/pages/releaseview.action?pageId=756458638)
