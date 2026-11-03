---
content_hash: 019a8c895e7e5cb91660fc9e7da514efd187caa4dd594bcd164e3460f91ebe79
fetched_at: '2026-06-29T00:09:24.586058+00:00'
page_id: '423937966'
product: rm
source: tdn-rm
title: Processo de Inventário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937966
version: 2
---

Para se trabalhar com o Inventário deve-se primeiramente cadastrar um layout de inventário conforme a geração do mesmo pelo leitor de código de barras. Após o cadastro do layout e geração do arquivo TXT, deve-se realizar o processo de Inventário no menu Utilitários|Processo de Inventário. Para que este seja realizado com sucesso, basta inserir o código do layout utilizado no arquivo texto, o caminho onde se encontra o arquivo texto a ser importado, a data do inventário e posteriormente selecionar a funcionalidade que melhor atender, sendo elas:

**Atualizar dados da tabela de Patrimônio com os dados da tabela de Inventário**  
A atualização de dados da tabela de Patrimônio com os dados da tabela de Inventário, não funciona junto com a importação. Deve ser escolhida somente após a importação dos dados e a devida conferência.

Escolhendo essa opção e avançando etapa é possível escolher os campos que deverão ser atualizados, dentre eles estão, Filial, Centro de Custo, Localização, Departamento e Responsável. Assim o sistema irá atualizar a tabela de Patrimônio (IPATRIMONIO) com os dados da tabela de inventário (IINVENTARIO).

Quando se tratar de atualização de Filial, Departamento e Centro de Custo é possível contabilizar a transferência dos patrimônios. O sistema irá gerar uma transferência de Controle, e esta ficará pendente para contabilização na consulta de transferência de controle. Desmarcando "contabilização transferência de controle", o sistema irá gerar a transferência no menu de consulta da transferência de controle com status "não contabilizado".

Ao cancelar a transferência de controle (processos| cancelamento da transferência de controle) o sistema irá desfazer a atualização. Nesta opção, o sistema também permite atualizar patrimônios agregados.

Para que o processo seja executado é obrigatório informar a Data da Atualização, que será levada em consideração na execução das transferências de controle e consequentes do processo de inventário. Esta deverá estar dentro do período de cálculo.

**Importar e atualizar os dados simultaneamente**  
O sistema irá importar os dados para a tabela IINVENTÁRIO, além de atualizar as informações no cadastro do patrimônio.

Assim como acontece com a opção acima, avançando etapa é possível escolher os campos que deverão ser atualizados no cadastro do patrimônio, dentre eles estão, Filial, Centro de Custo, Localização, Departamento e Responsável.

Quando se tratar de atualização de Filial, Departamento e Centro de Custo é possível contabilizar a transferência dos patrimônios. O sistema irá gerar uma transferência de Controle, e esta ficará pendente para contabilização na consulta de transferência de controle. Desmarcando "contabilização transferência de controle", o sistema irá gerar a transferência no menu de consulta da transferência de controle com status "não contabilizado".

Cancelando a transferência de controle (processos|cancelamento da transferência de controle) o sistema irá desfazer a atualização. Nesta opção, o sistema também permite atualizar patrimônios agregados.

Para que o processo seja executado, é obrigatório informar a Data da Atualização, que será levada em consideração na execução das transferências de controle e consequentes do processo de inventário. Esta deverá estar dentro do período de cálculo.

**Excluir registro da tabela de inventário (Recomendado)**  
Ao marcar esta opção, o sistema limpará toda a tabela de inventário antes de importar os dados do arquivo informado. É sempre aconselhável marcar esta opção na hora da importação, pois ela evita que dados velhos sejam mantidos na tabela, a menos que deseja importar mais de um arquivo. Neste caso esta opção deve ser marcada somente para o primeiro, caso contrário ele limpará os dados dos arquivos importados anteriormente.

Ao excluir os registro da tabela de inventário, o sistema irá gravar essa informação no cadastro de patrimônio, anexo histórico de inventário.

Veja Também
