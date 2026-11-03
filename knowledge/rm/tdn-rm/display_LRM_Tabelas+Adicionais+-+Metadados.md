---
content_hash: 972424a4027216f010561800c679863009e34a941b23947e7734744e72f1e028
fetched_at: '2026-06-29T00:11:56.436881+00:00'
page_id: '866025936'
product: rm
source: tdn-rm
title: Tabelas Adicionais - Metadados
type: documentation
url: https://tdn.totvs.com/display/LRM/Tabelas+Adicionais+-+Metadados
version: 11
---

Nos cards dos períodos que estiverem "Em medição", será possível inserir registros de tabelas cadastradas previamente no Módulo de Serviços Globais, através do menu [Metadados](https://tdn.totvs.com/display/LRM/Metadados+-+Como+incluir+um+projeto).

Pré-Requisito

Para que as tabelas fiquem disponíveis para seleção no parâmetro do projeto, será necessário informar os 5 campos, destacados na imagem abaixo, como chave primária e visíveis na tabela que será criada. Além disso, o campo PERIODO deverá ser do tipo Varchar tamanho 10:

Após a criação da tabela, inclusão de modelo de negócio, formulário, projeto de metadados e execução do processo de Gerar projeto de metadados; deverá selecionar no parâmetro do projeto, a tabela criada e que será usada para preenchimento através do Portal de Medição:

Os projetos que tiverem as tabelas selecionadas no parâmetro, conforme destacado acima, irão exibir, a opção de Tabelas Adicionais, do respectivo card dos períodos "Em medição":

E, poderão ser preenchidas através da importação de arquivo do Excel, que deverá ser baixado previamente:

E importado, após o preenchimento das informações salvas no mesmo arquivo:

Gravando esses dados na respectiva tabela de metadados:

Caso tenha necessidade de fazer alguma correção na planilha, será possível excluir os dados importados anteriormente através do botão destacado abaixo: e fazer uma nova importação:
