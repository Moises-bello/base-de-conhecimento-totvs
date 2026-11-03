---
content_hash: e1073037c658aff968c285d7210325016fa31b31210ad272aa3570c0f308dd46
fetched_at: '2026-06-29T00:10:04.686941+00:00'
page_id: '452719233'
product: rm
source: tdn-rm
title: Informações Pessoais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719233
version: 5
---

As informações pessoais são formalidades legais e são importantes para o processamento da folha de pagamento e todos os controles afins. Este cadastro guarda informações fundamentais dos funcionários, tanto relativos à sua identificação quanto necessários à emissão de relatórios legais ou eventuais.  
   
**Identificação:**  
Com as informações da Identificação é possível cadastrar os dados relativos aos funcionários.  
   
Matrícula eSocial**:** Campo que identifica a Matrícula do trabalhador no eSocial. Será preenchido na inclusão do funcionário com vínculo empregatício e não pode ser editado. Para que o campo seja preenchido automaticamente é necessário que o usuário configure a Máscara para Matrícula do Trabalhador em Configurações | Parâmetros | Parametrizador | 06.07 - eSocial | Configurações Gerais.

**Observação:** Nos casos de admissão por Reintegração dos funcionários que possuem vínculo trabalhista, o preenchimento da matricula deverá ser feito manualmente, onde será necessário informar a matricula do funcionário reintegrado.

Nome Social: Campo criado para atender ao Decreto 8.727, DE 28 DE ABRIL DE 2016 .  
É o nome pela qual a pessoa se identifica e é socialmente reconhecida.  
   
**Atenção:**  
 •  Este campo é utilizado na geração do eSocial leiaute S-2205 -Alteração de Dados Cadastrais do Trabalhador.    
   
**Observações:**  
1.   Se por acaso, você cadastrar um funcionário "teste", a sua exclusão somente poderá ser efetuada dentro do próprio mês de inclusão e caso não haja movimentação lançada na Ficha Financeira.   
2.   Ao cadastrar um funcionário com o mesmo Nome, Nascimento, Estado Natal e Cidade de uma pessoa já registrada o sistema irá informar foi encontrada uma pessoa com os mesmos dados e irá vincular o novo registro ao já existente. Desta forma todos os dados pessoais de um registro estarão diretamente ligados ao outro, ou seja, ao efetuar alterações nos dados pessoais em um registro o outro será atualizado automaticamente.  
No link de "Localizar pessoa" será incluído um novo funcionário com alguns campos já preenchidos baseados no funcionário que está selecionado.  
**Exemplo:**  
Se o usuário tem vários autônomos para incluir em determinado mês deve incluir o primeiro autônomo e depois clicando neste botão será copiado para outro registro os dados que podem ser copiados para não necessitar ser cadastrado novamente. Dados como: sexo, naturalidade, data de admissão, tipo de admissão, etc...  
   
**Documentação**   
É obrigatório a apresentação dos documentos relacionados nesta pasta com a finalidade de cadastrar/identificar o empregado. Sendo assim a empresa cumprirá corretamente com as obrigações trabalhistas a que está subordinada, tanto com relação ao empregado quanto nas relações com o Ministério do Trabalho e Emprego - MTE.

[Carteira de Trabalho Digital.](https://tdn.totvs.com/display/LRM/CTPS+DIGITAL)  
   
RIC  
O RIC é o Registro de Identidade Civil, tendo validade nacional e é emitido pelos órgãos estaduais.  
O "Número do RIC", assim como o "Órgão Emissor" e da "Data de Emissão" serão utilizados na geração da carga inicial do S-2100 do eSocial.  
   
   
**Documentos Estrangeiros**  
Todos os campos ficarão disponíveis quando o campo "Nacionalidade" for diferente de "10-Brasileira".  
   
Dados Gerais de Estrangeiro  
Preencher em caso de trabalhador estrangeiro. Estes campos serão utilizados na geração da carga inicial do S-2200 do eSocial.  
Data de Chegada Brasil: Preencher com a data de chegada do trabalhador no Brasil, no caso de estrangeiro  
Classificação da Condição no Brasil: preencher conforme a classificação da condição do trabalhado no Brasil  
Cônjuge no Brasil: Marcar o flag somente se o trabalhador estrangeiro for casado com Brasileiro.  
Nro. de Filhos no Brasil: preencher com a quantidade de filhos nascidos no Brasil.   
   
Documentos de Estrangeiro  
O campo Registro Geral-RNE, assim com os campos "Órgão Emissor" e "Data Emissão" serão utilizados na geração da carga inicial do S-2200 e S-2300 do eSocial.

**Endereço Principal:**   
Nas informações de Endereço Principal é preenchido o endereço do funcionário podendo ser utilizado o recurso de preenchimento automático do CEP, buscando dados importados da base dos Correios realizados em TOTVS Serviços Globais | Serviços | Importação de CEP's .  
**Atenção:**   
Cadastre o(s) telefone(s) de contato do funcionário respeitando a máscara cadastrada em Configurações | Parametrizador | RH - Máscaras e Quebras.  
Tipo de Rua | Tipo de Bairro  
Serão listados os tipos cadastrados em TOTVS Gestão Fiscal | Cadastros | Globais | Mais | Endereço | Tipo de Rua e Tipo de Bairro.  
   
O campo Tipo de Rua será utilizado na geração da carga inicial do S-2200 do eSocial.  
Para saber quais são os tipos válidos poderá verificar o leiaute do eSocial,  "Tabela 20 – Tabela de Tipos de Logradouros".  
   
**Atenção I:**  
Deverá através do Parametrizador | eSocial especificar qual será o "Conceito de Classificação para o Tipo de Rua".  Veja mais detalhes no help do Parametrizador | eSocial.  
   
Moradia  
Os campos disponibilizados serão utilizados na geração da carga inicial do S-2100 do eSocial.  
   
   
**Anotação Pessoal:**   
Através das informações de anotações pessoais são registradas todas anotações dos funcionários.

**Atenção:**   
A ordenação dos registros de anotações pessoais somente é possível pelos campos Cód. Anotação, Data da Anotação e Data da Resolução.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários  
eSocial - Configurações Gerais
