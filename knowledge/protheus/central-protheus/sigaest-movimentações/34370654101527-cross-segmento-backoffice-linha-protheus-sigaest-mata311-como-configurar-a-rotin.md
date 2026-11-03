---
article_id: 34370654101527
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 08a3adbbd838f4629a265faf23af936c4aad939ca915062cf1733bda8b1e7c2f
fetched_at: '2026-06-28T22:38:57.149553+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA311 - Como configurar
  a rotina Solicitacao de transferencia via Mile?
type: support-article
updated_at: '2025-08-22T17:05:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34370654101527-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA311-Como-configurar-a-rotina-Solicitacao-de-transferencia-via-Mile
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34370654087191) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como posso configurar a rotina MATA311, para uso via Mile?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**  
Na execução automatica da rotina, não devem ser informados os campos:

* NNT\_FILIAL, NNS\_FILIAL e NNS\_FILORI, pois estes são preenchidos de acordo com a filial logada
* NNT\_COD e NNS\_COD, pois são preenchidos automaticamente pela rotina

Mais detalhes: [Solicitação de Transferencia de Materiais - MATA311 - Estoque - P12](https://tdn.totvs.com/x/hywPIQ)

### **Configurar o layout conforme necessidade da importação dos dados. Pontos de atenção:**

**Tipo Adapter:** MVC  
**Adapter:** MATA311  
**Criar dois canais:**  
Principal com ID saída NNTMASTER e ocorrência 1-Única  
Secundário com ID saída NNSDETAIL com ocorrência N-Várias  
**Não informar os campos:**  
NNT\_FILIAL , NNS\_FILIAL , NNS\_FILORI ,NNT\_COD e NNS\_COD.

A rotina utiliza a configuração padrão de máximo permitido para linhas na grid de um modelo MVC (990)   
Saiba mais: [MILE - Model Integrator Layout Engine](https://tdn.totvs.com/display/framework/MILE+-+Model+Integrator+Layout+Engine)

### **Exemplo de utilização**

![EXEMPLOMILE311.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/34371054129431)

Configurações dos cadastros, bem como layout, seguem ao final do artigo em anexo, para facilitar a visualização e importação caso desejar pra validação interna.

![Screenshot_3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34371054131607)

**Saiba mais:**

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310 / MATA311 - Como configurar a Transferência entre Filiais (MATA310 / MATA311) no Protheus?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418209855639-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA310-MATA311-Como-configurar-a-Transfer%C3%AAncia-entre-Filiais-MATA310-MATA311-no-Protheus-?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA310/MATA311 - Como definir o Preço de Venda do Pedido de Venda derivado do processo de Transferência entre Filiais ?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021390332-MP-SIGAEST-Custo-do-produto-derivado-do-processo-de-transfer%C3%AAncia-via-MATA311-)

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
