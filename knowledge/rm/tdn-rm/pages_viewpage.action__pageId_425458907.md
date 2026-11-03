---
content_hash: 99a69b453b27faa201ffd168734530253c520cf0aa6a1b175c311f463e095411
fetched_at: '2026-06-29T00:09:32.714494+00:00'
page_id: '425458907'
product: rm
source: tdn-rm
title: Avaliação Institucional - EDU - Duplicado 1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458907
version: 1
---

**Avaliação Institucional**

---

Permitir que os Funcionários das Empresas Parceiras, possam através do portal, responder a Avaliação Institucional.   
Para isso, durante o processo de execução da Avaliação Institucional será gerado o registro do funcionário na tabela PPESSOA, devido a isso o cadastro de funcionário teve as seguintes alterações:  
§ Criação do campo código da pessoa (CODPESSOA) para estabelecer o vínculo entre o cadastro do funcionário e o cadastro de pessoa;  
   
§   Criação dos campos naturalidade (CODNATURALIDADE) e estado natal ( ESTADONATAL);  
   
§  Alteração no tamanho do campo NOME para 120 caracteres;  
   
§  O código da pessoa só será preenchido se houver a geração de uma Avaliação a ser respondida pelo funcionário;  
   
§  Para acesso ao portal o código de usuário a ser considerado continuará sendo o definido no cadastro de funcionário da empresa parceira.  
Caso ocorra alguma alteração nos campos de sincronização automática no cadastro de funcionário deve disparar a atualização das informações no cadastro de pessoa e em todos os funcionários vinculados a esta mesma pessoa. De forma inversa toda alteração em uma pessoa deve disparar a atualização em todos os funcionários vinculados a esta pessoa simultaneamente.  
Essa alteração estará disponível em:  
§ RM.exe;  
§ Portal;  
§ Fluig (Wokflows: Cadastro de Empresa Parceira / Cadastro de Funcionário da Empresa Parceira);  
§ Experência #8;  
§ Páginas Públicas (Cadastro das Empresas Parceiras e seus funcionários).  
**Processo para geração de pessoa vinculada ao funcionário**  
Nos casos em que os funcionários não possuam vínculo com uma pessoa e for necessário gerar um código de pessoa o sistema seguir os seguintes passos:  
Verificar o parâmetro "Validar unicidade de Pessoa por" no Recursos Humanos | Configurações |Parametrizador | Gerais | Validações:            -  Nome, Data de Nascimento, Estado natal e Cidade natal            -  CPF A partir do valor definido no parâmetro de unicidade o sistema:

* Verifica se o funcionário possui as informações preenchidas, ou seja, se unicidade é por CPF os funcionários devem possuir esta informação preenchida. Caso não esteja preenchido o processo deve permitir a definição desta informação antes do próximo passo.
* Verifica se a pessoa já está cadastrada através dos campos de unicidade Não existe uma pessoa cadastrada: será gerada uma nova pessoa a partir dos dados do funcionário da empresa e o código da pessoa será inserido no registro do funcionário.

Encontrou uma pessoa cadastrada: busca o código da pessoa e atualiza o registro do funcionário  
  §  Possui mais de uma pessoa cadastrada: abre-se uma nova aba no processo para definir qual pessoa deve ser utilizada na associação.  
**Processo de cadastro de avaliação institucional** 1º Passo: Incluir a possibilidade de gerar avaliações institucionais para os funcionários da empresa parceira  
2º Passo: Selecionar os candidatos a partir do cadastro dos funcionários das empresas parceiras. Apenas usuários ativos devem ser listados. Possibilitar a visualização das avaliações já geradas para o funcionário.  
 3º Passo: Selecionar a avaliação     - Selecionar período     - Selecionar grupo     - Objeto avaliado     - Item avaliado  
§  Curso (disponibilizar uma forma para seleção do curso) - para que seja possível gerar avaliações institucionais para funcionários de empresa, selecionando como item avaliado o "Curso", é necessário que a empresa possua convênio e público alvo cadastrados.  
§  Pode-se definir um novo tipo de item avaliado  
    - Especificar uma determinada pessoa - disponibilizar um lookup para selecionar a pessoa. Para geração de avaliações institucionais para funcionários de empresa, selecionando como item avaliado uma "Pessoa", NÃO é necessário que a empresa possua convênio e público alvo cadastrados.  
   
retornar ao menu anterior   
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Documento Técnico: Funcionalidades para Empresas (Responder Avaliações)](http://tdn.totvs.com/pages/viewpage.action?pageId=240976862)
