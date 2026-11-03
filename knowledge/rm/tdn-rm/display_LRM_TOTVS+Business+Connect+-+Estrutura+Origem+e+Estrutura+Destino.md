---
content_hash: 99356cde1ee510e64e5234f5de3bfbe437f3e1b147e141251b22532a365bebc0
fetched_at: '2026-06-29T00:09:37.409991+00:00'
page_id: '425459608'
product: rm
source: tdn-rm
title: TOTVS Business Connect - Estrutura Origem e Estrutura Destino
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Business+Connect+-+Estrutura+Origem+e+Estrutura+Destino
version: 4
---

**Estrutura Origem e Estrutura Destino**

---

Nas abas Estrutura Origem e Estrutura Destino estão disponíveis "Tabelas" das conexões (Origem e Destino) definidas nas abas anteriores. Elas deverão ser indicadas, bem como as propriedades de cada campo.   
    
 A visão da Estrutura (Origem e Destino) é dividida em:

* **Tabelas Disponíveis:** Todas as tabelas definidas na Conexão deverão ser apresentadas neste campo.
* **Tabelas de Importação :** As tabelas selecionadas no campo Tabelas Disponíveis e que forem adicionadas à estrutura, podem ser visualizadas no campo Tabelas de Importação. Estão disponíveis os botões:
  + **Adicionar:** Para adicionar uma tabela à estrutura, selecione a tabela desejada no campo Tabelas Disponíveis, e ao clicar no botão Adicionar será aberta uma janela onde é possível definir quais os campos da tabela serão adicionados.
  + **Remover:** Remove um campo da tabela ou a tabela que foi adicionada ao campo Tabelas de Importação, de acordo com a seleção.
  + **Limpar:** Limpa todas as Tabelas de Importação incluídas, deixando em branco para que uma nova seja criada.
  + **Carregar:** Permite importar uma Estrutura a partir de um arquivo no formato \*.tst.
  + **Gravar:** Permite exportar uma Estrutura para um arquivo no formato \*.tst.
  + **Atualizar:** Quando alguma alteração for feita via banco e um novo campo for incluído pra tabela já utilizada, deve-se clicar no ícone Atualizar para que seja carregado esse novo campo nas opções.
* **Campos de Configurações (Tabelas e Campos)**

Tabelas: Ao selecionar uma tabela, no quadro Tabelas de Importação, na parte inferior da visão são mostrados os campos para configuração da tabela selecionada. Alguns campos aparecem para todos os tipos de conexão:

* + **Filtro Estático:** Filtro da tabela para importação.
  + **Detalhes:** Tabelas selecionadas com detalhes da tabela ativa.
  + **Mestre:** Tabela mestre da tabela ativa.
  + **Alias:** Alias atribuído à tabela para o processo de importação.
  + **Campos:** Campos selecionados da tabela.
  + **Conexão:** Campo somente leitura, que informa a conexão de origem da tabela.
  + **Nome:** Nome da tabela na fonte de dados. O nome deve sempre começar com " qry\_ ".
  + **Tipo da Tabela:** Campo somente leitura que informa se a tabela é fonte ou origem de dados na importação.

Quando a Conexão criada (Origem ou Destino) for do tipo Banco de Dados, além dos campos citados, também está disponível nos campos da Estrutura (Origem ou Destino) o campo:

* + **SQL:** Informe a sentença SQL.

Campos: Ao selecionar um campo da tabela em Tabelas de Importação, são apresentados na parte inferior da visão as opções para configuração do campo. As opções são iguais para todos os campos, independente do tipo da conexão. São elas:

