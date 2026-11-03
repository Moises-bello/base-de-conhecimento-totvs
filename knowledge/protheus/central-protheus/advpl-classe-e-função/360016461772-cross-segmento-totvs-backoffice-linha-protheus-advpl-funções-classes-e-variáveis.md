---
article_id: 360016461772
category: ADVPL - Classe e Função
content_hash: 83d5449c1d59b5eacdcbba8d12ada42a2dd5db67e6cb09e0d50648d8d9cb4c3c
fetched_at: '2026-06-28T22:40:16.895762+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Funções, classes
  e variáveis de propriedade interna
type: support-article
updated_at: '2026-02-24T19:20:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016461772-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%B5es-classes-e-vari%C3%A1veis-de-propriedade-interna
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19025383464343)Tempo aproximado para leitura: **00:06:00 min**  
  
**Ocorrência**  
Cliente está utilizando uma função, classe ou variável não documentada em uma customização e a mesma apresenta inconsistências ou tem seu comportamento alterado.  
  
**Ambiente**  
Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 11.8  
  
**Causa**  
Funções, classes e variáveis restritas em fontes customizados não estão previstas pelo suporte padrão, dado o fato de que as mesmas não estão documentadas, assim sendo, podem vir a ser descontinuadas ou sofrer alterações de comportamento sem prévio aviso.  
  
**Solução**  
Cliente terá que desenvolver uma rotina que atenda a necessidade, utilizando funções documentadas e/ou registrar sua necessidade na [**Central Colaborativa**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039467434), para análise a viabilidade de implementação.

