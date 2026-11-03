---
article_id: 360027115311
category: RH - Integração de Titulo
content_hash: a3a35e94b19a540ed2fea5fe5dc3bdf0d73a5614020e9579f8e331b829490f44
fetched_at: '2026-06-28T22:43:36.108385+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE  - Como realizar a exclusão de um título financeiro
  gerado pelo módulo de Gestão de Pessoal através do módulo Financeiro
type: support-article
updated_at: '2025-07-14T20:42:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027115311-RH-Linha-Protheus-GPE-Como-realizar-a-exclus%C3%A3o-de-um-t%C3%ADtulo-financeiro-gerado-pelo-m%C3%B3dulo-de-Gest%C3%A3o-de-Pessoal-atrav%C3%A9s-do-m%C3%B3dulo-Financeiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17491709743767) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como realizar a exclusão de um título financeiro gerado pelo módulo de Gestão de Pessoal através do módulo Financeiro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para excluir automaticamente um título financeiro gerado pelo módulo gestão de pessoal, no módulo financeiro (SE2 - Contas a pagar) e também no módulo Gestão de Pessoal (RC1 - Movimentações de Títulos) será necessário ativar o parâmetro **MV\_GPEEXTT.**

1. Acesse o Configurador / Ambiente / Cadastros / Parâmetros, Localize o parâmetro **MV\_GPEEXTT** e verifique se está configurado com **.T.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17490582643479)**

2. No módulo Financeiro acesse Atualizações / Contas a pagar (FINA050) Clique em Outras Ações e Excluir;  
  
3. Será apresentada uma janela com a mensagem de que o título foi gerado pelo módulo SIGAGPE e se realmente deseja deletá-lo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17491464494999)

4. Clicando em SIM, o título à ser excluído será apresentado na janela Contas a Pagar - EXCLUIR: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17491487340951)

5. Após conferir os dados e clicar em Confirmar é possível verificar a exclusão no Módulo GPE (RC1 - Movimentações de Títulos) e no módulo Financeiro (SE2 - Contas a Pagar).   
  
**Detalhe:** Essa opção de deletar através da rotina do Financeiro, não impede que o título continue sendo excluído através da rotina GPEM660 ( manutenção/movimentação de títulos).   
  
**Observação:**  
Ainda sobre a funcionalidade do parâmetro MV\_GPEEXTT, uma vez configurado com .F. ,  na tentativa de exclusão através do módulo Financeiro, será apresentada uma mensagem, informando que só é possível excluir no módulo GPE:   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20939339068951)  
  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
