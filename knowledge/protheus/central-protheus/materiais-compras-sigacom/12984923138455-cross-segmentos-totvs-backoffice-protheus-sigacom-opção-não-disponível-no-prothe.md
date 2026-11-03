---
article_id: 12984923138455
category: Materiais - Compras (SIGACOM)
content_hash: 1daa6f50bd68ec0a664f4592143fecac67b8280f74df4b2e004cbbcaf021e7eb
fetched_at: '2026-06-28T22:41:22.036567+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Opção não disponível
  no Protheus Função COMPCTE Called by A103GRVATF
type: support-article
updated_at: '2023-03-09T21:50:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12984923138455-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-COMPCTE-Called-by-A103GRVATF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03****Ocorrência**

Ao realizar a exclusão de Documento de Entrada, o sistema está apresentando o erro a seguir : 

InterFunctionCall: cannot find function COMPCTE in AppMap on A103GRVATF(MATA103.PRW) 09/12/2022 16:01:14 line : 8115 

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS -Versão 12  
  
**Causa**

O error.log em questão ocorre devido a falta da função COMPCTE que esta contida no fonte ATFXINT  
  
**Solução**

Validar o pacote de atualização de arquivos fontes do Ativo Fixo que contém as correções acumuladas das issues abaixo com data de corte em  12/02/2023. Para efetuar o download;

12.1.33 <https://suporte.totvs.com/portal/p/10098/download#detail/1039601>

12.1.2210 <https://suporte.totvs.com/portal/p/10098/download#detail/1081156>

Saiba mais em :

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
