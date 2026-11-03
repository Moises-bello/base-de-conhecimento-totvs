---
article_id: 360016596851
category: 'Financeiro - Liberação de Baixa '
content_hash: 779a7462e060f3857cf189daae44ad54f19063625189d2bd424416ce8a6b9f48
fetched_at: '2026-06-28T22:37:33.021421+00:00'
product: protheus
section_id: 35057590391959
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA580 - Como utilizar
  a rotina liberação para baixa
type: support-article
updated_at: '2026-06-12T17:28:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016596851-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA580-Como-utilizar-a-rotina-libera%C3%A7%C3%A3o-para-baixa
---

**Dúvida**  
Como utilizar a rotina liberação para baixa?  
  
**Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 12  
  
**Solução**  
A rotina **Liberação Para Baixa (FINA580)** será executada somente se o parâmetro **MV\_CTLIPAG** estiver configurado com o **valor T**, que significa que o sistema verifica se a Dt. Liberação campo **E2\_DATALIB** está preenchido ou caso contrário não controla essa validação apresentando a mensagem “**Esta rotina só será executada quando o parâmetro MV\_CTLIPAG = T”**

Caso só exista a necessidade de consistir em liberação de títulos com valor acima de uma determinada quantia, basta configurar o parâmetro **MV\_VLMINPG**. Isso fará com que para valores abaixo do que foi informado no parâmetro **MV\_VLMINPG**, a liberação seja feita automaticamente.

**Exemplo*****:***Ao preencher o parâmetro **MV\_VLMINPG = 1000 (sem milhar)**o sistema não validará nenhum valor de título menor que este (para efeito da liberação da Baixa).

Então poderá ser incluído um título no Valor de **R$ 999,99**que o sistema não solicitará que o mesmo seja liberado.

O parâmetro **MV\_CANLIPG** verifica se um título já liberado para pagamento (campo **E2\_DATALIB preenchido)** e que tenha sofrido alguma alteração deverá ser liberado novamente. Se igual a **"S"**, deve ser liberado novamente.

 O parâmetro **MV\_ALTLIPG** verifica se o título liberado para pagamento pode ter o **valor** alterado. Se = S títulos já liberados poderão sofrer alteração em seu valor.

**Importante**  
Por padrão, ao habilitar o parâmetro `MV_CTLIPAG`, o Protheus valida a liberação para todos os títulos gerados no Contas a Pagar (`SE2`), não havendo uma configuração nativa por "Tipo de Título" para ignorar essa validação.  
   
Para atender a essa necessidade via customização (Ponto de Entrada), pode ser analisada a seguinte solução:  
   
**Uso do Ponto de Entrada**`F580LbA`**(Liberação Automática):** Este ponto de entrada permite automatizar a liberação de títulos conforme regras específicas. É possível validar se o título posicionado é do tipo `PR` e retornar `.T.`, fazendo com que o sistema preencha a data de liberação automaticamente.  
   
Documentação: [**F580LbA - Bloqueia liberação automática**](https://tdn-homolog.totvs.com/pages/viewpage.action?pageId=649328939)

Caso o título seja criado pelo documento de entrada, preencha o código de aprovador no parâmetro **MV\_FINAPXX**.  
  
**Exemplo**:  
**MV\_FINAP01**, será inserido o código de aprovador para títulos de moeda 01.  
**MV\_FINAP02**, será inserido código de aprovador para títulos de moeda 02.

**Saiba mais:** [Liberação para Baixa - FINA580 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=312165854)
