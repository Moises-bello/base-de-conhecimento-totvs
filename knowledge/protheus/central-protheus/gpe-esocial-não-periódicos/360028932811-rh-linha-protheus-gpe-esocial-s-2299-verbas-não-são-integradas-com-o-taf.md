---
article_id: 360028932811
category: GPE - eSocial - Não Periódicos
content_hash: a3a78d9a52d4d058f69870d60fa05059442674a78b39fb202a20070baf2b4cf1
fetched_at: '2026-06-28T22:45:05.891935+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2299 - Verbas não são integradas com
  o TAF
type: support-article
updated_at: '2026-06-15T18:48:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028932811-RH-Linha-Protheus-GPE-eSocial-S-2299-Verbas-n%C3%A3o-s%C3%A3o-integradas-com-o-TAF
---

**Ocorrência**  
S-2299 - Verbas não enviadas no evento, devido erro de estrutura das tabelas. O evento S-2299 é enviado ao TAF com identificador do pagamento, informações de lotação tributária, mas sem Verbas/Rubricas.   
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
O erro ocorre devido divergência do tamanho dos campos nas tabelas envolvidas, em alguns casos está com tamanho igual no dicionário, mas no banco de dados está divergente.  
Verifique no dicionário (SX3) o tamanho dos campos das tabelas envolvidas no processo e se o tamanho dessas tabelas no Banco de Dados estão idênticos.  
Um exemplo que verificamos no suporte é que ao consultar o dicionário (SX3) os campos RR\_CC, RD\_CC e CTT\_CUSTO estão todos com o mesmo tamanho de acordo com o definido no Grupo de campos (X3\_GRPSXG = 004).  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029692351)  
  
Mas ao consultar a Estrutura da tabela no Banco de Dados verificamos que uma das tabelas está com um campo de tamanho diferente ao do definido na SX3.  
  
\*Print do RD\_CC com tamanho diferente da SX3.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029693171)​  
  
\*Print do RR\_CC com tamanho igual ao da SX3.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029704012)​​  
  
O tamanho só estará diferente se a alteração não foi realizada via configurador, ou seja, o grupo de campos não é ajustado automaticamente.   
  
**Solução**  
**Orientação para analista Totvs.**  
O tamanho de campo deverá ser o mesmo no dicionário (SX3) e no banco de dados.  
  
Observação: Os ajustes no tamanho dos campos deverão ser realizados sempre via SIGACFG (configurador) e quando houver mais de uma tabela envolvida para o mesmo campo, realizar a alteração pelo grupo de campos.   
  
Em caso de dúvidas para realizar os ajustes em seu ambiente, consulte o seu Gerente de Contas para solicitar um analista "*in loco*".  
  
**Saiba Mais**  
Para saber mais consulte os links abaixo:   
[S-2299 - Ao calcular uma rescisão o sistema envia os dados para o TAF no evento S-2299 porem as verbas (rubricas) do calculo não são geradas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018741171)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)
