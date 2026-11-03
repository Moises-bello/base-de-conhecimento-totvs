---
article_id: 4421883568023
category: Financeiro - Contas a Pagar
content_hash: 55a3f418e47a7c517479bddf0989aae5b87d7e6907d656f571c57a6c6b1bdc4c
fetched_at: '2026-06-28T22:38:08.371345+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus- SIGAFIN - FINA677 - HELP: F677APROA
  - Processo de aprovação não habilitado'
type: support-article
updated_at: '2022-02-11T12:39:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421883568023-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA677-HELP-F677APROA-Processo-de-aprova%C3%A7%C3%A3o-n%C3%A3o-habilitado
---

**Ocorrência**No módulo Financeiro, ao tentar realizar aprovação da prestação de contas, é apresentada a mensagem F677APROA - Processo de aprovação não habilitado!  
  
![F677APROA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4421890583959/F677APROA.png)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - FINA677 - Todas as versões  
  
**Causa**Esse incidente ocorre, pois não há Workflow de aprovação parametrizado via FINA691 - Assistente de Configurações  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acessar a **rotina FINA691** - **Assistente de Configuração**  
2. Em **Configurar aprovações**, deve marcar ao menos uma etapa de aprovação para as ações de **Prestação de Contas**.   
3. Sair da rotina e acessa-la novamente para realizar a aprovação. 

Obs: Recomendamos que para as etapas de Viagens, seja marcado uma das etapas de conferencia, já que o processo de cancelamento/exclusão em alguns casos é irreversível, umas vez que foi conferido e aprovado automaticamente.

**Saiba mais**:   
<https://tdn.totvs.com/display/public/PROT/Viagens+-+Financeiro+-+P12>

Helps relacionados:  
[Cross Segmento - BackOffice Linha Protheus - SIGAFIN - FINA677 - HELP: RECNO - Aprovação da Prestação de Contas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407080924439)  
  
[Cross Segmento - Backoffice Linha Protheus- SIGAFIN - FINA 677 - Help: NO\_ACCESS\_677 - Usuário sem acesso para manipular prestação de contas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018818192-MP-SIGAFIN-FINA-677-Help-NO-ACCESS-677-Usu%C3%A1rio-sem-acesso-para-manipular-presta%C3%A7%C3%A3o-de-contas)  
  
[Cross Segmento - Backoffice Linha Protheus- SIGAFIN - FINA677 - HELP F677ACESSO: Usuario não possui acesso para liberar financeiro](Cross%20Segmento%20-%20Backoffice%20Linha%20Protheus-%20SIGAFIN%20-%20FINA677%20-%20HELP%20F677ACESSO:%20Usuario%20n%C3%A3o%20possui%20acesso%20para%20liberar%20financeiro)
