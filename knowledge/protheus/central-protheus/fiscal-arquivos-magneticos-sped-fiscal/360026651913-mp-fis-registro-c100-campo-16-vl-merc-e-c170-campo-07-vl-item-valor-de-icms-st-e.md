---
article_id: 360026651913
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 26084088a269637ae439f1b5749324f9029a2002da1b5b9260a3d5d3b2295249
fetched_at: '2026-06-28T22:42:03.809019+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: MP - FIS - Registro C100 Campo 16_VL_MERC e C170 CAMPO 07_VL_ITEM_Valor De
  ICMS-ST E IPI
type: support-article
updated_at: '2021-04-30T13:42:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026651913-MP-FIS-Registro-C100-Campo-16-VL-MERC-e-C170-CAMPO-07-VL-ITEM-Valor-De-ICMS-ST-E-IPI
---

**Dúvida**

Nos registros de entrada, os valores de ICMS/ST e IPI destacados nos documentos fiscais, quando o informante não tem direito ao crédito, devem ser incorporados ao valor das mercadorias?

**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
Resposta: Sim, nestes casos, os valores do ICMS/ST e/ou IPI destacados devem ser adicionados ao valor das mercadorias que é informado no campo 16 – VL\_MERC do registro C100, bem como no campo 07 – VL\_ITEM do registro C170, uma vez que compõem o custo das mercadorias.

Como o informante não tem direito à apropriação do crédito, os campos VL\_ICMS\_ST e/ou VL\_IPI dos registro C100, C170 e C190 não devem ser informados.

Atenção: Essa resposta foi publicada no guia pratico EFD ICMS /IPI na pagina 46

Link Guia Pratico EFD ICMS/IPI: <http://sped.rfb.gov.br/estatico/72/BBFB8C50E653125B3174BA1ECC91A1A8255EB7/GUIA%20PR%C3%81TICO%20DA%20EFD%20-%20Vers%C3%A3o%202.0.18.pdf>

Quando o ICMS- ST for calculo na nota fiscal e seu valor não é creditado, o valor de ICMS ST deve ser considerado nos registros C100 campo 16 - VL\_MERC, C170 campo 07 VL\_ITEM e C190 campo 05 VL\_OPR

Configuração de TES

TES

Aba ADM

Crd. ICMS ST (F4\_CREDST) = 4=Subst. Trib ou 3=Debita

Importante

Os campos 24 VL\_ICMS\_ST Registro C100, 18 VL\_ICMS\_ST Registro C170 e 09 VL\_ICMS\_ST Registro C190 não deve ser preenchidos devido não existir credio de ICMS ST na nota fiscal.

Quando o IPI for calculado na nota fiscal e seu valor não é creditado, o valor de IPI deve ser considerado nos registros C100 campo 16 - VL\_MERC, C170 campo 07 VL\_ITEM e C190 campo 05 VL\_OPR

 Configuração de TES

TES

Aba Impostos

Calcula IPI (F4\_IPI) = Sim  
L. Fisc. IPI (F4\_LFIPI) = “Diferente de Tributado”

Importante

Os campos 25 VL\_IPI Registro C100, 24 VL\_IP Registro C170 e 11 VL\_IPI Registro C190 não deve ser preenchidos devido não existir crédio de IPI na nota fiscal.  
  
**Informações adicionais sobre a gravação do campo 16\_VL\_MERC no SPED FISCAL, registro C100:**

O fonte do SPEDFISCAL adiciona no campo 16 VL\_MERC somente o valor do IPI em operações de entradas.  
  
Em operações de devolução no qual o valor do IPI não é adicionado ao valor das mercadoria, como não é apresentando erro no validador do SPED FISCAL, caso o setor fiscal discorde da forma que o campo 16\_VL\_MERC é gravado quando o informante do IPI não tem direito ao crédito, será necessário o envio das considerações legais para possamos validar junto com a nossa consultoria segmentos.  
  
Abaixo trecho completo do fonte tratando o campo VL\_MERC do C100:  
  
aTotaliza[10] += (cAliasSFT)->FT\_TOTAL + Iif( (cAliasSFT)->FT\_TIPO <> "D", (cAliasSFT)->FT\_DESCZFR, 0 ) //Totaliza o documento fiscal  
  
//Adiciona valor de IPI ou ST não creditado ao valmerc  
  
If cEntSai == "1" .And. (!(cAliasSF4)->F4\_LFIPI$"T" .Or. (cAliasSFT)->FT\_CREDST $ "3|4" ) .And. !(cAliasSFT)->FT\_TIPO$"DB"  
  
    If!(cAliasSF4)->F4\_LFIPI$"T" .And. !(cAliasSF4)->F4\_IPI$"R"  
  
    aTotaliza[10] += (cAliasSD1)->D1\_VALIPI  
  
  
Na condição em que se soma o valor do IPI, somente dos movimentos de entrada, caso o TES não tenha o campo F4\_LFIPI como T (Tributado) e o campo F4\_IPI diferente de R:  
  
  
If cEntSai == "1" .And. (!(cAliasSF4)->F4\_LFIPI$"T" .Or. (cAliasSFT)->FT\_CREDST $ "3|4" ) .And. !(cAliasSFT)->FT\_TIPO$"DB"  
    If!(cAliasSF4)->F4\_LFIPI$"T" .And. !(cAliasSF4)->F4\_IPI$"R"  
    aTotaliza[10] += (cAliasSD1)->D1\_VALIPI  
  
Note que o sistema pega o valor diretamente da tabela SD1 e a validação para entrar nessa condição é específica, ou seja:  
  
cEntSai == 1 = Nota fiscal de entrada, campo F4\_LFIPI diferente de T e campo FT\_TIPO diferente de devolução ou beneficiamento.  
  
O campo F4\_LFIPI livro fiscal de IPI no cadastro de TES não pode ser Tributado e o campo F4\_IPI não pode ser R.

Link TDN:

<http://tdn.totvs.com/display/PROT/TUOX94_C100_C170_C190_Valor_Mercadoria_IPI_e_ICMS>

<http://tdn.totvs.com/display/public/PROT/ARQ0051_SPEDFISCAL+-+Registro+C100_Campo_16_VL_MERC+E+C170_CAMPO_07_VL_ITEM_Valor+De+ICMS-ST+E+IPI>
