---
content_hash: 30c7626bfaf38aca08269d016f30ab42e579dac6d019aee94355b2f56b8596d1
fetched_at: '2026-06-29T00:09:34.530250+00:00'
page_id: '425459179'
product: rm
source: tdn-rm
title: Ligações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459179
version: 4
---

**Ligações**

---

Na aba Ligações existem diversos campos a serem preenchidos, com o objetivo de configurar e identificar as conexões de origem e destino do conceito que esta sendo criado.

Na área central, temos:

* Área **"Arraste uma tabela de destino aqui":** Nessa área as ligações de conexão de origem e destino serão realizadas.

No canto direito, temos:

* Conexões:
  + **Conexão de Origem:** Na aba Conexões Origem são criadas as conexões com a aplicação origem. Ao criar uma conexão, é necessário informar o nome da mesma e o tipo e preencher os dados correspondentes.

A conexão de origem pode ser do tipo: Arquivo Texto, Banco de Dados, Data Server RM.Net, Web Service.  
    
 Saiba mais detalhes sobre os **tipos de conexão**, **clicando aqui**.  
    
 ***Nota:*** Sentenças personalizadas só podem ser utilizadas em conexões de banco de dados na origem.

* + **Conexão de Destino:** Na conexão de destino deve ser informados todos os dados para estabelecer a conexão com a aplicação de destino. Semelhante a Conexões Origem, essa conexão poderá ser de diversos tipos, sendo necessário informar as propriedades correspondentes de cada um.

A conexão de destino pode ser do tipo: Arquivo Texto, Banco de Dados, Data Server RM.Net, Web Service.

Saiba mais detalhes sobre os **tipos de conexão** **clicando aqui**.  
    
 ***Nota:***Sentenças personalizadas só podem ser utilizadas em conexões de banco de dados na origem.  
    
 **Configurações Extras**

Quando o RM.exe estiver sendo executado utilizando o RM.Host.Service, é necessário realizar algumas configurações para poder fazer uso do recurso Conceito, sendo este com Conexão (Origem ou Destino) do tipo Arquivo XML ou Arquivo Texto.

A configuração permite carregar os arquivos (de origem ou destino) a partir de outro diretório que não o "C:", como por exemplo, da Área de Trabalho .Para isso é necessário alterar a propriedade de Logon do Host no Serviço do Windos.

Acesse "Serviços | RM.Host.Service | Logon" e marque a opção "Permitir que o serviço interaja com a área de trabalho", ou defina uma conta de rede que tenha permissão para acessar a área de trabalho especificada.

* **Operações:** As operações permitem a intermediar a ligação de campos da conexão de origem com os campos da conexão de destino. Vários tipos de operações estão disponíveis para facilitar a manipulação.

Veja mais sobre **os tipos de operações** **clicando aqui**.

* **Parâmetros:** Os parâmetros são utilizados para filtrar os dados a serem gravados, atualizados ou excluídos na conexão de destino. Podemos filtrar um certo número de registro de acordo com a data por exemplo.

Eles podem ser dos seguintes tipos:

* + **Data Hora:** O parâmetro Data/Hora permite que os dados sejam filtrados pela data/hora especificados.
  + **Filtro:** Permite realizar pré-seleção dos dados utilizando os campos do filtro global.
  + **Lista de Opções:** Permite que seja criado uma lista de opções para seleção antes do processamento do conceito.
  + **Lógico:** Permite que filtrar dados de acordo com a situação TRUE ou FALSE.
  + **Lookup:** O lookup permite selecionar a informação antes de realizar o processamento do conceito. Os campos devem ser preenchidos:

Action: Tabela que vai ser utilizada.

Campos: Os campos que vão aparecer para serem selecionados na descrição e no código.

Descrição: Campo da tabela que vai aparecer no Lookup.

Código: Campo que vai ser usado para o filtro.

* + **Número Decimal:** Permite informar número decimal antes do processamento do conceito.
  + **Número Inteiro:** Permite informar número inteiro antes do processamento do conceito.
  + **Texto:** Permite informar texto antes do processamento do conceito.
  + **Contexto:** O conceito permite realizar a configuração dos contextos: Coligada, Filial, DataSistema, Projeto, Nível de Ensino, Unidade Bibliotecária, Localidade, Entrar Como, Tipo de Usuário, Chapa, Código Externo, Exercício Fiscal.
  + **Valor Fixo:** São utilizados quando o valor do campo será fixo, sem variações. Pode ser do tipo string, data, número entre outros.
  + **Expressão:** São utilizados para fazer expressões que irão ser gravadas no campo. Exemplo: cálculos matemáticos, funções etc.
