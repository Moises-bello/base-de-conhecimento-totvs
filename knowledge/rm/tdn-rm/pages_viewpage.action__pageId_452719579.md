---
content_hash: ddba07f553460ee39eb6baba8407749a4226215b444ebd28936899d001525e5a
fetched_at: '2026-06-29T00:10:08.786774+00:00'
page_id: '452719579'
product: rm
source: tdn-rm
title: Aviso Prévio Trabalhado
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719579
version: 10
---

**Tipo de Demissão**  
Serão apresentados os tipos que correspondem as demissões por iniciativa do empregador ou do empregado, ambas sem justa causa, e comum acordo.  
Serão listados os seguintes tipos:

* 2 - Inic. Empregador sem justa causa
* 4 - Inic. Empregado sem justa causa
* V - Comum acordo

**Data de Início do Aviso**

Preencher com a data de início do aviso prévio.   
   
**Data de Demissão Prevista**

Preencher com a data prevista de desligamento.  
**Observação:** A data informada deve ser igual ou superior ao inicio do aviso prévio.

**A****tenção:**

A alteração do Aviso Prévio Trabalhado somente poderá ser realizada quando a rescisão não estiver calculada ou cadastrada com a situação do funcionário igual D - demitido no mês atual. Nesses casos, para fazer alteração do aviso prévio primeiro deve-se cancelar a rescisão.

**Tipo de Redução Aviso**

* Caso o tipo de demissão seja "2 - Inic. Empregador sem justa causa" ,será habilitado as opções "Dias" e "Jornadas".
* Caso o tipo de demissão seja "V - Comum Acordo", será habilitado a opção "Dias", "Jornadas" e "Nenhum" .

**A****tenção:**

Para ambos os tipos será permitida a redução do aviso conforme previsto em lei.

* Quando marcada a opção "Nenhum" para o tipo de demissão  "V - Comum Acordo, não será realizada a redução do aviso.

         Maiores informações veja em : [Aviso Prévio Trabalhado-Tipo Redução Aviso "Nenhum".](https://tdn.totvs.com.br/pages/viewpage.action?pageId=516194630)

**Forma Redução Aviso**

Disponível para os tipos de demissão "2 - Inic. Empregador sem justa causa" e "V - Comum Acordo", deverá informar se a forma de redução do aviso será pelo Início ou pelo Fim. Caso não marque nenhuma, será considerado pelo Início.  
   
**Tipo de Aviso Prévio**  
Indica quem avisou o desligamento.  
   
**Motivo da Mudança**  
Informar o motivo da mudança que será gravado no histórico de situação do funcionário.  
   
Observação: Após o cadastramento do aviso prévio individual ou coletivo, a situação do funcionário será alterada para "V - Aviso Prévio".  
   
**Gerar Log Consolidado**  
   
Marcando este parâmetro, será gerado um log mais detalhado no processo de Aviso Prévio Coletivo em um arquivo txt onde constará:

1. Motivo pelo qual não foi possível cadastrar aviso prévio a um funcionário.
2. Totalizadores por seção e de todo o processo.

Caso não seja definido um caminho para salvar o arquivo, será salvo no caminho parametrizado no Parametrizador/Folha Normal/Geral/Diretório Utilizado para Processos que geram arquivos em .net (Jobserver).  
Se não for definido caminho em nenhum dos campos citados acima, será gerado na pasta RM.Net.  
Ao marcar a flag **Incluir Avisos Cadastrados no Log**, será imprimido no log, também os avisos que foram cadastrados com sucesso.  
Obs: Processo disponível apenas no cadastro de aviso prévio **coletivo**.

|  |  |
| --- | --- |
|  | Informações Complementares |

[Detalhamento do processo](http://tdn.totvs.com/pages/viewpage.action?pageId=273302982)

[DataServer FopAvisoPrevioData](https://tdn.totvs.com.br/display/LRM/DataServer+FopAvisoPrevioData)
