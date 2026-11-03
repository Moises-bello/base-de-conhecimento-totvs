---
article_id: 39243178305687
category: SIGAACD - Automação e Coleta de Dados
content_hash: c3356d8cba52491d661c375e1c0caad71d49bb4f4a2c92c925ec19fde3dc6389
fetched_at: '2026-06-28T22:39:12.599865+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como gerar um Log
  de auditoria para o ACD?
type: support-article
updated_at: '2026-03-23T22:26:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39243178305687-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-gerar-um-Log-de-auditoria-para-o-ACD
---

O ponto de entrada CBLOGALT, ativado pelo parâmetro MV\_LOGACD, permite gravar logs customizados no ACD do Protheus. Para usar, configure MV\_LOGACD como ativo, implemente a função U\_CBLOGALT, utilize o array PARAMIXB para identificar operações e compile o código. Exemplo inclui gravação em tabela customizada ZZ1.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39243178286359) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

Como rastrear logs de uso do ACD? para gravar logs dos processos efetuados?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus - SIGAACD - Todas as releases)

**Solução**

O ponto de entrada **CBLOGALT** é executado pela função genérica `CBLog` sempre que o parâmetro **MV\_LOGACD** estiver ativado. Sua principal função é permitir que o sistema realize gravações customizadas em tabelas específicas do cliente no momento em que o log padrão do ACD é gerado.

Ele disponibiliza o array `PARAMIXB` com as seguintes posições:

|  |
| --- |
| Posição [1] - Tipo do Log, sendo:   * 01 = endereçamento * 02 = transferência * 03 = baixa de cq * 04 = inventário * 05 = conferência * 06 = requisição * 07 = divisão etiqueta * 08 = preparação de endereçamento * 09 = expedição * 10 = devolução * 11 = desmonta embalagem   Posição [2] - Lista de campos |

**Passos**

1. Certifique-se de que o parâmetro **MV\_LOGACD** está configurado como `.T.` (Ativo) no **Configurador (SIGACFG)**.
2. Implemente a função de usuário `U_CBLOGALT` em seu ambiente de desenvolvimento.
3. Utilize o array `PARAMIXB` para identificar a operação e os dados que estão sendo processados.
4. Compile o código e realize os testes nas rotinas de coleta de dados.

**Exemplo de implementação:**

```
/*/{Protheus.doc} CBLOGALT
Ponto de entrada para gravação customizada do Log do ACD
@type  Function
@author KCSBuilder
/*/
User Function CBLOGALT()
    Local aArea   := GetArea()
    Local aEstrut := PARAMIXB // Recebe os parâmetros do log
 
    // Exemplo: Gravação em tabela customizada ZZ1
    DbSelectArea("ZZ1")
    If RecLock("ZZ1", .T.)
       ZZ1->ZZ1_FILIAL := xFilial("ZZ1")
       ZZ1->ZZ1_USUARI := __cUserID
       ZZ1->ZZ1_DATA   := DATE()
       ZZ1->ZZ1_HORA   := TIME()
       ZZ1->ZZ1_ROTINA := FUNNAME()
       ZZ1->(MsUnlock())
    Endif
 
    RestArea(aArea)
Return
```

**Saiba Mais:**

[*Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)  
[*SIGAACD - Quais Coletores de Dados são homologados para uso no módulo Automação e Coleta de Dados (SIGAACD)?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018771512-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Quais-Coletores-de-Dados-s%C3%A3o-homologados-para-uso-no-m%C3%B3dulo-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados-SIGAACD?source=search)  
[*Configurar impressora para impressão de etiquetas*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/23970894011799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Configurar-Local-de-impress%C3%A3o-ACDA060-para-utilizar-na-impress%C3%A3o-de-Etiquetas)
