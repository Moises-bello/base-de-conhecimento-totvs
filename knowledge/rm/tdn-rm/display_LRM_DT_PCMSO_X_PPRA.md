---
content_hash: 18357f4e3c0e0e34accbf65c7819efa57092a96775e29fdd89abdf0cfe2708ef
fetched_at: '2026-06-29T00:08:25.126257+00:00'
page_id: '270913149'
product: rm
source: tdn-rm
title: DT_PCMSO_X_PPRA
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_PCMSO_X_PPRA
version: 45
---

# PCMSO x PPRA 12.1.15

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM | | |
| **Segmento Executor:** | Construção e Projetos | | |
| **Módulo:** | SSO - Segurança e Saúde Ocupacional | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Geração de Exames Pendentes | SmtGerarExamesPendentesActionProc |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Funcionários | FopFuncAction | | Exames | SmtExamesAction | | Riscos | SmtPPRARiscosAction | | Avaliação e Reconhecimento de Riscos | SmtPPRAMedicoesAction | | | |
| **Chamado:** | n / a | | |
| **Requisito (ISSUE):** | [RHRHU001-313](http://jiraproducao.totvs.com.br/browse/RHRHU001-313) | | |
| **País:** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | n / a | | |

## 1 - Objetivo

Permitir ligação sistêmica entre o PPRA e o PCMSO. Neste contexto é possível associar exames aos riscos, podendo gerar os exames pendentes conforme a configuração/associação estabelecida.

## 2 - Definição da Regra de Negócio

## 2.1 - Req.5 - Parâmetro "Origem para Exames Pendentes"

Permite escolher como são gerados os exames pendentes, podendo ser uma **associação direta de perfis** **de exames** ou a partir do **PPRA**.

*****2.1.1 - Objetivo*****

Conseguir mudar a origem das informações para geração de exames pendentes de acordo com a forma que o cliente desejar.

***2****.1.2 - Critérios***

* + A opção para habilitar a nova forma de associação é exibida em um “check box” chamado “Utilizar "Associação PPRA" como origem na geração de exames pendentes";
  + Por padrão, o parâmetro deverá ser do tipo “Associação de perfis de exames” que é o modelo atual do mercado;
  + O parâmetro está no parametrizador do módulo de Segurança e Saúde Ocupacional na opção de “Exames".
  + Quando a opção deste check box é alterada, uma mensagem é exibida alertando ao usuário dos impactos desta mudança**:**
  - ***Atenção!***

    ***A partir da mudança deste parâmetro, todos os exames pendentes serão gerados a partir destas definições. Os exames pendentes já gerados serão mantidos.***  
    ***Alterando o parâmetro, também deve ser revisto o relatório do PCMSO. O mesmo deve ser importado e o processo "Gerar modelo de PCMSO" deve ser executado novamente.***
  - ***Atenção!***

    ***Ao desabilitar essa opção, o sistema utilizará a “Associação de perfis de exames” como origem na geração de exames pendentes.***  
    ***A “Associação de perfis de exames” é um modelo obsoleto e futuramente será descontinuado.***  
    ***Além disso, desmarcar o parâmetro pode impactar a geração de exames pendentes gerando inconsistências no sistema, por isso sugerimos não desmarcar.***  
    ***Dúvidas em relação a alteração do parâmetro e impactos possíveis, contate o Suporte Técnico.***  
    ***Deseja desabilitar o parâmetro e voltar a utilizar a “Associação de perfis de exames” como origem na geração de exames pendentes?***

## 2.2 - Cadastro de Associações de PCMSO x PPRA

Permite associar os perfis de exames a riscos, níveis de riscos, reconhecimentos/avaliações e pessoa.

## *******2.2.1 - Objetivo*******

Estabelecer a necessidade de realização de exames conforme exposição ao risco/nível de risco.

## ***2.2.2 - Critérios***

* + Acionado por meio de um botão no menu do SSO;

* + É obrigatório escolher um tipo de vínculo para que o cadastro habilite os campos: Risco, Cód. Nível de risco, Reconhecimento/Avaliação de Risco e Pessoa;

* + De acordo com o tipo de vínculo escolhido, serão habilitados os campos, da seguinte maneira:

    - **Risco:** obrigatório informar o campo Risco e limpa/desabilita Cód. Nível de Risco, Reconhecimento/Avaliação de Risco e Pessoa;
    - **Cód. Nível de Risco:** obrigatório informar os campos Risco e Cód. Nível de Risco e limpa/desabilita Reconhecimento/Avaliação de Risco, Pessoa;
    - **Avaliação de Risco:** obrigatório informar Risco e Avaliação de Risco e limpa/desabilita Cód. Nível de Risco e Pessoa;  
      **Observação:** É considerado somente avaliação de riscos, filtrando e desconsiderando "reconhecimento";
    - **Pessoa:** obrigatório informar o campo Pessoa e desabilita Risco, Cód. Nível de Risco e Reconhecimento/Avaliação de Risco.

* + Perfil de Exame tem o preenchimento obrigatório;
  + O Tipo de Vínculo só pode ser alterado na inclusão de **novos registros**;
  + Não é permitido vincular um **mesmo Perfil de Exame** mais de uma vez para um mesmo item. Por exemplo: se eu já vinculei o perfil de exame “Audiométrico” ao Risco “Ruído”, não deverá permitir vincular novamente o perfil para o Risco “Ruído”. Entretanto, se houver um vínculo entre o perfil de exame “Audiométrico” com o tipo de Vínculo Nível de Risco, com o Risco “Ruído” e um nível qualquer, é diferente do vínculo por Risco e permitirá a associação;

* + Na visão do cadastro é possível ordenar, agrupar e filtrar por Risco, Nível de Risco, Pessoa e Perfil de Exame.

## 2.3 - Assistente de Associação de PCMSO x PPRA

Permite associar grandes quantidades de perfis de exames a riscos, níveis de riscos e pessoas com facilidade e poucos cliques.

## *******2.3.1 - Objetivo*******

Conseguir associar riscos a perfis de exames em momentos que houver muita necessidade de entrada de informações, como implantação de sistema ou mudança de riscos.

## ***********2****.3.2 - Critérios***********

* + Acionado por meio de um botão no menu do SSO;

* + Na primeira etapa do assistente, o usuário deve escolher se deseja fazer a associação de perfis de exames para risco/nível, reconhecimento/avaliação de risco ou para pessoa. **Observação:** É considerado somente avaliação de riscos, filtrando e desconsiderando "reconhecimento";

* + Na etapa seguinte, é oferecido ao usuário um **lookup multirecords** para que ele selecione riscos, reconhecimento/avaliação de riscos ou funcionários que deseja fazer associações de perfis de exames;
  + Na próxima etapa, a tela deve é dividida em duas partes, onde temos:

    - **Perfis associados**: treeview que mostra risco/nível do risco, avaliação de riscos ou pessoas, de acordo com as escolhas das etapas anteriores. Para cada risco, nível, avaliação de riscos ou pessoas exibido, é incluído um “nó” para cada perfil de exame a ele associado;
    - **Perfis de exames**: exibidos os perfis de exame cadastrados no sistema.
  + Para associar um perfil a riscos, níveis, avaliação de riscos ou pessoas, o usuário deve clicar no perfil de exame e arrastar para o item desejado. Ao soltar o botão do mouse, é criado um nó referente ao perfil de exame;
  + Para remover um vínculo, basta selecioná-lo na treeview e pressionar **DELETE**;
  + Não é possível incluir um perfil já cadastrado para o item;
  + Se a associação for por **Risco/Nível Risco**:

    - É permitido associar o perfil tanto ao risco, quanto diretamente aos Níveis de Risco (último nível da árvore);
    - Ao arrastar o perfil de exame para a raiz da árvore, este perfil é associado a todos os riscos selecionados. Não são criadas associações aos sub-ítens Nível de Risco.
  + Se a associação for por **Avaliação de Risco**:

    - Não é permitido associar o perfil diretamente ao risco, somente às Avaliações (último nível da árvore);
    - Ao arrastar o perfil de exame para a raiz da árvore, este perfil é associado à todas as Avaliações (último nível da árvore). Não são criadas associações diretas aos riscos;
    - Ao passar o mouse em cima do ítem na árvore, é apresentado mensagem tooltip com dados complementares (controle de medição, data início e fim da medição).
  + Se for vinculado algum perfil de exame que contenha exame do tipo “Mudança de Função”, antes de avançar a etapa, é exibido um alerta informando o usuário que na próxima execução da geração de exames pendentes, todos os funcionários expostos àquele perfil terão a pendência gerada;
  + Ao executar o processo, são criados e excluídos registros de vínculo entre os riscos/níveis/avaliação de riscos/pessoas aos perfis de exame de acordo com as escolhas feitas pelo usuário;
  + Após a execução, está disponível um log contendo informações sobre todos os vínculos que foram criados ou removidos durante a execução do assistente;
  + Para fins de esclarecimento, este assistente terá o funcionamento semelhante ao atual **Assistente de Associação de Perfil**.

## 2.4 - Alertas para Exames do tipo "Mudança de Função"

Alerta sobre impactos de exames do tipo "Mudança de Função" em perfis de exames.

## *******2.4.1 - Objetivo*******

Informar ao usuário para que ele tenha ciência que da próxima vez que o assistente de Geração de Exames Pendentes for executado, todas as pessoas (funcionários) expostas ao risco/perfil terão a pendência gerada.

**Observação:** Para a [Previdência](http://sislex.previdencia.gov.br/paginas/05/mtb/7.htm),"**Mudança de Função**" é toda e qualquer alteração de atividade, posto de trabalho ou de setor que implique a exposição do trabalhador à risco diferente daquele a que estava exposto antes da mudança. No SSO, "**Mudança de Função**" é:

* + Qualquer inclusão de um novo exame no perfil de um funcionário.
  + Qualquer inclusão de um novo Risco no mapeamento do funcionário.  
     Portanto, mesmo se não houve alteração na função ou seção, mas houve a necessidade de um novo exame, é gerado exames pendentes com o motivo mudança de função.

## ***2.4.2 - Critérios***

* + No cadastro de perfis de exames, sempre que entrar um novo exame do tipo “mudança de função”, é alertado ao usuário que na próxima execução da geração de exames pendentes, todos os funcionários expostos àquele perfil terão a pendência gerada;
  + No cadastro de Associações PCMSO x PPRA, sempre que forem associados perfis de exames que contenham exames do tipo “mudança de função”, é alertado ao usuário que devido à existência de um exame do tipo “mudança de função”, na próxima execução da geração de exames pendentes, todos os funcionários expostos àquele perfil terão a pendência gerada.

## 2.5 - Visualização de Exames associados ao PPRA

Permite visualizar listagem de exames associados ao PPRA.

## *******2.5.1 - Objetivo*******

Conseguir visualizar todos os exames que estão associados ao PPRA, bem como o tipo de vínculo, risco, nível e perfil de exame.

## *******2.5.2 - Critérios*******

* + Anexo em Reconhecimento/Avaliação de Riscos que exibe todos os exames associados bem como sua origem (risco, nível) e o perfil de exame a que está associado;
  + Este anexo serve apenas para visualização. Não há nenhum tipo de edição dos dados exibidos, nem inclusão ou exclusão de registros.

## 2.6 - Geração de Exames Pendentes

Permite gerar exames pendentes para os funcionários considerando as novas possibilidades de associações de exames aos riscos, níveis e rec/aval. 

## *******2.6.1 - Objetivo*******

Conseguir ter o correto controle de pendência de exames.

*******2.6.2 - Fluxo Geração Exame Admissional*******

*******2.6.3 - Fluxo Geração Exame Periódico*******

*******2.6.4 - Fluxo Geração Exame Demissional*******

*******2.6.5 - Fluxo Geração Exame Mudança de Função*******

*******2.6.6 - Fluxo Geração Exame Retorno ao Trabalho*******
