---
article_id: 36146077515287
category: 'Financeiro - Baixas Automáticas a Receber '
content_hash: 5ac1a73f70c6c565a9134ffb991b562d9d49d29f7b8223d5ad3c627553a86aa2
fetched_at: '2026-06-28T22:37:38.794972+00:00'
product: protheus
section_id: 35057325714199
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a
  Receber - FINA110 - Ponto de entrada F110SE5
type: support-article
updated_at: '2025-11-06T12:17:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36146077515287-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Contas-a-Receber-FINA110-Ponto-de-entrada-F110SE5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36146077509783) Tempo aproximado para leitura: 00**:05:00 min**  
  
**Dúvida**

Como utilizar o PE F110SE5 ?  
  
**Solução**  
O F110SE5 atua na rotina **FINA110 - Baixas Automáticas** e tem como principal objetivo permitir a **manipulação dos títulos processados na tabela SE5** (Baixas e Movimentos Bancários).

* **Onde Atua:** É acionado **após** o processamento de um título na rotina FINA110, permitindo que você altere informações do registro que já foi gravado na tabela **SE5**.
* **Finalidade Comum:** Usado para gravar informações complementares ou realizar validações/ajustes específicos no movimento bancário (SE5) que não são contemplados pelo padrão da rotina, antes ou depois da gravação.

A **FINA110** processa a baixa de títulos e, se for uma baixa que gera movimento bancário, grava o registro na **SE5** (e, por equivalência, na FK5).

O **F110SE5** entra em ação exatamente nesse momento de gravação da SE5. Ele permite que utilize o ADVPL para ler, alterar ou incluir lógica customizada relacionada aos dados do título que está sendo baixado e seu respectivo registro na SE5.

```
User Function F110SE5()
Local aRecno := ParamIxb[1]
Local nCntFor :=0
dbSelectArea("SE5")
DbSetOrder(1)
For nCntFor := 1 to Len(aRecno)
SE5->(dbGoto(aRecno[nCntFor]))
MSGAlert("Titulo posicionado na SE5 Filial:" + SE5->e5_filial + Chr(13)Chr(10) + ", Data," DtOC(SE5->e5_data) + Chr(13)+Chr(10) + ", Tipo," + SE5->e5_tipo + Chr(13)+Chr(10) + ", Moeda" + SE5->e5_moeda + Chr(13)+Chr(10) + ", Valor," + str(SE5->e5_valor ) + Chr(13)+Chr(10) + ", Natureza," + SE5->e5_natureza + Chr(13)+Chr(10) + ", Numero do cheque," + SE5->e5_numcheq + Chr(13)+Chr(10) + ", Documento," + SE5->e5_documen )
Next nCntFor
Return Nil
```

Atenção: O trecho de código padrão que define o P.E. é uma simples chamada à função,  
  
Lembrando que só compilar o fonte do exemplo acima em seu RPO, não terá nenhum funcionalidade, e somente irá apresentar um alerta.

Para que o ponto de entrada `F110SE5` se torne ativo e funcional, é estritamente necessário que seja realizada a implementação da sua lógica, determinando quais campos serão alterados, quais conteúdos serão retirados, e quais campos terão os novos conteúdos conforme a sua necessidade.

A lógica ADVPL deve ser implementada para realizar o manuseio programático (leitura, alteração, gravação de dados).

Exemplo prático: Para que o Ponto de Entrada F110SE5 modifique o campo `E5_HISTOR` durante a execução da rotina FINA110 (Baixas Automáticas), a lógica em ADVPL deve ser obrigatoriamente acrescentada no código exemplo e compilada.

**Escopo do Suporte Padrão:**

* Fornecer o nome do P.E. correto para uma necessidade e confirmar sua existência e momento de chamada no fonte padrão.
* Quando o P.E. (a chamada original no código-fonte) não é executado ou apresenta comportamento inesperado, mesmo sem customização.

Entretanto, **não prestamos apoio na análise, desenvolvimento ou correção** da lógica de programação ADVPL implementada pelo cliente dentro do P.E.

Saiba mais:

* [F110SE5 - Manipulação de títulos processados na tabela SE5](https://tdn.totvs.com/pages/viewpage.action?pageId=146965587)
* [SUP.PROTHEUS - Modalidades e Escopo de Atendimento do Suporte Técnico](https://tdn.totvs.com/pages/viewpage.action?pageId=543089204)