* + **Entrada:** Ponto de entrada da operação ou campo.
  + **Controle de Exclusão:** Indica se o campo deve ser utilizado para controle de exclusão. Este parâmetro deve trabalhar em conjunto com o parâmetro Controle de Exclusão da aba Identificação.Ao informar no parâmetro da aba Identificação qual campo será utilizado como controle, é importante na aba Estrutura selecionar o campo informado e configurar este parâmetro como True. Caso contrário o conceito que utilizar este parâmetro não irá funcionar corretamente.
  + **Auto Incremento:** Informe se o campo é um campo de auto-incremento gerenciado pelo banco.
  + **Chave Primária:** Informe se o campo é parte da chave primária da tabela.
  + **Obrigatório:** Informe se o campo é obrigatório ou se pode receber valores nulos.
  + **Somente Leitura:** Informe se o campo permite ou não gravação de dados.
  + **Valor default:** Informe o valor assumido pelo campo quando nenhum outro valor for atribuído.
  + **Alias:** Informe o alias atribuído ao campo no processo de importação.
  + **Descrição:** Informe notas ou observações acerca do campo.
  + **Nome:** Informe o nome do campo na fonte de dados.
  + **Tabela:** Campo somente leitura, onde é possível visualizar o nome da tabela à qual o campo pertence.
  + **Campo PK Referencia:** Determina o nome do campo PK referenciado por este campo.
  + **Campo Referencia:** Determina o nome do campo referenciado por este campo.
  + **Entidade Referencia:** Determina o nome da entidade referenciada por este campo

**Relacionamento entre Tabelas**  
    
  Nas Estruturas Origem e Destino é possível adicionar mais de uma tabela para montar as estruturas das conexões criadas.  
 A primeira tabela adicionada é considerada como a tabela principal, e será reconhecida normalmente no momento de realizar as correspondências, diferente das outras tabelas que não serão apresentadas. Para que as demais tabelas sejam identificadas é necessário realizar o relacionamento entre as mesmas com a tabela principal.  
 Ao clicar no lookup Detalhes, uma visão é aberta para que se possa realizar este relacionamento. No lado esquerdo da visão são mostrados os relacionamentos existentes, e abaixo estão disponíveis os botões Add e Remove, para adicionar um relacionamento ou remover o relacionamento selecionado, respectivamente.  
 No lado direito estão disponíveis os campos para configurar o relacionamento. Os campos são:  
    
 ***Relacionamento***

* **Campos:** Vincular o campo da tabela com o campo da tabela mestre.

Ao clicar no lookup Campos para vincular o campo da tabela com o da tabela mestre, uma visão é aberta para informar os mesmos. No lado esquerdo da visão são mostrados os campos que já foram criadas as correspondências.   
 Abaixo estão disponíveis os botões Add e Remove, para adicionar um campo ou remover o campo selecionado, respectivamente.Do lado direito estão disponíveis os campos:

* + **Detalhe:** Campo da tabela que deverá fazer correspondência com o campo da tabela mestre.
  + **Mestre:** Campo da tabela mestre.
* **Cardinalidade:** Informe se o relacionamento será de um para muitos, ou de um para um.

***Tabela***

* **Detalhe:** Informe a tabela que deverá ter um relacionamento com a tabela mestre.
* **Nome:** Campo do tipo somente leitura, onde consta o nome da tabela mestre do relacionamento que está sendo criado

***Nota:*** *Para que a configuração possa ser realizada corretamente, é necessário primeiro informar a tabela no campo Detalhe, para depois informar os campos e a cardinalidade em Relacionamento.*

***Dica:*** Ao criar mais de uma Conexão Origem, pode-se apontar na aba Estrutura Origem os recursos da segunda conexão, acrescentando as tabelas na estrutura conforme demonstrado.

**Observações:**

Saiba sobre **Relacionamento entre Tabelas**[**clicando aqui**](http://tdn.totvs.com/display/LRM/Relacionamento+entre+Tabelas).

---

**Recursos Adicionais**

Acesse o boletim técnico abaixo para ver mais detalhes sobre relacionamento de tabelas:

[Criando um Relacionamento entre Tabelas Mestre-Detalhe](http://totvsconnect.blogspot.com/2011/07/como-fazer-conceito-com-relacionamento)
