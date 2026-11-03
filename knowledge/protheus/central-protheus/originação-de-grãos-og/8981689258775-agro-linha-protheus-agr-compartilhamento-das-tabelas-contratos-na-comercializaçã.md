---
article_id: 8981689258775
category: Originação de Grãos (OG)
content_hash: a83a06e1c3276ce401048135708ca2af43fdf145b6a639a60d70826ed53e3f71
fetched_at: '2026-06-28T22:45:37.615728+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Compartilhamento das tabelas - Contratos na comercialização,
  previsões financeiras
type: support-article
updated_at: '2025-01-17T19:06:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8981689258775-Agro-Linha-Protheus-AGR-Compartilhamento-das-tabelas-Contratos-na-comercializa%C3%A7%C3%A3o-previs%C3%B5es-financeiras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20176686212247) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como compartilhar os contratos e previsões financeiras no **Originação de Grãos**?  
  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**O contrato de comercialização pode gerar as previsões financeiras como títulos no **Contas a Pagar** ou no **Contas a Receber**.  
Caso desejar que não gere previsão financeira, é possível desabilitar esta funcionalidade através do parâmetro: **MV\_AGRPREV - Permitir incluir contratos de compra e venda sem informar previsão financeira**.  
**MV\_AGRPREV = .F. > Exige as previsões financeiras nos contratos de compra e venda**  
**MV\_AGRPREV = .T. > Permite incluir contratos de compra e venda sem informar previsão financeira**Os títulos são criados com as seguintes configurações:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9034609920535)

Desta forma, para que não tenha duplicidade de títulos no financeiro segue abaixo as configurações possíveis:   
  
**Configuração 1 - Utilizando a Comercialização Clássica e MV\_AGRPREV= .F.**É recomendado o uso exclusivo das tabelas**NJR - Contrato****NNW - Alteração do Contrato****NN7 - Previsão Financeira Contratos****NNY - Cadências do Contrato****SE1 - Contas a Receber****SE2 - Contas a Pagar****N8L - Vinculo Tits a Receber****N8M - Vinculo Tits a Pagar**  
**Configuração 2 - Utilizando a Comercialização Clássica e MV\_AGRPREV = .T.**É recomendado o uso **exclusivo** das tabelas  
**NJR - Contrato**  
**NNW - Alteração do Contrato**  
**NN7 - Previsão Financeira Contratos**  
**NNY - Cadências do Contrato**As tabelas abaixo, podem ser **exclusivo ou compartilhado**  
**SE1 - Contas a Receber**  
**SE2 - Contas a Pagar**  
**N8L - Vinculo Tits a Receber**  
**N8M - Vinculo Tits a Pagar  
  
Configuração 3 - Utilizando a Nova Comercialização e MV\_AGRPREV = .F.**A nova comercialização é mais flexível com o uso do compartilhamento das tabelas, podendo ser usados da seguinte maneira:  
**NJR - Contrato                                               SE1 - Contas a Receber**  
**NNW - Alteração do Contrato                      SE2 - Contas a Pagar**  
**NN7 - Previsão Financeira do Contrato       N8L - Vinculo Tits a Receber**  
**NNY - Cadências do Contrato                       N8M - Vinculo Tits  a Pagar**  
**N9A - Regras Fiscais do Contrato**Segue as três formas possíveis:  
Exclusivo                                                            Exclusivo                           
Compartilhado                                                  Exclusivo   
Compartilhado                                                  Compartilhado  
  
**Configuração 4 - Utilizando a Nova Comercialização e MV\_AGRPREV = .T.****NJR - Contrato                                               SE1 - Contas a Receber**  
**NNW - Alteração do Contrato                      SE2 - Contas a Pagar**  
**NN7 - Previsão Financeira do Contrato       N8L - Vinculo Tits a Receber**  
**NNY - Cadências do Contrato                       N8M - Vinculo Tits  a Pagar**  
**N9A - Regras Fiscais do Contrato**Segue as quatro formas possíveis:  
Exclusivo                                                            Exclusivo                           
Compartilhado                                                  Exclusivo  
Compartilhado                                                  Compartilhado  
Exclusivo                                                           Compartilhado  
  
Para utilizar a tabela de **Contrato - NJR** **exclusiva** e o financeiro **compartilhado** será necessário não  
utilizar a numeração sequencial por filial.  
Desta forma o numero do titulo não irá se repetir a cada filial se tornando fácil a identificação no financeiro e único no **contrato** independente de **filial**.  
Na nova comercialização, a definição por onde fazenda e filial será realizado a entrega do contrato é definido nas **Regras Fiscais - N9A** no campo **Fil. Origem - N9A\_FILORG**.
