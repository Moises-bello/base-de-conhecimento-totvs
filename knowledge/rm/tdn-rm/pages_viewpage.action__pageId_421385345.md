---
content_hash: e47ae3173df5648fbfcefd31ee127011dc6a6a9d6b0eeb4257c85e8d60b57508
fetched_at: '2026-06-29T00:09:15.317048+00:00'
page_id: '421385345'
product: rm
source: tdn-rm
title: Consistência de Projetos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385345
version: 6
---

**Consistência de Projeto**   
 O objetivo desta tela é descrever o tratamento de consistência de planilhas de Serviço e Atividades e Projeto baseado em fórmulas pré-definidas.  
 Nesta tela é possível Validar a fórmula criada para as Planilhas de Serviços, Planilha de Atividades e o Projeto.  
 Para isso deve-se cadastrar uma fórmula (Menu - Opções - Parâmetros - TOTVS Obras e Projetos - Projetos - Planilha de Serviços/Planilha de Atividades ou Projeto) no campo Fórmula de Consistência, com a fórmula que tratam os dados da validação.  
 A consistência poderá ser feita a qualquer momento através do menu principal e também ao gerar uma revisão, desde que esteja parametrizado;

**Exemplo:**  
 Este processo visa fornecer informações de quais serviços da Planilha de Serviços, quais atividades da Planilha de Atividades e quais possíveis irregularidades podem existir no projeto em aberto.

**Exemplos de Tipos de Fórmulas:**  
 Devem ser implementadas funções de fórmulas para que atendam as validações das planilhas e projetos, algumas idéias de validações, como as listadas abaixo já podem ser testadas e ajustadas:  
 \*Para as validações abaixo foram utilizadas as funções de fórmula com os seguintes códigos: 97, 98, TABTRF, QTDEALOCADAATVSRV, CONSISTIRCOTACAOPRJ.

• Verificar se existe algum insumo sem preço  
  SELECT COUNT(1) TOTAL  FROM MISM (NOLOCK)  WHERE (SELECT COUNT(1) TOTAL  FROM MISMPRC (NOLOCK)  WHERE IDPRJ = :FRM\_98  AND CODCOLIGADA = :FRM\_97  AND IDISM = MISM.IDISM         AND PRECOATIVO = 1 ) = 0  AND IDPRJ = :FRM\_98  AND CODCOLIGADA = :FRM\_97  
 EXECSQL('2222'); Se RESULTSQL('2222','total') > 0 Entao 0 Senao 1 FimSe

• Verificar se a unidade do preço é a mesma do insumo e se são compatíveis  
  SELECT COUNT(1) TOTAL  FROM MISM (NOLOCK)  INNER JOIN  MISMPRC (NOLOCK) ON MISM.CODCOLIGADA = MISMPRC.CODCOLIGADA  AND MISM.IDPRJ = MISMPRC.IDPRJ  AND MISM.IDISM = MISMPRC.IDISM   LEFT JOIN  TUND TUNDISM (NOLOCK) ON TUNDISM.CODUND = MISM.CODUND LEFT JOIN    TUND TUNDPRC (NOLOCK) ON TUNDPRC.CODUND = MISMPRC.CODUND  WHERE TUNDISM.CODUNDBASE <> TUNDPRC.CODUNDBASE    AND MISM.CODCOLIGADA = :FRM\_97          AND MISM.IDPRJ = :FRM\_98  
 EXECSQL('2223'); Se RESULTSQL('2223','total') > 0 Entao 0 Senao 1 FimSe

• Verificar se existe cotação de moeda para efetuar indexação ou conversão do preço   
  CONSISTIRCOTACAOPRJ

• Verificar se existe alguma tarefa sem valor  
  Se TABTRF('ATIVA') = 1  Entao Se TABTRF('VALORTOTAL') > 0  Entao 1  Senao 0  FimSe  FimSe

• Verificar se existe alguma tarefa com quantidade zerada  
  Se TABTRF('ATIVA') = 1  Entao Se TABTRF('SERVICO') = 1  Entao Se TABTRF('QUANTIDADE') > 0  Entao 1  Senao 0  FimSe  Senao 1  FimSe  Senao 1  FimSe

• O sistema deverá garantir que todos os serviços foram totalmente alocados, nunca com quantidades superiores as previstas na Planilha de Serviço  
  Se TABTRF('SERVICO') = 1  Entao  Se QTDEALOCADAATVSRV <> TABTRF('QUANTIDADE')  Entao 0   Senao 1   FimSe    SeNao 1  FimSe

 Veja Também

---
