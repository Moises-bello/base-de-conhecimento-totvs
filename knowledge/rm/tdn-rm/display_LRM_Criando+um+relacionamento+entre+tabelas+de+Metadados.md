---
content_hash: 9ee9c13c2f780b3239ede12691fb9c99029998d2a26246d7efb4d43d42c8baf0
fetched_at: '2026-06-29T00:10:21.930957+00:00'
page_id: '494975058'
product: rm
source: tdn-rm
title: Criando um relacionamento entre tabelas de Metadados
type: documentation
url: https://tdn.totvs.com/display/LRM/Criando+um+relacionamento+entre+tabelas+de+Metadados
version: 15
---

# Objetivo

Esse documento irá mostrar como criar um relacionamento entre tabelas de um Metadados.

# Criando Tabelas

---

Iremos criar duas tabelas, TESTERELACIONAMENTO e TESTERELACIONAMENTOFILHA.

A coluna CPF nas duas tabelas são chaves primárias.

# Criando o Relacionamento entre as tabelas

---

Iremos agora criar a relação entre as duas tabelas.

Criar o relacionamento entre elas, usando as chaves CPF como CHAVE e CHAVEESTRANGEIRA.

Observação

Caso a relação possua duas ou mais chaves, dê preferência em adicionar a primeira chave e Salvar, então depois adicionar as seguintes.

O Nome do Relacionamento tem tamanho máximo de 30 caracteres.

# Relacionamento com duas ou mais chavesRELACIONA

---

O relacionamento entre tabelas do Metadados espera que seja criado com todas as chaves primárias da tabela Pai.

Sendo assim, quando a tabela Pai tiver 1 chave primária, o relacionamento deve ter 1 única definição de relação.  
Quando a tabela Pai tiver 2 ou mais chaves primárias, o relacionamento também deverá ter todas as chaves relacionadas.

É importante frisar que a FK só é criada na criação da tabela após a primeira geração do projeto. Desse modo, não é possível fazer a alteração de um FK em uma tabela já existente.Validação do Relacionamento

A partir da versão 12.1.2306 será realizada uma validação das chaves ao salvar o relacionamento.   
Somente será possível criar relacionamentos desde que todas as chaves da tabela Pai estejam também informadas no relacionamento.

# Regra Update / Regra Delete

---

No Relacionamento podemos aplicar operações para atualizar ou excluir o registro da tabela pai, podendo haver diferentes requisitos sobre o efeito nos valores associados em tabelas filho.   
Há quatro opções disponíveis:

|  |  |  |
| --- | --- | --- |
| **Especificação** | **Update na tabela Pai** | **Delete na tabela Pai** |
| **NO ACTION** | Nenhuma ação será executada. | Nenhuma ação será executada. |
| **CASCADE** | Valores associados na tabela filha também serão atualizado. | Registros associados em tabela filha também serão excluídos. |
| **SET NULL** | Valores associados na tabela filha serão definidos como NULL. | Valores associados na tabela filha serão definidos como NULL. |
| **SET DEFAULT** | Valores associados na tabela filha serão definidos para o valor padrão especificado na definição da coluna; o valor padrão deverá estar presente na coluna de chave primária. | Valores associados na tabela filha serão definidos para o valor padrão especificado na definição da coluna; o valor padrão deverá estar presente na coluna de chave primária. |

No módulo de **Metadados** existem 2 opções onde informamos os relacionamentos entre tabelas:

* Na tela "**Relacionamento**": Por essa tela o relacionamento é feito diretamente no banco de dados.
* Na tela de "**Modelo de Negócio**": Por essa tela o relacionamento é feito pelo DataSet tipado, ou seja, somente quando o registro é manipulado pela aplicação.

Quando o relacionamento é feito na tela de "**Relacionamento**" é executado um Script SQL diretamente no banco de dados para criar a relação/chave estrangeira.  
Quando o relacionamento é feito na tela de "**Modelo de Negócio**" o relacionamento é feito somente via aplicação no momento de **Excluir** um registro.  
Ou seja, não é feito nada em banco de dados, é tudo feito no DataSet tipado que o **Metadados** cria ao **Gerar o Projeto**.  
Com isso tem-se o seguinte:  
Quando se define a regra **CASCADE**, seja na tela "**Relacionamento**" ou "**Modelo de Negócio**" essa regra sempre será utilizada ao **Excluir** um registro.  
Para utilizar a regra de **NO ACTION** é necessário estar configurado para **NO ACTION** na tela de "**Modelo de Negócio**", desde que na tela "**Relacionamento**" não esteja configurado para **CASCADE**.  
**OBSERVAÇÃO**: Na tela de "**Modelo de Negócio**" quando não for definida uma regra de Exclusão (Delete) o padrão é sempre **CASCADE**.

# Configurando o Modelo de Negócio

---

Iremos agora configurar o modelo de Negócio.

1) Adicionar uma nova tabela:    
OBS: caso o relacionamento já tenha sido criado, as tabelas relacionadas serão apresentadas, como abaixo:

Clicando no OK, a estrutura de tabelas do modelo de negócio ficará assim:

IMPORTANTE

Caso o relacionamento não tenha sido criado antes na etapa anterior e precise ser realizado por aqui, deve ser seguido os mesmos critérios,  veja mais informações.

# Configurando a Apresentação do Formulário

---

Iremos agora configurar a apresentação de formulário

Nesse caso, apenas as Abas (Teste Relacionamento) e (Teste Relacionamento Filha) foram criadas.

# Criando e Gerando um Projeto de Metadadados

---

Iremos agora criar um projeto de metadados e iremos compila-lo afim de poder usá-lo.

Defina o nome do projeto, versão e os demais campos, e defina também o local onde estará localizado o metadado.

Após configurar o projeto, vá em processos e Gerar Projeto de Metadados

Clique em executar.

Caso o processo termine em sucesso, vamos prosseguir para o formulário criado.

# Acessando um formulário criado

---

Iremos agora acessar um formulário criado.

Acesse em Seviços Globais >> Customização >> TESTERELACIONAMENTOPRJ

Crie um novo registro.

Observe que as duas tabelas estão presentes no fomulário.

As tabelas filhas estão disponíveis separadas por abas.

# Relacionamento entre dois metadados

---

Existe a possibilidade de se relacionar dois metadados entre si, porém as tabelas deles terão que estar relacionadas, ou seja, a relação PK / FK deve existir no banco de dados.

Sem esse relacionamento vários erros conceituais podem acontecer, como alterar uma chave primária em um metadados e um lookup em outro que dependia do valor, passar a não funcionar corretamente.

Por isso é necessário o relacionamento pré-existente entre as tabelas desses metadados.

Utilizando as tabelas relacionadas TESTERELACIONAMENTO e TESTERELACIONAMENTO2, conseguimos relacionar dois metadados diferentes de forma correta.

O exemplo abaixo mostra a tentativa de alterar uma chave primária, onde uma exceção é levantada.

Observe que existe um vinculo entre os registros

PESSOA de CPF 2 de nome Laura e DEPENDENTE de CPF 2, por isso a exceção acima foi levantada.
