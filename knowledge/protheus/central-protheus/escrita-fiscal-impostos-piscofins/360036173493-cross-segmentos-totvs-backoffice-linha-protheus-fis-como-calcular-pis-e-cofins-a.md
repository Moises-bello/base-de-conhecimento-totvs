---
article_id: 360036173493
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 3c022c53540f3e14bd682d67394f01ea2199437925548e089d3e247c4cda2c6b
fetched_at: '2026-06-28T22:39:36.816366+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Como calcular PIS
  e COFINS alíquota zero?
type: support-article
updated_at: '2021-09-14T02:38:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036173493-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-PIS-e-COFINS-al%C3%ADquota-zero
---

**Dúvida**Como calcular PIS e COFINS Alíquota Zero?

**Ambiente**  
Microsiga Protheus – Livros fiscais – A partir da versão 11.80  
  
**Solução**

Para o sistema considerar o cálculo de PIS/COFINS alíquota zero, observar a seguinte configuração para alíquota zero 04,06 -Saída ou 73 - Entrada

TES

Aba Impostos

Livro ICMS ou ISS = diferentes de Não -> Deve ser configurado campo de um dos livro com opção diferente de não para geração dos valore de PIS COFINS nas tabelas SF3 e SFT

PIS/COFINS = Ambos  
Cred. Pis/Cof = Calcula

ABA Outros  
Sit Trib Pis = 04,06 ou 73  
Sit Trib Cof = 04,06 ou 73

Após a correta configuração, caso o sistema não considere a alíquota zero para PIS/COFINS, observe o preenchimento dos parâmetros MV\_APURCOF e MV\_APURPIS. Quando o preenchimento estiver como True(.T.) sempre serão consideradas as alíquotas dos parâmetros MV\_TXPIS e MV\_TXCOFIN.

**Importante**

Para notas de entrada deve ser preenchido o campo F4\_CODBCC = ? Para preenchimento do campo FT\_CODBCC referente a operação da CFOP.

Existe uma tabela disponibilizada pela Receita referente a base de credito dos registros M105/M505 - determinada pela CFOP informado no documento fiscal.

O código é gravado no campo FT\_CODBCC esse campo é alimentado pela TES campo F4\_CODBCC.

Se o código informado não for o coreto para CFOP correta a se utilizada a composição dos valores do registros M105 e M505 será gerado de forma incorreta.

Link  da Tabela CFOP - Operações Geradoras de Créditos

<http://sped.rfb.gov.br/arquivo/show/1681>

Nome do arquivo: Tabela\_CFOPOperacoesGeradorasCreditos.xls

Será a presentado o Grupo de código da base de credito e CFOP relacionadas.
