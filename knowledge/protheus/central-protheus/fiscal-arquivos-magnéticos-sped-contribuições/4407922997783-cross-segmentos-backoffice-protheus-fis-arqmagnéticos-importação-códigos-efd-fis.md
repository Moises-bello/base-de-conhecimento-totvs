---
article_id: 4407922997783
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 681057bb2373ec9f1a230500dc8c9f2c84da694b146b79538891cd3b175b75c0
fetched_at: '2026-06-28T22:42:06.679290+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Importação Códigos
  EFD (FISA001) - EFD Contribuições - Código da Receita automático para Apuração e
  campo 03 dos Registros M205/M605
type: support-article
updated_at: '2025-02-21T18:16:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407922997783-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Importa%C3%A7%C3%A3o-C%C3%B3digos-EFD-FISA001-EFD-Contribui%C3%A7%C3%B5es-C%C3%B3digo-da-Receita-autom%C3%A1tico-para-Apura%C3%A7%C3%A3o-e-campo-03-dos-Registros-M205-M605
---

**Dúvida**Como preencher automaticamente **Código da Receita** do PIS e COFINS na Apuração **(FISA001**) e campo **03** (**COD\_REC**) dos Registros **M205** e **M605**  
  
**Ambiente**TOTVS Backoffice (**Linha Protheus**) - A partir da versão **12.1.25**  
  
**Solução** **Passo 1** - Realize os cadastros na rotina **Importação** **Códigos** **EFD** para preenchimento automático dos **Códigos da Receita de PIS/COFINS na** **Apuração (FISA001) e campo 03 (COD\_REC) dos Registros M205/M605 no Arquivo EFD Contribuições (FISA008)**  
Caminho: **Módulo Livros Fiscais 09** > **Miscelenea** >  **Apuracoes** > **Apuração** **Efd** **Contribuições** > Rotina: **Importação** **Códigos** **EFD** > **Selecione** **tabela** **dos** **codigos** ? = **5-Cod.Receita**

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407922994455)

**Passo 2** - Cadastro: **+ Incluir**:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407922593431)

**Exemplo:**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407919180823)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407919141911)

**Passo 3** - Processar Apuração do EFD Contribuições (**FISA001**), meu Exemplo no Regime = **Não Cumulativo.**

**Passo 4** - Confira o Código da Receita gerado na Apuração (*Print* abaixo de exemplo, referente cadastro na rotina **Importação Códigos EFD**):

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407922724503)

**Passo 5** - Geração do **Arquivo da EFD Contribuições** (**FISA008**)

**Passo 6** - Confira o **campo 03 COD\_REC** dos **Registros M205 / M605**:

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4407922821143)

**Observação e Atenção:**

O sistema verifica Primeiro o Processo da Rotina: **Importação Códigos EFD**, caso esteja em branco o cadastro, verificar como está o Parâmetro **MV\_CDRCEC**, caso a Rotina de **Importação Códigos EFD** e **MV\_CDRCEC**, estejam sem preenchimento/cadastro, verificar o Código da Receita na Apuração (**FISA001**), onde deverá ser preenchido manualmente para correta geração dos Registros **M205/M605 campo 03**.

Documentação parâmetro **MV\_CDRCEC**:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=238029762>

Documentação **Importação Códigos EFD**:  
<https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407922997783-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Importa%C3%A7%C3%A3o-C%C3%B3digos-EFD-FISA001-EFD-Contribui%C3%A7%C3%B5es-C%C3%B3digo-da-Receita-autom%C3%A1tico-para-Apura%C3%A7%C3%A3o-e-campo-03-dos-Registros-M205-M605?source=search>

O **código da Natureza** a ser gravada nos **Títulos da Apuração**, poderão ser informados nos parâmetros: **MV\_PISAPC** - Informe a natureza a ser considerada para o título do **PIS** no regime **Cumulativo**. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro **MV\_PISNAT**.  
**MV\_PISAPNC** - Informe a natureza a ser considerada para o título do **PIS** no regime **Não Cumulativo**. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro **MV\_PISNAT**.    
**MV\_COFAPC** - Informe a natureza a ser considerada para o título da **COFINS** no regime **Cumulativo**. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro **MV\_COFINS**.   
**MV\_COFAPNC** - Informe a natureza a ser considerada para o título da **COFINS** no regime **Não Cumulativo**. Se o parâmetro estiver em branco, é considerado o conteúdo do parâmetro **MV\_COFINS**Documentação Completa para correta Geração da **Apuração do EFD Contribuições** (**FISA001**) e para correta **Geração do Arquivo EFD Contribuições** (**FISA008**):

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/9995225390743-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Boletim-t%C3%A9cnico-Apura%C3%A7%C3%A3o-e-gera%C3%A7%C3%A3o-arquivo-txt-EFD-Contribui%C3%A7%C3%B5es?source=search>
