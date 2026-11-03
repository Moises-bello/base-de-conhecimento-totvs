---
article_id: 38269019474711
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 797a90ea1ccd4deb5d7ce7cebef8a358d1d5552af536a4cb2ee637a364b1b222
fetched_at: '2026-06-28T22:37:20.328031+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - AJUDA:REGNOIS  Não
  existe registro relacionado a chave informada no alias SX5, ordenação 1 . C7_LOCAL     :=
  XX < -- Invalido na inclusão da medição
type: support-article
updated_at: '2026-02-09T14:35:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38269019474711-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-AJUDA-REGNOIS-N%C3%A3o-existe-registro-relacionado-a-chave-informada-no-alias-SX5-ordena%C3%A7%C3%A3o-1-C7-LOCAL-XX-Invalido-na-inclus%C3%A3o-da-medi%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38269042735127) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
  
AJUDA:REGNOIS     
Não existe registro relacionado a chave informada no alias SX5, ordenação 1.

Tabela SC7 29/01/2026 10:12:35  
DT Emissao           - C7\_EMISSAO   := 29/01/2026  
Fornecedor           - C7\_FORNECE   := 012127  
Loja                 - C7\_LOJA      := 01  
Cond. Pagto          - C7\_COND      := 005  
                    - ALCADA       := S  
                    - MED\_GCT      := GCT  
Moeda                - C7\_MOEDA     := 1  
Contato              - C7\_CONTATO   :=                  
Filial Entr.         - C7\_FILENT    :=     
Vlr.Frete            - C7\_FRETE     := 0  
Vlr.Despesas         - C7\_DESPESA   := 0  
Vlr.Seguro           - C7\_SEGURO    := 0  
Mensagem             - C7\_MSG       :=      
Reajuste             - C7\_REAJUST   :=      
Cod. Usuario         - C7\_USER      := 000591  
--------------------------------------------------------------------------------  
Tabela SC7 29/01/2026 10:12:35  
Erro no Item   1  
--------------------------------------------------------------------------------  
Item                 - C7\_ITEM      := 0001  
Produto              - C7\_PRODUTO   := xxxxxxxxx         
Descricao            - C7\_DESCRI    := SUPORTE TECNICO INFORMAT                            
Quantidade           - C7\_QUANT     := 1  
Qtde da SC           - C7\_QTDSOL    := 1  
Unidade              - C7\_UM        := SV  
Qtd. 2a UM           - C7\_QTSEGUM   := 0  
Prc Unitario         - C7\_PRECO     := 1000  
Aliq. IPI            - C7\_IPI       := 0  
Dt. Entrega          - C7\_DATPRF    := 29/01/2026  
**Armazem              - C7\_LOCAL     := XX < -- Invalido**  
Tipo Entrada         - C7\_TES       := XXX  
Observacoes          - C7\_OBS       :=   
Item Medicao         - C7\_ITEMED    := 001  
Vl. Desconto         - C7\_VLDESC    := 0  
Centro Custo         - C7\_CC        := XXXXXXX  
Cta Contabil         - C7\_CONTA     := XXXXXXXX          
Item Cont.           - C7\_ITEMCTA   :=            
Classe Valor         - C7\_CLVL      := XXXXXXXXX   
Num.Contrato         - C7\_CONTRA    := 0000000000000XX  
Rev.Contrato         - C7\_CONTREV   :=      
Num.Planilha         - C7\_PLANILH   := 000001  
Num.Medicao          - C7\_MEDICAO   := 000004  
Cod Nota Emp         - C7\_CODNE     :=               
Item Nt Emp          - C7\_ITEMNE    :=      
Fil. Origem          - C7\_FISCORI   := 01  
Rateio               - C7\_RATEIO    := 2  
------------------------------------------------------------------  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS protheus Gestão de Contratos  - Todas as versões  
  
**Solução**

Segue possibilidades da causa do erro abaixo:

1.É apresentado a mensagem Regnois quando o sistema não localiza as informações preenchidas no cadastro para o campo mencionado .Não estamos afirmando nada , mas uma das possíveis causas pode ter sido importado um produto para a rotina de cadastro de produtos com um armazém que não existe cadastrado na rotina AGRA045, para a mesma filial do contrato/medição.

 2.Acesse a rotina de Cadastro de produto na mesma filial do contrato/ medição , verifique se o armazém atrelado no cadastro de produto se existe no cadastro da Rotina de locais de Estoque AGRA045.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38269019461015)

3.Verifique se o compartilhamento das tabelas NNR,CN9, CND, CNE,SC7,SB1 se não estão divergentes? No padrão as tabelas de Contrato, armazém e Pedido são exclusivo. Para certificar de que existe o cadastro do armazém na mesma Filial do contrato/Medição.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38269042738711)

**Saiba Mais:**

[**Artigos Materiais - Gestão de Contratos - (SIGAGCT)**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
