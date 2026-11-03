---
article_id: 4408870498199
category: Materiais - Compras (SIGACOM)
content_hash: 7b89f69c1d8b3d389c46169b5747d9276b6fcf9d08e549eea310d7f926964035
fetched_at: '2026-06-28T22:41:17.393250+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Documento de entrada
  integrando com o ativo, help : SN1MASTER N1_CBASE JAGRAVADO Já existe registro com
  esta informação. Troque a chave principal deste registro.'
type: support-article
updated_at: '2023-07-26T13:57:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408870498199-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Documento-de-entrada-integrando-com-o-ativo-help-SN1MASTER-N1-CBASE-JAGRAVADO-J%C3%A1-existe-registro-com-esta-informa%C3%A7%C3%A3o-Troque-a-chave-principal-deste-registro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16304246863255) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida :**

Ao efetuar a inclusão de um documento de entrada com integração com o módulo do ativo fixo, o sistema emite o help :

**SN1MASTER**  
**N1\_CBASE**  
**JAGRAVADO**  
**Já existe registro com esta informação.**  
**Troque a chave principal deste registro.**

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**Para a identificação do por quê o sistema está emitindo esse help, deve-se verificar duas situações :

1-) O conteúdo do parâmetro ***MV\_CBASEAF.***

Este parâmetro define o próximo código base do ativo imobilizado a ser incluído automaticamente na nota fiscal de entrada (conteúdo padrão "NFE0000001"), pois é através dele que o sistema grava o ***campo N1\_CBASE,** o qual deve ser ajustado para um próximo número da sequencia não existente nas  tabelas do Ativo Fixo*

**[MV\_CBASEAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360008310232-MP-SIGAATF-ATFA240-Pr%C3%B3ximo-c%C3%B3digo-base-do-Ativo-Imobilizado-a-ser-inclu%C3%ADdo-automaticamente-pelo-documento-de-entrada-MV-CBASEAF)**  
  
2-) Consulte no ***campo N1\_ITEM*** se há ***X3\_RELACAO*** com inicializador padrão preenchido (inicializador padrão) com "0001" .  
Caso positivo limpe o conteúdo do X3\_RELACAO e realize novo teste em ambiente de HOMOLOGAÇÃO.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