**Recursos restritos e de propriedade interna, com a compilação bloqueada a partir da** [**release 12.1.33**](https://tdn.totvs.com/pages/releaseview.action?pageId=630389705)**, que não possuem suporte:**

|  |  |
| --- | --- |
| 1 | **StaticCall()** |
| 2 | **PTInternal()** |

Como solução, vide documentações:

[Função StaticCall() não compila/mudou o comportamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411463269911)  
[Função PTINTERNAL() não compila/mudou o comportamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411463486871)

**Recursos restritos e de propriedade interna, que apesar de não terem a compilação bloqueada, não possuem suporte.**

Observação: Podem vir a sofrer alterações de comportamento ou até mesmo serem descontinuadas no futuro.

|  |  |
| --- | --- |
| 1 | VALIDAAUTONFE |
| 2 | MA410IMPOS |
| 3 | MALIBDOFAT |
| 4 | TFONTEX |
| 5 | NFEPROCNFE |
| 6 | AVCPYFILE |
| 7 | F\_OPCOES |
| 8 | AUTONFEENV |
| 9 | MASAPREREQ |
| 10 | FTVDVENDA |
| 11 | MAALCDOC |
| 12 | FISA022TRS |
| 13 | FGX\_STATF2 |
| 14 | NG400TAR |
| 15 | CODSITRI |
| 16 | IW\_MULTILINE |
| 19 | FWCHKFUNCACCESS |
| 20 | WSNFESBRA |
| 21 | SPEDDANFE |
| 22 | SPEDPEXP |
| 23 | WebService - NFESBra |
| 24 | CBGrvEti |
| 25 | A460ESTORNA |
| 26 | GETNUMSC7 |
| 27 | ISCAIXALOJA |
| 28 | XNUMCAIXA |
| 29 | CALCEST / CALCESTL |
| 30 | FRTGERASL |
| 31 | MSCLEARBUFFER |
| 32 | CA100INCL |
| 33 | SPEDNFERE2 |
| 34 | FCARRTAB |
| 35 | SALDOTERC |
| 36 | FABAIXACR |
| 37 | A093PROD |
| 38 | OOBJ:GETDATA |
| 39 | AVSTACTION |
| 40 | VTGETSENHA |
| 41 | A450GRAVA |
| 42 | OPENSXS |
| 43 | FINA110 |
| 44 | A410INCLUI |
| 45 | FP\_CODFOL |
| 46 | NFECABDOC |
| 47 | OPENSRC |
| 48 | EXTRACT |
| 49 | INCNOTA |
| 50 | MOVIMENTO |
| 51 | ATFA050 |
| 52 | PLSQUERY |
| 53 | PROXNUM |
| 54 | FILE2PRINTER |
| 55 | SPF\_SEEK |
| 56 | SPF\_UPDATE |
| 57 | FWSQLUsrFilial |
| 58 | APPEND FROM |
| 59 | ACPORET |
| 60 | FBUSCACPO |
| 61 | A093PROD |
| 62 | LASTKEY |
| 63 | RPCSETYPE |
| 64 | WFPREPENV |
| 65 | SALDOB2 |
| 66 | TMSA050EDI |
| 67 | GERATMP |
| 68 | A103ATUSE2 |
| 69 | CTBANFS |
| 70 | WAITRUNSRV |
| 71 | A103CONSNFESEF |
| 72 | SPDCRIATRB |
| 73 | A103NFISCAL |
| 74 | TTPVIEWER |
| 75 | MACANDELF2 |
| 76 | MADELNFS |
| 77 | RET\_CBARRA |
| 78 | A440LIBERA |
| 79 | RFMASHUPS |
| 80 | FWJWT2BEAR |
| 81 | CTGERPLAN |
| 82 | NXTSX5NOTA |
| 83 | FMONTA\_TPR |
| 84 | COPY TO |
| 85 | FDIASAFASPERIODO |
| 86 | CBCHKTEMPLATE |
| 87 | MsExcel |
| 88 | ENGSX3117 |
| 89 | FWLOOKUP |
| 90 | FRETAFASBRA |
| 91 | FWMVCROTAUTO |
| 92 | MontaBlock |
| 93 | A94EXLIBER |
| 94 | ESTRUT |
| 95 | A030ALTERA |
| 96 | MSFCREATE |
| 97 | TMSA200PRC |
| 98 | HEADPROVA |
| 99 | DETPROVA |
| 100 | PARAMBOX |
| 101 | FWUIWORKSHEET |
| 102 | CrdXTitAtr |
| 103 | MA410RODAP |
| 104 | WRITEPROFDEF |
| 105 | FINDPROFDEF |
| 106 | CBOPENPORT |
| 107 | FATATUEMPN |
| 108 | MAAVALSC9 |
| 109 | VLDLOCALIZ |
| 110 | A410MultT |
| 111 | PivotTable |
| 112 | A381Manut |
| 113 | MATXFIS |
| 114 | MaFisAdd |
| 115 | CTGercomp |
| 116 | WFNotifyAdmin |
| 117 | a260Processa |
| 118 | a415Tabela |
| 119 | MaAvalCred |
| 120 | A100Distri |
| 121 | \_\_SaveParam() |
| 122 | A110APROV |
| 123 | MDeMata103 |
| 124 | BuscaTaxa() |
| 125 | CriaVar |
| 126 | E\_FIELD |
| 127 | ApOleClient |
| 128 | GetServerPort |
| 129 | CheckStation |
| 130 | CTBAFIN |
| 131 | A415DESCAB |
| 132 | A410RECALC |
| 133 | X31UPDTABLE |
| 134 | FA050Venc |
| 135 | A097ProcLib |
| 136 | MaAvLibPed |
| 137 | A120Pedido |
| 138 | LoadLayout() |
| 139 | FtNfDevol |
| 140 | FtNfVendas |
| 141 | TK271CallCenter |
| 142 | LJ7VENDA |
| 143 | MA020PcCgc |
| 144 | A140NFiscal |
| 145 | procMonitorDoc |
| 146 | ProxDoc |
| 147 | PutMarcacoes |
| 148 | Fa050Visua |
| 149 | SaldoCt7 |
| 150 | F4LOTE |
| 151 | CBRetEtiEan |
| 152 | RetSldEnd |
| 153 | A310Proc |
| 154 | SpedNFeTrf |
| 155 | SetPrvt |
| 156 | TK273GRVPTC |
| 157 | APPEXCEL |
| 158 | VTNewEmpr |
| 159 | TWFMAIL |
| 160 | MaColsToFis |
| 161 | WFNotifyAdmin |
| 162 | FWAUTHUSER |
| 163 | fBuscaSal |
| 164 | XFUNWizard |
| 165 | A410Altera |
| 166 | MC050CON |
| 167 | AVGXML2DBF |
| 168 | MaLiberOk |
| 169 | MaRgrDesc |
| 170 | ApiForCli |
| 171 | A415Baixa |
| 172 | INFImpBMP |
| 173 | STBCalcSald |
| 174 | FVALBENNIF |
| 175 | A450F4Con |
| 176 | EECView |
| 177 | CALLPROC |
| 178 | TWorkspace |
| 179 | TWorkspaceFolder |
| 180 | ExplEstr |
| 181 | RetFldProd |
| 182 | STWMANAGREPORTPRINT |
| 183 | CN300VlCli |
| 184 | OpenFile |
| 185 | \_\_CopyFile |
| 186 | MATFilCalc |
| 187 | A161MapCot |
| 188 | INFCodeBare |
| 189 | INFTexto |
| 190 | CallRM |
| 191 | DistanciaGPS |
| 192 | TECGtCoord |
| 193 | NG420GRAVA |
| 194 | RetSem |
| 195 | nBIWeekOfYear |
| 196 | TAvPrinter |
| 197 | CTGerComp |
