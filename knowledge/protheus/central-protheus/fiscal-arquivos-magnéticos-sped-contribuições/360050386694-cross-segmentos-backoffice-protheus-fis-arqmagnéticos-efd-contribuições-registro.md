---
article_id: 360050386694
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: a6d2a895310b058156ec933b0b07cfa0c6c810de443d30168d2f05b5e846e78d
fetched_at: '2026-06-28T22:42:05.299881+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Registro M400/M800 O Valor Total da Receita Bruta no Período Deve ser Igual à
  Soma dos Valores dos Itens dos Documentos de Saída Cujo CST é Igual a 04, 06, 07,
  08 ou 09.
type: support-article
updated_at: '2025-04-24T20:26:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050386694-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Registro-M400-M800-O-Valor-Total-da-Receita-Bruta-no-Per%C3%ADodo-Deve-ser-Igual-%C3%A0-Soma-dos-Valores-dos-Itens-dos-Documentos-de-Sa%C3%ADda-Cujo-CST-%C3%A9-Igual-a-04-06-07-08-ou-09
---

**Dúvida**Erro no PVA:   
  
**A soma de VL\_TOT\_REC dos registros M400/M800 (XXXXX) deve ser igual à soma de VL\_ITEM dos registros A170, C170, C175, C181/C185, C381/C385, C481/C485, C491/C495, C601/C605, C870/C880,**  
**D201/D205 e D601/D605, de VL\_DOC dos registros D300, de VL\_BRT do registro D350, de VL\_OPER do registro F100, de VL\_TOT\_REC do registro F200, de VL\_REC\_CAIXA dos registros F500 e F510 e de**  
**VL\_REC\_COMP dos registros F550 e F560 e de VL\_REC\_FIN dos registros I100, quando CST\_PIS = 04, 06, 07, 08, 09.**

**Registro M400: Receitas Isentas, não Alcançadas pela Incidência da Contribuição, Sujeitas a**  
**Alíquota Zero ou de Vendas com Suspensão – PIS/Pasep**

**Registro M800: Receitas Isentas, Não Alcançadas pela Incidência da Contribuição, Sujeitas a**  
**Alíquota Zero ou de Vendas Com Suspensão – Cofins**  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**  
O valor apresentado no validador é o resultado da soma de todos os registros **M400** (**PIS**) e **M800** (**COFINS**) que foram apresentados em seu arquivo.  
  
A soma do registro **M400** - **Campo 3** de todos os registros existentes no arquivo para o **CST 04, 06, 07, 08 ou 09** são compostos através da tabela **CKT** - **Receita PIS/COF Nao Tributada**, campo **Vl. Rec. (CKT\_VLREC)**.   
  
O valor apresentado na apuração é armazenado na tabela **CL0** - **Cadastro de Inscrição Estadual**, campo **Vl.Oper.Cum (CL0\_VLOPC)**.  
  
Ambas as tabelas são gravadas no momento da apuração e com base nos valores da **SFT** (Tabela de itens do livro fiscal).  
  
Será necessário avaliar se existem notas que estão escrituradas erradas na **SFT**, pois isso pode causar a divergência apresentada no arquivo.  
  
Algumas divergências em tabelas que identificadas que poderão ser analisadas:  
  
1. Nota inutilizada onde a emissão (**FT\_EMISSAO**) e a data de inutilização (**FT\_DTCANC**) estão em meses divergentes. Não existe para a **SEFAZ** inutilização em mês diferente, inclusive o manual da **EFD Contribuições** detalha apenas situações onde o cancelamento ou devolução do documento ocorre em períodos diferentes. Neste caso, é recomendado alterar o conteúdo do campo **FT\_DTCANC** para a mesma data da emissão do documento. Somente realizar esta alteração caso identifique esta divergência em notas Inutilizadas.  
  
2. Nota denegada sem **FT\_CODRSEF** preenchido.  
  
3. Nota fiscal escriturada errada. Avalie o **Cadastro de TES (Tabela SF4)**.

Para os **CST's 04 ou 06** todos os cadastros de **TES** devem estar configuradas desta forma:  
  
**PIS/COFINS = Ambos**  
**Cred. Pis/Cof = Calcula**  
**Sit Trib Pis = 04 ou 06**  
**Sit Trib Cof = 04 ou 06**

Para os **CST's 07,08 ou 09,** todos os cadastros de **TES** devem estar configuradas desta forma:  
  
**PIS/COFINS = não considera**  
**Cred. Pis/Cof = não calcula**  
**Sit Trib Pis = 07,08 ou 09**  
**Sit Trib Cof = 07,08 ou 09**  
  
O preenchimento das tabelas de Natureza da Receita deve ser feito em algum dos cadastros:  
  
**-Pedido de Venda (SC6), nos campos C6\_TNATREC, C6\_CNATREC, C6\_GRPNATR e C6\_DTFIMNT;**  
**-Exceção fiscal (SF7), nos campos F7\_TNATREC, F7\_CNATREC, F7\_GRUPONC e F7\_DTFIMNT;**  
**-Produto (SB1), campos B1\_TNATREC, B1\_CNATREC, B1\_GRPNATR e B1\_DTFIMNT;**  
**-Tipos de Entrada e Saída (SF4), campos F4\_TNATREC, F4\_CNATREC, F4\_GRUPONC e F4\_DTFIMNT.**  
  
Faça a analise dos dados acima e identifique se há alguma nota que se enquadre nestas situações. Caso seja identificada alguma divergência, efetue as devidas correções dos documento e refaça a apuração da EFD Contribuições antes de gerar um novo arquivo.

Mais Informações:

<https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016305951-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Como-gerar-os-registros-M400-M410-e-M800-M810>
