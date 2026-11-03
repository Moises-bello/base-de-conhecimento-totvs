---
content_hash: 0b0acfe1418ae94bb79f06c40ea14b525691fd4fd3209a60ffcdac3f9814004b
fetched_at: '2026-06-29T00:09:35.848877+00:00'
page_id: '425459393'
product: rm
source: tdn-rm
title: TOTVS Obras e Projetos x BackOffice Protheus - Perguntas Frequentes / Dicas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459393
version: 9
---

**Perguntas Frequentes / Dicas**

---

**Pacotes de Integração: TOP x BackOffice Protheus**   
    
 **Pergunta 1 -  Em relação ao processo de compras, no Backofice RM existe a opção de solicitar compras informando o "preço orçado" dos insumos, para conhecimento do comprador. Isto poderá ser feito na integração TOP x Backoffice Protheus?**  
    
 Resposta: Não. Esta informação não é sincronizada, pois o Protheus não guarda os preços "sugeridos".

**Pergunta 2 - Em relação ao processo de compras. Como o usuário do TOP saberá o que foi comprado através do módulo de compras Protheus?**  
    
 **Resposta:** Toda compra lançada no Protheus a partir de uma necessidade do TOP (possui um projeto/tarefa associada) irá gerar uma "apropriação" no TOP, com as informações da compra efetuada.

**Pergunta 3 - Como identificar/gerenciar problemas na integração?**  
    
 **Resposta:** Primeiramente verifique se a integração está ativada e se os demais parâmetros da integração estão definidos, no TBC e no BackOffice Protheus (veja Manual Técnico RM e Boletim Técnico Protheus para detalhes).   
    
 **Dica:** Se ainda assim a integração não ocorrer, verifique se alguma mensagem de erro foi gravada nos logs do sistema, como segue:

**Para processos que utilizem a tecnologia de Stored Procedures (a maioria dos cadastros do Protheus para o RM). Parâmetros relacionados:**

MV\_PMSRMLG = (0) Alerta no Servidor; (1) Arquivo LOG; (2) Trace. Na opção 1 somente erros são armazenados, na opção 2 todos as execução de procedimentos são armazenadas. Com a opção 2 serão gravadas todas as chamadas às Stored Procedures. MV\_DIRLOG armazena o local arquivo log.

**Para processos que utilizem a tecnologia de WebServices**

Verificar se o WebService esta respondendo acessando o mesmo por um browser qualquer.

**Exemplo**: Internet Explorer ou Firefox.

Com isto é possível identificar se o Web Service esta respondendo e se o namespace informado na configuração está correto.

- Para ambos os processos:

No RM serão logadas a maioria das chamadas às stored procedures e as chamadas do RM aos WebServices do Protheus e eventuais mensagens de erro. Para acessar: RM.exe | Integração | Ferramentas | Monitor da Fila de Integração.   
   
**Pergunta 4: A mensagem de erro é apresentada no envio da solicitação de compra para o Protheus: Movimento ?47?! - Série PHT: A tarefa do projeto não foi especificada. Os campos "Data de Dedução" e "Apropriado" não devem ser informados. Código da Informação: \[0dc060f56fed3fed055af476510b102\]. Observação: O erro pode ocorrer na solicitação do armazém.\***  
   
**Resposta:** Verifique se a parametrização foi feita corretamente. Acesse: BackOffice / Gestão de Estoque,Compras e Faturamento / Ambiente / Parâmetros / Gestão Compras / Solicitação Compras / Selecione o Tipo do Movimento / Selecionar a opção "Não Informa" na etapa 69.
