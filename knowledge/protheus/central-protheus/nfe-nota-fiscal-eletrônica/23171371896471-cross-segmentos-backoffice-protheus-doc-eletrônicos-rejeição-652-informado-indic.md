---
article_id: 23171371896471
category: NFe - Nota Fiscal Eletrônica
content_hash: 5d0e52f38306c3e97886c678a99dd4917ff160cae178d4d7b6c2f56484be1437
fetched_at: '2026-06-28T22:40:07.141397+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Rejeição 652: informado
  indicador de desoneração inválido para a ZFM [nItem:999]'
type: support-article
updated_at: '2025-06-09T19:00:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23171371896471-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Rejei%C3%A7%C3%A3o-652-informado-indicador-de-desonera%C3%A7%C3%A3o-inv%C3%A1lido-para-a-ZFM-nItem-999
---

**Dúvida**Como corrigir a Rejeição 652 : informado indicador de desoneração inválido para a ZFM [nItem:999]  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.33

Cross Segmentos - TSS - a partir da versão 12

**Solução**

A regra de validação da Sefaz **NT 2023.004**, diz o seguinte:

Se informado **motDesICMS** = 7 (desoneração Suframa): tag **indDeduzDeson** deve ser igual a 1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23243094152727)

A **Rejeição 652** pode ocorrer quando uma NF-e for emitida com o **motDesICMS** igual a 7 (desoneração Suframa) e não for informada a tag **indDeduzDeson** igual a 1.

![image-2024-4-17_17-1-19.png](https://tdn.totvs.com/download/attachments/832657483/image-2024-4-17_17-1-19.png?version=1&modificationDate=1713384079367&api=v2)

Documentação de apoio para configuração de nota de Suframa:

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Como configurar o sistema para calcular SUFRAMA?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-sistema-para-calcular-SUFRAMA?source=search)

**Além da configuração é necessário atualizar o Protheus e TSS.**

Atualizações Protheus (patch de acordo com sua versão do seu Protheus)

12.1.2310 [Clique aqui](https://suporte.totvs.com/portal/p/10098/download?e=1124963)

12.1.2410 [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1171486)

[RDMAKES](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)

**Atualizações necessárias para o TSS.**

Substituir o RPO do TSS pelo da documentação abaixo:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981-MP-TSS-Atualiza%C3%A7%C3%A3o-do-Reposit%C3%B3rio-RPO-do-TSS?source=search)

[TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-TSS-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS?source=search)

Caso seu TSS esteja em versões anteriores a 12.1.2310 será necessário migrar para versão mais recente.

[MP - TSS - Migração para 12.1.2310 - (Instalação)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038065954-MP-TSS-Migra%C3%A7%C3%A3o-para-12-1-2310-Instala%C3%A7%C3%A3o?source=search)

**Importante**

Para enviar a tag <indDeduzDeson>1</indDeduzDeson> quando o motDesICMS = 7 (desoneração Suframa), deve-se verificar as configurações na tabela Livro Fiscal por Item de NF:

FT\_AGREG <> D (Diferente de D);  
FT\_MOTICMS = 7;  
CD2\_DESCZF > 0 na linha do CD2\_IMP = ZFM.

Abaixo a relação dos CST(s) que podem ser enviados com a tag indDeduzDeson = 1:

ICMS20 – CST 20: Redução de base de cálculo;  
ICMS30 – CST 30: Isenta ou não tributada e com cobrança do ICMS por ST;  
ICMS40 – CST 40, 41, 50: Isenta, Não tributada ou Suspensão;  
ICMS70 – CST 70: Redução de base de cálculo e cobrança do ICMS por ST;  
ICMS90 – CST 90: Outros.

Observação: Para gerar a tag do ICMS - ST, os campos da tabela SB1  (B1\_PICMRET - Saída e B1\_PICMENT - Entrada) deverão ser preenchidos com o percentual calculado de ICMS Solidário ou Retido.

**ASSUNTOS RELACIONADOS**

**[Protheus - NF-e - Nota Técnica 2023.004](https://tdn.totvs.com/pages/releaseview.action?pageId=832657483)**

**[Configuração para Suframa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034294253-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-o-sistema-para-calcular-SUFRAMA)**

**[13 Tipos de configuração para nota de Suframa](https://tdn.totvs.com/pages/releaseview.action?pageId=605019302)**

Caso sua nota não esteja nas conformidades das configurações do Suframa devera entrar em contato com Suporte fiscal.
