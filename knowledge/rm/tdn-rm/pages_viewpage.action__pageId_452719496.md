---
content_hash: d3bebfb31a1cecc6c2b14f1b063b6581eee72f5e7b9118cabf763d71f08efd8a
fetched_at: '2026-06-29T00:10:08.004995+00:00'
page_id: '452719496'
product: rm
source: tdn-rm
title: Alteração Global de Eventos Programados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719496
version: 2
---

Os eventos programados são aqueles que deverão ser lançados na movimentação da folha do empregado, que tenha uma competência inicial e final pré-determinada para lançamento, semelhantes aos Códigos Fixos do Funcionário, porém com a possibilidade de informar o Centro de Custo do Evento Programado, e a Competência Inicial e Final, além do evento poderá ser cadastrado mais de uma vez para o mesmo Funcionário.   
 Poderá ser realizada a alteração dos Eventos Programados para um ou mais funcionários simultaneamente, conforme necessidade.  
 Deverá informar o **Comportamento** que o sistema deve adotar ao processar a Alteração Global de Eventos Programados, podendo ser: Incluir, Alterar (para os casos do funcionário já possuir o evento) ou Excluir.  
 Na tela de **Evento Programado a ser Incluído**, o usuário poderá selecionar se **Permite inclusão de Evento já Cadastrado** para que seja permitida a inclusão de um evento já existente no cadastro do funcionário, desde que tenha um valor ou periodicidade diferente do já existente.

**Exemplo:** Funcionário comissionista, com o evento 'Comissão' programado para o período de **01/01/2010 a 01/06/2010,** no valor de **R$100,00**. Considere que seja necessário programar uma nova comissão para este mesmo funcionário, porém, com período de lançamento igual a **01/04/2010 a 01/08/2010,** e valor de **R$200,00**. Ao processar a **Alteração Global de Eventos** **Programados** o sistema irá registrar no Cadastro dois eventos de mesmo código, porém, ao realizar o lançamento na Folha de Pagamento o valor será somado (se estiver dentro do mesmo período de lançamento).

As opções **Usar Competência Inicial** e **Usar Competência Final** são visível apenas para os comportamentos **Alterar** e **Excluir**, e servirão para o usuário determinar qual a competência inicial e final deverá ser considerada na Alteração ou Exclusão de Eventos que já estão programados para o funcionário.  
    
 O campo **Tipo de Evento Programado** deverá receber o Tipo (Folha, Rescisão, 13º, etc.), que deverá ser assumido pelo Evento Programado na Inclusão, ou que será consistido na Alteração/Exclusão de dados do funcionário.

**Observações:**  
 1. Os tipos de eventos deverão ser criados em **Cadastro | Tabela Dinâmica**, através da tabela de código: **TPEVTPROG.**  
    
 2. No parâmetro 'Tipo Evento Programado' serão listados somente os tipos com código de 0(zero) a 39(trinta e nove).  
    
 3. Para os Eventos Programados dos Tipos Rescisão e 13º Salário deve-se, além de criar o tipo na Tabela Dinâmica e vincular ao evento no Cadastro do Funcionário, informá-los também nas pastas **Eventos Programados** disponíveis no parâmetro do sistema, em **Opções | Parâmetros | RM Labore**.

O campo **Fórmula** a ser utilizada na composição do **Valor/Hora** do evento deverá ser preenchido caso o mesmo não tenha um valor pré-determinado. Para este campo ser habilitado deve-se marcar o campo **Alterar Valor por Fórmula.**

**Observação:**  
 Para Alterar as horas do evento via fórmula, o usuário deverá atentar-se ao fato do sistema, em geral, trabalhar apenas em minutos. Para a fórmula retornar o valor correto (em horas), não gerando perdas no arredondamento, o usuário deverá informar o valor expresso em minutos, pois no momento da Inclusão/Alteração  o sistema transformará estes minutos em horas.  
    
 **Exemplo:**  
 Se a quantidade de horas for 13:48hs, deverá informar 828 => ((13horas \* 60 minutos) + 48 minutos)  
 Poderão ser informados dois complementos **(Complemento 1 e Complemento 2)** de caráter apenas informativos, podendo ser utilizados mediante necessidade do usuário.  
    
 Para empresas que utilizam cálculo de centro de custo, parametrizado em **Opções | Parâmetros | RM Labore | Parâm.  Cálculo**, poderá ser informado um centro de custo específico para evento.

**Observações:**  
 1. Se marcar o parâmetro 'Utilizar Centro de Custo' e não preencher o centro de custo o sistema irá considerar somente o evento que tiver sem centro de custo.  
    
 2. Se não marcar o parâmetro 'Utilizar Centro de Custo' o sistema irá considerar todos os centros de custos.
