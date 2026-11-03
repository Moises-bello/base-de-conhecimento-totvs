---
content_hash: d018df18a124a25279fd56ff37630df4b9367f1327f9199a0ae424d47ca5d72b
fetched_at: '2026-06-29T00:10:04.625699+00:00'
page_id: '452719228'
product: rm
source: tdn-rm
title: Roteiro - Relatório PCMSO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719228
version: 3
---

**Roteiro - Relatório PCMSO**

Este roteiro tem como objetivo, instruir na definição das informações que irão permitir montar e acompanhar o PCMSO de sua empresa. A Norma Regulamentadora - NR-7, estabelece a obrigatoriedade da elaboração e implementação, por parte dos empregadores e instituições que admitam empregados, do Programa de Controle Médico de Saúde Ocupacional - PCMSO, com o objetivo de promoção e preservação da saúde do conjunto de seus trabalhadores.

O conteúdo do PCMSO deverá atender na íntegra o que preconiza a Norma Regulamentadora nº 07 – NR - 07, aprovada pela Portaria nº 3214, de 08 de junho de 1978, do Ministério do Trabalho e Emprego – MTE, e as demais portarias e legislações:

Portaria nº 24, de 29 de dezembro de 1994, que aprova o texto disposto na NR - 07;

Portaria nº 08, de 08 de maio de 1996, que altera a NR - 07; Lei nº 6514, de 22 de dezembro de 1977, que altera o Capítulo V do Titulo II da Consolidação das Leis do Trabalho, relativo a segurança e medicina do trabalho e dá outras providências;

Lei nº 8112, de 11 de dezembro de 1990, em seus artigos 69, 72, 186 (parágrafo 2º) e 212; A elaboração, implementação, acompanhamento e avaliação do PCMSO poderão ser feitas pelo Serviço Especializado em Engenharia de Segurança e em Medicina do Trabalho - SESMT ou por médico do trabalho, empregado ou não da empresa indicado pelo empregador.

O PCMSO deverá ter caráter de prevenção, rastreamento e diagnóstico precoce dos agravos à saúde relacionados ao trabalho, inclusive de natureza subclínica, além da constatação da existência de casos de doenças profissionais ou danos irreversíveis à saúde dos trabalhadores. 

**Parametrização Necessária**  
 Para a elaboração do PCMSO é preciso que a estrutura do modelo do relatório deve ser importante conforme a sua parametrização de utilização de exames. Bem como em *Relatórios | Tipo de Relatório* seja incluído um relatório de tipo Saúde. Selecione o relatório incluído e execute o processo *Gerar modelo de PCMSO*.

Após, é necessário que em *Relatórios | Relatórios de Saúde* seja incluído um novo relatório, aonde o Cód. Tipo Relatório seja o mesmo do incluído em Tipo de Relatório. É recomendado que seja parametrizado apenas os campos de *Período* e a aba *Parametrização*.

 Dados da aba parametrização do relatório de saúde ocupacional:

- CODCOLIGADA - A coligada que se deseja gerar o relatório PCMSO.  
- CODRELATORIO - O código do relatório incluído em *Tipo de Relatório*.  
- CODLOCALTRABALHO - o código do local de trabalho em que se deseja gerar PCMSO.  
- DATAINICIO - A data início dos dados a serem levados no PCMSO.  
- DATAFIM - A data final dos dados a serem levados no PCMSO

Com todos os passos acima realizados, é possível gerar e visualizar o relatório.  
   
**Dados Necessários**  
   
o    **QUALIFICAÇÃO DOS RESPONSÁVEIS**  
   
 É preciso que haja responsáveis pela monitoração biológica nas seções que fazem parte do local de trabalho. Será levado em conta também os responsáveis que não possuírem seção no cadastro.  
 Para cadastrar os responsáveis o caminho é *PCMSO | Resp. Monitoração Biológica*.  
   
o    **FUNÇÕES E PERIODICIDADE DE EXAMES**  
   
 O anexo I é preenchido levando em conta as funções.  
   
 Será gerada apenas com as funções em que no anexo *Quadro de Lotação* está inserida alguma seção pertencente ao local de trabalho.  
   
 É preciso parametrizar a aba *Seções* do *Local de Trabalho*, informando as seções que serão geradas no PCMSO. Bem como também é necessário incluir a *Filial* e o *Cód. Seção de Referência* que será utilizado.  
   
 O campo *Atividades* do PCMSO fica localizado no sistema em *Função | Anexos | Quadro de Lotação*, abra a seção correspondente e vá à aba *Informações sobre a Função*. Preenchendo essa aba o campo será preenchido.  
   
 Para preencher os campos *Risco* e *Agente* é preciso que em *PPRA | Riscos* esteja incluído um item de risco e seu agente agrupador.  
 É preciso também que em *PPRA | Reconhecimento e Avaliação de Risco* seja incluído um controle de tipo *Reconhecimento*, com o código do item de risco incluído acima e o tipo passivo lotação, inserindo a função e a seção que se deseja preencher no PCMSO.  
   
 Por último, para preencher os campos *Exame* e *Periodicidade* é preciso que:  
 Em *PCMSO | Perfil de Exame* haja um perfil de exame com o anexo *Bateria de Exames* preenchido. Será levado em conta os exames e o tipo de cada exame desse anexo.  
 Associar o perfil de exame à lotação em *PCMSO | Assist. Associação de Perfil*.  
 Para verificar se o perfil de exame está associado à função abra o anexo *Perfis de Exame* da função.  
   
 Com todos os dados acima corretamente parametrizados o PCMSO será gerado corretamente, sem que falte qualquer dado ou esteja incorreto.   
   
**Observações:**

* Deve ser importado um tipo de relatório PCMSO para utilização de exames do tipo perfil de exame e um para utilização do tipo PCMSO X PPRA.
