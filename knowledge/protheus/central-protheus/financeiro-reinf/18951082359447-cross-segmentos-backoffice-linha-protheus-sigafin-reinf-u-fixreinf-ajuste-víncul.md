---
article_id: 18951082359447
category: Financeiro - Reinf
content_hash: 04d5c69e017f54343c377cde3e2052d80a3aa069cf557001a025c51f3937d81c
fetched_at: '2026-06-28T22:37:51.869917+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - U_FIXREINF
  - Ajuste - Vínculo da Natureza de Rendimento para títulos lançados antes da vigência
type: support-article
updated_at: '2023-11-12T21:17:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18951082359447-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-U-FIXREINF-Ajuste-V%C3%ADnculo-da-Natureza-de-Rendimento-para-t%C3%ADtulos-lan%C3%A7ados-antes-da-vig%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18951039327127) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ajuste - Vínculo da Natureza de Rendimento para títulos lançados antes da vigência do EFD-Reinf Bloco 40  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**

Caso alguma das informações solicitadas nos eventos da serie R-4000 tenham sido inseridas no Backoffice Protheus antes da atualização do ambiente para a EFD-Reinf 2.1.2,  
e portanto não tendo as pré-condições necessárias para o envio dos dados ao TAF, uma alternativa é a execução da rotina padrão de ajuste de base REINF (U\_FIXREINF).  
que fará gravação das tabelas FKW (**Impostos x Natureza Rendimento**) e FKY (**Impostos x Nat. Rend. x Baixas**).

Aviso

* + [Documento de Entrada - Preenchimento automático da Natureza de Rendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=761500629)
  + [Pedido de Vendas - Preenchimento automático da Natureza de Rendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=747314010)
  + [Títulos do financeiro e demais origens - Preenchimento automático da Natureza de Rendimento](https://tdn.totvs.com/display/PROT/Facilitador+de+preenchimento+-+Natureza+de+Rendimento+X+Natureza+Financeira)
* Para utilizar esse modelo de preenchimento das Naturezas de Rendimento, revise o cadastro de Produto (para Doc. de Entrada/Saída) e o cadastro de Naturezas Financeiras (para títulos sem vinculo com nota fiscal).
* A proposta é que seja ajuste de base seja executado antes de realizar as baixas dentro do período de vigência do EFD-Reinf Bloco 40, pois irá gerar dados na tabela FKW, que é pré-condição para gravar os dados na tabela FKY. Porém, caso o título já tenha sofrido baixa parcial ou total dentro da vigência do EFD-Reinf Bloco 40, também será gravada a tabela FKY.
* Recomendamos que seja aplicado o ajuste primeiramente em ambiente de homologação antes de efetiva-lo no ambiente produtivo do Protheus;

## **EXEMPLO DE UTILIZAÇÃO**

1. A execução desse ajuste de base deve ser executado **obrigatoriamente no programa inicial do Smartclient**: U\_FIXREINF

## **DEMAIS INFORMAÇÕES**

[Wizard de configuração de ajuste de base Reinf](https://tdn.totvs.com/pages/viewpage.action?pageId=802753445)  
  
Após o processamento será gravado um log contendo os registros afetados na tabela REINFLOG do banco de dados.   
  
Obs. Necessário estar com os fontes abaixo a partir das datas:  
FIXCOMREIN.PRW 03/11/2023 17:07:31  
FIXFATREIN.PRW 03/11/2023 16:54:39  
FIXFINREIN.PRW 03/11/2023 12:00:50  
FIXREINF.PRW 03/11/2023 10:37:16  
  
Download da patch:   
12.1.2210:<https://suporte.totvs.com/portal/p/10098/download?e=1125597> ; 12.1.2310:<https://suporte.totvs.com/portal/p/10098/download?e=1125599> ; 12.1.33:<https://suporte.totvs.com/portal/p/10098/download?e=1125598> ;

## **ASSUNTOS RELACIONADOS**

[FAQ - 0015 - Como enviar dados no R-4000 inseridos antes da atualização do sistema?](https://tdn.totvs.com/pages/viewpage.action?pageId=736955879)
