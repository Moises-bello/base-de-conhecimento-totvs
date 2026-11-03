---
article_id: 4416000279447
category: Desenvolvedor de Produtos (SIGADPR)
content_hash: f6f5c6d9d477467d1d20a3152443a55ef0e6c4c8a394837e68e54ab26e6b04b2
fetched_at: '2026-06-28T22:42:48.718132+00:00'
product: protheus
section_id: 360005696254
source: central-protheus
title: Manufatura - Linha Protheus - SIGADPR - Campos correspondentes do SIGADPR ao
  SIGAPCP
type: support-article
updated_at: '2021-12-17T14:05:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416000279447-Manufatura-Linha-Protheus-SIGADPR-Campos-correspondentes-do-SIGADPR-ao-SIGAPCP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:38 min** **Dúvida**Para implantação do **Desenvolvedor de Produtos**, quais os campos do **SIGADPR****- Desenvolvedor de Produtos** que são equivalentes no **SIGAPCP - Planejamento e Controle da Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Desenvolvedor de Produto (SIGADPR) - Versão 12  
  
**Solução**  
Segue a listagem dos campos equivalentes do **SIGADPR** para o **SIGAPCP**.  
É necessário que esses campos tenham o mesmo tamanho, para que a integração ocorra sem erro**.**

|  |  |
| --- | --- |
| Campos do **SIGADPR** | Campos do **SIGAPCP** |
| **DG0\_DTULRO - Dt Últ Repos** | **B1\_UCALSTD - Ult. Calculo** |
| **DG0\_VLPRRO - Preço Repos** | **B1\_CUSTD - Custo Stand.** |
| **DG0\_DTULEN -Dt Últ Entr** | **B1\_UCOM - Ult. Compra** |
| **DG0\_VLULEN - Preço Últ En** | **B1\_UPRC - Ult. Preco** |
| **DG0\_CDPJ - Projeto** | **AF8\_PROJET - Projeto** |
| **DG0\_CDEDT - EDT - Estrut** | **AFC\_EDT - EDT** |
| **DG0\_DSPJ - Desc Projeto** | **AF8\_DESCRI - Descrição** |
| **DG1\_NRSQ - Sequência** | **D4\_TRT - Seq.Estrut.** |
| **DG1\_NRSQ - Sequência** | **G1\_TRT - Sequência** |
| **DG1\_CDMT - Compon Eng** | **D4\_COD - Produto** |
| **DG1\_CDMT - Compon Eng** | **G1\_COMP - Componente** |
| **DG1\_CDMTDV - Compon Desen** | **G1\_COMP - Componente** |
| **DG1\_DTBG - Data Início** | **G1\_INI - DT Inicial** |
| **DG1\_TPVV - Tipo Quantid** | **G1\_FIXVAR - Qtd. Fix/Var** |
| **DG1\_VLPNLS - Fator Perda** | **G1\_PERDA - Índice Perda** |
| **DG3\_CDACDE - Prod Destino** | **B1\_COD - Código** |
| **DG3\_CDACDE - Prod Destino** | **B1\_DESC - Descrição** |
| **DG3\_CDUN - Unid Medida** | **B1\_UM - Unidade** |
| **DG3\_CDGE - Gr.Estoque** | **B1\_GRUPO - Grupo** |
| **DG3\_CDFA - Família** | **B1\_TIPO - Tipo** |
| **DG3\_CDUNDE - Unid Med Des** | **B1\_UM - Unidade** |
| **DG3\_CDUN2 - Un Med Des 2** | **B1\_SEGUM - Seg.Un.Medi.** |
| **DG3\_VLPNUN - Fator Conver** | **B1\_CONV - Fator Conv.** |
| **DG3\_TPPNUN - Tipo Convers** | **B1\_TIPCONV - Tipo de Conv** |
| **DG3\_DTULEN - Data Últ Ent** | **B1\_UCOM - Ult. Compra** |
| **DG3\_DTULRO - Data Últ Rep** | **B1\_UCALSTD - Ult. Calculo** |
| **DG3\_CDDPPA - Depósito Pad** | **B1\_LOCPAD - Armazem Pad.** |
| **DG9\_DSAT - Des Operação** | **G2\_DESCRI - Descr. Oper.** |
| **DG9\_CDMQ - Máquina** | **G2\_RECURSO - Recurso** |
| **DG9\_NRUNAC - Unidades** | **G2\_LOTEPAD - Lote Padrão** |
| **DG9\_QTTESU - Tempo Prepar** | **G2\_SETUP - Setup (Hs)** |
| **DG9\_QTTEMQ - Tempo Máquin** | **G2\_TEMPAD - Tempo Padrao** |
| **DG9\_QTRC - Nr Homens** | **G2\_MAOOBRA - Mao-de-Obra** |
| **DG9\_TPTEAT - Tratamento T** | **G2\_TPOPER - Tipo Operac.** |
| **DG9\_TPALFE - Tipo Alocaçã** | **G2\_TPALOCF - Tp.Aloc.Ferr** |
| **DG9\_CDFE - Ferramenta** | **G2\_FERRAM - Ferramenta** |
| **DG9\_TPTEOV - Tipo Sobrepo** | **G2\_TPSOBRE - Tipo Sobrep.** |
| **DG9\_QTTEOV - Tempo Sobrep** | **G2\_TEMPSOB - Tempo Sobre.** |
| **DG9\_QTTEPP - Tempo Pospro** | **G2\_TEMPEND - Tempo Fim** |
| **DG0\_QTACEA - Qtde Base** | **B1\_QB - Base Estrut.** |
| **DGC\_NRBU - Nr Orçam** | **CK\_NUM - Num. Pedido** |
| **DGC\_NRSQBU - Nr Seq Orç** | **CK\_ITEM - It.Contrato** |
| **DGC\_CDACBU - Prod Orçam** | **CK\_PRODUTO - Produto** |
| **DGC\_NRPD - Nr Pedido** | **C6\_NUM - Num. Pedido** |
| **DGC\_NRSQPD - Seq Pedido** | **C6\_ITEM - Item** |
