---
article_id: 4417338976535
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 428c72ead97f0b46e2dc4a5fd98688c4f6a3d59da2fb810d53fc2fd77db83e9d
fetched_at: '2026-06-28T22:42:10.755721+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DIME SC - Registro
  25 - Somatório de itens do quadro não confere com o valor Informado
type: support-article
updated_at: '2022-08-17T19:35:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417338976535-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DIME-SC-Registro-25-Somat%C3%B3rio-de-itens-do-quadro-n%C3%A3o-confere-com-o-valor-Informado
---

**Dúvida**

**Registro 25**- Somatório de itens do quadro não confere com o valor Informado

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417338200215/mceclip0.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Livros Fiscais - a partir de **12.1.27**

**Solução** **Registro tipo 25 – Resumo da apuração dos débitos**

Tem como base as informações contidas na apuração do ICMS do período.  
  
Para geração dos itens abaixo , deverá ser adicionado manualmente na **Apuração do ICMS** (**MATA953**) os códigos abaixo relacionados de cada item do Quadro 04 :

| Código Apuração | Item | Descrição |
| --- | --- | --- |
| 25020 | 020 | Debito por diferencial de alíquota do ativo permanente |
| 25030 | 030 | Debito por diferencial de alíquota do material de uso e consumo |
| 25040 | 040 | Débitos de maquinas/equipamentos importados para ativo permanente |
| 25045 | 045 | Débito da Diferença de Alíquota de Operação ou Prestação a Consumidor Final de Outro Estado - EC87 |
| 25060 | 060 | Outros estornos |
| 25065 | 065 | Estorno de Crédito da Entrada em Decorrência da Utilização de Crédito Presumido |
| 25070 | 070 | Outros Débitos |

O item 045 deste quadro deve obrigatoriamente possuir o mesmo valor do item 130 do quadro 13 - Registro 34.  
Em caso de divergências de valores , verifique na apuração DIFAL se foi efetuado a devida dedução do débito.

**Importante**:

É preciso informar o código de Subitem na **Apuração do ICMS** para ser considerado na **DIME** e não ocorrer o erro no **Registro 25**.

**Informações adicionais:**

**Declaração de ICMS e do Movimento Econômico do Estado de Santa Catarina**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=655881026#SCDIME-Declara%C3%A7%C3%A3odeICMSedoMovimentoEcon%C3%B4micodoEstadodeSantaCatarina-RegistroTipo20-Dadosdocontabilistarespons%C3%A1vel>
