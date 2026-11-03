---
content_hash: 01fca2692988310d37de425bfa0727ec066273bf8b603f9ca2aaeda82a03f866
fetched_at: '2026-06-29T00:09:36.813591+00:00'
page_id: '425459525'
product: rm
source: tdn-rm
title: BackOffice RM x Protheus SigaMNT - Análise Técnica de Pneus
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459525
version: 4
---

**Análise Técnica de Pneus**

---

O processo  de  Análise Técnica de Pneus permite que o usuário analise o estado de um pneu, podendo assim dar o destino condizente ao mesmo como por exemplo: Ressolar, consertar, estoque usado, estoque reformado , analise fornecedor, Sucata e Estoque novo.  
    
 Para realizar o processo de Análise Técnica de Pneus o usuário deverá, no SigaMNT,  acessar o caminho **Atualizações | Controle de Pneus | Análise Técnica |Análise Técnica** e efetuar o processo.  
    
 **Observação**: *Para detalhes de como realizar uma análise técnica de pneus no Protheus SigaMNT favor consultar a documentação do mesmo.*  
    
    
   
    
    
 Durante a análise técnica, caso necessário, a rotina do SigaMNT Frotas solicitará ao usuário que selecione o produto ao qual este pneu deverá ser considerado no módulo de estoque após a alteração de status.  
    
 Ao finalizar a análise técnica, dependendo do procedimento realizado no SigaMNT o sistema enviará ao Backoffice RM uma mensagem (StockTurnover) de baixa, ou uma de entrada ou as duas mensagens juntas.  
 Para verificar qual movimento será gerado no RM basta verificar o conteúdo da tag 'Type' no XML da mensagem única .  
    
 Ficando assim:   
    
 'Type' = '000' será gerado um movimento de baixa de estoque  
 'type' =  '001'  será gerado um movimento de entrada de estoque  
    
 Após a Análise Técnica ser finalizada no Protheus SigaMNT o usuário deverá acessar o TOTVS Gestão de Estoque, Compras e Faturamento, acessar o movimento gerado (baixa de estoque ou entrada de estoque) e confrontar  os dados do movimento com os dados da mensagem única afim de verificar se os mesmos foram gerados corretamente.  
     
 Para mais informações sobre o processo de Análise Técnica de Pneus, acesse os boletins técnicos.

---

**Recursos Adicionais**

TDN - Boletim Técnico:  [Processo de Análise Técnica de Pneus](http://tdn.totvs.com/download/attachments/76251261/PROTHEUS_BT_AN%c3%81LISE+T%c3%89CNICA+DE+PNEUS_BR_CON000158.pdf?version=1&modificationDate=1380053410000)
