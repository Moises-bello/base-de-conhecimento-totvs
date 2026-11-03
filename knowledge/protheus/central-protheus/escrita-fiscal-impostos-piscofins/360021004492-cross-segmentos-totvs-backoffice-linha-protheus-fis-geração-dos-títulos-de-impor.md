---
article_id: 360021004492
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 478a9be5ba2b1c0239327cf166de4208db5dd70d9fe5666ed736c039611a440d
fetched_at: '2026-06-28T22:39:36.822700+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Geração dos títulos
  de importação ISS/PIS/COFINS no contas a pagar
type: support-article
updated_at: '2025-07-31T14:54:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021004492-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Gera%C3%A7%C3%A3o-dos-t%C3%ADtulos-de-importa%C3%A7%C3%A3o-ISS-PIS-COFINS-no-contas-a-pagar
---

**Dúvida**  
KCS - Como Gerar os títulos de importação ISS e PIS/COFINS apuração no contas à pagar?  
  
**Ambiente**  
Protheus – Módulo Compras – A partir da versão 11.80.  
  
  
**Solução**

Para a correta geração dos títulos de importação (ISS/PIS/COFINS) no contas à pagar, é necessário seguir a seguinte configuração:

Fornecedor = EX

CFOP = Iniciar com 3

F4\_INTBSIC = 3 - Ambos

Parâmetros:

MV\_PREFCOF = COF  
MV\_PREFPIS = PIS  
MV\_PREFISS = ISS  
MV\_PISIMP = PIS  
MV\_COFIMP = COF  
MV\_ISSIMP = ISS

Obs: Sem a presença de aspas (" ").

Além de efetuar o preenchimento dos parâmetros acima, na rotina Documento de Entrada (MATA103) é preciso ativar a tecla F12 e na janela que abrir, preencher os campos de Gera Tit. PIS/COF Importação? e Gera Tit. ISS Importação? igual a "Sim":

![image (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/33848524226711)
