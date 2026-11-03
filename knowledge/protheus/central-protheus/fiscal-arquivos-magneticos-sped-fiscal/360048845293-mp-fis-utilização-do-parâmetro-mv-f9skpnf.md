---
article_id: 360048845293
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 5742bfb2366fe84902ab741e2cc4f0ad41d48b1ee93ecb47bdec6e24081e0a2f
fetched_at: '2026-06-28T22:42:03.849527+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Utilização do Parâmetro MV_F9SKPNF
type: support-article
updated_at: '2021-04-28T14:25:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048845293-MP-FIS-Utiliza%C3%A7%C3%A3o-do-Par%C3%A2metro-MV-F9SKPNF
---

**Dúvida**  
Utilização do parâmetro MV\_F9SKPNF.

**Ambiente**  
Protheus - Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
MV\_F9SKPNF:

Tratamento para o bloco G do SPED Fiscal que indica se o Sistema irá considerar as informações da tabela SF9.

Campo F9\_VALICMS e campos informados nos parâmetros: MV\_F9CC, MV\_F9PL, MV\_F9FRT, MV\_F9ICMST e MV\_F9DIF.

**Importante**

Indica se o sistema desconsidera as informações das Notas Fiscais e da integração com o módulo **Ativo Fixo (SIGAATF)** e busca da tabela **Manutenção CIAP (SF9)** todas as informações para gerar os registros do Bloco G.

Se preenchido como **.T.**(*True/*Verdadeiro), busca da tabela **Manutenção CIAP (SF9).** Caso contrário, segue o fluxo normal, podendo utilizar as tabelas **Ativo Mobilizado (SN1), Saldos e Valores (SN3)** ou **Itens da Nota Fiscal de Entrada (SD1).**

Para inclusão manual realizada no rotina **Manutenção do CIAP - MATA905**, o campo Valor do ICMS Próprio **F9\_VALICMP** só é habilitado para inclusão quando o parâmetro **MV\_F9SKPNF = .T.**

Link contendo informações referente CIAP no SPED FISCAL:

<https://tdn.totvs.com/display/public/PROT/FIS0005_SPED_FISCAL>
